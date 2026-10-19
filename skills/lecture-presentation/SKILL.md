---
name: lecture-presentation
description: Lớp "trình diễn" cho bài giảng đại học, dựa trên Chương 10 "Kỹ năng thuyết trình" (giáo trình Kỹ năng giao tiếp kinh doanh). Biến nội dung bài học đã có thành một bài giảng thu hút - mở đầu gây ấn tượng (12 cách), cấu trúc "Cái đinh", chuyển ý, kết luận đáng nhớ (9 cách), lời giảng kèm chỉ dẫn giọng nói và cử chỉ, nhịp tương tác, ngân hàng câu hỏi - và xuất "Bản thiết kế bài giảng" cho academic-pptx dựng slide. Dùng sau lesson-builder (teaching-skills) và trước academic-pptx; cũng chạy độc lập khi chưa có giáo án. Kích hoạt khi người dùng muốn bài giảng "ấn tượng", "thu hút", "có hook", "kịch bản giảng", "lời giảng cho slide", "speaker notes", "kỹ năng thuyết trình", "mở đầu/kết thúc bài giảng", "luyện giảng", hoặc yêu cầu kết hợp teaching-skills với academic-pptx để làm slide bài giảng.
---

# Kỹ năng thuyết trình cho bài giảng

Skill này là **lớp trình diễn** của bài giảng: lesson-builder quyết định _dạy gì và theo nhịp nào_, academic-pptx quyết định _slide trông thế nào_, còn skill này quyết định **giảng viên nói gì, nói thế nào, mở và kết ra sao để sinh viên chú ý và nhớ**. Cơ sở là Chương 10 – _Kỹ năng thuyết trình_: cấu trúc "Cái đinh" (mũi đinh sắc – thân đinh chắc – mũ đinh vững), 30 giây đầu, quy tắc Con số 3, nguyên tắc 3S, quy tắc thời gian, giọng nói và ngôn ngữ cơ thể. Nội dung đã được chuyển từ bối cảnh kinh doanh sang bối cảnh **giảng viên – sinh viên**.

## Vị trí trong chuỗi skill

```
teaching-skills / lesson-builder  →  lecture-presentation  →  academic-pptx (+ pptx)
  arc S1…Sn, outcomes,                 hook, kết luận, chuyển ý,     dựng .pptx: action title,
  lecture notes, slides outline,        lời giảng + chỉ dẫn trình     thiết kế, citation,
  activity sheets                       bày, Q&A → BẢN THIẾT KẾ       QA, Notes
```

- **Có artifact của lesson-builder** (`lessons/W<N>_lesson_plan.md`, `_lecture_notes.md`, `_slides_outline.md`, `_activity_*.md`): đọc chúng, **giữ nguyên** nội dung chuyên môn, timing và tiêu đề đã được giảng viên xác nhận; chỉ **bổ sung** lớp trình diễn. Mọi thay đổi so với artifact gốc phải được nêu ở checkpoint.
- **Chưa có**: nếu người dùng có cài teaching-skills, đề nghị chạy `lesson-builder` (mode `full`) trước. Nếu người dùng muốn làm luôn, chạy độc lập theo 6 bước dưới đây.
- **Dựng slide**: giao Bản thiết kế cho **academic-pptx** (đọc kèm skill pptx). `deck-studio` của teaching-skills là đường thay thế khi cần Marp/PDF/Beamer hoặc theme chung cho cả khóa học. Chỉ dùng **một** công cụ dựng slide cho mỗi bộ.

Hợp đồng chi tiết giữa các skill (đầu vào, đầu ra, cách giải quyết xung đột quy tắc) nằm ở `references/integration.md`. **Đọc file đó trước** khi chạy cùng hai skill kia.

## Quy tắc bắt buộc (tương thích teaching-skills)

