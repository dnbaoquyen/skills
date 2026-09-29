---
name: slr-screening
description: Screens references for a systematic literature review (SLR), scoping review, or meta-analysis — only the screening stage. It covers Title/Abstract/Keyword (TAK) screening and full-text screening against explicit inclusion/exclusion criteria, logs a reason for every decision, and reports PRISMA 2020 flow counts. Use it whenever the user has a set of search results (RIS, BibTeX, CSV exports from Scopus, Web of Science, PubMed, etc.) or PDFs and wants to decide which studies are relevant to their research question. Also use it for requests like "sàng lọc tài liệu", "sàng lọc tiêu đề tóm tắt từ khóa", "sàng lọc toàn văn", "lọc bài báo cho tổng quan hệ thống", "tiêu chí chọn/loại", "title/abstract screening", "full-text screening", "eligibility assessment", "inclusion/exclusion criteria", or "PRISMA flow numbers". It does not run searches, extract data, or write the review.
---

# SLR Screening (TAK + Full-text)

This skill helps with **one stage only** of a systematic review: deciding which retrieved records are truly relevant. It runs in two sequential passes:

1. **TAK screening** (Title, Abstract, Keywords): a fast, _inclusive_ pass that removes records that are clearly irrelevant.
2. **Full-text screening**: a strict pass over the remaining articles that confirms each eligibility criterion against the paper itself.

Searching databases, extracting data, appraising quality, and synthesising results are out of scope. If the user asks for those, say so briefly and point them to the right next step.

**Language:** Reply in the user's language. If they write in Vietnamese, write the explanations, reasons, and reports in Vietnamese, and keep the standard English terms in parentheses the first time they appear (e.g. "tiêu chí loại trừ (exclusion criteria)").

## Core principles (read before screening anything)

1. **Criteria first, screening second.** Never screen without written, operational eligibility criteria. Vague criteria give inconsistent decisions.
2. **The AI is a reviewer, not the judge.** Present every decision as a _recommendation_ with evidence. The researcher makes the final call. Say this once, clearly, at the start. Do not repeat it on every record.
3. **Evidence or "unclear".** Every criterion judgement must quote or point to the text it rests on: a phrase from the title/abstract/keywords, or a page/section of the full text. If the text does not say, the answer is `unclear`. Never infer study design, population, or setting from the journal name, the authors, or your background knowledge.
4. **Asymmetric caution.**
   - TAK: when in doubt, keep it (`MAYBE` goes on to full-text). A wrongly excluded study is lost for good. A wrongly kept one costs only one full-text read.
   - Full-text: every criterion must be clearly met. If a key criterion is still `unclear` after reading the whole paper, mark it `UNCLEAR`, flag it for the researcher, and suggest contacting the authors.
5. **One primary reason per exclusion**, taken from a fixed, ordered list of reason codes (see below). PRISMA reporting needs this.
6. **Consistency over speed.** Apply exactly the same criteria text to every record. If the criteria change mid-way, stop, record the change in the protocol log, and re-screen the records already done.
7. **Never invent records, abstracts, DOIs, or page numbers.** If a record has no abstract, screen on the title and keywords, and mark the missing fields `unclear`.

## Workflow

### Step 0 — Set up the screening protocol

Collect or build the following with the user, then save it as `screening_protocol.md` in the working folder. Start from `assets/screening_protocol_template.md`.

- **Research question** and the framework that fits it: PICO/PICOS (interventions), PEO (exposures and associations), SPIDER (qualitative), PCC (scoping reviews). See `references/criteria-frameworks.md`.
- **Eligibility criteria**, each written as a checkable statement with an ID (`C1`, `C2`, ...). Use the same IDs for inclusion and exclusion so that "not C3" is the exclusion. Cover the framework elements plus study design, publication type, language, and date range.
- **Operational notes** for borderline cases, e.g. "mixed samples count as eligible if ≥ 50% of the participants are adults, or if results for adults are reported separately".
- **Ordered exclusion reason codes**, derived from the criteria. See `references/exclusion-reasons.md`.
- **Reviewer mode**: (a) AI as second reviewer next to a human (recommended), or (b) AI as first-pass screener with human checks of all exclusions, or of a random sample.

If the user's criteria are vague, e.g. "papers about digital transformation", do not start screening. Propose concrete wording and ask them to confirm. Show 1–2 examples of how a borderline paper would be decided.

**Calibration (pilot):** Before the full run, screen 10–20 records, show the decisions and reasons, and ask the user to mark any they disagree with. Tighten the criteria wording until you both agree. Log every change to the criteria in the protocol's change log.

### Step 1 — Prepare the records

If the user gives database exports, run:

```bash
python3 scripts/prepare_records.py <file1.ris> [file2.bib file3.csv ...] -o records.csv
```

The script reads RIS, BibTeX, and CSV exports (Scopus, Web of Science, PubMed CSV, Zotero/EndNote exports). It normalises the fields to `record_id, title, abstract, keywords, authors, year, journal, doi, source_file`. It removes duplicates by DOI, then by normalised title + year, and writes `duplicates_removed.csv` so the removals can be audited. The printed counts go into PRISMA ("records identified" and "duplicates removed").

If the user pastes records straight into the chat, number them `R001, R002, ...` yourself and keep those IDs throughout.

