# Cấu trúc thư mục đầu ra

```
course_passport.yaml                     # schema teaching-skills
kit/
├── README.md                            # mục lục, cách dùng bộ học liệu
├── 00_REVIEW.md                         # 🧑 buổi duyệt duy nhất (checkpoint 4 khối)
├── 00_assumptions.md                    # sổ giả định
├── 00_source_map.md                     # trích đề cương + bản đồ giáo trình theo buổi
├── 00_alignment_matrix.md               # CLO × buổi × bài tập
├── PROGRESS.md                          # tiến độ theo lô (để tiếp tục khi bị gián đoạn)
├── W01/ … Wnn/                          # mỗi buổi một thư mục
│   ├── W01_bai_giang_chi_tiet.md (.docx)   # tài liệu chính cầm lên lớp
│   ├── W01_slides.pptx                     # Notes = lời giảng
│   ├── W01_ren_luyen_<ky-nang>.md (.docx)  # mỗi kỹ năng một bộ: checklist + hướng dẫn + bài tập
│   └── lesson-builder/                     # artifact gốc: lesson_plan, lecture_notes,
│       └── …                               #   slides_outline, activity_*, presentation_blueprint
└── assessments/
    ├── A1_<ten>/                        # mỗi thành phần đánh giá một thư mục
    │   ├── de_bai.md (.docx)               # cho sinh viên
    │   ├── rubric.md
    │   ├── dap_an_huong_dan_cham.md        # chỉ dành cho giảng viên
    │   ├── checklist_tu_kiem_tra.md        # cho sinh viên
    │   └── integrity_check.md
    └── …
course_dashboard.html                    # nếu có script của teaching-skills
```

Tên file không dấu, dùng gạch dưới; tiêu đề bên trong file viết tiếng Việt có dấu. File dành cho sinh viên và file chỉ dành cho giảng viên **không được để lẫn nội dung**: đáp án không bao giờ nằm trong file đề.