1. **Không bịa.** Hook bằng số liệu, câu chuyện, trích dẫn, video là chỗ dễ bịa nhất. Số liệu hoặc trích dẫn chưa chắc chắn phải gắn `[VERIFY: <nội dung> — <lý do chưa chắc>]`. Câu chuyện hay ví dụ cần trải nghiệm thật của giảng viên thì gắn `[NEEDS PROFESSOR INPUT: <cần gì>]`. Tình huống giả định phải ghi rõ là giả định.
2. **Giảng viên quyết định.** Kết thúc bằng một checkpoint 4 khối (Produced / Key decisions / Flags / Open questions), theo `shared/checkpoint_protocol.md` của teaching-skills. Khi giảng viên nói "cứ làm đi", rút gọn checkpoint.
3. **Bám mục tiêu.** Mỗi hook, câu chuyện, hoạt động phải phục vụ một outcome của buổi học. Hook "vui nhưng lạc đề" là lỗi (sách: "xôi hỏng bỏng không").
4. **Ghi chỉ dẫn trình bày bằng chữ nghiêng trong ngoặc**, giống lecture_writer: _(dừng 3 giây)_, _(nhấn: "…")_, _(hỏi lớp: "…")_, _(hạ giọng)_, _(bước xuống giữa lớp)_. Không dùng ngoặc vuông cho chỉ dẫn. Ngoặc vuông chỉ dành cho các marker của teaching-skills (`[VERIFY]`, `[NEEDS PROFESSOR INPUT]`, `[BOARD]`, `[NEEDS CONTENT]`).

## Quy trình 6 bước

### Bước 1 – Xác định tình huống và mục tiêu

Nếu có `course_passport.yaml` hoặc lesson plan thì lấy từ đó: chủ đề, outcomes, `class_size`, `modality`, độ dài buổi học, `learner_profile.known_difficulties`. Không hỏi lại những gì đã có. Nếu không có thì hỏi gộp trong một lần: môn và chủ đề; đối tượng (năm học, ngành, kiến thức nền); sĩ số; thời lượng; hình thức và thiết bị; mục tiêu.

Trả lời 4 câu hỏi của sách: **Giảng cái gì? Giảng như thế nào** (cung cấp thông tin / thuyết phục / truyền cảm hứng)? **Sinh viên sẽ cảm nhận thế nào? Sinh viên sẽ thay đổi thế nào?**

Viết **thông điệp cốt lõi**: một câu ≤ 140 ký tự, kiểu headline của Steve Jobs. Đây là câu sinh viên phải nhớ khi ra về.

### Bước 2 – Phân tích thính giả và diễn giả

- **Sinh viên:** họ được gì từ bài này? Người nghe quan tâm đến chính họ chứ không quan tâm đến diễn giả, nên mọi thông điệp phải viết theo hướng "vì người nghe". Các khó khăn thường gặp (`known_difficulties`) là nguồn tốt nhất cho hook và cho phần trả lời trước quan niệm sai.
- **Sĩ số:** lớp nhỏ thì hỏi đáp cụ thể, mời phát biểu. Lớp đông thì bài giảng phần lớn là một chiều, nên phải rõ ràng, chính xác và dùng tương tác toàn lớp (giơ tay, bình chọn).
- **Văn hóa lớp:** hài hước phải đúng lúc, đúng mức. Với lớp quốc tế, tránh thành ngữ khó dịch.
- **Giảng viên:** thế mạnh phong cách (kể chuyện, số liệu, hài hước…) quyết định nên chọn hook nào. Nếu chưa biết thì hỏi ở phần Open questions.

### Bước 3 – Chọn lọc: "Bắt buộc → Cần → Nên"

- Gắn nhãn Bắt buộc / Cần / Nên cho các ý của từng segment. Đây là nền cho phương án co giãn thời gian: hết giờ thì cắt từ "Nên" lên. **Không bao giờ cắt kết luận/closure.**
- Thân bài có **3 ý chính** (tối đa 5), theo quy tắc Con số 3. Lý do: người nghe quên khoảng 40% sau 20 phút và khoảng 90% sau một tuần, nên cần ít ý và nhắc lại.
- Số liệu phải mới, có nguồn và được quy đổi về điều quen thuộc (ví dụ: va chạm ở 70 km/h tương đương rơi từ tầng 6). Nêu cả giới hạn và phản biện; bỏ qua rủi ro là một trong "5 yếu tố cản trở".