### Step 2 — TAK screening

For each record, judge every criterion from the title, abstract, and keywords only, as `yes` / `no` / `unclear`, each with a short supporting quote.

**Decision rule:**

- Any criterion clearly `no` → `EXCLUDE`, with the code of the _first_ failing criterion in the ordered reason list.
- All criteria `yes` → `INCLUDE`, which means it goes on to full text.
- Otherwise (some `unclear`, none `no`) → `MAYBE`, which also goes on to full text.

Also give a confidence level (`high` / `medium` / `low`). Any `EXCLUDE` with `low` confidence should be flagged for human review.

Write the results to `tak_screening.csv` with these columns (the stats script expects them):

```
record_id,title,year,decision,reason_code,C1,C2,...,confidence,evidence,notes
```

- `decision` ∈ {`INCLUDE`, `MAYBE`, `EXCLUDE`}. `reason_code` is empty unless the decision is `EXCLUDE`.
- `C1..Cn` hold `yes`/`no`/`unclear`.
- `evidence` holds short quotes for each criterion, separated by `|`, e.g. `C1: "nurses in ICU" | C3: "cross-sectional survey"`.

**Working in batches.** For large sets (more than about 50 records), go through them in batches of 20–30. Append each batch to the CSV and give a short progress line, e.g. "Batch 3/12: 7 include, 5 maybe, 13 exclude". Do not print every reason in chat. The CSV is the record. After each batch, look back at the decisions for drift, e.g. the same kind of paper decided differently.

Use the output format in `references/output-formats.md` when showing individual decisions in chat.

### Step 3 — Retrieve full texts (user action)

List the records that go on to full text (`INCLUDE` + `MAYBE`) as `fulltext_to_retrieve.csv`, with DOIs. Ask the user to supply the PDFs, named by `record_id` if possible. Any the user cannot get are counted as "reports not retrieved" in PRISMA. They are not exclusions.

### Step 4 — Full-text screening

Read each full text properly. Check the methods section for design, sample, setting, and measures, not just the abstract. For long PDFs, read the Abstract, Introduction (aims), Methods, and the start of Results in full, and skim the rest.

For each criterion, record `yes` / `no` / `unclear` with a location, e.g. `p.4, Methods – Participants: "..."`.

**Decision rule:**

- All criteria `yes` → `INCLUDE`.
- Any `no` → `EXCLUDE`, with **one** primary reason code: the first failing criterion in the ordered list. Other failures can go in `notes`.
- A key criterion still `unclear` → `UNCLEAR`. Explain what is missing and suggest emailing the corresponding author.

Also check for **multiple reports of the same study**: the same sample or dataset in several papers, or a conference abstract followed by the full paper. Link them under one study ID and note which report is primary. PRISMA counts studies and reports separately.

Write the results to `fulltext_screening.csv`:

```
record_id,title,year,decision,reason_code,C1,C2,...,confidence,evidence,linked_reports,notes
```

### Step 5 — Quality control and reporting

Run:

```bash
python3 scripts/screening_stats.py --tak tak_screening.csv --fulltext fulltext_screening.csv \
  [--identified N --duplicates M --not-retrieved K] \
  [--human-tak human_tak.csv --human-fulltext human_ft.csv]
```

This prints:

- **PRISMA 2020 flow counts** for the screening part of the diagram: records screened, excluded at TAK, reports sought/not retrieved/assessed, reports excluded _by reason_, and studies included.
- **Agreement statistics** if the human reviewer's decisions are given (`record_id,decision` columns): percent agreement and Cohen's κ, plus a `conflicts_*.csv` file listing the disagreements to resolve. For TAK, `INCLUDE` and `MAYBE` are both counted as "include" because both go on to full text. As a rough guide, κ ≥ 0.6 is acceptable and κ ≥ 0.8 is good. If κ < 0.6 at the pilot, go back to Step 0 and sharpen the criteria.

Finish with a short summary for the user:

1. Counts at each stage (and a note on which boxes of the PRISMA diagram they fill).
2. The exclusion reasons table for full text (PRISMA asks for this).
3. The records flagged for the human (low-confidence exclusions, `UNCLEAR`, conflicts).
4. A suggested sentence for the methods section describing how screening was done. It must say honestly that an AI assistant was used and how its decisions were checked.

## Handling tricky cases

Read `references/edge-cases.md` when you meet any of these: records without abstracts, non-English papers, conference abstracts, protocols, reviews (include for citation chasing?), preprints and their published versions, retracted papers, mixed populations, secondary analyses of the same dataset, and grey literature.

## Files in this skill

- `scripts/prepare_records.py`: parse RIS/BibTeX/CSV, remove duplicates, and output `records.csv`.
- `scripts/screening_stats.py`: PRISMA counts, Cohen's κ, and the conflict list.
- `assets/screening_protocol_template.md`: the protocol template (criteria, reason codes, change log).
- `references/criteria-frameworks.md`: PICO/PEO/SPIDER/PCC, and how to write criteria you can check (with examples).
- `references/exclusion-reasons.md`: standard ordered exclusion codes and how to choose the primary reason.
- `references/output-formats.md`: the output blocks for chat for TAK and full-text decisions.
- `references/edge-cases.md`: decision guidance for borderline record types.
