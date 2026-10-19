---
name: syllabus-to-course-kit
description: Từ ĐỀ CƯƠNG CHI TIẾT HỌC PHẦN + GIÁO TRÌNH, tự động tạo trọn bộ học liệu cho cả môn - bài giảng chi tiết từng buổi (nội dung trình chiếu, lời giảng, ví dụ minh họa, câu hỏi và hoạt động tương tác ngắn để thu hút chú ý), file slide .pptx, checklist + hướng dẫn + bài tập rèn luyện từng kỹ năng, và hệ thống bài tập cá nhân, bài tập nhóm, giữa kỳ, cuối kỳ kèm rubric và đáp án theo đúng phần đánh giá của đề cương. Điều phối teaching-skills (teaching-pipeline, course-designer, lesson-builder, assessment-architect, submission-auditor), lecture-presentation và academic-pptx; không hỏi thêm giảng viên ngoài hai tài liệu, mọi giả định được ghi vào sổ giả định. Kích hoạt khi người dùng gửi đề cương và giáo trình và muốn "soạn cả môn", "làm bộ học liệu", "từ đề cương ra bài giảng", "soạn bài giảng và bài tập theo đề cương", "chuẩn bị học phần".
---

# Từ đề cương + giáo trình → bộ học liệu hoàn chỉnh

**Hợp đồng với giảng viên:** giảng viên đưa **hai tài liệu**: đề cương chi tiết học phần và giáo trình. Skill trả về **toàn bộ học liệu** mà không hỏi thêm. Thông tin nào hai tài liệu không có thì xử lý bằng **mặc định ghi rõ** hoặc bằng **thiết kế chịu được nhiều tình huống** (ví dụ: hoạt động co giãn theo sĩ số). Không bao giờ bịa thông tin. Giảng viên đọc lại tất cả ở **một** buổi duyệt duy nhất cuối cùng.

## Phụ thuộc

| Skill                                                                                                                            | Vai trò                                                                  | Nếu thiếu                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| teaching-skills (plugin: `teaching-pipeline`, `course-designer`, `lesson-builder`, `assessment-architect`, `submission-auditor`) | Lập passport, giáo án, bài giảng chi tiết, hoạt động, đề và rubric       | Dừng và hướng dẫn cài: `/plugin marketplace add dnbaoquyen/teaching-skills` rồi `/plugin install teaching-skills` |
| `lecture-presentation`                                                                                                           | Lớp thu hút chú ý: mở đầu, chuyển ý, kết luận, lời giảng, tương tác ngắn | Vẫn chạy được nhưng báo rằng bài giảng sẽ thiếu lớp trình diễn                                                    |
| `academic-pptx` + `pptx`                                                                                                         | Dựng file .pptx                                                          | Chỉ xuất bản thiết kế dạng Markdown; nói rõ là chưa có file .pptx                                                 |
| `docx` (tùy chọn)                                                                                                                | Xuất bài giảng chi tiết và bài tập ra .docx                              | Giao Markdown                                                                                                     |

## Chế độ chạy: một lượt, chỉ duyệt một lần

- Theo Checkpoint Protocol của teaching-skills, chế độ này tương đương giảng viên đã nói **"cứ làm đi"**: các checkpoint trung gian rút gọn thành ghi chú trong `kit/00_REVIEW.md`, không dừng lại hỏi.
- **Ngoại lệ duy nhất được dừng:** khi hai tài liệu không đọc được, không phải đề cương/giáo trình, hoặc mâu thuẫn đến mức không thể chọn một cách hợp lý (ví dụ: tổng trọng số khác 100% mà không rõ thành phần nào sai). Khi đó hỏi **một** câu duy nhất, kèm phương án mặc định.
- Các quy tắc bắt buộc của teaching-skills vẫn giữ nguyên:
  - nội dung chuyên môn chưa chắc chắn → `[VERIFY: …]`;
  - thông tin thể chế không có trong đề cương (ngày thi, quy chế…) → `[NEEDS PROFESSOR INPUT: …]`;
  - không đưa dữ liệu sinh viên vào passport;
  - không khuyến nghị công cụ phát hiện AI.