### Bước 4 – Dựng "Cái đinh" trên arc có sẵn

```
MŨI ĐINH  = activation + mở đầu   (30 giây đầu quyết định)
THÂN ĐINH = các segment input/active, 3 ý chính, chuyển ý chặt chẽ
MŨ ĐINH   = check + closure + kết luận (không bao giờ bị cắt)
```

**Mở đầu**: hook → (chào, giới thiệu ngắn ở buổi đầu hoặc khi có khách mời) → đề tài và ý nghĩa → **outcomes bằng lời của sinh viên** → dàn ý 3 ý → thỏa thuận cơ chế (khi nào hỏi, có thảo luận nhóm không). Chọn 1–2 hook trong `references/openings.md`. Nên ưu tiên hook **kiêm luôn activation** của lesson-builder (câu hỏi bất ngờ, dự đoán, giơ tay, câu đố về bài trước), để không tốn thêm phút. Không mở bằng câu khô khan kiểu "Hôm nay tôi rất vui…", cũng không mở bằng thông báo hành chính.

**Thân bài**: mỗi ý chính đi theo trình tự _nêu vấn đề → nội dung → nhấn trọng tâm → ví dụ → kết luận nhỏ → chuyển ý_. Chọn một bố cục logic: thời gian; nguyên nhân – kết quả; vấn đề – giải pháp; đối lập; lập luận – dẫn chứng. Mỗi lần chuyển ý cần một câu chuyển (mẫu trong `references/integration.md` §4) và một khoảng dừng. Rà lập luận theo `references/logic-and-reasoning.md`.

**Kết luận**: câu chuyển → tóm tắt 3 ý (phần quan trọng nhất) → closure hoặc check (phiếu 1 phút…) → liên hệ với nghề nghiệp/đời sống → câu kết (sound bite, quay về hook) → kêu gọi hành động và nối sang buổi sau. Slide cuối cùng là **slide Kết luận**, giữ nguyên trên màn hình suốt phần hỏi đáp. **Không kết bằng slide "Cảm ơn"** (quy tắc của academic-pptx và cũng là tinh thần "dừng đúng lúc" của sách). Xem `references/closings.md`.

### Bước 5 – Nhịp độ và tương tác

- **Tỉ lệ của sách (50% giảng – 25% người nghe tham gia – 25% dự phòng)** áp dụng nguyên văn cho **bài nói đơn lẻ** (seminar, báo cáo, bảo vệ). Với **buổi học** đã có arc của lesson-builder, áp dụng như sau: thời gian giảng viên nói **≤ 2/3**, sinh viên hoạt động **≥ 1/3**, slack 2–3 phút theo lesson-builder, còn phần "dự phòng" của sách trở thành **nội dung "Nên" có thể cắt** cộng với **phần mở rộng đã chuẩn bị sẵn**.
- Không giảng liền quá 20–25 phút mà không có hoạt động. Giữa các hoạt động, cứ khoảng 10 phút chèn một **"điểm chạm" ≤ 1 phút**: giơ tay, câu hỏi nhanh, dự đoán (xem `references/interactive-activities.md`).
- Thiết kế hoạt động dài (TPS, jigsaw, case…) là việc của `activity_designer` trong lesson-builder. Skill này chỉ lo phần **lời dẫn vào hoạt động, câu chuyển ra và cách phản hồi**.
- Chuẩn bị **ngân hàng câu hỏi**: 3–5 câu sinh viên dễ hỏi nhất, mỗi câu kèm câu trả lời và một slide phụ lục (theo quy ước Appendix của academic-pptx). Chủ động trả lời trước quan niệm sai: "Có thể các bạn đang nghĩ… Thực ra…".

### Bước 6 – Lời giảng và chỉ dẫn trình bày

