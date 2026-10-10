#!/usr/bin/env python3
"""
@file        : scripts/next_id.py
@description : بيطلّع الـ ID التالي الحر لأي نوع في الملفات الخمسة، عشان مفيش ID يتكرر أو يتخمّن.
               الـ IDs عمرها ما بتتعاد استخدامها (حتى لو القرار/المهمة اتلغت — بتتعلّم Superseded).
الاستخدام    : python scripts/next_id.py --root <مجلد الملفات> adr
               python scripts/next_id.py --root <مجلد> cl | mod | backlog | risk | constitution | cc
               python scripts/next_id.py --root <مجلد> task --phase 3
               python scripts/next_id.py --root <مجلد> phase
               python scripts/next_id.py --root <مجلد> fr --key INP        (FR-INP-n)
               python scripts/next_id.py --root <مجلد> ac --key INP        (AC-INP-n)
"""
import argparse
import re
import sys
from pathlib import Path

FILES = ["AI_INSTRUCTIONS.md", "ARCHITECTURE.md", "SPECKIT.md", "PLAN.md", "PROJECT_TRACKER.md"]


def load(root):
    out = {}
    for f in FILES:
        p = Path(root) / f
        out[f] = p.read_text(encoding="utf-8") if p.exists() else ""
    return out


def max_num(pattern, texts, group=1):
    nums = []
    for t in texts.values():
        nums += [int(m.group(group)) for m in re.finditer(pattern, t)]
    return max(nums) if nums else 0


def main():
    ap = argparse.ArgumentParser(description="الـ ID التالي")
    ap.add_argument("--root", default=".")
    ap.add_argument("--phase", type=int)
    ap.add_argument("--key", help="مفتاح الـ Spec (مثال: INP, CMB, DRP)")
    ap.add_argument("kind", choices=["adr", "cl", "mod", "backlog", "risk", "constitution", "cc", "task", "phase", "fr", "ac"])
    a = ap.parse_args()
    texts = load(a.root)

    if a.kind == "adr":
        n = max_num(r"ADR-(\d{3})", texts) + 1
        print("ADR-%03d" % n)
    elif a.kind == "cl":
        # يدعم المدى CL-11…15
        top = 0
        for t in texts.values():
            for m in re.finditer(r"CL-(\d+)(?:\s*[…\.]{1,3}\s*(\d+))?", t):
                top = max(top, int(m.group(1)), int(m.group(2) or 0))
        print("CL-%02d" % (top + 1))
    elif a.kind == "mod":
        print("MOD-%d" % (max_num(r"MOD-(\d+)", texts) + 1))
    elif a.kind == "backlog":
        print("B-%d" % (max_num(r"\bB-(\d+)\b", texts) + 1))
    elif a.kind == "risk":
        print("R%d" % (max_num(r"\|\s*R(\d+)\s*\|", texts) + 1))
    elif a.kind == "constitution":
        print("C-%02d" % (max_num(r"\*\*C-(\d+)\*\*", texts) + 1))
    elif a.kind == "cc":
        print("CC-%02d" % (max_num(r"CC-(\d{2})\b", texts) + 1))
    elif a.kind == "phase":
        nums = [int(m.group(1)) for m in re.finditer(r"^Phase (\d+):", texts["PROJECT_TRACKER.md"], flags=re.M)]
        print("Phase %d" % (max(nums) + 1 if nums else 0))
    elif a.kind == "task":
        if a.phase is None:
            sys.exit("--phase مطلوب لنوع task")
        pat = r"[├└]── %d\.(\d+)\s" % a.phase
        nums = [int(m.group(1)) for m in re.finditer(pat, texts["PROJECT_TRACKER.md"])]
        print("%d.%d" % (a.phase, max(nums) + 1 if nums else 1))
    elif a.kind in ("fr", "ac"):
        if not a.key:
            sys.exit("--key مطلوب (مثال: INP)")
        tag = a.kind.upper()
        n = max_num(r"%s-%s-(\d+)" % (tag, re.escape(a.key)), texts)
        print("%s-%s-%d" % (tag, a.key, n + 1))


if __name__ == "__main__":
    main()