#!/usr/bin/env python3
"""QA tự động cho một bộ slide bài giảng (.pptx) — chỉ đọc file .pptx, dùng được cho mọi môn.

Quy ước mà deck cần tuân theo (do syllabus-to-course-kit sinh ra):
  - Dòng đầu speaker notes: "[<phần> · <số> phút]"; phần "Phụ lục" không tính giờ.
  - Slide có hoạt động: notes chứa "TƯƠNG TÁC (".
  - Loại slide ghi ở thuộc tính name của p:cSld (title/section/break/conclusion = slide cấu trúc);
    deck không có thông tin này thì đoán theo nền màu đặc.

Ngưỡng tính theo ÂM TIẾT (tách theo khoảng trắng). Một "từ" tiếng Anh ≈ 1,5 âm tiết tiếng Việt:
  ≤ 4 gạch/slide · ≤ 12 âm tiết/gạch · ≤ 55 âm tiết thân slide · chữ ≥ 20pt (trừ nguồn trích, số trang)
  Độ tương phản chữ/nền ≥ 4,5 (chữ lớn ≥ 3) — WCAG AA.
  Thời lượng slide chỉ giảng ≈ ceil(âm tiết lời giảng / 130 + 0,3 × số chỉ dẫn dừng/hỏi lớp);
  lệch quá ±1 phút → lời giảng quá mỏng (hụt giờ) hoặc quá dày (lố giờ).

Dùng: python3 qa_deck.py deck.pptx [--minutes 180]
Thoát: 0 = không có lỗi chặn · 1 = có lỗi chặn
"""
import argparse, math, re, sys
from collections import Counter
from pptx import Presentation

ap = argparse.ArgumentParser()
ap.add_argument("deck"); ap.add_argument("--minutes", type=int, default=None)
a = ap.parse_args()
prs = Presentation(a.deck)
W, H = prs.slide_width, prs.slide_height
EMU = 914400
issues = []
BLOCK = {"S1", "S2", "M1", "L1", "N3", "F1", "A1", "C1"}

def flag(i, code, msg): issues.append((i, code, msg))
def syl(t): return len(re.findall(r"\w+", t))
def _lum(h):
    v = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    v = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in v]
    return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2]
def _ratio(a, b):
    la, lb = sorted((_lum(a), _lum(b)), reverse=True); return (la + 0.05) / (lb + 0.05)
def slide_bg(sl):
    c = sl._element.xpath("./p:cSld/p:bg//a:srgbClr/@val"); return c[0] if c else "FFFFFF"
def fill_of(sh):
    c = sh._element.xpath("./p:spPr/a:solidFill/a:srgbClr/@val"); return c[0] if c else None
def has_bg(sl):
    # Đọc XML trực tiếp: truy cập sl.background sẽ tự tạo <p:bg> và làm sai kết quả.
    return bool(sl._element.xpath("./p:cSld/p:bg"))

