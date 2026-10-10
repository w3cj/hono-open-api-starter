# 📐 SPECKIT — المواصفات (Spec-Kit Style)

> **@file** : SPECKIT.md
> **@description** : المواصفات المطلوبة بالظبط لكل موديول في Bun + Hono API Starter: الدستور، الـ Cross-cutting، الـ Specs (FR/AC)، سجل Clarifications، وDefinition of Done. (الحالة في PROJECT_TRACKER.md مش هنا)
> **@updated** : `[ { "date": "2026-10-10", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف + Specs لموديولات المراحل 1–6" } ]`
> **النطاق** : Backend فقط — المراحل 0–7.

---

## Part 0 — طريقة الاستخدام

### 0.1 دورة Spec-Kit
```markdown
Spec ← Clarify (CL) ← Plan (PLAN.md) ← Tasks (TRACKER) ← Implement ← Verify (DoD)
```

### 0.2 علامات
| العلامة | المعنى |
|---|---|
| `FR-<KEY>-n` | متطلب وظيفي |
| `AC-<KEY>-n` | معيار قبول قابل للاختبار |
| `[NEEDS CLARIFICATION]` | ممنوع الافتراض — اسأل (Part 9.3) |
| `[DECIDED: ADR-x]` | محسوم بقرار معماري |
| `[VERIFY]` | لازم يتأكد بتشغيل فعلي |

### 0.3 قالب Spec
```markdown
### SPEC-<KEY>: <الاسم>
Layer / Phase / Depends — 1 الهدف · 2 النطاق · 3 العقد · 4 الأخطاء · 5 قواعد (FR) · 6 Edge cases · 7 AC + Tests · 8 أسئلة مفتوحة
```
الـ Spec مفيهوش حالة تنفيذ (دي في PROJECT_TRACKER).

---

## Part 1 — Constitution (غير قابلة للتفاوض)

| ID | المبدأ |
|---|---|
| **C-01** | **Security by Default:** deny by default، Zod على كل مدخل، لا أسرار في الكود أو اللوجز. [DECIDED: ADR-008/009] |
| **C-02** | **Tenant Isolation:** كل جدول عمل فيه `tenant_id` مفهرس وكل استعلام عليه مفلتر. [DECIDED: ADR-006] |
| **C-03** | **Layered Dependency:** controller → service → repository؛ الـ service لا يستورد Hono. [DECIDED: ADR-010] |
| **C-04** | **All-or-Nothing:** كتابة متعددة الجداول في Transaction واحدة. [DECIDED: ADR-018] |
| **C-05** | **UTC Everywhere:** تخزين ومعالجة بـ UTC وISO 8601، والتحويل المحلي عند العرض فقط. [DECIDED: ADR-019] |
| **C-06** | **Honest Status:** لا "تم" من غير تشغيل فعلي (typecheck + lint + tests). |
| **C-07** | **Safe Errors:** لا stack ولا تفاصيل داخلية للعميل، وrequestId دايماً. [DECIDED: ADR-011] |
| **C-08** | **No Early Services:** الخدمات المؤجلة (Backlog) متتبنيش قبل قرار. [DECIDED: ADR-014] |
| **C-09** | **Conflicts → Ask:** أي تعارض جوهري = سؤال للمستخدم قبل التنفيذ. |
| **C-10** | **Small Increments:** موديول واحد في المرة، وتغيير الـ schema بترحيل مرقّم بـ `.down.sql`. [DECIDED: ADR-005] |

---

## Part 2 — Cross-Cutting Specs (بتنطبق على كل الموديولات)

### CC-01 الرد الموحّد
كل endpoint (ما عدا مسارات Better Auth وcallbacks) بيرد بالـ Envelope (ARCHITECTURE §11). `meta.requestId` إلزامي.

### CC-02 التحقق
Zod على body/query/params. Schemas صارمة، حدود أطوال، وحقول غير معروفة ما بتوصلش للـ DB.

### CC-03 الصلاحيات والمستأجر
كل مسار محمي بيمرّ: Authentication ← Tenant Context ← Authorization (`resource:action`). الاستثناءات (health، تسجيل، دخول) صريحة.

### CC-04 المعاملات
أي service بيكتب في أكتر من جدول بيشتغل جوه `withTransaction`. ممنوع طلب خارجي جوّاها.

### CC-05 الوقت
`TIMESTAMPTZ` في الـ DB، ISO 8601 UTC في الـ API، والـ clock بيتحقن في الـ services.

