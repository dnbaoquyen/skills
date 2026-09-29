# Output formats for chat

Keep the chat output short and put the full detail in the CSV files. Use the formats below when showing individual decisions, e.g. during calibration or when the user asks about one record. Translate the labels into the user's language. The Vietnamese versions are shown here.

## TAK decision (one record)

```
[R014] Title of the paper (2021)
Quyết định (Decision): MAYBE → chuyển sang sàng lọc toàn văn   | Độ tin cậy: medium
  C1 Đối tượng      yes      "survey of 412 bank customers in Hanoi"
  C2 Yếu tố         yes      "perceived risk, trust and usefulness"
  C3 Kết cục        unclear  abstract says "digital banking" – not clear if mobile app
  C4 Bối cảnh       yes      "Hanoi"
  C5 Thiết kế       yes      "PLS-SEM"
  C6 Ấn phẩm        yes      journal article, 2021, English
Lý do: C3 chưa rõ → giữ lại để đọc toàn văn.
```

## Full-text decision (one record)

```
[R014] Title of the paper (2021) – full text, 18 pp.
Quyết định: EXCLUDE   | Mã lý do chính: CONCEPT (C3)   | Độ tin cậy: high
  C1 yes  p.6 Methods: "412 retail customers aged 18–60"
  C2 yes  p.4 Table 1: hypotheses H1–H6 (PU, PEOU, trust, risk...)
  C3 no   p.5: "digital banking refers to internet banking via desktop browsers"
  C4 yes  p.6: "Hanoi and Ho Chi Minh City"
  C5 yes  p.7: survey + PLS-SEM
  C6 yes
Ghi chú: Nghiên cứu về internet banking trên máy tính, không phải mobile banking.
```

## Batch progress line

```
Đợt 3/12 (R061–R090): 7 INCLUDE · 5 MAYBE · 18 EXCLUDE (DESIGN 8, CONCEPT 6, CONTEXT 4) · 2 cần người kiểm tra (low-confidence exclude: R072, R088)
```

## End-of-stage summary

```
SÀNG LỌC TAK – HOÀN TẤT
Số bản ghi được sàng lọc:        n = 1,248
  Loại ở vòng TAK:               n = 1,061
  Chuyển sang toàn văn:          n = 187   (INCLUDE 94, MAYBE 93)
Cần người nghiên cứu xem lại:    n = 23    → xem cột notes = "REVIEW" trong tak_screening.csv
```

## Suggested wording for the methods section (adapt; keep it honest)

> Records were screened in two stages, title/abstract/keywords followed by full text, against pre-specified eligibility criteria (Supplementary Table S1). An AI assistant (name/version) was used as a [second reviewer / first-pass screener] and gave a recommendation with supporting text for each criterion. All [exclusions / disagreements / a random X% sample] were checked by [reviewer initials], and disagreements were resolved by discussion [with a third reviewer]. Agreement between the AI assistant and the human reviewer was κ = X.XX at the title/abstract stage and κ = X.XX at the full-text stage.
