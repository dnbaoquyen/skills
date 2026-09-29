#!/usr/bin/env python3
"""PRISMA 2020 screening counts, AI-vs-human agreement (Cohen's kappa), and conflict lists.

Usage:
    python3 screening_stats.py --tak tak_screening.csv [--fulltext fulltext_screening.csv]
        [--identified N] [--duplicates M] [--not-retrieved K]
        [--human-tak human_tak.csv] [--human-fulltext human_ft.csv] [--outdir .]

Screening CSVs need at least: record_id, decision, reason_code.
Human CSVs need at least: record_id, decision.
TAK decisions: INCLUDE | MAYBE | EXCLUDE   (INCLUDE and MAYBE both go on to full text)
Full-text decisions: INCLUDE | EXCLUDE | UNCLEAR

Standard library only.
"""

import argparse
import csv
import os
from collections import Counter

DECISION_ALIASES = {
    "include": "INCLUDE", "included": "INCLUDE", "yes": "INCLUDE", "chon": "INCLUDE", "chọn": "INCLUDE",
    "exclude": "EXCLUDE", "excluded": "EXCLUDE", "no": "EXCLUDE", "loai": "EXCLUDE", "loại": "EXCLUDE",
    "maybe": "MAYBE", "unsure": "MAYBE", "uncertain": "MAYBE",
    "unclear": "UNCLEAR", "awaiting": "UNCLEAR",
}


def norm_decision(d):
    d = (d or "").strip()
    return DECISION_ALIASES.get(d.lower(), d.upper())


