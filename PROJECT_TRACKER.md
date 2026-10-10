# 📋 PROJECT TRACKER — تتبع المشروع

> **@file** : PROJECT_TRACKER.md
> **@description** : الحالة الحيّة للمشروع: شجرة المهام، حالة الموديولات، التركيز الحالي، القرارات المفتوحة، العوائق، Backlog، Change Log، وسياق الـ AI. **بيتحدّث في كل جلسة.**
> **@updated** : `[ { "date": "2026-10-10", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف + تهيئة شجرة المهام من PLAN.md" } ]`
> **النطاق** : Bun + Hono API Starter.

---
> **القاعدة الذهبية:** الحالة ✅ = اتنفذ **واتحقق** فعلاً. الأمانة قبل النسبة. (AI_INSTRUCTIONS §11)

---

## 📌 Project Info

| الحقل | القيمة |
|---|---|
| **Project Name** | `bun-hono-api-starter` |
| **Description** | Backend Starter متعدد المستأجرين (Bun + Hono + TS + PostgreSQL + Drizzle + Better Auth) — راجع ARCHITECTURE.md |
| **Started** | 2026-10-10 |
| **Last Updated** | 2026-10-10 |
| **Current Phase** | Phase 0 — Repo Analysis & Setup |
| **Overall Progress** | **0%** (0 / 63 مهمة ✅ Verified) |
| **Repo State** | ❓ لا يوجد repo وقت التهيئة — كل بند تقني `[VERIFY]` لحد فحص الواقع |
| **Release Branch الحالي** | — (يتحدد عند أول فرع؛ Tree ID من `git branch -a`) |

## 🎯 Project Goals
1. أساس Backend آمن ومتعدد المستأجرين يتبع قواعد BomBa.
2. مصادقة وصلاحيات وعزل مستأجرين مثبتة باختبارات.
3. ترحيلات منضبطة وقاعدة بيانات بقيود حقيقية.
4. جودة قابلة للقياس (typecheck + lint + tests 80/95).
5. وثائق حيّة تخلّي أي AI Agent يكمّل بدون ضياع سياق.

---

## 📊 Status Legend (موحّد — AI_INSTRUCTIONS §11.2)

| الرمز | الحالة | المعنى |
|---|---|---|
| ⬜ | NOT_STARTED | لسه |
| 🔵 | IN_PROGRESS | شغّال عليه (واحدة بس في CURRENT FOCUS) |
| 🟣 | IMPLEMENTED | الكود/المحتوى اتكتب، التحقق الكامل لسه |
| ✅ | VERIFIED | typecheck+lint+tests+build عدّوا + docs محدثة |
| 🔴 | BLOCKED | واقف — السبب في BLOCKERS |
| ⏸️ | ON_HOLD | مؤجّل بقرار المستخدم |

**الأولويات:** 🔴 High (30min–2hr) · 🟡 Medium (2hr–1day) · 🟢 Low (> 1day) · **COMPLETED غير مستخدمة.**

## 📈 Progress Dashboard

```
Overall % = (✅ ÷ إجمالي المهام) × 100          ← 🟣 لا يُحسب
```

| Phase | الاسم | الإجمالي | ✅ | 🟣 | 🔵 | 🔴 | % |
|---|---|---|---|---|---|---|---|
| 0 | Repo Analysis & Setup | 7 | 0 | 1 | 0 | 0 | 0% |
| 1 | Project Foundation | 10 | 0 | 0 | 0 | 0 | 0% |
| 2 | Database Foundation | 12 | 0 | 0 | 0 | 0 | 0% |
| 3 | Authentication | 7 | 0 | 0 | 0 | 0 | 0% |
| 4 | Authorization | 6 | 0 | 0 | 0 | 0 | 0% |
| 5 | Multi-Tenancy | 7 | 0 | 0 | 0 | 0 | 0% |
| 6 | Core API Modules | 9 | 0 | 0 | 0 | 0 | 0% |
| 7 | Basic Hardening & Release | 5 | 0 | 0 | 0 | 0 | 0% |
| **Σ** | | **63** | **0** | **1** | **0** | **0** | **0%** |

---

## 🌳 TASK TREE (الشجرة الرئيسية)

> الـ Deliverable لكل مهمة في `PLAN.md` (جدول المرحلة) والمواصفات في `SPECKIT.md`.

