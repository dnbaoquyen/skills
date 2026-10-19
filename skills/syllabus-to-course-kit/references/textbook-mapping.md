# Bản đồ giáo trình theo buổi

Mục đích: mỗi buổi học có một **gói nguồn** để lesson-builder và lecture-presentation viết nội dung **từ giáo trình**, không viết từ trí nhớ.

## Cách đọc

- Chỉ đọc các chương và mục mà đề cương dẫn chiếu. Nếu đề cương chỉ ghi "Chương 3" thì đọc cả chương.
- PDF scan: đọc theo trang, mỗi lần tối đa 20 trang. PDF có lớp chữ thì trích văn bản trước cho nhanh.
- Ghi **số trang in trên sách** (không phải số trang của file PDF) để trích dẫn đúng.

## Gói nguồn cho mỗi buổi (`kit/00_source_map.md`, một mục cho mỗi buổi)

```
### W<n> – <chủ đề> · CLO: … · Giáo trình: Chương X, tr. a–b
- Khái niệm cốt lõi: <thuật ngữ> — định nghĩa ngắn (tr. …)
- Quy trình / kỹ năng: <tên> — các bước (tr. …)          ← nguồn cho bộ rèn luyện kỹ năng
- Phân loại / mô hình / khung: … (tr. …)
- Ví dụ, tình huống, câu chuyện có sẵn: … (tr. …)         ← ưu tiên dùng làm minh họa và mở đầu
- Số liệu, trích dẫn danh nhân: … (tr. …) — ghi chú nếu đã cũ, cần [VERIFY] khi trình chiếu
- Lỗi thường gặp / điều nên tránh: … (tr. …)              ← nguồn cho quan niệm sai và checklist
- Câu hỏi ôn tập cuối chương: … (tr. …)                   ← nguồn cho câu hỏi tương tác và đề
- Nội dung nhạy cảm cần tránh trên lớp: … (nếu có)
```

## Quy tắc

- **Cái gì có trong giáo trình thì dùng giáo trình.** Ví dụ hay số liệu ngoài giáo trình chỉ dùng khi giáo trình không có hoặc đã cũ, và phải gắn `[VERIFY]`.
- Số liệu trong giáo trình có thể đã lỗi thời. Khi đưa lên slide, ghi năm của số liệu và gắn `[VERIFY: cập nhật số liệu mới]` nếu chúng hơn khoảng 5 năm.
- Ví dụ trong giáo trình không phù hợp với lớp học (nhạy cảm, quá cũ, ngoài ngữ cảnh sinh viên) thì thay bằng tình huống giả định, ghi rõ là "tình huống giả định".
- Một buổi mà giáo trình không có nội dung tương ứng (đề cương dẫn tài liệu khác không được cung cấp): ghi `[NEEDS PROFESSOR INPUT: tài liệu cho W<n>]`, vẫn dựng khung buổi học, và gắn `[VERIFY]` cho mọi nội dung chuyên môn.

## Khi giảng viên chưa ghép chương với buổi

Thường gặp: giáo trình nhiều tập, đánh số chương liên tục (1–21), trong khi đề cương đánh số chương theo môn (1–10). **Không được giả định "chương n của đề cương = chương n của giáo trình".**

1. Đọc **đề cương trước**, lấy danh sách nội dung từng buổi.
2. Với **mọi** file giáo trình, đọc trang tên chương và danh mục mục ở trang đầu. Nên dựng một ảnh ghép trang đầu của tất cả các file để đọc một lần.
3. Ghép buổi với chương theo **nội dung**, ghi mức tin cậy (Cao / TB / Chưa có) vào `kit/00_chapter_map.md`. Một buổi có thể lấy từ nhiều chương; một chương có thể không thuộc buổi nào.
4. Nội dung đề cương yêu cầu nhưng giáo trình không có mục riêng (ví dụ "rào cản" chỉ nằm rải rác trong nhiều trang): tổng hợp từ các trang liên quan và **ghi rõ trên slide là phần tổng hợp**, không gán cho giáo trình.

## Tải tài liệu từ Google Drive

- File scan không trả về chữ qua công cụ đọc của Drive; phải tải file PDF về rồi đọc từng trang.
- Công cụ tải của Drive giới hạn 10 MB. File lớn hơn thì nhờ giảng viên chia sẻ thư mục "Bất kỳ ai có đường liên kết – Người xem", rồi tải trực tiếp. Nhắc giảng viên tắt chia sẻ khi xong.
- Kiểm tra từng file sau khi tải (`pdfinfo`). File hỏng thì thử sửa bằng `pikepdf`; nếu trang vẫn trống thì ghi vào Flags và xin giảng viên tải lên lại, không đoán nội dung chương.
