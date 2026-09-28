---
name: slr-search-strategy
description: Guides a reproducible, step-by-step systematic literature review (SLR) search phase - framing the research question (PICO/PICOC/SPIDER), building concept blocks and synonym lists, writing database-specific Boolean search strings (Scopus, Web of Science, PubMed, IEEE Xplore, ACM DL, ScienceDirect, Google Scholar), validating them against a gold-standard set, defining inclusion/exclusion criteria, and logging everything per PRISMA 2020 / PRISMA-S. Use when the user mentions systematic review, SLR, scoping review, mapping study, search string, search strategy, inclusion/exclusion criteria, PRISMA, or "lược khảo có hệ thống", "chuỗi tìm kiếm", "tiêu chí chọn lọc".
---

# SLR Search Strategy & Selection Criteria

Help the user design the **search and selection phase** of a systematic literature review so that another researcher could rerun it and get the same records. Work step by step, stop at each checkpoint for the user's confirmation, and produce files (not just chat text) that go into the review's protocol.

Reply in the user's language (e.g. Vietnamese), but keep search strings, database field codes and standard terms (PICO, PRISMA, etc.) in their original form.

## Guiding principles

1. **Reproducibility first** - every decision (term added/removed, filter, date, hit count) is written to the search log with a date and rationale.
2. **Sensitivity over precision** in the search; precision comes later from screening criteria.
3. **Never invent hit counts or papers.** If you cannot run the query yourself, give the string and ask the user to paste back the number of results.
4. **One concept per block**, OR within a block, AND between blocks.
5. **Criteria must be operational** - a second reviewer must be able to apply each one to a title/abstract without asking you what it means.

## Workflow

### Step 1 - Frame the question

Ask for (or propose) the research question(s) and pick a framework:

| Framework | Best for                                 | Elements                                                          |
| --------- | ---------------------------------------- | ----------------------------------------------------------------- |
| PICO      | Clinical / intervention studies          | Population, Intervention, Comparison, Outcome                     |
| PICOC     | Software engineering, IS, social science | + Context (Kitchenham & Charters guideline)                       |
| SPIDER    | Qualitative / mixed methods              | Sample, Phenomenon of Interest, Design, Evaluation, Research type |
| PCC       | Scoping reviews (JBI)                    | Population, Concept, Context                                      |

Output: RQs + a filled framework table. Decide which elements become **search blocks** (usually 2-3; Comparison and Outcome are often better handled by screening, not by the search string).

**Checkpoint:** user confirms RQs and blocks.

### Step 2 - Build concept blocks

For each block, collect:

- Synonyms, acronyms, spelling variants (US/UK), singular/plural, older terminology
- Controlled vocabulary where available (MeSH for PubMed, Emtree for Embase, IEEE/ACM CCS terms)
- Truncation candidates (`adopt*`) - check they do not explode into noise (`art*` is bad)
- Phrase searching for multi-word terms (`"machine learning"`)
- Proximity operators where supported (`W/3` Scopus, `NEAR/3` WoS)

Sources for terms: the user's seed papers (titles, abstracts, author keywords), existing reviews on the topic, thesauri. Ask the user for 5-15 **known relevant papers (gold-standard set)** now; they are needed in Step 4.

Output: `concept-blocks.md` using `templates/concept-blocks.md`.

### Step 3 - Write the search strings

Write one generic Boolean string, then translate it per database. Key syntax differences:

| Database       | Field / syntax                                                 | Notes                                                    |
| -------------- | -------------------------------------------------------------- | -------------------------------------------------------- |
| Scopus         | `TITLE-ABS-KEY( ... )`, `W/n`, `PRE/n`, `*`                    | Limits: `PUBYEAR > 2014`, `LIMIT-TO(DOCTYPE,"ar")`       |
| Web of Science | `TS=( ... )`, `NEAR/n`, `*`                                    | `TS` = title, abstract, author keywords, Keywords Plus   |
| PubMed         | `term[tiab]`, `term[MeSH Terms]`, `*`                          | Combine MeSH + free text; check Automatic Term Mapping   |
| IEEE Xplore    | `("All Metadata":term)` or `("Abstract":term)`                 | Max ~ 40 terms / 7 wildcards per query - split if needed |
| ACM DL         | `Abstract:(term)`, `Title:(term)`                              | Choose "ACM Full-Text collection" vs "Guide" explicitly  |
| ScienceDirect  | Title-Abs-Key field, **no wildcards**, max 8 Boolean operators | Usually needs to be split into several queries           |
| Google Scholar | Max 256 chars, no truncation, only first 1000 results viewable | Use only as supplementary source; record it as such      |

