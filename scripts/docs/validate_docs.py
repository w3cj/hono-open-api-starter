#!/usr/bin/env python3
"""
@file        : scripts/validate_docs.py
@description : فحص اتساق الملفات الخمسة (AI_INSTRUCTIONS / ARCHITECTURE / SPECKIT / PLAN / PROJECT_TRACKER)
               بدون أي اعتماد خارجي. بيكشف: ملفات ناقصة، Headers تالفة، مفردات حالة غلط، عدم تطابق IDs بين PLAN و Tracker،
               عدم تطابق Dashboard، ADR/CL/SPEC مرجعها مش معرّف، أكتر من مهمة 🔵.
الاستخدام    : python scripts/validate_docs.py --root <مجلد الملفات> [--strict] [--json]
خروج         : 0 = سليم (أو تحذيرات فقط) · 1 = فيه أخطاء (أو تحذيرات مع --strict)
"""
import argparse
import json
import re
import sys
from pathlib import Path

FILES = ["AI_INSTRUCTIONS.md", "ARCHITECTURE.md", "SPECKIT.md", "PLAN.md", "PROJECT_TRACKER.md"]
STATUS_RE = r"(⬜|🔵|🟣|✅|🔴|⏸\ufe0f?)"
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class Report:
    def __init__(self):
        self.items = []  # (level, code, message)

    def add(self, level, code, msg):
        self.items.append((level, code, msg))

    def err(self, code, msg):
        self.add("ERROR", code, msg)

    def warn(self, code, msg):
        self.add("WARN", code, msg)

    def info(self, code, msg):
        self.add("INFO", code, msg)

    def count(self, level):
        return sum(1 for i in self.items if i[0] == level)


def norm_status(s):
    return s.replace("\ufe0f", "")


def read_all(root: Path, rep: Report):
    texts = {}
    for f in FILES:
        p = root / f
        if not p.exists():
            rep.err("F001", f"الملف مش موجود: {f}")
            continue
        texts[f] = p.read_text(encoding="utf-8")
    return texts


def check_headers(texts, rep):
    for f, t in texts.items():
        head = "\n".join(t.splitlines()[:14])
        for tag in ("@file", "@description", "@updated"):
            if tag not in head:
                rep.err("H001", f"{f}: الـ Header ناقص `{tag}` في أول 14 سطر")
        m = re.search(r"@updated\*\*\s*:\s*`(\[.*\])`", head)
        if not m:
            rep.err("H002", f"{f}: مش قادر أقرأ @updated كـ JSON داخل backticks")
            continue
        try:
            arr = json.loads(m.group(1))
        except json.JSONDecodeError as e:
            rep.err("H003", f"{f}: @updated JSON غير صالح ({e})")
            continue
        last_date, last_ver = "", (0, 0, 0)
        for i, e in enumerate(arr):
            for k in ("date", "version", "by", "comment"):
                if k not in e:
                    rep.err("H004", f"{f}: @updated[{i}] ناقص المفتاح `{k}`")
            d, v = e.get("date", ""), e.get("version", "")
            if not ISO_DATE.match(d):
                rep.err("H005", f"{f}: تاريخ غير ISO في @updated[{i}]: {d!r}")
            if not SEMVER.match(v):
                rep.err("H006", f"{f}: version غير SemVer في @updated[{i}]: {v!r}")
            else:
                vt = tuple(int(x) for x in v.split("."))
                if vt < last_ver:
                    rep.err("H007", f"{f}: version بيرجع لورا في @updated[{i}]")
                last_ver = vt
            if d and last_date and d < last_date:
                rep.warn("H008", f"{f}: تواريخ @updated مش مرتبة تصاعدياً")
            last_date = d or last_date


def parse_tracker(t):
    tasks, phases = {}, {}
    for line in t.splitlines():
        m = re.match(r"^Phase (\d+):\s*(.*?)\s*\.{3,}", line)
        if m:
            phases[int(m.group(1))] = m.group(2)
        m = re.match(r"^[├└]── (\d+)\.(\d+)\s+.*?\.{3,}\s*" + STATUS_RE, line)
        if m:
            tasks[(int(m.group(1)), int(m.group(2)))] = norm_status(m.group(3))
    return tasks, phases


