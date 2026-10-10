# 🏗️ ARCHITECTURE — المعمارية والقرارات التقنية

> **@file** : ARCHITECTURE.md
> **@description** : المرجع التقني الثابت لمشروع Bun + Hono API Starter: الـ Stack، الهيكل، الطبقات، قاعدة البيانات، المصادقة، الصلاحيات، تعدد المستأجرين، وسجل القرارات (ADR). (بيحل محل `AI_CONTEXT.md` — الجزء الثابت)
> **@updated** : `[ { "date": "2026-10-10", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف + تسجيل ADR-001…ADR-021" } ]`
> **النطاق** : Backend فقط. أي بند `[VERIFY]` لازم يتأكد بتشغيل فعلي قبل الاعتماد عليه.

---

## 0. الملخص التنفيذي

```markdown
- Backend Starter عام متعدد المستأجرين: Bun + Hono + TypeScript strict + PostgreSQL + Drizzle + Zod + Better Auth.
- معمارية modular monolith: controller → service → repository، وكل موديول بحدود واضحة.
- قاعدة بيانات Postgres فقط، مفتاح SERIAL + public_id UUIDv7، ترحيلات py/sy بـ down.
- مصادقة Better Auth بجلسات كوكيز + API Keys، وتشفير bcrypt عبر AuthService.
- عزل مستأجرين بطبقة تطبيق (tenant_id في كل استعلام)، وRLS تقييم فقط حالياً.
- معاملات الكل أو لا شيء للكتابة متعددة الجداول، وUTC بصيغة ISO 8601 للوقت.
- نطاق أول إصدار: المراحل 0–7. الباقي في Backlog.
```

---

## 1. Tech Stack

| المكوّن | التقنية | ملاحظة |
|---|---|---|
| Runtime | Bun | ADR-001 — توافق المكتبات `[VERIFY]` (CL-04) |
| HTTP | Hono | `hono/secure-headers` بدل Helmet |
| اللغة | TypeScript (strict) | `any` ممنوع |
| Validation | Zod | كل مدخل خارجي |
| قاعدة البيانات | PostgreSQL 16 (Docker محلياً / Neon إنتاجاً) | ADR-002 |
| ORM + Migrations | Drizzle ORM + drizzle-kit | ADR-005 |
| المصادقة | Better Auth | ADR-009 — SERIAL وbcrypt مخصص `[VERIFY]` (CL-01/02) |
| Logging | Pino (JSON على stdout) | ADR-020 |
| API Docs | OpenAPI + Scalar | `/openapi.json` و`/docs` |
| الاختبارات | `bun test` | تغطية 80% عام / 95% صلاحيات |
| الجودة | ESLint (flat) + Prettier | بدون Biome |

مؤجّل (Backlog): Redis · Queue · Email provider · Storage · Webhooks · Billing · Feature Flags · OpenTelemetry · Docker الإنتاجي · CI/CD. (انظر §19.)

---

## 2. Adaptive Architecture — الأسئلة الستة (PART 4 من القواعد)

| # | السؤال | الإجابة المعتمدة (ADR-014) |
|---|---|---|
| Q1 | الـ Apps | `app-server` فقط (Hono) |
| Q2 | نوع الـ API | REST + OpenAPI |
| Q3 | Realtime | لا |
| Q4 | الـ Auth | Better Auth: إيميل وباسورد + تأكيد إيميل (OAuth لاحقاً B-16) |
| Q5 | Queue/Jobs | لا في البداية (B-2، وCL-05 لاختيار الأداة) |
| Q6 | Storage | لا في البداية (B-4) |

### قرارات الإضافة
```markdown
Redis → rate limiting موزّع | caching ضروري (B-1)      Queue → jobs/events كتير (B-2)
Storage → upload حقيقي (B-4)                              GraphQL/Realtime → خارج النطاق
```

---

## 3. هيكل المشروع (repo مستقل — ADR-015)

```
bun-hono-api-starter/
├── src/                  # التطبيق (القسم 4)
├── tests/                # unit · integration · security
├── scripts/              # db (تسمية الترحيلات) · security · setup
├── docs/                 # PLAN__Bun-hono-api-starter.md (الأصل) · decisions/ · security/
├── docker-compose.dev.yml   # Postgres 16 فقط حالياً
├── drizzle.config.ts · bunfig.toml · tsconfig.json · package.json · .env.example
├── AI_INSTRUCTIONS.md · ARCHITECTURE.md · SPECKIT.md · PLAN.md · PROJECT_TRACKER.md
└── README.md · CHANGELOG.md
```
المشروع مبني بحيث ينتقل كما هو لـ `apps/app-server` داخل Monorepo بعدين (المنفذ 2001 من قواعد BomBa).

