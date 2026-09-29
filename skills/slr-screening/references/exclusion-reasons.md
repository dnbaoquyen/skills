# Exclusion reason codes

PRISMA 2020 asks for the number of full-text reports excluded **with reasons**. Each excluded report gets exactly **one primary reason**. To make that consistent, reasons are checked in a fixed order, and the first failing one is recorded.

## Recommended default order

Checking the cheap, objective criteria first makes the decisions reproducible:

| Order | Code                                    | Meaning                                                              | Tiếng Việt                                    |
| ----- | --------------------------------------- | -------------------------------------------------------------------- | --------------------------------------------- |
| 1     | `DUPLICATE`                             | Duplicate record, or the same report as one already screened         | Trùng lặp                                     |
| 2     | `PUB_TYPE`                              | Wrong publication type (editorial, letter, thesis, abstract only...) | Sai loại ấn phẩm                              |
| 3     | `LANGUAGE`                              | Language not eligible                                                | Ngôn ngữ không phù hợp                        |
| 4     | `DATE`                                  | Outside the date range                                               | Ngoài khoảng thời gian                        |
| 5     | `DESIGN`                                | Wrong study design (e.g. review, conceptual, non-empirical)          | Sai thiết kế nghiên cứu                       |
| 6     | `POPULATION`                            | Wrong population / sample                                            | Sai đối tượng / quần thể                      |
| 7     | `CONTEXT`                               | Wrong setting / country / context                                    | Sai bối cảnh                                  |
| 8     | `INTERVENTION` / `EXPOSURE` / `CONCEPT` | Wrong intervention, exposure, or concept                             | Sai can thiệp / yếu tố phơi nhiễm / khái niệm |
| 9     | `COMPARATOR`                            | Wrong or no comparator (only if required)                            | Sai nhóm so sánh                              |
| 10    | `OUTCOME`                               | Relevant outcome not measured or not reported                        | Không có kết cục phù hợp                      |
| 11    | `NO_DATA`                               | Eligible, but no usable data (results not separable, protocol only)  | Không có dữ liệu sử dụng được                 |
| 12    | `RETRACTED`                             | Retracted publication                                                | Bài bị rút                                    |

Adapt the list to the protocol. Map each code to a criterion ID (e.g. `POPULATION` ↔ C1), and write the final ordered list into `screening_protocol.md` **before** screening starts.

## Rules

- **TAK stage:** record a reason code for each exclusion too. PRISMA does not require reasons at TAK, but they help audit the decisions and find drift.
- **Full-text stage:** a single primary code in `reason_code`. Other failing criteria can go in `notes`, e.g. `also: OUTCOME`.
- **`UNCLEAR` is not an exclusion reason.** Resolve it (contact the authors, or discuss with the reviewer team) before the final counts. If it is still unresolved at the end, report those studies as "awaiting classification", which is how Cochrane handles them.
- **Reports not retrieved** (no full text available) are **not** exclusions. They are a separate box in PRISMA.
