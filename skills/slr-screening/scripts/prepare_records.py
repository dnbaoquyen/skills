#!/usr/bin/env python3
"""Parse RIS / BibTeX / CSV database exports into one deduplicated records.csv.

Usage:
    python3 prepare_records.py scopus.ris wos.bib pubmed.csv -o records.csv

Outputs:
    records.csv             record_id,title,abstract,keywords,authors,year,journal,doi,source_file
    duplicates_removed.csv  the removed duplicates and the record they duplicate (for auditing)

Standard library only.
"""

import argparse
import csv
import os
import re
import sys
import unicodedata

FIELDS = ["record_id", "title", "abstract", "keywords", "authors", "year", "journal", "doi", "source_file"]

csv.field_size_limit(min(sys.maxsize, 2**31 - 1))

# --------------------------------------------------------------------------- RIS

RIS_MAP = {
    "TI": "title", "T1": "title",
    "AB": "abstract", "N2": "abstract",
    "KW": "keywords",
    "AU": "authors", "A1": "authors",
    "PY": "year", "Y1": "year", "DA": "year",
    "JO": "journal", "T2": "journal", "JF": "journal", "JA": "journal",
    "DO": "doi",
}
RIS_LINE = re.compile(r"^([A-Z][A-Z0-9])  - ?(.*)$", re.M)


def parse_ris(text):
    records, cur, last = [], {}, None
    for raw in text.splitlines():
        line = raw.rstrip("\r")
        m = RIS_LINE.match(line)
        if m:
            tag, val = m.group(1), m.group(2).strip()
            if tag == "ER":
                if cur:
                    records.append(cur)
                cur, last = {}, None
                continue
            field = RIS_MAP.get(tag)
            last = field
            if not field or not val:
                continue
            if field in ("keywords", "authors"):
                cur.setdefault(field, []).append(val)
            elif field not in cur:  # first occurrence wins (TI before T2 etc.)
                cur[field] = val
        elif last and line.strip() and last in ("abstract", "title") and last in cur:
            cur[last] += " " + line.strip()  # continuation line
    if cur:
        records.append(cur)
    return records


# ------------------------------------------------------------------------ BibTeX

BIB_MAP = {
    "title": "title", "abstract": "abstract", "keywords": "keywords",
    "author_keywords": "keywords", "author": "authors", "year": "year",
    "journal": "journal", "booktitle": "journal", "doi": "doi",
}


def _bib_value(s, i):
    """Read a BibTeX value starting at s[i]; return (value, next_index)."""
    while i < len(s) and s[i] in " \t\r\n":
        i += 1
    if i >= len(s):
        return "", i
    if s[i] == "{":
        depth, j = 0, i
        while j < len(s):
            if s[j] == "{":
                depth += 1
            elif s[j] == "}":
                depth -= 1
                if depth == 0:
                    return s[i + 1:j], j + 1
            j += 1
        return s[i + 1:], len(s)
    if s[i] == '"':
        j = i + 1
        while j < len(s) and not (s[j] == '"' and s[j - 1] != "\\"):
            j += 1
        return s[i + 1:j], j + 1
    m = re.match(r"[^,}\s]+", s[i:])
    return (m.group(0), i + m.end()) if m else ("", i)


def parse_bibtex(text):
    records = []
    for m in re.finditer(r"@(\w+)\s*\{", text):
        if m.group(1).lower() in ("comment", "string", "preamble"):
            continue
        i = m.end()
        # skip citation key
        k = text.find(",", i)
        if k == -1:
            continue
        i = k + 1
        rec = {}
        while i < len(text):
            fm = re.match(r"\s*([\w\-]+)\s*=\s*", text[i:])
            if not fm:
                break
            name = fm.group(1).lower()
            val, i = _bib_value(text, i + fm.end())
            val = re.sub(r"[{}]", "", re.sub(r"\s+", " ", val)).strip()
            field = BIB_MAP.get(name)
            if field and val and field not in rec:
                if field == "authors":
                    rec[field] = [a.strip() for a in re.split(r"\s+and\s+", val) if a.strip()]
                elif field == "keywords":
                    rec[field] = [k.strip() for k in re.split(r"[;,]", val) if k.strip()]
                else:
                    rec[field] = val
            while i < len(text) and text[i] in " \t\r\n,":
                i += 1
            if i < len(text) and text[i] == "}":
                break
        records.append(rec)
    return records


# --------------------------------------------------------------------------- CSV

CSV_ALIASES = {
    "title": ["title", "article title", "document title", "ti"],
    "abstract": ["abstract", "ab"],
    "keywords": ["author keywords", "keywords", "index keywords", "keywords plus", "de", "mesh terms"],
    "authors": ["authors", "author", "author full names", "au"],
    "year": ["year", "publication year", "py", "publication date", "create date"],
    "journal": ["source title", "journal", "journal/book", "publication title", "so", "source"],
    "doi": ["doi", "di"],
}


