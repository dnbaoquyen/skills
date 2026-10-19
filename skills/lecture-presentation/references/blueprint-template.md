# Mẫu đầu ra: Bản thiết kế bài giảng

File: `lessons/W<N>_presentation_blueprint.md`. Điền đủ các mục A–F, sau đó trình bày checkpoint (mục G).

- **Mục C** là đầu vào trực tiếp cho academic-pptx: mỗi khối là một slide. Trường "Speaker notes" đưa vào phần Notes của slide; trường "Hiển thị" và "Exhibit" là nội dung trên slide.
- Khi có artifact của lesson-builder, mỗi slide ghi rõ **Nguồn**:
  - `outline` – giữ nguyên tiêu đề và nội dung từ `W<N>_slides_outline.md`;
  - `outline+` – giữ nội dung, chỉ thêm notes;
  - `mới` – slide do skill này thêm (hook, chuyển phần, Kết luận, phụ lục).
- Marker `[VERIFY]`, `[NEEDS PROFESSOR INPUT]`, `[BOARD]` từ artifact gốc phải được giữ nguyên.

---

## A. Thông tin chung

- **Môn học / Chủ đề / Tuần:**
- **Nguồn:** lesson plan · lecture notes · slides outline · activity sheets (đường dẫn) — hoặc "chạy độc lập"
- **Đối tượng:** năm học, ngành, kiến thức nền, sĩ số · **Khó khăn đã biết:** (từ `known_difficulties`)
- **Thời lượng:** … phút · **Hình thức / phòng / thiết bị:**
- **Kiểu bài:** buổi học (theo arc) / bài nói đơn lẻ (theo quy tắc 75% của sách)
- **Mục đích:** cung cấp thông tin / thuyết phục / truyền cảm hứng
- **Outcomes** (nguyên văn từ passport hoặc lesson plan): (1) … (2) … (3) …
- **Thông điệp cốt lõi** (≤ 140 ký tự):
- **3 ý chính:** (1) … (2) … (3) …
- **Hook:** … — lý do; có kiêm activation không
- **Cách kết:** … — quay về hook bằng cách nào; kêu gọi hành động là gì

## B. Nhịp độ (bám arc của lesson-builder)

| Seg | Phút | Mode       | Phần "Cái đinh"    | Nội dung chính | Điểm chạm / hoạt động | Giảng viên nói |
| --- | ---- | ---------- | ------------------ | -------------- | --------------------- | -------------- |
| S1  |      | activation | Mũi đinh — hook    |                |                       |                |
| S2  |      | input      | Thân — ý 1         |                |                       |                |
| …   |      |            |                    |                |                       |                |
| Sn  |      | closure    | Mũ đinh — kết luận |                |                       |                |

Tổng: … phút (thời lượng trừ 2–3 phút slack) · Giảng viên nói … phút (≤ 2/3) · Sinh viên hoạt động … phút (≥ 1/3)

## C. Kịch bản từng slide

Lặp lại khối sau cho mỗi slide:

```
### Slide <số> · <Seg> · <loại: bìa | hook | outcomes | dàn ý | nội dung | hoạt động | chuyển phần | tóm tắt | Kết luận | References | Phụ lục> · Nguồn: <outline | outline+ | mới>
- Action title: <một câu khẳng định; slide cấu trúc được dùng nhãn>
- Hiển thị: <≤ 4 gạch, mỗi gạch ≤ ~8 từ, tổng ≤ 40 từ — hoặc 1 con số lớn / 1 câu hỏi>
- Exhibit: <hình/biểu đồ/sơ đồ: thể hiện gì, mắt nhìn vào đâu trước, chú thích "so what">; Alt text: <1 câu>
- Citation: <(Tác giả, năm) nếu là thứ mượn — hoặc "không">
- Hiện dần: <không | các bước …>
- Speaker notes (≈ <n> phút):
    <Lời giảng văn nói…> _(dừng 3 giây)_ <…> _(nhấn: "…")_ <…> _(hỏi lớp: "…" — chờ 5 giây)_
    Chuyển sang slide sau: "<câu chuyển>"
- Tương tác: <không | điểm chạm ≤ 1 phút: … | hoạt động: xem W<N>_activity_<tên>.md — lời dẫn vào: "…"; lời dẫn ra: "…">
- Marker: <[VERIFY …] / [NEEDS PROFESSOR INPUT …] / [BOARD …] — hoặc "không">
```

Thứ tự slide chuẩn:

1. Bìa
2. Hook (kiêm activation)
3. Outcomes ("Sau buổi này, các bạn có thể…")
4. Dàn ý 3 ý
5. Các slide nội dung và hoạt động của từng ý; slide dàn ý lặp lại ở mỗi lần chuyển phần, tô sáng ý sắp học (dùng làm section divider)
6. Tóm tắt / check / closure
7. **Kết luận** (2–4 ý chính + sound bite + kêu gọi hành động + nối sang buổi sau + liên hệ). Slide này giữ suốt Q&A; không có slide "Cảm ơn" sau nó.
8. References
9. Phụ lục Q&A

## D. Ngân hàng câu hỏi

| #   | Câu hỏi hoặc quan niệm sai dễ gặp | Trả lời ngắn | Xử lý (trả lời ngay / cuối buổi / trao đổi riêng) | Slide phụ lục |
| --- | --------------------------------- | ------------ | ------------------------------------------------- | ------------- |

Câu hỏi giảng viên đặt cho lớp (kiểm tra hiểu bài): …

## E. Co giãn thời gian

- **Thiếu … phút:** cắt (từ nhãn "Nên" lên) …; nói tóm tắt …; **không cắt** kết luận/closure
- **Dư … phút:** mở rộng bằng … (đã chuẩn bị sẵn: thêm ví dụ, debrief sâu hơn, câu hỏi phụ lục)

## F. Chuẩn bị và luyện giảng

- [ ] Xử lý hết `[VERIFY]` / `[NEEDS PROFESSOR INPUT]` (danh sách ở mục G)
- [ ] Tập to ít nhất 1–2 lần với slide, bấm giờ từng phần; ghi âm hoặc quay lại để tự xem
- [ ] Thẻ ghi ý chính (gạch đầu dòng, tô đậm); không đọc nguyên văn
- [ ] Đến sớm kiểm tra máy chiếu, âm thanh, video, đồng hồ đếm ngược, công cụ bình chọn
- [ ] Đạo cụ cho hook/hoạt động (đồ vật, ô chữ, thẻ màu, link)
- [ ] Bài tập thư giãn 2 phút trước giờ; nước uống
- [ ] Nhắc khi giảng: quét ánh mắt W/M, khoảng 3 giây mỗi người; dừng 3 giây khi chuyển ý; không quay lưng quá 2 giây; không đọc slide; hạ giọng ở câu chốt

## G. Checkpoint

```
## Checkpoint: Bản thiết kế bài giảng W<N>

**Produced:** lessons/W<N>_presentation_blueprint.md (<số> slide)
**Key decisions made for you (review these):**
- Hook: … — lý do
- Cách kết: … — lý do
- Slide thêm/sửa so với outline: …
- Phương án cắt khi thiếu giờ: …
**Flags:** <marker còn mở; segment vượt giờ; xung đột quy tắc đã xử lý theo integration.md §3 — hoặc "none">
**Open questions:** <câu chuyện hoặc ví dụ cần trải nghiệm thật của giảng viên; thế mạnh phong cách — hoặc "none">

Ready to proceed, or what should change?
```