rows = []
for i, sl in enumerate(prs.slides, 1):
    notes = sl.notes_slide.notes_text_frame.text if sl.has_notes_slide else ""
    m = re.match(r"\[(.+?) · (\d+) phút\]", notes)
    part, mins = (m.group(1), int(m.group(2))) if m else ("?", 0)
    inter = "TƯƠNG TÁC (" in notes
    kind = sl._element.cSld.get("name") or ""
    struct = kind in ("title", "section", "break", "conclusion") if kind else has_bg(sl)
    texts = [sh for sh in sl.shapes if sh.has_text_frame and sh.text_frame.text.strip()]
    def _size(sh):
        r = [r.font.size.pt for p in sh.text_frame.paragraphs for r in p.runs if r.font.size and r.text.strip() and not r.text.strip().isdigit()]
        return max(r) if r else 0
    head = [t for t in texts if struct or t.top < int(1.6 * EMU)] or texts
    title = max(head, key=lambda s: (_size(s), -s.top)) if head else None  # chữ lớn nhất ở phần đầu slide = tiêu đề
    body = [sh for sh in texts if sh is not title and sh.top < int(6.8 * EMU) and not re.fullmatch(r"\d+", sh.text_frame.text.strip())]
    rows.append(dict(i=i, part=part, mins=mins, inter=inter, struct=struct, title=title.text_frame.text if title else ""))
    if not notes.strip(): flag(i, "N3", "thiếu speaker notes")
    if not m and part != "Phụ lục": flag(i, "N4", "notes thiếu dòng đầu [phần · N phút]")
    # Mật độ chữ (chỉ slide nội dung)
    refs = "tham khảo" in (title.text_frame.text.lower() if title else "")
    if not struct and part != "Phụ lục" and not refs:
        bullets = [p.text for sh in body for p in sh.text_frame.paragraphs if p.text.startswith("•")]
        if len(bullets) > 4: flag(i, "D1", f"{len(bullets)} gạch đầu dòng (>4)")
        long = [b for b in bullets if syl(b) > 12]
        if long: flag(i, "D2", f"{len(long)} gạch >12 âm tiết: «{long[0][3:]}»")
        tot = sum(syl(sh.text_frame.text) for sh in body)
        if tot > 55: flag(i, "D3", f"{tot} âm tiết thân slide (>55)")
        if title and syl(title.text_frame.text) < 5: flag(i, "T1", "tiêu đề quá ngắn — có thể là nhãn chủ đề, không phải câu khẳng định")
    # Bố cục, cỡ chữ
    for sh in sl.shapes:
        if sh.left is not None and (sh.left + sh.width > W + 5000 or sh.top + sh.height > H + 5000):
            flag(i, "L1", f"hình/khung vượt mép slide ({sh.name})")
        if not sh.has_text_frame: continue
        for p in sh.text_frame.paragraphs:
            for r in p.runs:
                t = r.text.strip()
                if not t or r.font.size is None: continue
                cite = t.startswith(("Nguồn", "Phỏng theo")) or re.fullmatch(r"\d+", t) or sh.top > int(6.8 * EMU)
                if r.font.size.pt < 20 and not cite and not struct:
                    flag(i, "F1", f"chữ {r.font.size.pt:.0f}pt (<20): «{t[:40]}»")
    # Độ tương phản chữ/nền (WCAG AA: 4,5 chữ thường; 3 chữ ≥ 24pt hoặc ≥ 18,5pt đậm)
    bg = slide_bg(sl)
    for sh in sl.shapes:
        if not sh.has_text_frame: continue
        under = fill_of(sh) or bg
        for p in sh.text_frame.paragraphs:
            for r in p.runs:
                if not r.text.strip() or r.font.color is None or r.font.color.type is None: continue
                try: fg = str(r.font.color.rgb)
                except AttributeError: continue
                big = r.font.size is not None and (r.font.size.pt >= 24 or (r.font.bold and r.font.size.pt >= 18.5))
                need = 3.0 if big else 4.5
                if _ratio(fg, under) < need:
                    flag(i, "C1", f"tương phản {_ratio(fg, under):.1f} < {need} (#{fg} trên #{under}): «{r.text.strip()[:30]}»")
    vis = " ".join(sh.text_frame.text for sh in sl.shapes if sh.has_text_frame)
    if "[VERIFY" in vis: flag(i, "M1", "marker [VERIFY] hiện trên slide — chỉ để trong notes")
    # Alt text cho slide có hình/sơ đồ (≥3 autoshape không chứa chữ dài)
    shapes = [sh for sh in sl.shapes if sh.shape_type == 1]
    if len(shapes) >= 3 and not struct:
        if not any(sh._element.xpath("./*[1]/p:cNvPr/@descr") for sh in sl.shapes):
            flag(i, "A1", "slide có sơ đồ/hình nhưng chưa có alt text")
    # Lời giảng ↔ thời lượng
    if mins and not inter and not struct:
        first = re.sub(r"^\[.*?\]", "", notes.split("\n\n")[0])
        pauses = len(re.findall(r"\((dừng|hỏi lớp|chờ)", first))
        spoken = re.sub(r"\(.*?\)", "", first)
        expect = max(1, math.ceil(syl(spoken) / 130 + 0.3 * pauses))
        if mins > expect + 1: flag(i, "N1", f"{mins} phút nhưng lời giảng chỉ đủ ~{expect} phút ({syl(spoken)} âm tiết) — hụt giờ")
        if mins < expect - 1: flag(i, "N2", f"{mins} phút nhưng lời giảng cần ~{expect} phút — lố giờ")

# Cấu trúc
main = [r for r in rows if r["part"] != "Phụ lục"]
concl = [r for r in rows if r["part"] == "Kết luận"]
if not any("tham khảo" in r["title"].lower() or "references" in r["title"].lower() for r in rows):
    flag(0, "S2", "thiếu slide Tài liệu tham khảo")
if concl and main and main[-1]["i"] != concl[-1]["i"] and "tham khảo" not in main[-1]["title"].lower():
    flag(0, "S1", "slide nội dung cuối không phải Kết luận/Tài liệu tham khảo")
gap = mx = 0
for r in main:
    if r["inter"] or r["part"] == "Nghỉ": mx = max(mx, gap); gap = 0
    else: gap += r["mins"]
mx = max(mx, gap)
if mx > 20: flag(0, "P1", f"đoạn giảng liên tục {mx} phút không có tương tác (>20)")
total = sum(r["mins"] for r in main)
if a.minutes and not (0.75 * a.minutes <= total <= a.minutes - 3):
    flag(0, "P2", f"tổng kế hoạch {total}/{a.minutes} phút (nên trong khoảng 75% đến thời lượng − 3 phút)")
act = sum(r["mins"] for r in main if r["inter"])

print("== Ghost deck ==")
for r in main: print(f"{r['i']:>2} {r['title']}")
print(f"\nTổng {total} phút · có tương tác {act} phút ({act*100//max(total,1)}%) · {len(rows)} slide")
print(f"== {len(issues)} vấn đề: {dict(Counter(c for _, c, _ in issues))} ==")
for i, c, msg in issues: print(f"slide {i:>2} [{c}]{' CHẶN' if c in BLOCK else ''} {msg}")
sys.exit(1 if any(c in BLOCK for _, c, _ in issues) else 0)
