#!/usr/bin/env python3
"""
@file        : scripts/recalc_dashboard.py
@description : بيعيد حساب جدول Progress Dashboard وسطر Overall Progress في PROJECT_TRACKER.md من شجرة المهام (المصدر الوحيد للحقيقة).
               المعادلة: Overall % = (✅ ÷ إجمالي المهام) × 100 — الـ 🟣 مش بيتحسب.
الاستخدام    : python scripts/recalc_dashboard.py --file PROJECT_TRACKER.md          (عرض الفروق فقط)
               python scripts/recalc_dashboard.py --file PROJECT_TRACKER.md --write  (تعديل الملف)
ملاحظة       : لو في Phase جديدة في الشجرة ومالهاش صف، بيضيف الصف قبل صف Σ تلقائياً (عند --write).
"""
import argparse
import re
import sys
from pathlib import Path

STATUS_RE = r"(⬜|🔵|🟣|✅|🔴|⏸\ufe0f?)"
ROW_RE = re.compile(r"^\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)%\s*\|$")
SIGMA_RE = re.compile(r"^\|\s*\*\*Σ\*\*\s*\|")


def parse(text):
    tasks, phases = {}, {}
    for line in text.splitlines():
        m = re.match(r"^Phase (\d+):\s*(.*?)\s*\.{3,}", line)
        if m:
            phases[int(m.group(1))] = m.group(2)
        m = re.match(r"^[├└]── (\d+)\.(\d+)\s+.*?\.{3,}\s*" + STATUS_RE, line)
        if m:
            tasks[(int(m.group(1)), int(m.group(2)))] = m.group(3).replace("\ufe0f", "")
    return tasks, phases


def stats(tasks):
    out = {}
    for ph in sorted(set(k[0] for k in tasks)):
        ts = [v for k, v in tasks.items() if k[0] == ph]
        tot, done = len(ts), ts.count("✅")
        out[ph] = dict(total=tot, done=done, impl=ts.count("🟣"), prog=ts.count("🔵"),
                       block=ts.count("🔴"), pct=round(done * 100 / tot) if tot else 0)
    return out


def main():
    ap = argparse.ArgumentParser(description="إعادة حساب Dashboard")
    ap.add_argument("--file", default="PROJECT_TRACKER.md")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    path = Path(args.file)
    text = path.read_text(encoding="utf-8")
    tasks, phases = parse(text)
    if not tasks:
        print("❌ مفيش مهام اتقرت من الشجرة (الصيغة: `├── N.M  الاسم ..... ⬜`)")
        sys.exit(1)
    st = stats(tasks)
    total = sum(s["total"] for s in st.values())
    done = sum(s["done"] for s in st.values())
    impl = sum(s["impl"] for s in st.values())
    prog = sum(s["prog"] for s in st.values())
    block = sum(s["block"] for s in st.values())
    overall = round(done * 100 / total) if total else 0

    lines = text.splitlines()
    existing, sigma_idx = {}, None
    for i, line in enumerate(lines):
        m = ROW_RE.match(line)
        if m:
            existing[int(m.group(1))] = (i, m.group(2))
        if SIGMA_RE.match(line):
            sigma_idx = i

    changed = False
    # تحديث الصفوف الموجودة
    for ph, (i, name) in existing.items():
        if ph not in st:
            continue
        s = st[ph]
        new = f"| {ph} | {name} | {s['total']} | {s['done']} | {s['impl']} | {s['prog']} | {s['block']} | {s['pct']}% |"
        if lines[i] != new:
            print(f"Phase {ph}: {lines[i]}\n      → {new}")
            lines[i] = new
            changed = True
    # إضافة Phases جديدة
    missing = [ph for ph in st if ph not in existing]
    if missing and sigma_idx is not None:
        add = []
        for ph in missing:
            s = st[ph]
            add.append(f"| {ph} | {phases.get(ph, '—')} | {s['total']} | {s['done']} | {s['impl']} | {s['prog']} | {s['block']} | {s['pct']}% |")
            print(f"+ Phase {ph} جديدة: {add[-1]}")
        lines[sigma_idx:sigma_idx] = add
        sigma_idx += len(add)
        changed = True
    elif missing:
        print("⚠️ في Phases جديدة بس مفيش صف Σ أضيف قبله — أضِف الصفوف يدوياً:", missing)
    # صف Σ
    if sigma_idx is not None:
        new_sigma = f"| **Σ** | | **{total}** | **{done}** | **{impl}** | **{prog}** | **{block}** | **{overall}%** |"
        if lines[sigma_idx] != new_sigma:
            print(f"Σ: {lines[sigma_idx]}\n   → {new_sigma}")
            lines[sigma_idx] = new_sigma
            changed = True
    # Overall Progress في Project Info
    for i, line in enumerate(lines):
        if "**Overall Progress**" in line:
            new = f"| **Overall Progress** | **{overall}%** ({done} / {total} مهمة ✅ Verified) |"
            if line != new:
                print(f"Overall: {line}\n      → {new}")
                lines[i] = new
                changed = True
            break

    print(f"\nالحقيقي: {done}/{total} ✅ = {overall}% · 🟣 {impl} · 🔵 {prog} · 🔴 {block}")
    if not changed:
        print("✅ الـ Dashboard مطابق للشجرة — مفيش تغيير.")
        return
    if args.write:
        path.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""), encoding="utf-8")
        print("📝 اتكتب في الملف.")
    else:
        print("ℹ️ ده عرض فقط — استخدم --write للتطبيق.")


if __name__ == "__main__":
    main()