### CC-06 الأخطاء
`AppError` + ERR constants. رسالة ar/en من `Accept-Language`. الأخطاء غير المتوقعة بترجع `SYS_001` من غير تفاصيل.

### CC-07 Pagination
cursor للقوائم الكبيرة، وحد أقصى للصفحة، وترتيب ثابت. (SPEC-PAGE)

### CC-08 Audit
أي تغيير حساس بيطلّع حدث domain بعد نجاح المعاملة، والـ listener بيكتب في `audit_logs`.

### CC-09 Testing Matrix
لكل موديول: unit + integration (Postgres) + صلاحيات + عزل مستأجر (لو فيه tenant_id).

---

## Part 3 — الأساس (Phase 1)

### SPEC-ENV: Environment Config
**Phase 1 · Depends:** —
- **FR-ENV-1** كل المتغيرات بتتحقق بـ Zod مرة واحدة عند الإقلاع وبتتصدّر كـ object typed.
- **FR-ENV-2** الإقلاع بيفشل برسالة واضحة (بدون طباعة القيم السرية) لو متغير مطلوب ناقص أو غلط.
- **FR-ENV-3** `BETTER_AUTH_SECRET` لا يقل عن 32 حرف، وممنوع قيمة افتراضية في الإنتاج.
- **AC-ENV-1** إقلاع بـ `DATABASE_URL` ناقص بيفشل.  **AC-ENV-2** قيمة سرية مش بتظهر في أي لوج.

### SPEC-ERR: Error System
**Phase 1 · Depends:** SPEC-ENV
- **FR-ERR-1** `AppError(code, status, message)` + كتالوج ERR مقسّم بالبادئات (`AUTH_` `USR_` `TEN_` `PERM_` `VAL_` `DB_` `SYS_`).
- **FR-ERR-2** error handler مركزي بيحوّل `ZodError` لـ `VAL_001` (400/422) وأي خطأ غير معروف لـ `SYS_001` (500).
- **FR-ERR-3** الرسالة ar/en من `Accept-Language` (الافتراضي من `DEFAULT_LANGUAGE`).
- **FR-ERR-4** الخطأ الأصلي بيتسجّل داخلياً مع requestId ولا يتبعت للعميل.
- **AC-ERR-1** خطأ غير متوقع بيرجع 500 بشكل Envelope من غير stack.  **AC-ERR-2** نفس الكود بيرجع برسالة عربي لو `Accept-Language: ar`.

### SPEC-RESP: Response Envelope
**Phase 1 · Depends:** SPEC-ERR
- **FR-RESP-1** نجاح: `{ success: true, data, message?, meta: { requestId } }`.
- **FR-RESP-2** فشل: `{ success: false, data: null, message, error: { code, details? }, meta: { requestId } }`.
- **FR-RESP-3** requestId بيتولّد في middleware ويرجع في هيدر `X-Request-Id` كمان.
- **AC-RESP-1** كل ردود الاختبار بتطابق الـ schema.

### SPEC-HEALTH: Health Checks
**Phase 1 · Depends:** SPEC-ENV
- **FR-HEALTH-1** `GET /health/live` بيرد 200 طالما العملية شغالة (من غير فحص خارجي).
- **FR-HEALTH-2** `GET /health/ready` بيفحص اتصال الـ DB ويرد 503 لو مش جاهز، من غير كشف تفاصيل البنية.
- **AC-HEALTH-1** الـ DB واقعة ⇒ ready=503 وlive=200.

---

## Part 4 — قاعدة البيانات (Phase 2)

### SPEC-MIG: Migrations Naming
**Phase 2 · Depends:** — · [DECIDED: ADR-005] · [VERIFY] CL-03
- **FR-MIG-1** الاسم: `{PREFIX}_{NNNN}_{ACTION}_{TABLE}` (`py` مستقل / `sy` بيعتمد على غيره).
- **FR-MIG-2** كل ترحيل له `.down.sql` بيعكسه بالترتيب التنازلي.
- **FR-MIG-3** النطاقات: CORE `0001–0007` · ENTITIES `0100+` · BUSINESS `0200+` · AUDIT `0300+` · SEED `0900+`.
- **FR-MIG-4** ممنوع تعديل ترحيل بعد الدمج، وممنوع تطبيقه تلقائياً عند إقلاع التطبيق.
- **AC-MIG-1** up ثم down ثم up بيرجع نفس الـ schema.  **AC-MIG-2** رقم بدون اتّباع الصيغة بيفشّل فحص الـ CI/السكريبت.