def check_tracker(texts, rep):
    t = texts.get("PROJECT_TRACKER.md")
    if t is None:
        return {}, {}
    tasks, phases = parse_tracker(t)
    if not tasks:
        rep.err("T001", "مفيش مهام اتقرت من شجرة PROJECT_TRACKER (الصيغة: `├── N.M  الاسم ..... ⬜`)")
        return tasks, phases
    in_prog = [k for k, v in tasks.items() if v == "🔵"]
    if len(in_prog) > 1:
        rep.warn("T002", "أكتر من مهمة 🔵 في نفس الوقت: " + ", ".join(f"{a}.{b}" for a, b in sorted(in_prog)))
    rows = {}
    row_re = r"^\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)%\s*\|$"
    for line in t.splitlines():
        m = re.match(row_re, line)
        if m:
            rows[int(m.group(1))] = tuple(int(m.group(i)) for i in range(3, 9))
    total_done = total = 0
    for ph in sorted(set(k[0] for k in tasks)):
        ts = [v for k, v in tasks.items() if k[0] == ph]
        tot, done = len(ts), ts.count("✅")
        p, r, b = ts.count("🟣"), ts.count("🔵"), ts.count("🔴")
        pct = round(done * 100 / tot) if tot else 0
        total += tot
        total_done += done
        if ph not in rows:
            rep.err("D001", f"Dashboard: Phase {ph} مش موجودة في جدول التقدم")
        elif rows[ph] != (tot, done, p, r, b, pct):
            rep.err("D002", f"Dashboard: Phase {ph} مختلفة — الجدول {rows[ph]} والحقيقي {(tot, done, p, r, b, pct)} (شغّل recalc_dashboard.py --write)")
    for ph in rows:
        if ph not in set(k[0] for k in tasks):
            rep.warn("D003", f"Dashboard فيه Phase {ph} مالهاش مهام في الشجرة")
    m = re.search(r"\*\*Overall Progress\*\*\s*\|\s*\*\*(\d+)%\*\*\s*\((\d+)\s*/\s*(\d+)", t)
    if m:
        pct = round(total_done * 100 / total) if total else 0
        if (int(m.group(1)), int(m.group(2)), int(m.group(3))) != (pct, total_done, total):
            rep.err("D004", f"Overall Progress مختلف — مكتوب {m.group(0)!r} والحقيقي {pct}% ({total_done}/{total})")
    else:
        rep.warn("D005", "ما لقيتش سطر Overall Progress بالصيغة المعتادة")
    return tasks, phases


def plan_ids(p):
    ids = set()
    for line in p.splitlines():
        m = re.match(r"^\|\s*(\d{1,2})\.(\d{1,2})\s*\|", line)
        if m:
            ids.add((int(m.group(1)), int(m.group(2))))
    for m in re.finditer(r"`(\d{1,2})\.(\d{1,2})\s", p):
        ids.add((int(m.group(1)), int(m.group(2))))
    return ids


def check_plan_vs_tracker(texts, tasks, rep):
    p = texts.get("PLAN.md")
    if p is None or not tasks:
        return
    pi, ti = plan_ids(p), set(tasks)
    for a, b in sorted(pi - ti):
        rep.err("P001", f"المهمة {a}.{b} في PLAN ومش في PROJECT_TRACKER")
    for a, b in sorted(ti - pi):
        rep.err("P002", f"المهمة {a}.{b} في PROJECT_TRACKER ومش في PLAN")


def check_adr(texts, rep):
    a = texts.get("ARCHITECTURE.md")
    if a is None:
        return
    defined = re.findall(r"^\|\s*\*{0,2}(ADR-\d{3})\*{0,2}\s*\|", a, flags=re.M)
    for d in sorted({x for x in defined if defined.count(x) > 1}):
        rep.err("A001", f"{d} متعرّف أكتر من مرة")
    nums = sorted(int(x[4:]) for x in set(defined))
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            rep.warn("A002", f"فجوة في ترقيم ADR بين {nums[i-1]:03d} و {nums[i]:03d}")
    refs = set()
    for t in texts.values():
        refs |= set(re.findall(r"ADR-\d{3}", t))
    for r in sorted(refs - set(defined)):
        rep.err("A003", f"{r} مذكور في الملفات ومش معرّف في ARCHITECTURE › ADR")


def expand_cl(text):
    ids = set()
    for m in re.finditer(r"CL-(\d+)(?:\s*[…\.]{1,3}\s*(\d+))?", text):
        a = int(m.group(1))
        b = int(m.group(2)) if m.group(2) else a
        ids.update(range(a, b + 1))
    return ids