```
Phase 0: Repo Analysis & Setup .................................... ⬜  (release/1.1)
├── 0.1  فحص الـ repo وتأكيد توافق Bun مع المكتبات المختارة ....... ⬜
├── 0.2  تهيئة المشروع: package.json + tsconfig strict + bunfig + paths .... ⬜
├── 0.3  ESLint flat config + Prettier + no-restricted-imports .... ⬜
├── 0.4  أدوات الاختبار bun test + عتبات التغطية 80/95 ............ ⬜
├── 0.5  Git: main/develop + قالب commit + أول فرع بـ Tree ID ..... ⬜
├── 0.6  ملفات التوثيق الخمسة في الجذر ............................ 🟣  (اتكتبت؛ لسه تتحط في repo وتتراجع)
└── 0.7  README + CHANGELOG + ملف الخطة الأصلية في docs/ .......... ⬜

Phase 1: Project Foundation ....................................... ⬜  (release/1.1)
├── 1.1  config/env.ts (Zod) + .env.example بأسماء القواعد ........ ⬜
├── 1.2  core/errors: AppError + ERR constants + كتالوج رسائل ar/en .... ⬜
├── 1.3  core/responses: Envelope موحّد + meta.requestId .......... ⬜
├── 1.4  middleware: request-id + error-handler مركزي ............. ⬜
├── 1.5  Logging: Pino + redaction + request-logger + حقل channel .... ⬜
├── 1.6  app.ts + server.ts + Graceful Shutdown ................... ⬜
├── 1.7  Health: live و ready ..................................... ⬜
├── 1.8  Security headers + CORS + حد حجم الـ body ................ ⬜
├── 1.9  alias skeleton: src/alias (index/core/libs) .............. ⬜
└── 1.10  اختبارات: env + errors + envelope + health .............. ⬜

Phase 2: Database Foundation ...................................... ⬜  (release/1.2)
├── 2.1  docker-compose.dev.yml (Postgres 16) + اتصال Drizzle ..... ⬜
├── 2.2  drizzle.config + سكريبت إعادة التسمية py/sy + ملفات .down.sql .... ⬜
├── 2.3  أدوات مشتركة: حقول التدقيق + public_id UUIDv7 + نوع timestamptz UTC .... ⬜
├── 2.4  Transaction helper (الكل أو لا شيء) + اختبار rollback .... ⬜
├── 2.5  py_0001_create_tenants ................................... ⬜
├── 2.6  py_0002_create_users + مواءمة جداول Better Auth .......... ⬜
├── 2.7  sy_0003_create_memberships ............................... ⬜
├── 2.8  sy_0004_create_sessions .................................. ⬜
├── 2.9  py_0005_create_roles + sy_0006_create_permissions ........ ⬜
├── 2.10  sy_0300_create_audit_logs (الأعمدة المدموجة) ............ ⬜
├── 2.11  seed: الأدوار والصلاحيات الافتراضية ..................... ⬜
└── 2.12  اختبارات تكامل على Postgres حقيقي (قيود + ترحيلات + rollback) .... ⬜

Phase 3: Authentication ........................................... ⬜  (release/1.3)
├── 3.1  Better Auth + Drizzle adapter ............................ ⬜
├── 3.2  AuthService: bcrypt cost 12 + توثيق التمليح + حد 72 بايت .... ⬜
├── 3.3  تسجيل + دخول + خروج ...................................... ⬜
├── 3.4  تأكيد الإيميل + إعادة تعيين الباسورد خلف EmailPort + Console adapter .... ⬜
├── 3.5  إدارة الجلسات + إلغاؤها + كوكيز آمنة + trusted origins .... ⬜
├── 3.6  middleware المصادقة + rate limit المدمج لمسارات Auth ..... ⬜
└── 3.7  اختبارات Auth ............................................ ⬜

Phase 4: Authorization ............................................ ⬜  (release/1.4)
├── 4.1  تعريف الصلاحيات (resource:action بالجمع) والأدوار الخمسة .... ⬜
├── 4.2  Permission evaluator (deny by default) ................... ⬜
├── 4.3  authorization middleware ................................. ⬜
├── 4.4  منع التصعيد + حماية آخر Owner + نقل الملكية .............. ⬜
├── 4.5  تسجيل التغييرات الحساسة في audit_logs .................... ⬜
└── 4.6  اختبارات الصلاحيات (≥ 95%) ............................... ⬜

Phase 5: Multi-Tenancy ............................................ ⬜  (release/1.4)
├── 5.1  tenant-context middleware (X-Tenant-Id + active_tenant_id) .... ⬜
├── 5.2  Data Access Layer بيحقن tenant_id تلقائياً ............... ⬜
├── 5.3  إنشاء tenant + membership + owner في معاملة واحدة ........ ⬜
├── 5.4  دعوات الأعضاء: إنشاء/قبول/انتهاء/إلغاء ................... ⬜
├── 5.5  إدارة الأعضاء: تغيير الدور والإزالة ...................... ⬜
├── 5.6  اختبارات عزل المستأجرين cross-tenant ..................... ⬜
└── 5.7  تقييم RLS مع Neon pooling وتوثيق القرار .................. ⬜

Phase 6: Core API Modules ......................................... ⬜  (release/1.5)
├── 6.1  Pagination/filter/sort helpers (cursor) .................. ⬜
├── 6.2  users: me + تعديل البروفايل + تغيير الباسورد + قائمة الجلسات وإلغاؤها .... ⬜
├── 6.3  tenants: تفاصيل + تعديل + إعدادات ........................ ⬜
├── 6.4  roles + permissions endpoints ............................ ⬜
├── 6.5  settings (tenant_id,key فريد) ............................ ⬜
├── 6.6  audit-logs: قراءة + فلترة + Pagination ................... ⬜
├── 6.7  api-keys: hash فقط + scopes + انتهاء + إلغاء ............. ⬜
├── 6.8  OpenAPI + Scalar (`/openapi.json` و`/docs`) .............. ⬜
└── 6.9  اختبارات API شاملة ....................................... ⬜

Phase 7: Basic Hardening & Release ................................ ⬜  (release/1.6)
├── 7.1  مراجعة security headers وCORS وحدود الطلبات .............. ⬜
├── 7.2  اختبارات أمنية: SQLi وcross-tenant وتصعيد صلاحيات وmalformed وoversized .... ⬜
├── 7.3  فحص الاعتماديات (bun audit) وفحص الأسرار ................. ⬜
├── 7.4  توثيق الأمان والمخاطر المتبقية ........................... ⬜
└── 7.5  مراجعة نهائية وCHANGELOG وTag الإصدار .................... ⬜

```

