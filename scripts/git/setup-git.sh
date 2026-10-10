#!/usr/bin/env bash
# @file        : scripts/git/setup-git.sh
# @description : تجهيز Git للمشروع (مهمة 0.5): قالب commit + فرع develop + أول فرع Tree ID.
#                الآمن لإعادة التشغيل: الفروع الموجودة بتتخطى من غير تعديل.
#                الأفضل تشغيله بعد دمج PR التهيئة عشان develop تبدأ من نظيفة.
# @usage       : bash scripts/git/setup-git.sh [--push]
# @updated     : [
#   { "date": "2026-10-10", "version": "1.0.0", "by": ["Arena Agent"], "comment": "إنشاء الملف" }
# ]

set -euo pipefail

FEATURE_BRANCH="feature/1.1.1-project-setup" # أول فرع Tree ID حسب PLAN.md (Phase 0 → 1.1.1)

# --- التحقق الأولي: لازم نكون جوه مستودع git وفيه main ---
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || {
  echo "❌ ده مش مستودع git — شغّل السكريبت من جوه المشروع"
  exit 1
}
cd "$ROOT"

if git rev-parse --verify --quiet main >/dev/null; then
  MAIN_BASE="main"
elif git rev-parse --verify --quiet origin/main >/dev/null; then
  # في الـ clone الجديد ممكن main المحلي لسه مش موجود — origin/main يكفي
  MAIN_BASE="origin/main"
else
  echo "❌ مفيش فرع main (ولا محلي ولا على origin) — اتأكد من المستودع الأول"
  exit 1
fi

# --- 1) قالب commit (الإعداد محلي لكل clone) ---
git config commit.template .gitmessage
echo "✅ قالب commit متظبط: commit.template = $(git config --get commit.template)"

# --- 2) فرع develop من main ---
if git rev-parse --verify --quiet develop >/dev/null; then
  echo "⏭️ فرع develop موجود بالفعل — هنسيبه في حاله"
else
  # --no-track: develop تبدأ من غير upstream غلط؛ الـ push بـ -u هو اللي يربطها بـ origin/develop
  git branch --no-track develop "$MAIN_BASE"
  echo "✅ اتعمل develop من $MAIN_BASE"
fi

# --- 3) أول فرع Tree ID من develop ---
if git rev-parse --verify --quiet "$FEATURE_BRANCH" >/dev/null; then
  echo "⏭️ فرع $FEATURE_BRANCH موجود بالفعل — هنسيبه في حاله"
else
  git branch "$FEATURE_BRANCH" develop
  echo "✅ اتعمل $FEATURE_BRANCH من develop"
fi

# --- 4) الدفع على origin (اختياري بـ --push) ---
if [[ "${1:-}" == "--push" ]]; then
  git push -u origin develop
  git push -u origin "$FEATURE_BRANCH"
  echo "✅ الفروع اترفعت على origin"
else
  echo "ℹ️ عشان ترفع الفروع:"
  echo "   git push -u origin develop && git push -u origin $FEATURE_BRANCH"
  echo "   (أو شغّل السكريبت تاني بـ --push)"
fi

# --- 5) التحقق النهائي: الفروع لازم تظهر في git branch -a ---
echo "──── git branch -a ────"
git branch -a