---

## 4. هيكل `src/` وإعدادات المشروع

```
src/
├── app.ts · server.ts
├── alias/                # index · core · libs  (ADR-010)
├── config/               # env.ts · database.ts
├── core/                 # errors/ · responses/ · constants/ · types/ · utils/
├── database/             # client.ts · schema/ · migrations/ · seeds/ · transactions/
├── middleware/           # request-id · error-handler · request-logger · authentication
│                         # authorization · tenant-context · security-headers
├── modules/              # auth · users · tenants · memberships · roles · permissions
│   └── <name>/           # settings · audit-logs · api-keys · health
│       ├── <name>.routes.ts · .controller.ts · .service.ts · .repository.ts
│       ├── <name>.validation.ts · .types.ts · .test.ts
│       └── index.ts      # الـ API العام للموديول
├── events/               # EventBus داخل الذاكرة + listeners (ADR-012)
└── openapi/              # registry · schemas
```
`.validation.ts` (Zod) منفصل عن `database/schema` (Drizzle) عشان نتفادى الخلط (ADR-015).

### tsconfig (Paths)
```json
{
  "compilerOptions": {
    "strict": true,
    "baseUrl": ".",
    "paths": { "@a": ["./src/alias/index.ts"], "@a/*": ["./src/alias/*"], "@/*": ["./src/*"] }
  }
}
```

### متغيرات البيئة (أسماء القواعد أولاً، والجديد بأسماء الخطة — ADR-015)
```bash
APP_NAME=bun-hono-api   APP_ENV=development   NODE_ENV=development   PORT_SERVER=2001
DATABASE_URL=postgresql://user:pass@localhost:5432/dbname   DATABASE_POOL_MAX=10   DATABASE_CONNECTION_TIMEOUT=10000
BETTER_AUTH_SECRET=<32+ chars>   BETTER_AUTH_URL=http://localhost:2001
CORS_ORIGINS=http://localhost:2002   TRUST_PROXY=false   RATE_LIMIT_WINDOW_MS=900000   RATE_LIMIT_MAX=100
LOG_LEVEL=debug   DEFAULT_LANGUAGE=en   ENABLE_API_DOCS=true   ENABLE_REGISTRATION=true   ENABLE_EMAIL_VERIFICATION=true
```
كل متغير يتحقق بـ Zod عند الإقلاع، والإقلاع بيفشل لو الإعداد غلط. `.env` مش بيدخل Git، و`.env.example` بدون أسرار.

---

## 5. طبقات الموديول والاعتماديات

```
Request → Middleware (request-id · auth · tenant · authorization) → Validation (Zod)
        → Controller → Service → Repository → Drizzle → PostgreSQL
```
- الاعتماد للداخل: Controller ← Service ← Repository ← Drizzle. الـ Service/Domain **ممنوع** يستورد Hono.
- الموديول بيملك منطقه وجداوله، وممنوع يعدّل جداول موديول تاني مباشرة (بيستدعي service موديول تاني عبر `index.ts`).
- نمط الكود: كائنات `XController` / `XService` / `XRepository` (زي قواعد BomBa).

---

## 6. نظام الـ Alias `@a` على الـ Backend (ADR-010)

```markdown
src/alias/index.ts → بيجمع: core.ts (hono, zod, drizzle helpers) + libs.ts (مكتبات خارجية) + public.ts (API عام للموديولات)
✅ المكتبات الخارجية والـ API العام للموديولات: من `@a`
✅ داخل نفس الموديول: مسارات `./` فقط
❌ ممنوع تصدير ملف داخلي من موديول (بيعمل circular dependency)
❌ ممنوع import مباشر من 'zod' أو 'hono' خارج src/alias (no-restricted-imports)
```
أي مكتبة جديدة بتتصدّر في `@a` قبل أول استخدام، وبتتشال منه لما تتحذف.

---

## 7. قاعدة البيانات