---

## 🧩 Module Implementation Status

| الموديول | Phase | Spec | الحالة |
|---|---|---|---|
| config/env | 1 | SPEC-ENV | ⬜ |
| errors + responses | 1 | SPEC-ERR · SPEC-RESP | ⬜ |
| health | 1 | SPEC-HEALTH | ⬜ |
| migrations + transactions | 2 | SPEC-MIG · SPEC-TXN | ⬜ |
| auth | 3 | SPEC-AUTH | ⬜ |
| authorization | 4 | SPEC-AUTHZ | ⬜ |
| multi-tenancy | 5 | SPEC-TENANT | ⬜ |
| users | 6 | SPEC-USERS | ⬜ |
| settings | 6 | SPEC-SETTINGS | ⬜ |
| audit-logs | 6 | SPEC-AUDIT | ⬜ |
| api-keys | 6 | SPEC-APIKEY | ⬜ |
| pagination | 6 | SPEC-PAGE | ⬜ |
| openapi | 6 | SPEC-OPENAPI | ⬜ |

> الجدول ده تحت ملكية الـ TRACKER؛ الحالة بتتحدث بعد ✅ المهمة المقابلة بس.

---

## 📝 DETAILED TASKS LOG (سجل المهام التفصيلي)

### القالب
```markdown
### Task <ID>: <الاسم>
- Branch: <feature/x.y.z-…>   - Spec: <SPEC-…>   - الحالة: <رمز>
- الخطوات الذرية: …    - دليل التحقق: typecheck/lint/test/…    - ملاحظات: …
```

### Task 0.1: فحص الـ repo وتأكيد توافق Bun
- Branch: — (قبل الفرع الأول)   - Spec: —   - الحالة: ⬜
- الخطوات الذرية: فحص الـ repo (لو موجود) · تثبيت كل مكتبة مختارة بنسخة مستقرة · تشغيل smoke test لكل واحدة تحت Bun · تسجيل النتيجة (CL-04).
- دليل التحقق: تقرير توافق مكتوب + أوامر اتنفذت فعلاً.
- ملاحظات: لا تفترض إن مكتبة شغالة بدون تشغيلها.