def check_cl(texts, rep):
    s = texts.get("SPECKIT.md")
    if s is None:
        return
    defined = set()
    for line in s.splitlines():
        if re.match(r"^\|\s*\*{0,2}CL-\d+", line):
            defined |= expand_cl(line.split("|")[1])
    refs = set()
    for t in texts.values():
        refs |= expand_cl(t)
    for n in sorted(refs - defined):
        rep.warn("C001", f"CL-{n:02d} مذكور ومش معرّف في SPECKIT › Clarifications")
    tr_ids = expand_cl(texts.get("PROJECT_TRACKER.md", ""))
    for n in sorted(defined - tr_ids):
        rep.warn("C002", f"CL-{n:02d} مفتوح في SPECKIT ومش ظاهر في PROJECT_TRACKER › OPEN DECISIONS")


def check_spec(texts, rep):
    s = texts.get("SPECKIT.md")
    if s is None:
        return
    defined = set()
    for line in s.splitlines():
        if line.startswith("###"):
            defined |= set(re.findall(r"SPEC-[A-Z0-9]+(?:-[A-Z0-9]+)*", line))
    for f in ("PLAN.md", "PROJECT_TRACKER.md", "ARCHITECTURE.md", "AI_INSTRUCTIONS.md"):
        t = texts.get(f, "")
        for r in sorted(set(re.findall(r"SPEC-[A-Z0-9]+(?:-[A-Z0-9]+)*", t)) - defined):
            rep.err("S001", f"{f}: {r} مش معرّف كعنوان ### في SPECKIT")


def check_vocab(texts, rep):
    for f, t in texts.items():
        for i, line in enumerate(t.splitlines(), 1):
            if "COMPLETED" in line and "غير مستخدمة" not in line and "COMPLETED غير" not in line:
                rep.warn("V001", f"{f}:{i} استخدام COMPLETED — المفردات الموحدة: NOT_STARTED/IN_PROGRESS/IMPLEMENTED/VERIFIED/BLOCKED/ON_HOLD")


def check_placeholders(texts, rep):
    n = sum(t.count("[PROJECT_NAME]") for t in texts.values())
    if n:
        rep.info("X001", f"لسه فيه {n} موضع [PROJECT_NAME] (طبيعي في النسخة العامة؛ بدّلها عند تهيئة مشروع فعلي)")
    v = sum(t.count("[VERIFY]") for t in texts.values())
    if v:
        rep.info("X002", f"فيه {v} علامة [VERIFY] محتاجة تأكيد من الواقع")


def check_map(texts, rep):
    a = texts.get("AI_INSTRUCTIONS.md", "")
    for f in FILES:
        if f not in a:
            rep.warn("M001", f"AI_INSTRUCTIONS مش بيذكر {f} في خريطة الملفات")


def main():
    ap = argparse.ArgumentParser(description="فحص اتساق الملفات الخمسة")
    ap.add_argument("--root", default=".", help="المجلد اللي فيه الملفات الخمسة")
    ap.add_argument("--strict", action="store_true", help="اعتبر التحذيرات أخطاء")
    ap.add_argument("--json", action="store_true", help="مخرجات JSON")
    args = ap.parse_args()
    rep = Report()
    texts = read_all(Path(args.root), rep)
    check_headers(texts, rep)
    tasks, _ = check_tracker(texts, rep)
    check_plan_vs_tracker(texts, tasks, rep)
    check_adr(texts, rep)
    check_cl(texts, rep)
    check_spec(texts, rep)
    check_vocab(texts, rep)
    check_placeholders(texts, rep)
    check_map(texts, rep)

    if args.json:
        print(json.dumps([{"level": l, "code": c, "message": m} for l, c, m in rep.items], ensure_ascii=False, indent=2))
    else:
        for level, code, msg in rep.items:
            icon = {"ERROR": "❌", "WARN": "⚠️ ", "INFO": "ℹ️ "}[level]
            print(f"{icon} [{code}] {msg}")
        print(f"\nالنتيجة: {rep.count('ERROR')} أخطاء · {rep.count('WARN')} تحذيرات · {rep.count('INFO')} معلومات")
    bad = rep.count("ERROR") + (rep.count("WARN") if args.strict else 0)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()