### 7.1 المحرك والمفاتيح (ADR-002 · 004)
- Postgres فقط (لا SQLite). المفتاح الأساسي `id SERIAL`، وعمود `public_id UUID` (UUIDv7) هو اللي بيظهر في الـ API. المفتاح الداخلي مش بيتكشف.
- `tenant_id INT NOT NULL` مفهرس في كل جدول عمل. `users` عامة (بدون tenant_id).
- حقول التدقيق: `created_at` · `updated_at` · `created_by` · `updated_by`. `deleted_at` فقط لما يكون في متطلب موثّق.
- الجداول الأولية: `tenants` · `users` · `memberships` · `sessions` · `roles` · `permissions` · `role_permissions` · `audit_logs` + جداول Better Auth `[VERIFY]`.

### 7.2 الترحيلات (ADR-005)
- الأصل: `drizzle-kit generate`. سكريبت في `scripts/db/` يعيد التسمية: `{PREFIX}_{NNNN}_{ACTION}_{TABLE}` ويكتب ملف `.down.sql`. (CL-03)
- `py` = جدول مستقل · `sy` = بيعتمد على غيره. النطاقات: CORE `0001–0007` · ENTITIES `0100+` · BUSINESS `0200+` · AUDIT `0300+` · SEED `0900+`.
- ممنوع تعديل ترحيل بعد الدمج · ترحيل مدمّر في الإنتاج بمراجعة وbackup · لا تطبيق تلقائي عند الإقلاع.
- ترتيب التنفيذ بالرقم، والاعتماد الدائري: جدول بلا FK ثم `alter` في ترحيل لاحق.

### 7.3 الأعمدة الزمنية والمالية
`TIMESTAMPTZ` (UTC) دايماً (ADR-019). أي مبلغ مالي مستقبلاً: `DECIMAL(18,4)` كـ string مع `decimal.js`، ممنوع float. (الـ Ledger خارج الـ Starter — ADR-007.)

---

## 8. تعدد المستأجرين (ADR-006)

```markdown
- قاعدة وسكيمة مشتركين + tenant_id في كل جدول عمل.
- العضوية: memberships (tenant_id, user_id, role_id, status) — فريد (tenant_id, user_id).
- الجلسة بتحمل active_tenant_id. هيدر X-Tenant-Id بيتحقق مقابل عضوية المستخدم قبل أي عملية.
- Data Access Layer بيحقن tenant_id تلقائياً. ممنوع استعلام جدول عمل من برّاه.
- لا نثق في tenant_id أو organization_id جاي من العميل من غير تحقق عضوية وصلاحية.
- RLS: تقييم في 5.7 (Neon pooling) — ممنوع ندّعي إن العزل محمي بـ RLS قبل ما تتفعّل وتتختبر (B-14).
```

---

## 9. المصادقة (ADR-008 · 009)

- Better Auth للهوية والجلسات (كوكيز HttpOnly + Secure في الإنتاج + SameSite + trusted origins). جداول المستأجرين والعضوية **مخصصة** مش plugin المنظمات (ADR-006).
- `AuthService` هو المكان الوحيد لتشفير الباسورد: `bcrypt` cost 12، وتعليق بيوثّق آلية التمليح، وحد أقصى لطول الباسورد (bcrypt بيقطع عند 72 بايت).
- تأكيد الإيميل وإعادة التعيين خلف `EmailPort` + Console adapter (المزود الفعلي B-3).
- Rate limit للـ Auth عبر المدمج في Better Auth لحد ما نفعّل Redis (ADR-021).
- ممنوع نسجّل باسوردات/tokens/كوكيز. الباسورد ما بيتبعتش في إيميل أبداً.

---

## 10. الصلاحيات (RBAC + Permissions)

- الأدوار على مستوى المستأجر: `owner` · `admin` · `manager` · `member` · `viewer`. إدارة المنصة منفصلة، و`owner` مش بيبقى platform admin تلقائياً.
- الصلاحيات `resource:action` بجمع أسماء الجداول: `users:read` · `members:invite` · `roles:manage` · `audit_logs:read` (ADR-020).
- Deny by default · الفحص على السيرفر دايماً · منع تصعيد الصلاحيات (مستخدم ميمنحش صلاحية ميملكهاش) · حماية آخر Owner · نقل الملكية بتأكيد · تسجيل التغييرات الحساسة.
- الـ API Keys بتاخد scopes صريحة، ومش بترث صلاحيات المستخدم كاملة.

---

## 11. تصميم الـ API (ADR-011)