## Quy trình

```
Phase 0 ĐỌC       đề cương → bảng trích (references/syllabus-extraction.md)
                  giáo trình → bản đồ chương (references/textbook-mapping.md)
Phase 1 PASSPORT  course_passport.yaml + kit/00_assumptions.md + kit/00_source_map.md
Phase 2 RÀ SOÁT   Gate 1.5 chỉ đọc (course-designer align-check): đề cương là văn bản đã
                  được duyệt → KHÔNG sửa outcomes/trọng số; lệch → ghi Flags
Phase 3 BUỔI HỌC  với từng buổi (theo lô 3–4 buổi):
                  lesson-builder full → lecture-presentation blueprint →
                  bài giảng chi tiết (templates/detailed-lecture.md) →
                  academic-pptx → .pptx → bộ rèn luyện kỹ năng (templates/skill-practice-kit.md)
Phase 4 BÀI TẬP   mỗi thành phần đánh giá trong đề cương → assessment-architect
                  (references/assessment-routing.md) + rubric + đáp án + integrity-check
                  + submission-auditor self-check (checklist tự kiểm tra cho sinh viên)
Phase 5 ĐÓNG GÓI  kit/README.md (mục lục), ma trận CLO × buổi × bài tập,
                  danh sách marker, dashboard → kit/00_REVIEW.md  🧑 DUYỆT MỘT LẦN
```

### Phase 0 – Đọc

- Đọc **toàn bộ** đề cương. Trích theo bảng trong `references/syllabus-extraction.md`: thông tin học phần, CLO và mức Bloom, nội dung từng buổi/chương, số tiết lý thuyết/thực hành, phương pháp, **đánh giá** (thành phần, trọng số, hình thức, tiêu chí, rubric nếu có), tài liệu.
- Đọc giáo trình theo các chương mà đề cương dẫn chiếu. PDF scan thì đọc theo trang, mỗi lần tối đa 20 trang. Lập bản đồ theo `references/textbook-mapping.md`: khái niệm, quy trình/kỹ năng, ví dụ, câu chuyện, số liệu, câu hỏi ôn tập, kèm **số trang** để trích dẫn.
- Giáo trình là **nguồn nội dung chuyên môn chính**. Dùng ví dụ ngoài giáo trình thì gắn `[VERIFY]`, trừ kiến thức phổ thông chắc chắn.

### Phase 1 – Passport

- Ghi `course_passport.yaml` theo schema của teaching-skills (`shared/course_passport_schema.md`). Trường nào không trích được thì để `null`/`"unknown"` trong passport: **không ghi phỏng đoán như sự thật**. Giá trị dùng để thiết kế được ghi trong `kit/00_assumptions.md` (theo `references/defaults-and-assumptions.md`).
- Nếu có `scripts/check_passport.py` thì chạy để kiểm tra. Lỗi thì sửa; không sửa được thì ghi vào Flags.

### Phase 2 – Rà soát căn chỉnh

- Chạy kiểm tra căn chỉnh **chỉ đọc**. Các lệch thường gặp: CLO không có bài đánh giá nào; buổi không gắn CLO; trọng số không đủ 100%; hai bài lớn cùng một tuần; một bài chiếm quá 40%.
- Đề cương là văn bản đã được duyệt, nên **không tự sửa**. Khi thiết kế buổi học và bài tập, ưu tiên lấp khoảng trống ở mức có thể (ví dụ: CLO chưa có bài đánh giá thì đưa vào một bài tập rèn luyện không tính điểm), và ghi lại cả lệch lẫn cách xử lý.

### Phase 3 – Từng buổi học

Với mỗi buổi trong `schedule`:

1. `lesson-builder` mode `full`: giáo án, lecture notes, slide outline, phiếu hoạt động. Nội dung lấy từ các trang giáo trình đã ánh xạ.
2. `lecture-presentation`: bản thiết kế bài giảng. Gồm phần mở đầu kiêm khởi động, chuyển ý, điểm chạm khoảng 10 phút một lần, slide Kết luận, ngân hàng câu hỏi.
3. Gộp thành **bài giảng chi tiết** theo `templates/detailed-lecture.md`. Đây là tài liệu giảng viên cầm lên lớp: mỗi slide có nội dung trình chiếu, lời giảng, ví dụ minh họa, câu hỏi/hoạt động, thời lượng, trang giáo trình.
4. Viết nội dung buổi vào `kit/Wnn/_nguon/wnn_content.py` theo `templates/session-content-schema.md`, rồi dựng slide và bài giảng chi tiết bằng `scripts/build_session.py`. Các quy tắc nội dung và thiết kế của academic-pptx vẫn áp dụng: action title, mỗi slide một exhibit, citation, slide Kết luận là slide cuối, slide Tài liệu tham khảo. Lời giảng nằm trong Notes; marker `[VERIFY]` chỉ có trong Notes và bài giảng chi tiết, không hiện trên slide.
   - **Kiểm tra bắt buộc:** chạy `scripts/qa_deck.py <deck> --minutes <thời lượng>` cho đến khi thoát mã 0. Sau đó render slide thành ảnh và xem lại bằng mắt. Cảnh báo không chặn (ví dụ D1 với bố cục hai cột) phải có lý do ghi trong `00_REVIEW.md`.
   - **Lời giảng phải đủ cho thời lượng.** Giảng bằng tiếng Việt khoảng 130 âm tiết/phút. Thời lượng slide chỉ giảng được tính từ lời giảng, không ước bằng tay. Tổng kế hoạch phải đạt ít nhất 75% thời lượng buổi; nếu thiếu, bổ sung phần đề cương yêu cầu (phương pháp học, kiểm tra nhanh, ví dụ cho kiến thức cốt lõi), không nói độn.
   - **Giao diện** (màu, phông) lấy theo yêu cầu của giảng viên, ghi trong `META["theme"]` và `00_assumptions.md`. Không có thì dùng mặc định trung tính.
5. **Bộ luyện tập** theo `templates/skill-practice-kit.md`, cho mỗi CLO chính của buổi. Dạng bộ luyện tập **phụ thuộc vào loại nội dung**, không phụ thuộc vào môn:
   - kỹ năng hoặc quy trình (thuyết trình, đàm phán, lập kế hoạch, thực hành thí nghiệm…): checklist hành vi + hướng dẫn từng bước + bài tập từ nhận diện đến vận dụng;
   - tính toán hoặc giải bài (kế toán, thống kê, lập trình…): lời giải mẫu từng bước → bài tập bớt dần gợi ý → bài tự giải; checklist là các bước kiểm tra lời giải;
   - khái niệm hoặc lý thuyết (luật, lịch sử, lý thuyết kinh tế…): câu hỏi hiểu → phân tích tình huống → lập luận; checklist là tiêu chí của một câu trả lời tốt.

   Một buổi có thể có nhiều dạng; ghi rõ dạng đã chọn trong file.

Chạy theo lô 3–4 buổi. Sau mỗi lô, cập nhật `kit/PROGRESS.md` để nếu phiên bị gián đoạn có thể **tiếp tục từ passport** mà không làm lại.

### Phase 4 – Hệ thống bài tập

- Mỗi thành phần đánh giá của đề cương đi theo `references/assessment-routing.md` đến mode tương ứng của `assessment-architect`:
  - bài tập cá nhân → `project-brief`;
  - bài tập nhóm → `group-assessment` (có cơ chế đánh giá đóng góp cá nhân và phiếu đánh giá chéo);
  - giữa kỳ / cuối kỳ → `exam` (blueprint → câu hỏi → đáp án) hoặc `project-brief` (tiểu luận, thuyết trình), **đúng hình thức đề cương quy định**.
- Rubric: đề cương có rubric thì dùng **nguyên văn**, chỉ bổ sung mô tả mức độ quan sát được và ghi rõ phần bổ sung. Không có thì `rubric_designer` tạo mới.
- Mỗi bài có: đề bài cho sinh viên, hướng dẫn, rubric, đáp án hoặc gợi ý chấm, checklist tự kiểm tra trước khi nộp (`submission-auditor` mode `self-check`). Chạy `integrity-check` cho từng bài.