---

## 🔄 CURRENT FOCUS (التركيز الحالي)

```
Working On : لا مهمة 🔵 — الوثائق (0.6) اتكتبت 🟣 وبانتظار نقلها لـ repo ومراجعتها
Next Up    : 0.1 (فحص الـ repo + توافق Bun) ثم 0.2 → 0.3 → 0.4
Parallel   : —
Blockers   : لا يوجد (انظر أدناه)
```
> قاعدة: مهمة واحدة 🔵 في نفس الوقت.

---

## ❓ OPEN DECISIONS (قرارات مفتوحة)

| ID | السؤال | يحجب | تاريخ الفتح | الخيارات / التوصية | الحالة |
|---|---|---|---|---|---|
| CL-04 | توافق Bun مع المكتبات المختارة | Phase 1 | 2026-10-10 | يتأكد بتشغيل فعلي في 0.1 | ⬜ |
| CL-03 | جدوى سكريبت تسمية py/sy و`.down.sql` فوق drizzle-kit | 2.2 | 2026-10-10 | يتأكد في 2.2؛ البديل: ترقيم drizzle الافتراضي | ⬜ |
| CL-01 | Better Auth مع مفاتيح SERIAL | 2.6 · 3.1 | 2026-10-10 | يتأكد قبل 2.6 | ⬜ |
| CL-02 | Better Auth مع bcrypt مخصص | 3.2 | 2026-10-10 | يتأكد قبل 3.2 | ⬜ |
| CL-05 | BullMQ ولا RabbitMQ | تفعيل B-2 | 2026-10-10 | مؤجّل لحد ما نحتاج Queue | ⬜ |
| **MOD-1** | الرد على Q9: فهمت إنه "أ" + قاعدتين إضافيتين (المعاملات وUTC). لو قصدت غير كده قولي | ADR-010 | 2026-10-10 | مسجّل كـ ADR-010 وADR-018 وADR-019 | ⬜ |

---

## 🚧 BLOCKERS (عوائق نشطة)

| ID | المهمة المتأثرة | السبب | المطلوب | مفتوحة من |
|---|---|---|---|---|
| — | — | لا عوائق نشطة حالياً | — | — |

---

## 💡 BACKLOG (أفكار — لا تُنفَّذ قبل ما تدخل الخطة)

| # | الفكرة | مصدرها | تاريخ |
|---|---|---|---|
| B-1 | Redis + rate limiting موزّع + Cache abstraction | الخطة الأصلية §15.4 §17 | 2026-10-10 |
| B-2 | Queue + Workers (CL-05) | الخطة الأصلية §18 | 2026-10-10 |
| B-3 | مزودات البريد (Resend/SMTP) | الخطة الأصلية §19 | 2026-10-10 |
| B-4 | تخزين S3-Compatible + الملفات | الخطة الأصلية §20 | 2026-10-10 |
| B-5 | الإشعارات + Webhooks (وارد/صادر) | الخطة الأصلية §21–22 | 2026-10-10 |
| B-6 | الفوترة (Stripe) خلف Feature Flag | الخطة الأصلية §23 | 2026-10-10 |
| B-7 | Feature Flags | الخطة الأصلية §25 | 2026-10-10 |
| B-8 | Idempotency + Transactional Outbox | الخطة الأصلية §18.4 §28 | 2026-10-10 |
| B-9 | OpenTelemetry + Metrics + Sentry | الخطة الأصلية §26 | 2026-10-10 |
| B-10 | Docker إنتاجي + Compose profiles + Codespaces devcontainer | الخطة الأصلية §31–32 | 2026-10-10 |
| B-11 | GitHub Actions CI/CD + Dependabot + فحوصات الأمان | الخطة الأصلية §33 | 2026-10-10 |
| B-12 | اختبارات أداء/حمل (k6/autocannon) | الخطة الأصلية §30 | 2026-10-10 |
| B-13 | نموذج الـ Ledger والكيانات والمستندات | DB PRD §5–7 | 2026-10-10 |
| B-14 | تفعيل RLS في الإنتاج كطبقة دفاع ثانية | DB PRD §4.5 | 2026-10-10 |
| B-15 | Backup/DR + سياسات الاحتفاظ والخصوصية | الخطة الأصلية §35–36 | 2026-10-10 |
| B-16 | OAuth/Passkeys/TOTP | الخطة الأصلية §8.3 | 2026-10-10 |
| B-17 | Bearer/JWT للموبايل والعملاء الخارجيين + Internal Token | القواعد + Express PRD | 2026-10-10 |
| B-18 | تصدير بيانات الحساب وحذفه | الخطة الأصلية §11 | 2026-10-10 |