- Versioning: `/api/v1`. Better Auth بيحتفظ بمساراته الموثّقة.
- الرد الموحّد:
```ts
// نجاح
{ success: true, data: T, message?: string, meta: { requestId: string } }
// فشل
{ success: false, data: null, message: string, error: { code: 'AUTH_001', details?: unknown }, meta: { requestId: string } }
// Pagination: نفس شكل النجاح + pagination / cursor
```
- أكواد الأخطاء بنمط القواعد: `AUTH_` · `USR_` · `TEN_` · `PERM_` · `VAL_` · `DB_` · `SYS_` + رقم ثابت. الأكواد دي ثابتة للقراءة الآلية.
- الرسائل: كتالوج ar/en بيتحدد من `Accept-Language` (إنجليزي افتراضي)، من غير react-i18next.
- Status codes قياسية (200/201/204/400/401/403/404/409/413/422/429/500/503).
- Pagination بـ cursor للأحجام الكبيرة، وحد أقصى للصفحة. الفلترة والترتيب بحقول مسموحة فقط (لا SQL identifier من العميل).
- لا نفرض الرد الموحّد على callbacks أو webhooks بتتطلب بروتوكول خاص.

---

## 12. Validation

Zod لـ: body · query · params · headers (عند الحاجة) · environment. Schemas صارمة (strict)، حدود أطوال وأرقام وأحجام arrays. حقول غير معروفة ما بتتحوّلش لأعمدة DB (mass assignment).

---

## 13. Logging

Pino بـ JSON على stdout (12-factor). الحقول: timestamp · level · service · env · requestId · route · status · duration. قنوات (error/access/security/audit) بحقل `channel`. redaction لـ authorization/cookie/password/token. تدوير ملفات اختياري في التطوير فقط.

---

## 14. عزل الأعطال والإيقاف (ADR-013)

```markdown
- الفشل بيتعزل على مستوى الطلب (error handler مركزي، الخادم ما بيقعش بسبب طلب واحد).
- unhandledRejection: تسجيل كامل + تنبيه. uncaughtException: إيقاف نضيف ثم إعادة تشغيل من الـ orchestrator.
- Graceful Shutdown على SIGTERM/SIGINT: وقف قبول طلبات جديدة · انتظار الطلبات الجارية بمهلة · إغلاق اتصالات الـ DB.
- كل استدعاء خارجي = Timeout. Health: live (العملية شغالة) و ready (جاهز يخدم، بيفحص الـ DB).
```

---

## 15. الأمان

`hono/secure-headers` · CORS بأصول محددة (لا wildcard مع credentials) · حد حجم الـ body · Zod على كل مدخل · Drizzle parameterized (ممنوع raw SQL بمدخل مستخدم) · CSRF عبر trusted origins/SameSite حسب توثيق Better Auth · لا stack traces للعميل · أسرار من `.env` فقط · `bun audit` + فحص أسرار (Phase 7).

---

## 16. المعاملات والوقت والأحداث والتدقيق

### 16.1 المعاملات (ADR-018)
```ts
// مثال: إنشاء مستأجر + عضوية المالك + الأدوار — الكل أو لا شيء
await withTransaction(async (tx) => {
  const tenant = await TenantsRepository.create(tx, dto)
  await MembershipsRepository.addOwner(tx, tenant.id, actorId)
  await AuditRepository.record(tx, { action: 'tenants:create', entityId: tenant.id })
})
```
المعاملة قصيرة وبدون طلبات خارجية. أي فشل = rollback كامل. اختبار rollback إلزامي.

### 16.2 الوقت (ADR-019)
تخزين ومعالجة بـ UTC وISO 8601 (`TIMESTAMPTZ` ↔ `2026-10-10T12:30:00.000Z`). ممنوع `new Date()` المحلي في المنطق من غير UTC. التحويل للتوقيت المحلي عند العرض فقط (Frontend). الوقت بيتحقن في الـ services (clock) عشان الاختبار.

### 16.3 الأحداث والتدقيق (ADR-012)
EventBus داخل الذاكرة (interface-based) بيستقبل أحداث الـ domain بعد نجاح المعاملة. الـ audit **listener** بيكتب في جدول `audit_logs` واحد: `id · tenant_id (nullable) · actor_id · action · entity_type · entity_id · diff · ip_address · user_agent · request_id · severity · tags · created_at`. الـ outbox مؤجّل (B-8). صفوف الـ audit مش "tamper-proof" — ممنوع وصفها كده.

---

## 17. Testing