### Phase 5 – Đóng gói và duyệt

- `kit/README.md`: mục lục toàn bộ học liệu theo cấu trúc ở `references/output-structure.md`.
- `kit/00_alignment_matrix.md`: ma trận CLO × buổi × bài tập (dấu ✓, kèm đường dẫn).
- `kit/00_REVIEW.md`: buổi duyệt duy nhất, theo định dạng checkpoint 4 khối. Gồm:
  - **Produced:** số file theo từng loại.
  - **Key decisions:** tối đa khoảng 7 quyết định quan trọng nhất đã đặt mặc định thay giảng viên.
  - **Flags:** lệch đề cương; danh sách gộp toàn bộ `[VERIFY]` và `[NEEDS PROFESSOR INPUT]` kèm đường dẫn file:dòng.
  - **Open questions:** chỉ những điều cần giảng viên mới trả lời được (câu chuyện thật, quy chế trường…).
- Nếu có `scripts/build_dashboard.py` thì dựng `course_dashboard.html`.

## Quy tắc chất lượng

1. **Bám đề cương:** mỗi buổi, mỗi slide nội dung, mỗi bài tập đều gắn CLO. Không dạy chủ đề ngoài đề cương. Phần mở rộng phải ghi rõ là "Nên" và được phép cắt.
2. **Bám giáo trình:** trích ý (không chép nguyên trang) và ghi số trang trong speaker notes và slide References. Trích nguyên văn chỉ dùng cho định nghĩa ngắn, có ngoặc kép và số trang.
3. **Thu hút chú ý:** mọi buổi đều có phần mở đầu trong 30 giây đầu, điểm chạm khoảng 10 phút một lần, không giảng liền quá 20–25 phút, có slide Kết luận (không kết bằng "Cảm ơn").
4. **Được luyện chứ không chỉ được nghe:** mỗi CLO chính của buổi có thời gian thực hành trên lớp và có bộ luyện tập phù hợp với loại nội dung (xem Phase 3 bước 5).
5. **Không mang thói quen của môn này sang môn khác:** mọi chi tiết riêng của một môn (ví dụ, thuật ngữ, rubric, cách chia buổi) chỉ nằm trong thư mục `kit/` và passport của môn đó, không bao giờ được ghi vào file của skill.
6. **Script dùng chung không chứa nội dung của môn nào.** Chữ, chú thích, hình riêng của môn chỉ nằm trong file nội dung của buổi (`caption`, `footer`, `draw()`). Khi sửa `scripts/`, tìm trong script tên môn và thuật ngữ của môn đang làm để chắc không có gì lọt vào.
7. **Không giả định ngầm:** mọi mặc định đều nằm trong `kit/00_assumptions.md` và các quyết định quan trọng nằm trong `00_REVIEW.md`.

## Tài liệu tham chiếu

- `references/syllabus-extraction.md` – các mục của đề cương chi tiết theo mẫu Việt Nam → trường passport; quy đổi tiết; ánh xạ động từ CLO → Bloom.
- `references/textbook-mapping.md` – cách lập bản đồ giáo trình theo buổi.
- `references/defaults-and-assumptions.md` – giá trị mặc định khi đề cương không ghi và cách thiết kế chịu được nhiều tình huống.
- `references/assessment-routing.md` – thành phần đánh giá → mode của assessment-architect.
- `references/output-structure.md` – cây thư mục đầu ra.
- `templates/detailed-lecture.md` – bài giảng chi tiết một buổi.
- `templates/skill-practice-kit.md` – checklist + hướng dẫn + bài tập rèn luyện một kỹ năng.
- `templates/session-content-schema.md` – cấu trúc file nội dung một buổi (META, SLIDES, theme, hình riêng).
- `scripts/build_session.py` – dựng .pptx (Notes = lời giảng) và bài giảng chi tiết .md từ file nội dung.
- `scripts/qa_deck.py` – kiểm tra tự động: mật độ chữ (theo âm tiết), cỡ chữ, tương phản WCAG, alt text, marker lộ trên slide, lời giảng so với thời lượng, nhịp tương tác, slide Kết luận và Tài liệu tham khảo.
