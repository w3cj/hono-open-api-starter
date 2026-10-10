# 📋 PROJECT TRACKER — تتبع المشروع

> **@file** : PROJECT_TRACKER.md
> **@description** : الحالة الحيّة للمشروع: شجرة المهام، حالة الموديولات، التركيز الحالي، القرارات المفتوحة، العوائق، Backlog، Change Log، وسياق الـ AI. **بيتحدّث في كل جلسة.**
> **@updated** : `[ { "date": "2026-10-10", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف + تهيئة شجرة المهام من PLAN.md" }, { "date": "2026-10-10", "version": "1.0.1", "by": ["Arena Agent"], "comment": "توثيق نتائج فحص توافق Bun للمهمة 0.1" }, { "date": "2026-10-10", "version": "1.0.2", "by": ["Arena Agent"], "comment": "توثيق تهيئة المشروع بالمهمة 0.2" }, { "date": "2026-10-10", "version": "1.0.3", "by": ["Arena Agent"], "comment": "توثيق ESLint وPrettier بالمهمة 0.3" } ]`
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
| **Overall Progress** | **6%** (4 / 63 مهمة ✅ Verified) |
| **Repo State** | هيكل Bun مهيّأ (0.2): `package.json` بالحزمة المختبرة + `tsconfig` strict و`@a`/`@/*` + `bunfig.toml` + `bun.lock` + `src/alias`. قالب Node/Turso القديم اتشال (محتواه محفوظ في git عند `05303ed`) |
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
| 0 | Repo Analysis & Setup | 7 | 4 | 1 | 0 | 0 | 57% |
| 1 | Project Foundation | 10 | 0 | 0 | 0 | 0 | 0% |
| 2 | Database Foundation | 12 | 0 | 0 | 0 | 0 | 0% |
| 3 | Authentication | 7 | 0 | 0 | 0 | 0 | 0% |
| 4 | Authorization | 6 | 0 | 0 | 0 | 0 | 0% |
| 5 | Multi-Tenancy | 7 | 0 | 0 | 0 | 0 | 0% |
| 6 | Core API Modules | 9 | 0 | 0 | 0 | 0 | 0% |
| 7 | Basic Hardening & Release | 5 | 0 | 0 | 0 | 0 | 0% |
| **Σ** | | **63** | **4** | **1** | **0** | **0** | **6%** |

---

## 🌳 TASK TREE (الشجرة الرئيسية)

> الـ Deliverable لكل مهمة في `PLAN.md` (جدول المرحلة) والمواصفات في `SPECKIT.md`.