`bun test`. Unit (services, schemas, permission evaluator) + Integration على **Postgres حقيقي** (قيود، ترحيلات، معاملات، rollback، عزل مستأجر) + Security (SQLi، cross-tenant، تصعيد، malformed، oversized). تغطية: 80% عام، 95% لمنطق الصلاحيات. كل اختبار قابل للتكرار (DB اختبار مخصص، fixtures ثابتة، وقت متحكَّم). ممنوع اختبارات مدمّرة على أي DB غير الاختبار.

---

## 18. Code Quality & Conventions

`eslint.config.mjs` (flat) + Prettier. `@typescript-eslint/no-explicit-any: error` · `no-unused-vars` بتتجاهل `_` · `no-restricted-imports` لحماية `@a` · `eqeqeq` · `curly`. File Header + JSDoc عربي مصري في كل ملف. Commit ذري بالعربي المصري وفروع بترقيم شجري (AI_INSTRUCTIONS §9).

---

## 19. الخدمات المؤجلة (لا تُبنى قبل قرار)

Redis (B-1) · Queue (B-2, CL-05) · Email (B-3) · Storage (B-4) · Notifications/Webhooks (B-5) · Billing (B-6) · Feature Flags (B-7) · Idempotency/Outbox (B-8) · OpenTelemetry/Sentry (B-9) · Docker الإنتاجي + Codespaces (B-10) · CI/CD (B-11) · Performance (B-12) · Ledger والمستندات (B-13). التفاصيل في PROJECT_TRACKER › BACKLOG.

---

## 20. سجل القرارات المعمارية (ADR)

> قرارات المستخدم بتاريخ 2026-10-10. أي قرار جديد = صف جديد (+ ملف في `docs/decisions/` لو كبير). الحالة: `Accepted` | `Accepted (تلقائي)` | `Proposed` | `Superseded` | `Open`.

