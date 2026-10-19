# Cấu trúc file nội dung một buổi học (`kit/Wnn/_nguon/wnn_content.py`)

File Python, đọc bởi `scripts/build_session.py`. Đây là **nguồn duy nhất** của buổi học: sửa ở đây rồi dựng lại, không sửa tay file .pptx hay .md.

```bash
python3 scripts/build_session.py kit/W03/_nguon/w03_content.py kit/W03 W03
python3 scripts/qa_deck.py kit/W03/W03_slides.pptx --minutes 180     # phải thoát mã 0
```

## META (dict)

| Khóa                                 | Bắt buộc | Ý nghĩa                                                                                                                     |
| ------------------------------------ | -------- | --------------------------------------------------------------------------------------------------------------------------- |
| `code`, `course`, `session`, `topic` | ✓        | Mã và tên học phần, tên buổi, chủ đề                                                                                        |
| `minutes`                            | ✓        | Thời lượng buổi (phút)                                                                                                      |
| `minutes_note`                       |          | Ghi chú cạnh thời lượng, ví dụ "(giả định — xem 00_assumptions.md #2)"                                                      |
| `clo`, `gt`                          | ✓        | CLO của buổi; nguồn giáo trình (chương, trang)                                                                              |
| `core`                               | ✓        | Thông điệp cốt lõi (≤ 140 ký tự)                                                                                            |
| `ideas`                              | ✓        | 3 (tối đa 5) ý chính, dùng cho slide chia phần                                                                              |
| `outcomes`                           | ✓        | Mục tiêu buổi học, viết bằng lời của sinh viên                                                                              |
| `prep`, `flex`                       | ✓        | Danh sách chuẩn bị / co giãn thời gian. Dùng `{slide:Tiền tố tiêu đề}` để tự điền số slide, **không ghi số slide bằng tay** |
| `theme`                              |          | Giao diện (xem dưới). Không có thì dùng mặc định trung tính                                                                 |

### `theme`

```python
META["theme"] = dict(bg="172849", text="FBFAF4", title="FBFAF4", muted="AEB4C6", panel="22385F",
                     accents=["49B296", "FFD23B", "FF5178", "962B7C", "09A1E5", "FF9259"], font="Alexandria")
```

- `bg`: màu nền. `text`, `title`: màu chữ thân slide và tiêu đề. `muted`: màu nguồn trích và số trang. `panel`: màu ô nền phụ. `accents`: các màu trang trí, dùng xoay vòng theo từng phần của buổi học (dải màu bên trái, đầu dòng, ô, biểu đồ). `font`: phông chữ.
- Màu chữ trên ô màu được trình dựng **tự chọn** theo độ tương phản. Màu nhấn nào có độ tương phản dưới 4,5 so với nền thì chỉ dùng để trang trí, không dùng cho chữ.
- Giao diện là **sở thích của giảng viên hoặc nhà trường**. Đặt nó trong kit của môn (ghi vào `kit/00_assumptions.md`), không đặt trong skill.
- Phông chữ không có sẵn trong Office (ví dụ Alexandria) phải được cài trên máy trình chiếu; nếu không, PowerPoint sẽ thay bằng phông khác. Kiểm tra phông có đủ dấu tiếng Việt trước khi dùng.

## SLIDES (list các dict)

| Khóa       | Ý nghĩa                                                                                                                                                         |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `kind`     | `title` · `hook` · `content` · `outline` · `section` (cần `idx`) · `diagram` · `activity` · `figure` · `break` · `summary` · `conclusion` · `refs` · `appendix` |
| `part`     | Tên phần ("Mở đầu", "Ý 1", "Kết luận", "Phụ lục"…). Mỗi phần có một màu nhấn riêng                                                                              |
| `title`    | Câu khẳng định (action title); riêng slide cấu trúc được dùng nhãn                                                                                              |
| `body`     | ≤ 4 gạch, mỗi gạch ≤ 12 âm tiết, tổng ≤ 55 âm tiết                                                                                                              |
| `notes`    | Lời giảng văn nói; chỉ dẫn trình bày viết _(…)_; marker `[VERIFY: …]`, `[NEEDS PROFESSOR INPUT: …]`                                                             |
| `min`      | **Chỉ khai báo cho slide có hoạt động** (`interact`). Slide chỉ giảng được tính tự động từ lời giảng (130 âm tiết/phút + 0,3 phút mỗi chỉ dẫn dừng/hỏi lớp)     |
| `interact` | `{form, time, online, task, answer, out}` — hình thức, thời gian, phiên bản online/lớp đông, nhiệm vụ, đáp án/kỳ vọng, lời dẫn ra                               |
| `visual`   | Kiểu có sẵn: `bars:Nhãn                                                                                                                                         | số;…`·`chips`(dùng`body`+`heads`) · `steps:A | B   | C`·`twocol:Đầu | a;b |     | Đầu | c;d`·`grid:Tiêu đề | mô tả;…`(tối đa 4 ô). Tên khác → hàm`draw(slide, name, k)` trong file nội dung tự vẽ |
| `caption`  | Dòng chú thích dưới hình (thay cho chữ cố định trong trình dựng)                                                                                                |
| `alt`      | **Bắt buộc với slide có hình**: một câu mô tả hình cho thấy điều gì                                                                                             |
| `src`      | Nguồn hiển thị ở chân slide; marker `[VERIFY]` bị lọc khỏi slide và chỉ giữ trong notes                                                                         |
| `own_cite` | `True` nếu `draw()` tự ghi nguồn                                                                                                                                |
| `example`  | Ví dụ minh họa (đưa vào Notes và bài giảng chi tiết)                                                                                                            |
| `footer`   | Dòng chân trang của slide kết luận (liên hệ, kênh hỏi đáp)                                                                                                      |

## Hình riêng của môn học

Sơ đồ hay hình vẽ chỉ dùng cho một môn thì viết trong file nội dung của môn đó, **không** thêm vào `build_session.py`:

```python
def draw(slide, v, k):   # k: shape, tb, arrow, cite, MSO_SHAPE, on, ACCENTS, TEXT_ACCENTS, LIGHT, BODY, TITLE…
    if v == "model": ...
```

Dùng `k["ACCENTS"]` và `k["on"](màu_nền)` thay cho mã màu cố định, để hình tự đổi theo giao diện.
