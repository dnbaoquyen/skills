# Hợp đồng tích hợp: teaching-skills ↔ lecture-presentation ↔ academic-pptx

Viết dựa trên: `dnbaoquyen/teaching-skills` (lesson-builder, deck-studio, shared/*) và `dnbaoquyen/academic-pptx-skill` (SKILL.md, content_guidelines.md, slide_patterns.md). Nếu hai skill đó thay đổi tên file hoặc quy tắc, cập nhật file này.

## 1. Ai làm gì

| Việc                                                         | Chủ sở hữu                                 | lecture-presentation làm gì                                                                                 |
| ------------------------------------------------------------ | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| Outcomes, lịch tuần, passport                                | teaching-skills (`course-designer`)        | Chỉ đọc                                                                                                     |
| Arc buổi học S1…Sn, timing, contingency                      | lesson-builder (`lesson_planner_agent`)    | Chỉ đọc; đề xuất đổi timing **qua checkpoint**, không tự đổi                                                |
| Lecture notes (nội dung chuyên môn)                          | lesson-builder (`lecture_writer_agent`)    | Giữ nguyên câu chữ chuyên môn; thêm hook, câu chuyển, chỉ dẫn trình bày; rút gọn thành lời giảng theo slide |
| Slide outline (assertion title, figure spec, `[BOARD]`)      | lesson-builder (`slide_outliner_agent`)    | Giữ nguyên tiêu đề và evidence; thêm slide hook, slide chuyển phần, slide Kết luận; gắn speaker notes       |
| Hoạt động dài (activity sheet, launch script, failure modes) | lesson-builder (`activity_designer_agent`) | Chỉ thêm lời dẫn vào/ra và cách phản hồi; điểm chạm ≤ 1 phút thì tự thiết kế                                |
| Hook, kết luận, chuyển ý, giọng nói, cử chỉ, Q&A, luyện tập  | **lecture-presentation**                   | Sở hữu                                                                                                      |
| Dựng file .pptx, thiết kế, citation, QA                      | **academic-pptx** + skill pptx             | Giao Bản thiết kế (mục C) làm đầu vào                                                                       |
| Dựng Marp/PDF/Beamer, theme cả khóa                          | deck-studio (thay thế academic-pptx)       | Giao cùng Bản thiết kế; deck-studio coi nó là outline đã xác nhận                                           |

## 2. Luồng chạy chuẩn

```
1. lesson-builder  (mode full)  → W<N>_lesson_plan.md, _lecture_notes.md,
                                   _slides_outline.md, _activity_*.md   🧑 checkpoint
2. lecture-presentation         → W<N>_presentation_blueprint.md        🧑 checkpoint
3. academic-pptx (+ pptx)       → outline action titles                  🧑 xác nhận (>10 slide)
                                → W<N>_deck.pptx, QA, Notes = speaker notes
4. Luyện giảng                  → checklist mục F của blueprint
```

Trường hợp đặc biệt:

- Chỉ có lesson plan, chưa có slide outline: tự dựng mục C từ arc và lecture notes, mỗi slide gắn segment ID, và báo ở checkpoint là slide outline do skill này tạo.
- Không có teaching-skills: chạy độc lập 6 bước. Outcomes do giảng viên cung cấp, hoặc skill đề xuất rồi gắn `[NEEDS PROFESSOR INPUT: xác nhận outcomes]`.
- Giảng viên chỉ cần lời giảng cho một bộ slide có sẵn: đọc bộ slide, viết mục C (speaker notes) cùng mục D–F, rồi gợi ý sửa slide theo §3 dưới dạng Flags.

## 3. Bảng giải quyết xung đột quy tắc

Nguyên tắc chung: **khi hai quy tắc về khả năng đọc hoặc mật độ chữ khác nhau thì lấy quy tắc chặt hơn; về nội dung chuyên môn thì theo teaching-skills; về hình thức file thì theo academic-pptx.**

| Vấn đề                  | Sách (Chương 10)                                                | lesson-builder / deck-studio                                            | academic-pptx                                                                   | **Quy tắc áp dụng**                                                                                                                                                                             |
| ----------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mật độ chữ              | ≤ 6 gạch × ≤ 6 từ                                               | ≤ 4 dòng × ~8 từ (R4)                                                   | ~40 từ, 3–5 gạch                                                                | **≤ 4 gạch, mỗi gạch ≤ ~8 từ, tổng ≤ 40 từ; không viết câu đầy đủ** (tiếng Việt tính theo âm tiết: ≤ 12 âm tiết/gạch, ≤ 55 âm tiết/slide) (riêng action title và trích dẫn được viết thành câu) |
| Tiêu đề                 | Headline ngắn, chuyển tải ý chính                               | Assertion title                                                         | Action title + ghost deck test                                                  | **Action title là một câu khẳng định**; slide cấu trúc (bìa, dàn ý, chia phần) được phép dùng nhãn                                                                                              |
| Cỡ chữ                  | "Đủ lớn cho hàng cuối"                                          | Body ≥ 24pt, title ≥ 36pt                                               | Body ≥ 20pt, title 24–28pt                                                      | Dựng qua academic-pptx: **body ≥ 24pt** khi giảng ở giảng đường lớn hoặc chưa biết phòng; 20pt chỉ dùng cho phòng nhỏ đã biết. Title giữ 24–28pt theo academic-pptx                             |
| Hình ảnh                | "Hình hơn chữ", hình chất lượng cao                             | Không hình trang trí; figure là code, có alt text                       | Không icon hay ảnh stock; một exhibit mỗi slide; full-bleed chỉ ở bìa/chia phần | Hình phải **mang nội dung**. Hook bằng hình hay một con số lớn đặt trên slide hook (coi như slide chia phần). Mỗi figure có alt text                                                            |
| Slide cuối              | Câu kết ấn tượng; có thể chiếu credits cảm ơn                   | "What we established today" + nối sang buổi sau                         | Slide Kết luận ở cuối, giữ suốt Q&A, **không có "Thank You"**                   | **Slide Kết luận ở cuối**: 2–4 ý chính, sound bite, kêu gọi hành động, nối sang buổi sau, liên hệ/QR. Lời cảm ơn được **nói**, không làm slide. Credits (nếu cần) đặt trước slide Kết luận      |
| Thời gian               | Kế hoạch dùng 75%: 50% giảng, 25% người nghe                    | Tổng segment = thời lượng − 2–3 phút slack; input ≤ 20–25 phút mỗi đoạn | ≤ 1 slide/phút; kết thúc sớm 1–2 phút                                           | Buổi học: theo arc. Giảng viên nói ≤ 2/3, sinh viên ≥ 1/3; phần dự phòng là nội dung "Nên" cắt được. Bài nói đơn lẻ: theo tỉ lệ 75% của sách                                                    |
| Mở đầu                  | Hook trong 30 giây; chào, giới thiệu, đề tài, dàn ý, thỏa thuận | Activation 3–5 phút, thông báo để sau; slide outcomes ngay sau bìa      | Câu hỏi nghiên cứu ở slide 2–3                                                  | Hook kiêm activation → slide outcomes ("Sau buổi này, các bạn có thể…") → dàn ý 3 ý. Giới thiệu bản thân chỉ ở buổi đầu                                                                         |
| Hỏi đáp                 | 5–10 phút cho mỗi 1–2 giờ; chuẩn bị trước câu hỏi               | Check và closure không bao giờ bị cắt                                   | Appendix chứa slide Q&A dựng sẵn                                                | Ngân hàng câu hỏi (mục D) + slide phụ lục cho 3–5 câu dễ gặp nhất; Q&A diễn ra trên slide Kết luận                                                                                              |
| Chỉ dẫn trong lời giảng | Dừng, nhấn, hạ giọng, cử chỉ                                    | Lời ghi chú nghiêng _(pause here…)_                                     | —                                                                               | _(…)_ in nghiêng; không dùng ngoặc vuông                                                                                                                                                        |
| Số liệu và trích dẫn    | Phải đúng và mới nhất; "sai số liệu" là lỗi nghiêm trọng        | `[VERIFY]`, không bịa                                                   | Citation ngay trên slide + slide References                                     | Gắn `[VERIFY]` đến khi giảng viên xác nhận; citation 12–14pt cuối slide; có slide References                                                                                                    |
| Animation               | (không đề cập)                                                  | Chỉ hiện dần cho ví dụ giải từng bước (R6)                              | Không trang trí                                                                 | Chỉ dùng hiện dần cho các bước lời giải hoặc lần lượt từng ý trong 3 ý; không hiệu ứng chuyển cảnh                                                                                              |

## 4. Mẫu câu chuyển ý (đặt trong speaker notes)

- Mở → ý 1: "Để trả lời câu hỏi lúc nãy, ta đi qua 3 bước. Bước thứ nhất…" _(dừng 3 giây, chỉ vào dàn ý)_
- Ý → ý: "Trên đây chúng ta đã thấy… Câu hỏi tiếp theo là…"
- Vào hoạt động: "Giờ đến lượt các bạn. Trong 3 phút, …" (sau đó đọc **launch script** từ activity sheet)
- Ra hoạt động: "Tôi nghe được hai hướng trả lời… Cả hai dẫn ta đến…"
- Vào kết luận: "Nói tóm lại…" / "Sau những gì đã phân tích, có thể kết luận…"
- Câu kết quay về hook: "Quay lại con số / câu chuyện / câu hỏi lúc đầu buổi…"

## 5. Đối chiếu tên gọi

| Chương 10                | lesson-builder          | academic-pptx                  |
| ------------------------ | ----------------------- | ------------------------------ |
| Mở đầu / mũi đinh / hook | Activation (S1)         | Title + Motivation             |
| Mục tiêu, dàn ý          | Outcomes slide          | Research question slide        |
| Thân bài / 3 vấn đề      | Input + active segments | Methods / Results              |
| Ví dụ minh họa           | Worked example          | Exhibit + "so what" annotation |
| Kết luận / mũ đinh       | Check + Closure         | Conclusions slide              |
| Ngân hàng câu hỏi        | (contingency)           | Appendix Q&A slides            |
| Headline / thông điệp    | Assertion title         | Action title / ghost deck      |