### SPEC-TXN: Transaction Helper
**Phase 2 · Depends:** SPEC-MIG · [DECIDED: ADR-018]
- **FR-TXN-1** `withTransaction(fn)` بيفتح معاملة ويمرّر `tx` للـ repositories، وcommit عند النجاح، وrollback عند أي exception.
- **FR-TXN-2** ممنوع طلب شبكة خارجي أو انتظار طويل جوه المعاملة.
- **FR-TXN-3** أحداث الـ domain بتتنشر بعد الـ commit مش قبله.
- **AC-TXN-1** فشل الخطوة التانية بيلغي الأولى (لا بيانات يتيمة).

---

## Part 5 — المصادقة والصلاحيات (Phase 3–4)

### SPEC-AUTH: Authentication
**Phase 3 · Depends:** SPEC-MIG · [DECIDED: ADR-008/009] · [VERIFY] CL-01/02
- **FR-AUTH-1** تسجيل بإيميل وباسورد (تحت `ENABLE_REGISTRATION`) + تأكيد إيميل (تحت `ENABLE_EMAIL_VERIFICATION`).
- **FR-AUTH-2** `AuthService` هو المكان الوحيد لتشفير/مقارنة الباسورد: bcrypt cost 12، حد أقصى لطول الباسورد بسبب حد 72 بايت.
- **FR-AUTH-3** الجلسة بكوكي HttpOnly، وSecure في الإنتاج، وSameSite مناسب، ومدة انتهاء، وقابلة للإلغاء.
- **FR-AUTH-4** رسائل فشل الدخول متطابقة (لا تكشف وجود الإيميل).
- **FR-AUTH-5** rate limit على تسجيل/دخول/إعادة تعيين عبر المدمج في Better Auth. [DECIDED: ADR-021]
- **FR-AUTH-6** إلغاء الجلسات بعد تغيير الباسورد.
- **AC-AUTH-1** بيانات غلط ⇒ `AUTH_004` بنفس الرسالة للحالتين.  **AC-AUTH-2** الباسورد ما بيظهر في لوج أو رد أو DB (hash فقط).  **AC-AUTH-3** جلسة ملغية بترجع `AUTH_001`.

### SPEC-AUTHZ: Authorization
**Phase 4 · Depends:** SPEC-AUTH
- **FR-AUTHZ-1** الأدوار: `owner` `admin` `manager` `member` `viewer` على مستوى المستأجر، وإدارة المنصة منفصلة.
- **FR-AUTHZ-2** الصلاحيات `resource:action` بالجمع، وكتالوج مركزي.
- **FR-AUTHZ-3** deny by default، والتحقق على السيرفر دايماً، والـ owner مش بيبقى platform admin تلقائياً.
- **FR-AUTHZ-4** منع تصعيد الصلاحيات: مستخدم ميقدرش يمنح صلاحية أو دور أعلى مما يملك.
- **FR-AUTHZ-5** منع إزالة/تنزيل آخر Owner، ونقل الملكية بتأكيد صريح.
- **FR-AUTHZ-6** تغييرات الأدوار والصلاحيات بتتسجّل في audit.
- **AC-AUTHZ-1** غياب صلاحية ⇒ `PERM_001` (403).  **AC-AUTHZ-2** محاولة تصعيد بتفشل ومتتنفّذش.  **AC-AUTHZ-3** تغطية منطق الصلاحيات ≥ 95%.

---

## Part 6 — تعدد المستأجرين (Phase 5)

### SPEC-TENANT: Tenant Context & Isolation
**Phase 5 · Depends:** SPEC-AUTHZ · [DECIDED: ADR-006]
- **FR-TENANT-1** المستأجر المختار من `X-Tenant-Id` أو `active_tenant_id` في الجلسة، ويتحقق مقابل عضوية نشطة قبل أي عملية.
- **FR-TENANT-2** الـ DAL بيحقن `tenant_id` في كل استعلام جداول العمل، وممنوع استعلام من برّاه.
- **FR-TENANT-3** `tenant_id` جاي من العميل في body/query بيتجاهل أو بيتقارن بالسياق الموثوق.
- **FR-TENANT-4** إنشاء tenant + عضوية المالك في معاملة واحدة. [DECIDED: ADR-018]
- **FR-TENANT-5** الدعوات: صلاحية بمدة، استخدام مرة واحدة، قابلة للإلغاء.
- **AC-TENANT-1** وصول مستأجر A لمورد مستأجر B ⇒ 404/403 حسب السياسة وبدون تسريب.  **AC-TENANT-2** فشل إنشاء العضوية بيلغي إنشاء الـ tenant.

