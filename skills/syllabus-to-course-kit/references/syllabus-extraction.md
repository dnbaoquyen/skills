# Trích đề cương chi tiết học phần → Course Passport

Đề cương chi tiết ở các trường Việt Nam thường gồm những mục dưới đây (tên mục có thể khác nhau). Tìm theo **nội dung**, không theo số mục.

| Mục trong đề cương                                                                                             | Trích gì                                                          | Trường passport / file                                                                                                                |
| -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Thông tin chung (tên, mã, số tín chỉ, loại học phần, học phần tiên quyết/học trước, đối tượng, khoa phụ trách) | mã, tên, số TC, tiên quyết, ngành/năm                             | `course.code`, `title`, `credits`, `prerequisites`, `level`, `discipline`                                                             |
| Phân bổ thời gian (số tiết LT / TH / thảo luận / tự học)                                                       | tổng tiết, tiết mỗi buổi                                          | `course.contact_hours_per_week`, `course.weeks`, độ dài buổi                                                                          |
| Mô tả tóm tắt học phần                                                                                         | phạm vi, vai trò                                                  | `learner_profile.motivation_context` (bắt buộc hay tự chọn, vì sao ngành cần)                                                         |
| Mục tiêu học phần (CO)                                                                                         | mục tiêu tổng quát                                                | Ghi vào `kit/00_source_map.md`; dùng để viết phần ý nghĩa của từng buổi                                                               |
| Chuẩn đầu ra học phần (CLO), ma trận CLO–PLO                                                                   | từng CLO nguyên văn                                               | `learning_outcomes[]`: `id` = mã CLO trong đề cương, `statement` nguyên văn, `bloom_level` theo bảng dưới                             |
| Nội dung chi tiết theo chương/buổi/tuần (kèm CLO, tài liệu, hoạt động dạy – học)                               | chủ đề buổi, mục giáo trình, CLO, hoạt động đề cương yêu cầu      | `schedule[]`: `id` W1…, `topic`, `outcomes`; hoạt động bắt buộc ghi vào `kit/00_source_map.md`                                        |
| Phương pháp giảng dạy                                                                                          | thuyết giảng, thảo luận, tình huống, đóng vai, thuyết trình nhóm… | Ràng buộc khi chọn hoạt động; hình thức online/kết hợp → `course.modality`                                                            |
| Đánh giá học phần (thành phần, trọng số, hình thức, thời điểm, tiêu chí, CLO đánh giá, rubric)                 | **mọi chi tiết, nguyên văn**                                      | `assessment_plan[]`: `id` A1…, `type`, `title`, `weight`, `outcomes_assessed`, `week`; rubric nguyên văn lưu ở `kit/00_source_map.md` |
| Tài liệu học tập (chính, tham khảo)                                                                            | giáo trình chính, tài liệu khác                                   | `kit/00_source_map.md`; giáo trình chính là nguồn nội dung                                                                            |
| Quy định học phần (chuyên cần, nộp muộn, liêm chính, AI)                                                       | nguyên văn                                                        | `policies.*`; không có thì để `""` và ghi `[NEEDS PROFESSOR INPUT]`                                                                   |

## Quy đổi thời gian (mặc định, đề cương ghi khác thì theo đề cương)

- 1 tiết = 50 phút. Buổi học = số tiết của buổi × 50 phút (thường 3 tiết = 150 phút, có nghỉ giữa giờ).
- 1 tín chỉ lý thuyết ≈ 15 tiết; 1 tín chỉ thực hành/thảo luận ≈ 30 tiết. Chỉ dùng để suy ra số buổi khi đề cương không ghi lịch.
- Đề cương chia theo **chương** thay vì theo buổi: chia buổi theo số tiết của từng chương, ghi cách chia vào sổ giả định.
- Buổi dài hơn 120 phút: dùng mẫu "khối 3 giờ" của lesson-builder (2–3 chu kỳ, nghỉ 8–10 phút giữa các chu kỳ).

## Động từ CLO → Bloom

| Động từ trong CLO                                                                     | `bloom_level`                                                                                                           |
| ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| nhận biết, nhớ, liệt kê, nêu, kể tên, định nghĩa                                      | remember                                                                                                                |
| hiểu, giải thích, trình bày, mô tả, phân biệt (mức hiểu), tóm tắt, cho ví dụ          | understand                                                                                                              |
| vận dụng, áp dụng, thực hiện, sử dụng, xử lý tình huống, thực hành, rèn luyện         | apply                                                                                                                   |
| phân tích, so sánh, đối chiếu, phân loại, chẩn đoán                                   | analyze                                                                                                                 |
| đánh giá, nhận xét, phản biện, lựa chọn có lập luận, thẩm định                        | evaluate                                                                                                                |
| thiết kế, xây dựng, lập kế hoạch, sáng tạo, soạn thảo, tổ chức (một sản phẩm/sự kiện) | create                                                                                                                  |
| thái độ / tự chủ – trách nhiệm (tuân thủ, chủ động, hợp tác, tôn trọng)               | Ghi `bloom_level: apply`, kèm chú thích "CLO thái độ" trong `00_source_map.md`; đánh giá bằng quan sát hoặc tự đánh giá |

Nếu một CLO có nhiều động từ thì lấy mức **cao nhất** mà bài đánh giá thực sự đo.

## Thành phần đánh giá → `type`

| Đề cương ghi                                         | `type`        |
| ---------------------------------------------------- | ------------- |
| Chuyên cần, thái độ, tham gia                        | participation |
| Bài tập cá nhân, bài tập về nhà                      | homework      |
| Bài tập nhóm, dự án nhóm, đồ án                      | project       |
| Thuyết trình (cá nhân/nhóm)                          | presentation  |
| Tiểu luận, báo cáo                                   | paper         |
| Kiểm tra giữa kỳ / thi cuối kỳ: tự luận, trắc nghiệm | exam          |
| Kiểm tra ngắn, kiểm tra thường xuyên                 | quiz          |
| Hồ sơ học tập                                        | portfolio     |

Nếu đề cương ghi "giữa kỳ: thuyết trình nhóm" thì `type: presentation`, không phải `exam`. Hình thức theo đề cương luôn được ưu tiên.

## Kiểm tra sau khi trích

- Tổng trọng số = 100%. Nếu không bằng: ghi Flags, giữ nguyên số trong đề cương, không tự chia lại.
- CLO nào cũng xuất hiện ở ít nhất một buổi và một bài đánh giá. Nếu không: ghi Flags; Phase 2 xử lý như trong SKILL.md.
- Thông tin mâu thuẫn trong đề cương (số tiết, số buổi): chọn bảng chi tiết hơn và ghi lý do.