---

## 📜 CHANGE LOG (سجل التغييرات)

| التاريخ | Task ID | الفعل | التفاصيل |
|---|---|---|---|
| 2026-10-10 | 0.6 | 🟣 Implemented | إنشاء AI_INSTRUCTIONS / ARCHITECTURE / SPECKIT / PLAN / PROJECT_TRACKER من الخطة الأصلية وPRDs والمهارات وقرارات UD-01…UD-17 |
| 2026-10-10 | — | ✅ قرارات | تسجيل ADR-001…ADR-021 في ARCHITECTURE |
| 2026-10-10 | — | ❓ فتح | CL-01…CL-05 + MOD-1 |

---

## 🧠 AI CONTEXT (سياق للـ AI الجديد)

### ما تم
- اتقرت الخطة الأصلية وPRD السيرفر (Express) وPRD الداتابيز وكل مهارات BomBa المطلوبة.
- المستخدم حسم Q1…Q16 كلها بتوصياتي، وأضاف قاعدتين: المعاملات (الكل أو لا شيء) وUTC بصيغة ISO 8601.
- اتكتبت الملفات الخمسة بشكل متكيّف مع Backend.

### الحالة الحالية
- مفيش كود ولا repo. الملفات الخمسة هي المخرج الوحيد. كل الحالات ⬜ ما عدا 0.6 (🟣).

### آخر تحقق
- `validate_docs.py` بس (فحص الوثائق). Typecheck/Lint/Test/Build: **لم تُشغَّل** (مفيش كود).

### الخطوة الجاية بالظبط
1. نقل الملفات الخمسة لجذر الـ repo ووضع الخطة الأصلية في `docs/PLAN__Bun-hono-api-starter.md`.
2. 0.1: فحص الـ repo وتوافق Bun (CL-04) ثم 0.2 → 0.5.

### قرارات مهمة (ملخّص — التفاصيل في ARCHITECTURE › ADR)
- Bun + Hono (ADR-001) · Postgres فقط (ADR-002) · DB PRD ملزم لطبقة الداتابيز فقط (ADR-003).
- `SERIAL` + `public_id` UUIDv7 (ADR-004) · bcrypt عبر AuthService (ADR-008) · جلسات Better Auth + API Keys (ADR-009).
- معاملات الكل أو لا شيء (ADR-018) · UTC بصيغة ISO 8601 (ADR-019).

### مشاكل معروفة / مخاطر
- R1: Better Auth مع SERIAL وbcrypt مخصص لسه `[VERIFY]` (CL-01/02).
- R8: rate limit بالذاكرة لحد B-1.

### Incomplete Blocks (علامات `[ ] - todo`)
| الملف | السطر | الناقص |
|---|---|---|
| — | — | لا يوجد |

### ملفات رئيسية
`AI_INSTRUCTIONS.md` · `ARCHITECTURE.md` · `SPECKIT.md` · `PLAN.md` · `PROJECT_TRACKER.md`

---

## 🗒️ SESSION LOG (أضف سطر لكل جلسة)

| # | التاريخ | الـ Agent | المهام | الحالة بعد الجلسة | ملاحظات |
|---|---|---|---|---|---|
| 1 | 2026-10-10 | Claude | إنشاء الملفات الخمسة | 0.6 🟣 | بانتظار نقلها لـ repo وبدء 0.1 |

---

## ✅ Update Protocol (مرجع سريع)

```markdown
بداية الجلسة : اقرأ CURRENT FOCUS + AI CONTEXT + OPEN DECISIONS + BLOCKERS.
أثناء العمل  : المهمة 🔵 واحدة بس · فكرة جديدة → BACKLOG · تعارض → OPEN DECISIONS + اسأل.
نهاية الجلسة : حدّث الحالات (✅ بدليل فقط) · CURRENT FOCUS · AI CONTEXT · CHANGE LOG · Dashboard (recalc_dashboard.py --write) · BLOCKERS · SESSION LOG.
```