Rules:

- Parenthesise every block; put phrases in straight double quotes.
- Keep a **generic** version and one **per-database** version, all in `search-strings.md` (`templates/search-strings.md`).
- Record filters separately from the string (years, language, document type, subject area) with a justification for each.

**Checkpoint:** user runs each string and reports hit counts; you record them.

### Step 4 - Validate and iterate

1. Check the gold-standard set: for each known paper, is it (a) indexed in the database, (b) retrieved by the string?
2. **Recall (sensitivity)** = retrieved gold papers / indexed gold papers. Aim for >= 90%; below that, find which block missed the paper and add terms.
3. Check precision on a random sample of ~50 hits (how many look relevant?). If very low, tighten with proximity, field restriction, or a NOT only if it demonstrably removes no gold papers.
4. Log each iteration: version number, change, reason, hit count per database, recall.

Optionally recommend a peer review of the strategy using the **PRESS 2015** checklist.

**Checkpoint:** user freezes the final version; record the exact search date per database.

### Step 5 - Define inclusion/exclusion criteria

Derive criteria directly from the framework elements plus practical limits. Give each an ID so screening decisions can cite it (e.g. `EC3`).

- **Inclusion (IC):** population/context, intervention/phenomenon, study type, outcome reported, publication type (peer-reviewed?), language, date range - each with justification.
- **Exclusion (EC):** mirror images plus: duplicates, no full text, secondary studies (unless included), short papers < N pages, extended versions superseded by a journal version, etc.
- Split into **title/abstract stage** criteria and **full-text stage** criteria.
- Define the **quality assessment** instrument now if the protocol needs one (e.g. CASP, MMAT, Kitchenham QA checklist), separate from eligibility.

Output: `selection-criteria.md` (`templates/selection-criteria.md`).

### Step 6 - Screening procedure (for reproducibility)

Propose, and let the user adjust:

- Tools: Rayyan, Covidence, ASReview, or a spreadsheet; dedup in Zotero/EndNote with rules written down.
- **Pilot/calibration:** two reviewers screen the same 20-50 records, compute Cohen's kappa, refine ambiguous criteria until kappa >= 0.6 (substantial agreement), log changes.
- Independent dual screening (or dual on a random 20% sample if resources are limited), conflicts resolved by discussion or a third reviewer.
- Supplementary searching: backward/forward snowballing (Wohlin 2014), with iterations logged.
- Record numbers at every stage for the **PRISMA 2020 flow diagram** (identified per database, duplicates removed, screened, excluded with reasons by EC-ID, full-text assessed, included).

### Step 7 - Deliverables

Produce / update these files in a `slr/` folder (or where the user wants):

- `protocol-search.md` - RQs, framework, databases and rationale, final strings, filters, dates
- `concept-blocks.md`, `search-strings.md`, `selection-criteria.md`
- `search-log.csv` (`templates/search-log.csv`) - one row per executed query
- A PRISMA-S checklist summary noting where each item is reported

Suggest registering the protocol (PROSPERO for health topics, OSF Registries otherwise) before screening starts.

## References to cite in the protocol

- Page et al. (2021) PRISMA 2020 statement. BMJ 372:n71
- Rethlefsen et al. (2021) PRISMA-S extension for reporting literature searches. Systematic Reviews 10:39
- McGowan et al. (2016) PRESS Peer Review of Electronic Search Strategies: 2015 guideline. J Clin Epidemiol 75:40-46
- Kitchenham & Charters (2007) Guidelines for performing SLRs in software engineering. EBSE-2007-01
- Wohlin (2014) Guidelines for snowballing in systematic literature studies. EASE '14
- Cooke, Smith & Booth (2012) Beyond PICO: the SPIDER tool. Qual Health Res 22(10)