---

## Part 7 — موديولات الـ API (Phase 6)

### SPEC-PAGE: Pagination, Filter, Sort
**Phase 6 · Depends:** SPEC-RESP
- **FR-PAGE-1** cursor pagination للقوائم الكبيرة، وحد أقصى للصفحة (مثلاً 100) يتحدد في الـ config.
- **FR-PAGE-2** حقول الفلترة والترتيب من قائمة مسموحة فقط، والترتيب ثابت (tie-breaker بـ `id`).
- **FR-PAGE-3** ممنوع تمرير أسماء أعمدة SQL من العميل مباشرة.
- **AC-PAGE-1** حقل ترتيب غير مسموح ⇒ `VAL_001`.

### SPEC-USERS: Users Module
**Phase 6 · Depends:** SPEC-AUTH · SPEC-PAGE
- **FR-USERS-1** `GET /api/v1/users/me` + تعديل البروفايل.
- **FR-USERS-2** تغيير الباسورد عبر `AuthService` مع إلغاء الجلسات الأخرى.
- **FR-USERS-3** قائمة جلسات المستخدم وإلغاء جلسة بعينها.
- **FR-USERS-4** ممنوع إرجاع hash أو أسرار في أي رد.
- **AC-USERS-1** رد `me` من غير أي حقل hash.  **AC-USERS-2** مستخدم ميقدرش يلغي جلسة مستخدم تاني.

### SPEC-SETTINGS: Tenant Settings
**Phase 6 · Depends:** SPEC-TENANT
- **FR-SETTINGS-1** جدول `settings (tenant_id, key, value)` فريد `(tenant_id, key)`.
- **FR-SETTINGS-2** قراءة وكتابة بصلاحيات، وتغيير الإعدادات الحساسة بيتسجّل في audit.
- **AC-SETTINGS-1** نفس الـ key في مستأجرين مختلفين مستقلين.

### SPEC-AUDIT: Audit Logs
**Phase 6 · Depends:** SPEC-TENANT · [DECIDED: ADR-012]
- **FR-AUDIT-1** الجدول بالأعمدة المدموجة (ARCHITECTURE §16.3) وappend-oriented، وممنوع endpoint تعديل أو حذف.
- **FR-AUDIT-2** القراءة بصلاحية `audit_logs:read` مع فلترة وPagination.
- **FR-AUDIT-3** إخفاء البيانات الحساسة من `diff`.
- **AC-AUDIT-1** حدث تغيير دور بيظهر بالـ actor وrequestId.  **AC-AUDIT-2** `diff` مفيهوش باسورد أو token.

### SPEC-APIKEY: API Keys
**Phase 6 · Depends:** SPEC-AUTHZ · SPEC-TENANT
- **FR-APIKEY-1** المفتاح بيتولّد عشوائي آمن، وبيتعرض كاملاً مرة واحدة فقط، وبيتخزن digest فقط مع prefix للتعريف.
- **FR-APIKEY-2** كل مفتاح له tenant وscopes صريحة وتاريخ انتهاء، وممنوع يرث صلاحيات المستخدم كاملة.
- **FR-APIKEY-3** إلغاء وتسجيل آخر استخدام، وكل عمليات الإنشاء والإلغاء في audit.
- **AC-APIKEY-1** مفيش plaintext للمفتاح في DB أو لوج.  **AC-APIKEY-2** مفتاح منتهي أو ملغي ⇒ `AUTH_002`/`AUTH_001`.

### SPEC-OPENAPI: API Documentation
**Phase 6 · Depends:** كل الموديولات
- **FR-OPENAPI-1** `/openapi.json` و`/docs` (Scalar) بيتولّدوا من تعريفات المسارات.
- **FR-OPENAPI-2** `/docs` تحت `ENABLE_API_DOCS` وبيتقفل أو يتقيّد في الإنتاج.
- **FR-OPENAPI-3** التوثيق بيذكر المصادقة وأمثلة الطلب والرد وأكواد الأخطاء.
- **AC-OPENAPI-1** كل مسار في `/api/v1` ظاهر في `/openapi.json` ومطابق للتنفيذ.