def read(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["decision"] = norm_decision(r.get("decision"))
    return rows


def binary(decision, stage):
    """Collapse to include/exclude for agreement. At TAK, MAYBE counts as include."""
    if stage == "tak":
        return "EXCLUDE" if decision == "EXCLUDE" else "INCLUDE"
    return decision


def cohen_kappa(a, b):
    n = len(a)
    if n == 0:
        return float("nan"), float("nan")
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
    kappa = 1.0 if pe == 1 else (po - pe) / (1 - pe)
    return po, kappa


def interpret(k):
    if k != k:
        return "n/a"
    for cut, label in ((0.8, "almost perfect"), (0.6, "substantial"), (0.4, "moderate"), (0.2, "fair"), (0.0, "slight")):
        if k > cut:
            return label
    return "poor"


def agreement(ai_rows, human_path, stage, outdir):
    human = {r["record_id"].strip(): r for r in read(human_path)}
    pairs, conflicts = [], []
    for r in ai_rows:
        rid = r["record_id"].strip()
        if rid not in human:
            continue
        a, h = binary(r["decision"], stage), binary(human[rid]["decision"], stage)
        pairs.append((a, h))
        if a != h:
            conflicts.append({
                "record_id": rid, "title": r.get("title", ""),
                "ai_decision": r["decision"], "ai_reason": r.get("reason_code", ""),
                "human_decision": human[rid]["decision"], "human_reason": human[rid].get("reason_code", ""),
                "ai_evidence": r.get("evidence", ""),
            })
    po, k = cohen_kappa([p[0] for p in pairs], [p[1] for p in pairs])
    missing = len(ai_rows) - len(pairs)
    path = os.path.join(outdir, f"conflicts_{stage}.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["record_id", "title", "ai_decision", "ai_reason",
                                          "human_decision", "human_reason", "ai_evidence"])
        w.writeheader()
        w.writerows(conflicts)
    print(f"\n  Agreement AI vs human ({stage.upper()}, n = {len(pairs)} paired records"
          + (f", {missing} without a human decision" if missing else "") + ")")
    print(f"    Percent agreement: {po:.1%}")
    print(f"    Cohen's kappa:     {k:.2f}  ({interpret(k)})")
    print(f"    Conflicts:         {len(conflicts)}  -> {path}")
    if k == k and k < 0.6:
        print("    ! kappa < 0.60: refine the criteria wording and re-calibrate before continuing.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tak", required=True)
    ap.add_argument("--fulltext")
    ap.add_argument("--identified", type=int, help="records identified from databases/registers")
    ap.add_argument("--duplicates", type=int, help="duplicate records removed before screening")
    ap.add_argument("--not-retrieved", type=int, default=None,
                    help="reports sought but not retrieved (default: TAK-passed records missing from full-text file)")
    ap.add_argument("--human-tak")
    ap.add_argument("--human-fulltext")
    ap.add_argument("--outdir", default=".")
    args = ap.parse_args()

    tak = read(args.tak)
    tak_c = Counter(r["decision"] for r in tak)
    unknown = {d for d in tak_c if d not in ("INCLUDE", "MAYBE", "EXCLUDE")}
    passed_ids = {r["record_id"].strip() for r in tak if r["decision"] in ("INCLUDE", "MAYBE")}
    tak_reasons = Counter((r.get("reason_code") or "UNSPECIFIED").strip() or "UNSPECIFIED"
                          for r in tak if r["decision"] == "EXCLUDE")

    print("=" * 60)
    print("PRISMA 2020 – SCREENING")
    print("=" * 60)
    if args.identified is not None:
        print(f"Records identified:                         n = {args.identified}")
    if args.duplicates is not None:
        print(f"Duplicate records removed:                  n = {args.duplicates}")
    print(f"Records screened (TAK):                     n = {len(tak)}")
    print(f"Records excluded (TAK):                     n = {tak_c['EXCLUDE']}")
    for code, n in tak_reasons.most_common():
        print(f"    {code:<38} {n}")
    print(f"Reports sought for retrieval:               n = {len(passed_ids)}"
          f"   (INCLUDE {tak_c['INCLUDE']}, MAYBE {tak_c['MAYBE']})")
    if unknown:
        print(f"  ! Unrecognised TAK decisions: {sorted(unknown)}")

    if args.fulltext:
        ft = read(args.fulltext)
        ft_ids = {r["record_id"].strip() for r in ft}
        not_retrieved = args.not_retrieved if args.not_retrieved is not None else len(passed_ids - ft_ids)
        ft_c = Counter(r["decision"] for r in ft)
        reasons = Counter((r.get("reason_code") or "UNSPECIFIED").strip() or "UNSPECIFIED"
                          for r in ft if r["decision"] == "EXCLUDE")
        extra = ft_ids - passed_ids
        print(f"Reports not retrieved:                      n = {not_retrieved}")
        print(f"Reports assessed for eligibility:           n = {len(ft)}")
        print(f"Reports excluded (full text):               n = {ft_c['EXCLUDE']}")
        for code, n in reasons.most_common():
            print(f"    {code:<38} {n}")
        if ft_c["UNCLEAR"]:
            print(f"Reports awaiting classification (UNCLEAR):  n = {ft_c['UNCLEAR']}")
        print(f"Reports included:                           n = {ft_c['INCLUDE']}")
        linked = sum(1 for r in ft if r["decision"] == "INCLUDE" and (r.get("linked_reports") or "").strip())
        if linked:
            print(f"  ({linked} included reports list linked reports – count unique studies separately)")
        if extra:
            print(f"  ! {len(extra)} full-text records were not passed at TAK: {sorted(extra)[:10]}")

    if args.human_tak or args.human_fulltext:
        print("\n" + "=" * 60)
        print("RELIABILITY")
        print("=" * 60)
        os.makedirs(args.outdir, exist_ok=True)
        if args.human_tak:
            agreement(tak, args.human_tak, "tak", args.outdir)
        if args.human_fulltext:
            if not args.fulltext:
                ap.error("--human-fulltext needs --fulltext")
            agreement(read(args.fulltext), args.human_fulltext, "fulltext", args.outdir)


if __name__ == "__main__":
    main()