```
Phase 0: Repo Analysis & Setup .................................... ⬜  (release/1.1)
├── 0.1  فحص الـ repo وتأكيد توافق Bun مع المكتبات المختارة ....... ✅
├── 0.2  تهيئة المشروع: package.json + tsconfig strict + bunfig + paths .... ✅
├── 0.3  ESLint flat config + Prettier + no-restricted-imports .... ✅
├── 0.4  أدوات الاختبار bun test + عتبات التغطية 80/95 ............ ✅
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
- Branch: — (قبل الفرع الأول)   - Spec: CL-04   - الحالة: ✅ VERIFIED
- واقع الـ repo: `package.json` و`pnpm-lock.yaml` بيستخدموا Node/tsx و`@hono/node-server` وDrizzle مع `@libsql/client` و`dialect: "turso"`. مفيش `postgres` أو `better-auth` أو `bcrypt` كاعتماديات مباشرة، ومفيش `bunfig.toml` أو Bun lockfile. الـ repo الحالي مختلف عن المكدس المعتمد في ARCHITECTURE.
- نطاق الاختبار: إصدارات `latest` المستقرة وقت الفحص (`npm view <package>@latest version`) اتثبتت بـBun في `/tmp/bun-cl04-project`، من غير تعديل `package.json` أو lockfile أو كود المشروع.
- البيئة: Bun `1.4.3` · PostgreSQL `16.4` من binaries مؤقتة `@embedded-postgres/linux-x64@16.4.0-beta.14`. Docker مش موجود في البيئة، فاشتغل PostgreSQL على `127.0.0.1:55432` للاختبار واتقفل بعده.
- المكتبات المختبرة: `hono@4.13.13` · `zod@4.6.5` · `drizzle-orm@0.45.4` · `postgres@3.4.9` · `better-auth@1.7.7` · `pino@10.4.0` · `bcrypt@6.0.0`.
- أمر التحقق: `/tmp/bun-cl04-agent/node_modules/.bin/bun /tmp/bun-cl04-project/smoke.mjs` — exit code `0` و`SUMMARY 7/7 passed`.
- النتائج: Hono مع `Bun.serve` رجّع HTTP 200 · Zod قبل ورفض البيانات المتوقعة · `postgres.js` نفّذ `SELECT` على PostgreSQL 16.4 · Drizzle نفّذ `CREATE` و`INSERT/RETURNING` و`SELECT` · Better Auth handler على Hono رجّع `/api/auth/ok` بـHTTP 200 و`{ok:true}` · Pino كتب سجل JSON منظم · bcrypt نجح في `hash/compare` على cost 12.
- حدود الدليل: اختبار Better Auth شمل إنشاء الـhandler ومسار `/ok` فقط، مش DB adapter أو جلسات/تسجيل دخول؛ CL-01 وCL-02 لسه مفتوحين لمهامهم. README الرسمي لـHono وDrizzle بيذكر Bun صراحة؛ توثيق `postgres` وPino وbcrypt بيركز على Node/Deno أو Node، فنجاح التشغيل دليل عملي للإصدارات دي مش ضمان دعم رسمي من أصحابها. التطبيق الموجود في الـrepo نفسه ما اتشغّلش تحت Bun بسبب اختلاف إعداداته واعتمادياته؛ ما اتعملش أي تغيير عليه.

### Task 0.2: تهيئة المشروع
- Branch: — (لسه قبل فرع 0.5)   - Spec: —   - الحالة: ✅ VERIFIED
- التنفيذ: `package.json` جديد بالاسم `bun-hono-api-starter` وأسماء scripts المؤكدة (`typecheck` / `lint` / `test`) والاعتماديات السبعة المختبرة في 0.1 بإصداراتها بالظبط + `typescript@5.9.3` و`@types/bun@1.4.2` و`@types/bcrypt@6.0.0` · `tsconfig.json` بـ`strict: true` ومسارات `@a` و`@a/*` و`@/*` · `bunfig.toml` (`[install] exact = true`) · `src/alias/` (index + core + libs) بتصدّر الحزمة كاملة من `@a` · هيكل `src/` الفاضي (config · core · database · middleware · modules · events · openapi).
- إزالة قالب Node/Turso القديم: `src/app.ts` و`src/index.ts` و`src/env.ts` و`src/db/` و`src/lib/` و`src/middlewares/` و`src/routes/` و`drizzle.config.ts` (dialect turso) و`vitest.config.ts` و`eslint.config.mjs` (antfu) و`pnpm-lock.yaml` — تنفيذ قرار المستخدم بمتابعة الوثيقة والخطة (مخالفات ADR-001/002/020)، والمحتوى القديم محفوظ في git عند `05303ed`.
- إصدار TypeScript: اتختار `5.9.3` (آخر 5.x الناضج بدل 7.x الجديد) لتوافق أنواع Drizzle/Better Auth — قرار صغير مسجّل.
- دليل التحقق: `bun install` → 48 حزمة وبـ`bun.lock` · `bun run typecheck` → exit code `0` بدون أخطاء · فحص runtime بـ`bun -e` استورد من `@a` و`@/alias/core` وطلع `Hono === HonoFromSrc` بمقدار `true` (المسارين بيوصلوا لنفس الوحدة).
- بوابات الجودة: typecheck ✅ · lint ⬜ (exit 127: eslint مش مثبت — إعداده مهمة 0.3) · test ⬜ (`bun test` v1.4.3 شغّال بس قال `No tests found!` — التجهيز مهمة 0.4) · build غير معرّف لحد دلوقتي.
- ملاحظات: `.env.example` و`.env.test` و`README.md` لسه بيوصفوا القالب القديم — مهامهم 1.1 و0.7 · `drizzle.config.ts` الجديد هيتعمل في 2.2 · السكريبت `test` = `bun test` محتاج Bun على PATH زي أي تشغيل حقيقي للمشروع.

### Task 0.3: ESLint flat config + Prettier + no-restricted-imports
- Branch: — (لسه قبل فرع 0.5)   - Spec: —   - الحالة: ✅ VERIFIED
- التنفيذ: تثبيت `eslint@10.12.0` و`@eslint/js@10.0.1` و`typescript-eslint@8.71.1` و`globals@17.13.0` و`eslint-config-prettier@10.1.8` و`prettier@3.9.10` · `eslint.config.mjs` (flat) بقواعد ARCHITECTURE §18 كاملة: `no-explicit-any: error` و`no-unused-vars` بتتجاهل `_` (كل الفئات) و`no-restricted-imports` بتحمي `@a` من الاستيراد المباشر للسبع مكتبات (مع إعفاء `src/alias/**`) و`eqeqeq: always` و`curly: all` + `no-eval`/`no-new-func` + `consistent-type-imports` · `prettier.config.mjs` (singleQuote + semi) · سكريبتات `format` و`format:check` بحدود مقصودة (`src/**/*.ts` و`*.json` و`*.mjs`) — الـ docs العربية خارج نطاق Prettier عمداً.
- اكتشاف وتصحيح أثناء التنفيذ: `eslint-config-prettier` بيسدّد قاعدة `curly` (specialRule) وهو آخر config، فبقت القاعدة المطلوبة ميتة؛ اتثبت ده بفحص حرف `curly` في `node_modules/eslint-config-prettier/index.js`، واتحل بإعادة تفعيل `curly: ['error','all']` بعد كائن `prettier`.
- دليل التحقق: `bun run lint` → exit `0` · `bun run format:check` → `All matched files use Prettier code style!` · `bun run typecheck` → exit `0` · الاختبار السلبي: ملف مؤقت `src/negative-check.ts` بخمسة انتهاكات (استيراد `hono` مباشر + `any` + متغير غير مستخدم + `==` + `if` بدون أقواس) → `5 problems (5 errors)` بكل القواعد المطلوبة شغّالة، وبعدها اتشال والبوابات رجعت خضرا.
- بوابات الجودة: typecheck ✅ · lint ✅ · format:check ✅ · test ⬜ (لسه 0.4).
- ملاحظات: `curly` لازم تفضل بعد `prettier` في `eslint.config.mjs` — لو اتنقلت القاعدة هتتهدى تاني؛ التعليق في الملف بيوثق ده.

### Task 0.4: أدوات الاختبار bun test + عتبات التغطية 80/95
- Branch: — (لسه قبل فرع 0.5)   - Spec: —   - الحالة: ✅ VERIFIED
- التنفيذ: `bunfig.toml` بـ `[test]`: `coverage = true` (التغطية شغالة مع كل `bun test`) · `coverageThreshold = { lines = 0.8, functions = 0.8 }` (بيتفحص **لكل ملف لوحده** زي موثق في Bun docs، وأي إخلال بيطلع exit 1) · `coverageSkipTestFiles = true` · `src/alias/alias.test.ts` باختبارات حقيقية على السطح العام `@a`.
- الاختبارات: كل الحزم الـ10 في `@a` موجودة ومعظمها callable · `Hono` من `@a` ومن `@/alias/core` **نفس الوحدة** (توافق المسارين) · سلوك فعلي: Hono بيرد على طلب HTTP · Zod بيقبل/يرفض · bcrypt وbetterAuth بواجهاتهم المطلوبة → `5 pass / 0 fail` + تقرير تغطية 100% lines/funcs على ملفات `src/alias`.
- الإثبات السلبي (عتبة التغطية): ملف مؤقت `src/tmp-low-coverage.ts` (دالة مغطاة + دالة لا) مع اختبار جزئي → الاختبارات كلها نجحت **بس** `bun run test` طلع **exit 1** لأن الملف تحت العتبة (funcs 50% · lines 33%) — العتبة بتتفرض فعلاً ومش شكلي؛ الملفين اتشالوا وبعدها رجع exit 0.
- عتبة **95% للصلاحيات (4.6)**: موثقة كقرار في تعليق `bunfig.toml` والسجل ده — Bun مفيش per-path thresholds، ففي 4.6 هترفع العتبة العامة لكل الملفات (زي `PLAN.md` 4.6). المفروضة دلوقتي 80/80 لكل ملف.
- بوابات الجودة: test ✅ (5/5 + coverage report) · lint ✅ · typecheck ✅ · format:check ✅.
- ملاحظة بيئة: `bun` كان بره PATH في بيئة التنفيذ هنا (تحت `/tmp`)، فالتشغيل تم مع إضافته على PATH زي أي بيئة Bun حقيقية.

---

## 🔄 CURRENT FOCUS (التركيز الحالي)

```
Working On : لا مهمة 🔵 — 0.4 ✅ وخلاص؛ مستني أمر المستخدم للمهمة الجاية
Next Up    : 0.5 (Git: main/develop + قالب commit + أول فرع بـ Tree ID) ثم 0.6 → 0.7
Parallel   : —
Blockers   : لا يوجد
```
> قاعدة: مهمة واحدة 🔵 في نفس الوقت.

---

## ❓ OPEN DECISIONS (قرارات مفتوحة)

| ID | السؤال | يحجب | تاريخ الفتح | الخيارات / التوصية | الحالة |
|---|---|---|---|---|---|
| CL-04 | توافق Bun مع المكتبات المختارة | Phase 1 | 2026-10-10 | smoke test فعلي 7/7 على Bun 1.4.3 (0.1)، والإصدارات المختبرة اتثبتت في المشروع في 0.2. الحالة: محسوم بموافقة المستخدم («كمل») | ✅ محسوم — اعتمد |
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
| 2026-10-10 | 0.1 | ✅ Verified | تشغيل smoke tests فعلية 7/7 للمكدس المخطط تحت Bun 1.4.3 وعلى PostgreSQL 16.4؛ اختلاف إعدادات الـ repo الحالي اتوثّق من غير تعديل للكود أو الاعتماديات، واعتماد CL-04 منتظر المستخدم |
| 2026-10-10 | 0.2 | ✅ Verified | تهيئة المشروع: package.json + tsconfig strict مع `@a`/`@/*` + bunfig + bun.lock + src/alias وهيكل src/؛ إزالة قالب Node/Turso القديم (محفوظ في git عند 05303ed)؛ typecheck يعدّي والـ aliases متحقق منها بـruntime |
| 2026-10-10 | 0.3 | ✅ Verified | ESLint flat + Prettier + حماية `@a`؛ الاختبار السلبي وقّع 5/5 انتهاكات؛ تصحيح تعارض `curly` مع eslint-config-prettier؛ lint وformat:check وtypecheck بيعدّوا |
| 2026-10-10 | — | ✅ قرارات | تسجيل ADR-001…ADR-021 في ARCHITECTURE |
| 2026-10-10 | — | ❓ فتح | CL-01…CL-05 + MOD-1 |

---

## 🧠 AI CONTEXT (سياق للـ AI الجديد)

### ما تم
- اتقرت الخطة الأصلية وPRD السيرفر (Express) وPRD الداتابيز وكل مهارات BomBa المطلوبة.
- المستخدم حسم Q1…Q16 كلها بتوصياتي، وأضاف قاعدتين: المعاملات (الكل أو لا شيء) وUTC بصيغة ISO 8601.
- اتكتبت الملفات الخمسة بشكل متكيّف مع Backend.
- 0.1 ✅: اتفحص الـ repo الفعلي (كان Node/tsx + Drizzle/Turso/libSQL)، واختبارات Bun/CL-04 عدّت 7/7 على Bun 1.4.3 وPostgreSQL 16.4 في مساحة مؤقتة.
- المستخدم وجه بمتابعة الوثيقة والخطة، وبعدها أمر بـ«كمل»: فاتعتمد CL-04 واتنفّذت 0.2.
- 0.2 ✅: `package.json` بالحزمة المختبرة السبعة بإصدارتها بالظبط + `typescript@5.9.3` و`@types/bun` و`@types/bcrypt` · `tsconfig` strict مع مسارات `@a` و`@a/*` و`@/*` · `bunfig.toml` · `src/alias` (index/core/libs) · هيكل `src/` الفاضي. قالب Node/Turso القديم اتشال بالكامل (محفوظ في git عند `05303ed`) — ده تنفيذ قرار مسار الوثائق.
- 0.3 ✅: `eslint.config.mjs` (flat) بقواعد §18 كاملة + حماية `@a` من الاستيراد المباشر (مع إعفاء `src/alias/**`) · `prettier.config.mjs` (singleQuote + semi) · سكريبتات `format`/`format:check` بحدود مقصودة تسيب الـ docs العربية في حالها. الاختبار السلبي أثبت إن القواعد الخمسة (restricted-imports وany وunused وeqeqeq وcurly) بتشتغل فعلاً.
- 0.4 ✅: `bunfig.toml` بـ coverage شغالة دائماً + عتبة 80/80 per file (lines/functions) + `coverageSkipTestFiles` · `src/alias/alias.test.ts` (5 اختبارات حقيقية على `@a`) · الإثبات السلبي أثبت إن أي ملف تحت العتبة بيطلع exit 1. عتبة 95% للصلاحيات قرارها مسجّل وتتفعّل في 4.6.

### الحالة الحالية
- 0.1 ✅ و0.2 ✅ و0.3 ✅ و0.4 ✅ و0.6 🟣؛ مفيش مهمة 🔵 دلوقتي؛ باقي المهام ⬜. CL-04 محسوم ✅.
- السكريبتات المؤكدة: `typecheck` ✅ · `lint` ✅ · `format`/`format:check` ✅ · `test` ✅ (5/5 مع تقرير تغطية وإجبار العتبة).

### آخر تحقق
- `bun run test` → `5 pass / 0 fail` + تقرير تغطية 100% (ملفات `src/alias`) · الإثبات السلبي: ملف تحت العتبة → exit `1` رغم نجاح الاختبارات.
- `bun run lint` → exit `0` · `bun run format:check` → `All matched files use Prettier code style!` · `bun run typecheck` → exit `0`.
- `python3 scripts/docs/validate_docs.py --root .` بعد تحديث الـ Tracker → 0 أخطاء.

### الخطوة الجاية بالظبط
1. استنى أمر المستخدم.
2. عند الأمر: نفّذ 0.5 بس (Git: main/develop + قالب commit + أول فرع بـ Tree ID)، وبعدها 0.6.

### قرارات مهمة (ملخّص — التفاصيل في ARCHITECTURE › ADR)
- Bun + Hono (ADR-001) · Postgres فقط (ADR-002) · DB PRD ملزم لطبقة الداتابيز فقط (ADR-003).
- `SERIAL` + `public_id` UUIDv7 (ADR-004) · bcrypt عبر AuthService (ADR-008) · جلسات Better Auth + API Keys (ADR-009).
- معاملات الكل أو لا شيء (ADR-018) · UTC بصيغة ISO 8601 (ADR-019).

### مشاكل معروفة / مخاطر
- R1: Better Auth مع SERIAL وbcrypt مخصص لسه `[VERIFY]` (CL-01/02)؛ اختبار 0.1 ما غطّاش adapter أو hasher مخصص.
- R2: الإصدارات المختبرة اشتغلت تحت Bun، لكن README بتاع `postgres` وPino وbcrypt مش بيوعد بدعم Bun صراحة؛ النتيجة عملية للإصدارات المذكورة ومش ضمان من أصحاب المكتبات.
- R8: rate limit بالذاكرة لحد B-1.
- R9: قالب Node/Turso القديم اتشال في 0.2 (قرار مسار الوثائق)؛ المحتوى محفوظ في git عند `05303ed`.
- `.env.example` و`.env.test` و`README.md` لسه بيوصفوا القالب القديم — مهامهم 1.1 و0.7.

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
| 2 | 2026-10-10 | Arena Agent | 0.1: فحص الـ repo واختبارات Bun/CL-04 | 0.1 ✅؛ CL-04 بانتظار اعتماد المستخدم | 7/7 smoke tests نجحوا على الإصدارات المسجلة؛ التطبيق الحالي مختلف عن الوثائق، ولم يتغير كوده أو اعتمادياته |
| 3 | 2026-10-10 | Arena Agent | 0.2: تهيئة المشروع + إزالة قالب Node/Turso | 0.2 ✅؛ CL-04 محسوم | typecheck يعدّي و`@a`/`@/*` متحقق منهم بـruntime؛ lint وtest بواباتهما 0.3 و0.4 |
| 4 | 2026-10-10 | Arena Agent | 0.3: ESLint + Prettier + no-restricted-imports · فتح PR #1 · جدول المهام · 0.4: bun test + عتبات التغطية | 0.3 ✅ و0.4 ✅؛ PR #1 مفتوح (commits `da6c852`+`cbd4b51`) | الاختبار السلبي لإثبات العتبة: ملف تحت 80% → exit 1 رغم نجاح الاختبارات؛ عتبة 95% للصلاحيات قرارها مسجّل وتتفعّل في 4.6 |
| 4 | 2026-10-10 | Arena Agent | 0.3: ESLint flat + Prettier + حماية `@a` | 0.3 ✅ | اختبار سلبي 5/5 انتهاكات اتصادوا؛ تصحيح تعارض `curly` مع eslint-config-prettier؛ lint وformat:check وtypecheck خضرا |

---

## ✅ Update Protocol (مرجع سريع)

```markdown
بداية الجلسة : اقرأ CURRENT FOCUS + AI CONTEXT + OPEN DECISIONS + BLOCKERS.
أثناء العمل  : المهمة 🔵 واحدة بس · فكرة جديدة → BACKLOG · تعارض → OPEN DECISIONS + اسأل.
نهاية الجلسة : حدّث الحالات (✅ بدليل فقط) · CURRENT FOCUS · AI CONTEXT · CHANGE LOG · Dashboard (recalc_dashboard.py --write) · BLOCKERS · SESSION LOG.
```