def parse_csv(text):
    sample = text[:5000]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
    except csv.Error:
        dialect = csv.excel
    reader = csv.DictReader(text.splitlines(), dialect=dialect)
    headers = {h.strip().lower().lstrip("﻿"): h for h in (reader.fieldnames or [])}
    colmap = {}
    for field, aliases in CSV_ALIASES.items():
        for alias in aliases:
            if alias in headers:
                colmap.setdefault(field, []).append(headers[alias])
    records = []
    for row in reader:
        rec = {}
        for field, cols in colmap.items():
            vals = [row.get(c, "") or "" for c in cols]
            vals = [v.strip() for v in vals if v and v.strip()]
            if not vals:
                continue
            rec[field] = "; ".join(vals) if field == "keywords" else vals[0]
        records.append(rec)
    return records


# ----------------------------------------------------------------- normalising

def norm_doi(doi):
    doi = (doi or "").strip().lower()
    doi = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", doi)
    doi = re.sub(r"^doi:\s*", "", doi)
    return doi.rstrip(".")


def norm_title(title):
    t = unicodedata.normalize("NFKD", title or "")
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9]+", "", t)


def finalize(rec, source):
    out = {k: "" for k in FIELDS}
    for k in ("title", "abstract", "journal"):
        out[k] = re.sub(r"\s+", " ", rec.get(k, "") or "").strip()
    for k in ("keywords", "authors"):
        v = rec.get(k, "")
        out[k] = "; ".join(v) if isinstance(v, list) else (v or "")
    ym = re.search(r"(19|20)\d{2}", rec.get("year", "") or "")
    out["year"] = ym.group(0) if ym else ""
    out["doi"] = norm_doi(rec.get("doi", ""))
    out["source_file"] = source
    return out


def load(path):
    with open(path, encoding="utf-8-sig", errors="replace") as f:
        text = f.read()
    ext = os.path.splitext(path)[1].lower()
    if ext in (".ris", ".txt", ".nbib") and RIS_LINE.search(text):
        recs = parse_ris(text)
    elif ext == ".bib" or text.lstrip().startswith("@"):
        recs = parse_bibtex(text)
    elif ext in (".csv", ".tsv"):
        recs = parse_csv(text)
    elif RIS_LINE.search(text):
        recs = parse_ris(text)
    else:
        sys.exit(f"Cannot detect format of {path} (expected RIS, BibTeX or CSV)")
    return [finalize(r, os.path.basename(path)) for r in recs]



def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+")
    ap.add_argument("-o", "--output", default="records.csv")
    ap.add_argument("--dup-output", default=None, help="default: duplicates_removed.csv next to output")
    args = ap.parse_args()

    all_recs = []
    for p in args.files:
        recs = load(p)
        print(f"{p}: {len(recs)} records")
        all_recs.extend(recs)
    no_title = [r for r in all_recs if not r["title"]]
    all_recs = [r for r in all_recs if r["title"]]

    kept, dups = [], []
    by_doi, by_title = {}, {}
    for r in all_recs:
        doi = r["doi"]
        tkey = (norm_title(r["title"]), r["year"])
        match = (by_doi.get(doi) if doi else None) or by_title.get(tkey)
        if match is None and tkey[0]:
            # same title, one record missing the year
            match = by_title.get((tkey[0], "")) if r["year"] else next(
                (v for (t, _), v in by_title.items() if t == tkey[0]), None)
        if match is not None:
            # keep the first record, fill its blank fields from the duplicate
            for k in FIELDS:
                if not match[k] and r[k]:
                    match[k] = r[k]
            dups.append({**r, "duplicate_of_title": match["title"]})
            if match["doi"]:
                by_doi[match["doi"]] = match
            continue
        kept.append(r)
        if doi:
            by_doi[doi] = r
        by_title[tkey] = r

    for i, r in enumerate(kept, 1):
        r["record_id"] = f"R{i:04d}"

    with open(args.output, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(kept)
    dup_path = args.dup_output or os.path.join(os.path.dirname(os.path.abspath(args.output)), "duplicates_removed.csv")
    with open(dup_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS + ["duplicate_of_title"])
        w.writeheader()
        w.writerows(dups)

    missing_abs = sum(1 for r in kept if not r["abstract"])
    print("-" * 50)
    print(f"Records identified (all files):   {len(all_recs) + len(no_title)}")
    print(f"Records without a title (dropped): {len(no_title)}")
    print(f"Duplicates removed:                {len(dups)}  -> {dup_path}")
    print(f"Records to screen:                 {len(kept)}  -> {args.output}")
    print(f"  of which without abstract:       {missing_abs}")


if __name__ == "__main__":
    main()