- Viết **văn nói**: câu ngắn, từ phổ thông, giải thích thuật ngữ, không biệt ngữ. Phép thử: đọc to lên có giống người đang nói chuyện không?
- **Lượng lời ≈ thời lượng.** Lời giảng của mỗi slide phải nói vừa trong số phút đã giao (ước lượng bằng cách đọc to và bấm giờ). Thừa lời thì cắt nội dung, không nói nhanh hơn.
- Chèn chỉ dẫn _(…)_ ở đúng chỗ: dừng khoảng 3 giây khi chuyển ý và trước/sau ý quan trọng; hạ giọng khi sắp kết thúc một ý chính để nhấn mạnh; câu hỏi cho lớp; di chuyển; quét ánh mắt theo hình W/M. Giọng phải hợp với phòng, với người nghe và với ý (xem `references/delivery.md`).
- Khi lecture_writer đã viết lecture notes, **giữ nguyên câu chữ chuyên môn**. Chỉ thêm hook, câu chuyển, chỉ dẫn trình bày và rút gọn thành lời nói theo từng slide.

## Đầu ra

1. **Bản thiết kế bài giảng** – `lessons/W<N>_presentation_blueprint.md` (dùng tên khác nếu không theo tuần), viết theo `references/blueprint-template.md`. Mục C (kịch bản từng slide) là đầu vào trực tiếp cho academic-pptx: action title, phần hiển thị, exhibit, citation, speaker notes, segment ID.
2. **Checkpoint** 4 khối. Key decisions ghi: hook đã chọn, cách kết, các slide thêm hoặc sửa so với outline, phương án cắt. Flags ghi: các marker còn mở, phần thừa giờ, xung đột quy tắc.
3. Khi giảng viên xác nhận: chuyển sang academic-pptx. Nếu có passport, thêm đường dẫn blueprint vào `artifact_refs[]` của tuần đó (chỉ append, không ghi đè).

## Tự kiểm tra trước checkpoint

Chạy `references/evaluation-checklist.md`. Tối thiểu phải đạt:

- [ ] Một thông điệp cốt lõi; 3 (≤5) ý chính; mọi phần đều phục vụ outcome.
- [ ] Hook trong 30 giây đầu, đúng đề tài; mở đầu có outcomes và dàn ý.
- [ ] Mỗi chỗ chuyển ý có câu chuyển và _(dừng)_; kết luận đủ 4 yếu tố; slide cuối là Kết luận, không phải "Cảm ơn".
- [ ] Ghost deck test: chỉ đọc các action title theo thứ tự cũng thấy được toàn bộ lập luận của bài.
- [ ] Không giảng liền > 20–25 phút; có điểm chạm khoảng 10 phút một lần; sinh viên hoạt động ≥ 1/3 thời gian (buổi học) hoặc khoảng 25% (bài nói).
- [ ] Mật độ chữ đạt chuẩn chung ở `references/integration.md` §3; slide nội dung nào cũng có speaker notes.
- [ ] Không có số liệu hay câu chuyện bịa; marker `[VERIFY]`/`[NEEDS PROFESSOR INPUT]` được liệt kê đủ ở Flags; mọi thứ mượn đều có citation.
- [ ] Không lỗi lập luận; có nêu giới hạn/phản biện; có ngân hàng câu hỏi và slide phụ lục.

## Tài liệu tham chiếu

- `references/integration.md` – hợp đồng với lesson-builder, deck-studio, academic-pptx; bảng giải quyết xung đột; mẫu câu chuyển ý.
- `references/blueprint-template.md` – mẫu Bản thiết kế bài giảng.
- `references/openings.md` – 12 cách mở đầu, ghép với activation.
- `references/closings.md` – 4 yếu tố và 9 cách kết luận, ghép với closure và slide Kết luận.
- `references/interactive-activities.md` – điểm chạm của sách, đối chiếu với catalog 15 kỹ thuật của lesson-builder.
- `references/delivery.md` – giọng nói, ngôn ngữ cơ thể, 3S, phong cách Obama, 10 bí quyết, 5 yếu tố cản trở, vượt qua hồi hộp, luyện tập, công thức T-I-S.
- `references/logic-and-reasoning.md` – 4 phép lập luận, 8 lỗi lập luận.
- `references/evaluation-checklist.md` – tiêu chí đánh giá (tự rà soát hoặc cho sinh viên đánh giá chéo).