---

## Part 9 — Clarifications Log

### 9.1 محسومة (من المستخدم — 2026-10-10)
| ID | القرار |
|---|---|
| UD-01 | DB PRD ملزم لطبقة الداتابيز فقط، وExpress PRD أفكار فقط. (ADR-003) |
| UD-02 | `SERIAL` + `public_id` UUIDv7. (ADR-004) |
| UD-03 | Postgres فقط. (ADR-002) |
| UD-04 | ترحيلات py/sy بسكريبت إعادة تسمية و`.down.sql`. (ADR-005) |
| UD-05 | `tenants` + `memberships` مخصصة. (ADR-006) |
| UD-06 | الـ Ledger خارج الـ Starter. (ADR-007) |
| UD-07 | bcrypt cost 12 عبر AuthService. (ADR-008) |
| UD-08 | جلسات Better Auth + API Keys. (ADR-009) |
| UD-09 | `@a` محدود على الـ backend + قاعدتي المعاملات وUTC. (ADR-010/018/019) |
| UD-10 | الرد الموحّد المدموج + أكواد `AUTH_001` + رسائل ar/en. (ADR-011) |
| UD-11 | EventBus في الذاكرة + جدول audit واحد، والـ outbox مؤجّل. (ADR-012) |
| UD-12 | عزل الفشل + Graceful Shutdown بدل Zero-Crash. (ADR-013) |
| UD-13 | النطاق 0–7 + الأسئلة الستة. (ADR-014) |
| UD-14 | repo مستقل + المنفذ 2001 + أسماء المتغيرات + `.validation.ts`. (ADR-015) |
| UD-15 | نظام الملفات الخمسة. (ADR-016) |
| UD-16 | التسليم في Claude Code/Codespaces. (ADR-017) |
| UD-17 | الافتراضات الصغيرة التسعة. (ADR-020) |

### 9.2 محسومة تلقائياً (ممكن تعترض)
rate limit مسارات الـ Auth عبر المدمج في Better Auth لحد Redis (ADR-021).

### 9.3 مفتوحة (Open) — لازم تأكيد قبل المهمة المذكورة
| ID | السؤال | يحجب | التوصية المبدئية |
|---|---|---|---|
| **CL-01** | Better Auth بيدعم مفاتيح SERIAL فعلاً؟ `[VERIFY]` | 2.6 · 3.1 | لو لا: نوفّق بجداول وسيطة بدل ما نكسر ADR-004 |
| **CL-02** | Better Auth بيقبل hasher مخصص (bcrypt)؟ `[VERIFY]` | 3.2 | لو لا: نسأل المستخدم بين Argon2id أو الافتراضي |
| **CL-03** | سكريبت إعادة التسمية و`.down.sql` فوق drizzle-kit ممكنين من غير هشاشة؟ `[VERIFY]` | 2.2 | لو لا: ترقيم drizzle الافتراضي + rollback يدوي موثّق |
| **CL-04** | توافق Bun مع Hono/Zod/Drizzle/postgres/Better Auth/Pino/bcrypt `[VERIFY]` | Phase 1 | يتأكد بتشغيل فعلي في 0.1 |
| **CL-05** | BullMQ ولا RabbitMQ للـ Queue | تفعيل B-2 | مؤجّل لحد الحاجة |

---

## Part 10 — Definition of Done

### 10.1 للموديول
```markdown
□ الكود مكتوب بالطبقات الصح (controller/service/repository)     □ Zod على كل مدخل
□ الصلاحيات والمستأجر مفروضين (CC-03)                           □ الكتابة متعددة الجداول في Transaction
□ الأخطاء بـ ERR والرد موحّد                                     □ التواريخ UTC ISO 8601
□ Tests: unit + integration + صلاحيات + عزل                       □ typecheck + lint + test بيعدّوا فعلاً
□ OpenAPI محدّث                                                  □ الوثائق (Impact Matrix) محدّثة وvalidate_docs بيعدّي
□ القيود المعروفة موثّقة ولا يوجد placeholder مُعلن كامل
```

### 10.2 للمرحلة
```markdown
□ كل المهام ✅ بدليل    □ Exit Criteria محقّقة    □ لا Blockers    □ PROJECT_TRACKER وCHANGELOG محدّثين
```