| ID | القرار | السبب | البدائل المرفوضة | الحالة |
|---|---|---|---|---|
| **ADR-001** | Runtime وFramework: Bun + Hono (طلب صريح من المستخدم بدل Node/Express في قواعد BomBa) | قرار المشروع | Node 20 + Express | Accepted |
| **ADR-002** | قاعدة البيانات: PostgreSQL فقط (Docker محلياً، Neon إنتاجاً). تخلّينا عن NFR-5 (تطابق Postgres/SQLite) | Postgres الحقيقي مطلوب للاختبارات (قفل صفوف، RLS)، وSQLite بيضاعف تعريف الـ schema | Postgres + SQLite | Accepted |
| **ADR-003** | DB PRD ملزم لطبقة الداتابيز فقط؛ باقي المشروع بالخطة الأصلية؛ Express PRD مصدر أفكار فقط | تحديد الأسبقية بوضوح | DB PRD ملزم للكل · أفكار فقط | Accepted |
| **ADR-004** | المفتاح الأساسي `SERIAL` + عمود `public_id` UUIDv7 يظهر في الـ API | يحترم DB PRD ويمنع كشف الأرقام التسلسلية | SERIAL فقط · UUID فقط | Accepted |
| **ADR-005** | الترحيلات: `drizzle-kit generate` + سكريبت إعادة تسمية py/sy + ملفات `.down.sql` (CL-03) | يوفّق بين DB PRD والأداة | ترقيم drizzle الافتراضي فقط | Accepted |
| **ADR-006** | `tenants` + `memberships` جداول مخصصة بأسماء DB PRD؛ Better Auth للهوية والجلسات فقط | تحكم كامل في SERIAL وtenant_id وRBAC | Better Auth organization plugin | Accepted |
| **ADR-007** | الـ Ledger والكيانات والمستندات خارج الـ Starter (B-13) | الـ Starter عام مش ERP | داخل الـ Starter من أول يوم | Accepted |
| **ADR-008** | تشفير الباسورد `bcrypt` cost 12 كـ custom hasher في Better Auth ومغلّف في `AuthService` (CL-02) | DB PRD والقواعد | Argon2id · افتراضي Better Auth | Accepted |
| **ADR-009** | المصادقة: جلسات Better Auth + API Keys. Bearer/JWT وInternal Token مؤجّلين (B-17) | أبسط ومتوافق مع "لا تضف بدري" | الأربع آليات من الأول | Accepted |
| **ADR-010** | `@a` على الـ Backend للمكتبات الخارجية والـ API العام للموديولات؛ داخل الموديول `./` | يتفادى الاعتماد الدائري | حرفي بالكامل · عدم التطبيق | Accepted |
| **ADR-011** | الرد الموحّد `{success,data,message,error?,meta:{requestId}}` + أكواد `AUTH_001` + رسائل ar/en من `Accept-Language` | دمج القواعد والخطة | عربي مصري فقط · أكواد شجرية | Accepted |
| **ADR-012** | EventBus داخل الذاكرة + audit listener + جدول `audit_logs` واحد بأعمدة مدموجة؛ الـ outbox مؤجّل (B-8) | الـ outbox ملوش لازمة قبل الـ queue | Outbox من الأول | Accepted |
| **ADR-013** | عزل الفشل على مستوى الطلب + Graceful Shutdown؛ `uncaughtException` = إيقاف نضيف وإعادة تشغيل (بدل "Zero-Crash") | حالة الـ process بعد uncaughtException غير مضمونة | الاستمرار بعد أي استثناء | Accepted |
| **ADR-014** | النطاق: المراحل 0–7 فقط؛ الأسئلة الستة: app-server/REST/لا Realtime/Better Auth/لا Queue/لا Storage؛ الباقي Backlog | MVP أولاً | تنفيذ الـ 13 مرحلة | Accepted |
| **ADR-015** | repo مستقل · المنفذ 2001 · أسماء المتغيرات من القواعد والجديد من الخطة · ملفات الموديول `.validation.ts` | قابل للنقل لـ `apps/app-server` | Monorepo من الأول | Accepted |
| **ADR-016** | نظام التوثيق: الملفات الخمسة في الجذر (يحل محل AGENTS/AI_CONTEXT/AI_SESSION/TODO)؛ أقسام الـ UI في baseline اتشالت، والخطة الأصلية في `docs/` | مهارة ai-project-docs-system أحدث | نظام الأربع ملفات | Accepted |
| **ADR-017** | التسليم: العمل في Claude Code/Codespaces على repo المستخدم؛ Claude بيكتب الوثائق والتعليمات | تشغيل Postgres وCI حقيقي | بناء الكود في sandbox | Accepted |
| **ADR-018** | أي كتابة متعددة الجداول (مثال: شركة + فرع) في Transaction واحدة بمبدأ الكل أو لا شيء | قاعدة من المستخدم | كتابات منفصلة | Accepted |
| **ADR-019** | UTC وISO 8601 عند التخزين والمعالجة؛ التحويل للتوقيت المحلي عند العرض فقط | قاعدة من المستخدم | توقيت محلي في الـ backend | Accepted |
| **ADR-020** | افتراضات صغيرة: 5 أدوار · صلاحيات `resource:action` بالجمع · Pino على stdout · `hono/secure-headers` · `bun test` بتغطية 80/95 · ESLint + Prettier · DECIMAL(18,4) للمال لاحقاً · Git بترقيم شجري وcommits مصرية | موافقة المستخدم | بدائل مذكورة في الأسئلة | Accepted |
| **ADR-021** | تلقائي: rate limit مسارات الـ Auth عبر المدمج في Better Auth لحد تفعيل Redis (B-1)، وموثّق كقيد | القواعد بتفرض rate limit على Auth وRedis مؤجّل | حل مخصص بالذاكرة | Accepted (تلقائي) |

### كيف تضيف ADR
```markdown
1. وضّح السياق + الخيارات + أثر كل خيار.   2. اسأل المستخدم (لو التعارض جوهري).
3. أضف الصف هنا + حدّث الأقسام المتأثرة + PROJECT_TRACKER (AI CONTEXT + CHANGE LOG).
4. Superseded لو القرار القديم اتلغى (متحذفوش).
```

---

## 21. Glossary

| المصطلح | المعنى |
|---|---|
| **Tenant** | المستأجر/المؤسسة — وحدة العزل |
| **Membership** | عضوية مستخدم في tenant بدور معيّن |
| **public_id** | UUIDv7 اللي بيظهر في الـ API بدل المفتاح الداخلي |
| **py / sy** | بادئة ترحيل: Primary (مستقل) / Secondary (يعتمد على غيره) |
| **DAL** | Data Access Layer — بيحقن `tenant_id` تلقائياً |
| **AuthService** | المكان الوحيد لتشفير الباسورد |
| **ERR** | كتالوج أكواد الأخطاء الثابتة |
| **Envelope** | شكل الرد الموحّد |
| **UTC / ISO 8601** | توقيت وصيغة التواريخ المعتمدة للتخزين والمعالجة |
| **ADR** | سجل قرار معماري |
| **UD** | قرار حسمه المستخدم (SPECKIT 9.1) |
| **RLS** | Row-Level Security في Postgres |