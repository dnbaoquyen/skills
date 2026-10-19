# Thành phần đánh giá → assessment-architect

Đọc nguyên văn phần đánh giá của đề cương trước. **Hình thức, trọng số, thời điểm, tiêu chí và CLO lấy theo đề cương.** assessment-architect chỉ làm cụ thể hóa.

| Thành phần (theo đề cương)                                       | Mode của `assessment-architect`                 | Bộ hồ sơ tạo ra                                                                                                                                                   |
| ---------------------------------------------------------------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chuyên cần / tham gia                                            | `rubric` (single-point)                         | Tiêu chí tham gia quan sát được, có cách tham gia thay thế cho sinh viên ít phát biểu; phiên bản online                                                           |
| Bài tập cá nhân (một hoặc nhiều bài)                             | `project-brief` (mỗi bài một brief) + `rubric`  | Đề bài theo cấu trúc Mục đích – Nhiệm vụ – Tiêu chí; mốc nộp; rubric; gợi ý chấm; checklist tự kiểm tra                                                           |
| Bài tập nhóm / dự án nhóm                                        | `group-assessment` + `rubric`                   | Đề bài nhóm có sự phụ thuộc thật giữa các thành viên; vai trò; cơ chế đánh giá cá nhân; phiếu đánh giá chéo; rubric; mốc nộp; checklist                           |
| Thuyết trình (cá nhân/nhóm)                                      | `project-brief` + `rubric`                      | Đề bài + rubric dùng `lecture-presentation/references/evaluation-checklist.md` làm khung tiêu chí kỹ năng trình bày; phiếu đánh giá chéo                          |
| Tiểu luận / báo cáo                                              | `project-brief` + `rubric` + `integrity-check`  | Đề bài có dữ liệu riêng hoặc trải nghiệm cá nhân, các bước trung gian; rubric; checklist trình bày                                                                |
| Kiểm tra giữa kỳ / thi cuối kỳ: tự luận, trắc nghiệm, tình huống | `exam` (blueprint → câu hỏi → đáp án → thủ tục) | Blueprint nội dung × Bloom theo CLO; đề; **đáp án và thang điểm chi tiết**; tối thiểu 2 đề tương đương nếu hợp lý; hướng dẫn coi thi để `[NEEDS PROFESSOR INPUT]` |
| Kiểm tra thường xuyên                                            | `quiz` / `question-bank`                        | Bộ câu hỏi ngắn có đáp án, dùng cho điểm chạm và ôn tập                                                                                                           |

## Bắt buộc với mọi bài

1. **Đúng đề cương:** đúng trọng số, đúng hình thức, đúng tuần, đúng CLO. Lệch phải có lý do trong Flags.
2. **Rubric:** đề cương có rubric thì giữ nguyên văn các tiêu chí và mức điểm, chỉ bổ sung mô tả hành vi quan sát được cho từng mức (ghi "bổ sung"). Không có thì tạo mới, mỗi tiêu chí gắn CLO.
3. **Bền vững trước AI:** chạy `integrity-check` và đặt `ai_resilience`. Không khuyến nghị công cụ phát hiện AI.
4. **Checklist tự kiểm tra cho sinh viên:** `submission-auditor` mode `self-check`, sinh ra từ đề bài và rubric.
5. **Đáp án do agent tự giải độc lập** (`answer_key_agent`). Chỗ chưa chắc gắn `[VERIFY]`.
6. **Bài tập rèn luyện ở các buổi** (trong bộ rèn luyện kỹ năng) không tính điểm. Đó là bậc thang dẫn tới bài tính điểm: kỹ năng nào có trong bài giữa kỳ/cuối kỳ thì phải được luyện trước ở các buổi.
