# Mặc định và thiết kế chịu được nhiều tình huống

Hai tài liệu thường **không** cho biết những thông tin dưới đây. Skill không hỏi mà xử lý theo cột thứ ba và ghi lại vào `kit/00_assumptions.md`. Passport giữ `null`/`"unknown"`, không ghi giá trị mặc định như sự thật.

| Thông tin                    | Thường lấy được từ             | Nếu không có: xử lý thế nào                                                                                                                                                                   |
| ---------------------------- | ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sĩ số                        | Hiếm khi có                    | Thiết kế cho **30–80 sinh viên**. Mỗi hoạt động ghi cách co giãn: < 30 (cả lớp), 30–80 (cặp/nhóm 4–6), > 80 (bình chọn, cặp đôi tại chỗ)                                                      |
| Hình thức (trực tiếp/online) | Mục phương pháp                | **Trực tiếp** là phương án chính; mỗi hoạt động có một dòng "Phiên bản online" (chat, poll, phòng chia nhóm)                                                                                  |
| Độ dài buổi                  | Phân bổ tiết                   | Số tiết × 50 phút; không có thì 3 tiết = 150 phút                                                                                                                                             |
| Trình độ, kiến thức nền      | Đối tượng, học phần tiên quyết | Suy từ năm học và học phần tiên quyết; ghi "suy luận"                                                                                                                                         |
| Khó khăn thường gặp          | Không có                       | Lấy từ phần "lỗi thường gặp" của giáo trình; ghi "suy từ giáo trình"                                                                                                                          |
| Lịch học, ngày thi           | Không có                       | Dùng W1…Wn; mọi ngày tháng ghi `[NEEDS PROFESSOR INPUT]`                                                                                                                                      |
| Quy định về AI, nộp muộn     | Đôi khi                        | Không có thì để `[NEEDS PROFESSOR INPUT]`. Bài tập vẫn được thiết kế bền vững trước AI (gắn với trải nghiệm cá nhân, có bước trung gian, có phần vấn đáp hoặc trình bày)                      |
| Mẫu slide của trường         | Không có                       | Giao diện mặc định trung tính của `build_session.py`; giảng viên yêu cầu màu/phông nào thì ghi vào `META["theme"]`                                                                            |
| Mẫu đề thi                   | Không có                       | Mẫu đề và đáp án của assessment-architect; có ghi chú để thay bằng mẫu của khoa                                                                                                               |
| Mức chi tiết lời giảng       | —                              | **Viết đầy đủ như kịch bản** bằng văn nói, đủ lời cho thời lượng của slide (giảng viên có thể rút gọn)                                                                                        |
| Ngôn ngữ                     | Ngôn ngữ của đề cương          | Theo đề cương; thuật ngữ chuyên ngành có thêm tiếng Anh trong ngoặc ở lần đầu xuất hiện                                                                                                       |
| Ví dụ minh họa               | Giáo trình                     | Giáo trình trước; sau đó là bối cảnh doanh nghiệp và đời sống Việt Nam gần với sinh viên; tình huống giả định thì ghi rõ                                                                      |
| Câu chuyện cá nhân để mở đầu | Không có                       | Chọn cách mở đầu không cần trải nghiệm riêng (câu hỏi, dự đoán, số liệu từ giáo trình, đồ vật). Đặt một ô `[NEEDS PROFESSOR INPUT: câu chuyện thật về …]` như **phương án thay thế tùy chọn** |
| Công cụ dựng slide           | —                              | academic-pptx (+ pptx)                                                                                                                                                                        |
| Định dạng tài liệu           | —                              | Markdown làm nguồn; .pptx cho slide; .docx cho bài giảng chi tiết và bài tập nếu có skill docx                                                                                                |

## Mẫu `kit/00_assumptions.md`

```
| # | Thông tin | Giá trị đã dùng | Căn cứ (đề cương mục … / giáo trình tr. … / mặc định) | Ảnh hưởng đến | Đổi thì phải làm lại gì |
```

Đánh dấu ★ những giả định có ảnh hưởng lớn (sĩ số, hình thức, độ dài buổi). Những mục này phải xuất hiện ở phần Key decisions của `00_REVIEW.md`.
