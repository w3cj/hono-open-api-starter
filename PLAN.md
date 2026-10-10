# 🗺️ PLAN — خطة العمل (Roadmap)

> **@file** : PLAN.md
> **@description** : Roadmap بيقسّم المشروع لمراحل ومهام ذرية بالترتيب والاعتماديات والبوابات. (الحالة في PROJECT_TRACKER.md مش هنا)
> **@updated** : `[ { "date": "2026-10-10", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف من الخطة الأصلية + قرارات UD-01…UD-17" } ]`
> **النطاق** : Bun + Hono API Starter — المراحل 0–7 فقط؛ الباقي في Backlog (PROJECT_TRACKER).

---

## 1. الرؤية والنطاق

**الرؤية:** Backend Starter عام (Bun + Hono + TypeScript + PostgreSQL + Drizzle + Better Auth) متعدد المستأجرين، آمن، قابل لإعادة الاستخدام في SaaS/CRM/ERP، من غير ربطه بدومين تجاري واحد. (المرجع الأصلي: `docs/PLAN__Bun-hono-api-starter.md`.)

**داخل النطاق (المراحل 0–7):** الأساس · قاعدة البيانات · المصادقة · الصلاحيات · تعدد المستأجرين · موديولات الـ API الأساسية · تأمين أساسي.

**خارج النطاق دلوقتي (بقرار UD-14):** Redis والـ Queue والبريد الفعلي والتخزين والإشعارات والـ Webhooks والفوترة والـ Feature Flags والـ Idempotency/Outbox والـ Observability المتقدمة وDocker الإنتاجي وCI/CD واختبارات الأداء ونموذج الـ Ledger. كلها في BACKLOG (`B-n`) وبتتفعّل بقرار المستخدم.

### مبادئ الخطة
```markdown
1. أمان وصحة بيانات قبل الأداء.   2. ابني اللي محتاجه لما تحتاجه.   3. مرحلة بتتقفل بـ Exit مُحقَّق فقط.
4. مهمة ذرية واحدة في المرة.      5. أي تعارض جوهري = سؤال للمستخدم.   6. لا ادعاء "جاهز للإنتاج" من غير دليل.
```

---

## 2. خريطة الاعتماديات

```
P0 Setup ──► P1 Foundation ──► P2 Database ──► P3 Auth ──► P4 Authorization ──► P5 Multi-Tenancy ──► P6 Core API ──► P7 Hardening
```
كل مرحلة تعتمد على اللي قبلها مباشرة. مفيش تنفيذ متوازي إلا في الوثائق.

---

## 3. المراحل (Phases)

> **IDs:** `Phase.Task` (مثال `3.5`). لكل مرحلة: **الهدف · Entry · المهام · Exit · المخاطر · الجهد (S ≤ 1 يوم · M 2–4 أيام · L 1–2 أسبوع · XL > 2 أسبوع)**.

---

### 🔹 Phase 0 — Repo Analysis & Setup  ·  `release/1.1` · `feature/1.1.1-project-setup` · **S–M**
**الهدف:** أرضية تشغيل نظيفة بتفرض القواعد آلياً من أول يوم، وتأكيد توافق Bun مع كل مكتبة قبل ما نعتمد عليها.
**Entry:** قرارات المستخدم UD-01…UD-17 متسجّلة (ARCHITECTURE §20).

| ID | المهمة | Deliverable |
|---|---|---|
| 0.1 | فحص الـ repo وتأكيد توافق Bun مع المكتبات المختارة | تقرير توافق (Hono/Zod/Drizzle/postgres/Better Auth/Pino/bcrypt) |
| 0.2 | تهيئة المشروع: package.json + tsconfig strict + bunfig + paths | هيكل `src/` + `@a` و`@/*` شغالين |
| 0.3 | ESLint flat config + Prettier + no-restricted-imports | `bun run lint` شغّال |
| 0.4 | أدوات الاختبار bun test + عتبات التغطية 80/95 | `bun run test` شغّال |
| 0.5 | Git: main/develop + قالب commit + أول فرع بـ Tree ID | فرع `feature/1.1.1-…` من `git branch -a` |
| 0.6 | ملفات التوثيق الخمسة في الجذر | الخمس ملفات + validate_docs بيعدّي |
| 0.7 | README + CHANGELOG + ملف الخطة الأصلية في docs/ | ملفات موجودة ومحدّثة |

**Exit:** `bun run typecheck` و`lint` و`test` بيعدّوا على الهيكل الفاضي · استيراد مباشر خارج `@a` بيفشّل lint · الوثائق في الجذر.
**المخاطر:** R2 (توافق Bun) · R9 (الواقع مختلف عن الافتراضات).

---

### 🔹 Phase 1 — Project Foundation  ·  `release/1.1` · `feature/1.1.2-foundation` · **M**
**الهدف:** سيرفر Hono بيشتغل بإعدادات مُتحقَّق منها، وأخطاء ورد موحّد، ولوجز، وإيقاف نضيف.
**Entry:** Phase 0 Exit متحقق.

| ID | المهمة | Deliverable |
|---|---|---|
| 1.1 | config/env.ts (Zod) + .env.example بأسماء القواعد | إقلاع بيفشل لو الإعداد غلط |
| 1.2 | core/errors: AppError + ERR constants + كتالوج رسائل ar/en | أكواد `AUTH_001` وما شابه |
| 1.3 | core/responses: Envelope موحّد + meta.requestId | SPEC-RESP متحقق |
| 1.4 | middleware: request-id + error-handler مركزي | لا stack trace للعميل |
| 1.5 | Logging: Pino + redaction + request-logger + حقل channel | لوجز JSON بدون أسرار |
| 1.6 | app.ts + server.ts + Graceful Shutdown | إيقاف نضيف على SIGTERM/SIGINT |
| 1.7 | Health: live و ready | `/health/live` و`/health/ready` |
| 1.8 | Security headers + CORS + حد حجم الـ body | إعدادات موثّقة ومختبرة |
| 1.9 | alias skeleton: src/alias (index/core/libs) | `@a` شغّال + قاعدة lint |
| 1.10 | اختبارات: env + errors + envelope + health | كلها خضرا |

**Exit:** السيرفر بيقوم على 2001 · env غلط يوقف الإقلاع · health بيرد · الأخطاء والرد بالشكل الموحّد · الاختبارات الأساسية بتعدّي.
**المخاطر:** R2 · R6 (Over-engineering).

---

### 🔹 Phase 2 — Database Foundation  ·  `release/1.2` · `feature/1.2.1-database` · **L**
**الهدف:** PostgreSQL + Drizzle + نظام ترحيلات منضبط + جداول CORE بقيودها، واختبارات على Postgres حقيقي.
**Entry:** Phase 1 Exit متحقق · CL-03 مراجَع.

| ID | المهمة | Deliverable |
|---|---|---|
| 2.1 | docker-compose.dev.yml (Postgres 16) + اتصال Drizzle | اتصال شغّال بحد pool |
| 2.2 | drizzle.config + سكريبت إعادة التسمية py/sy + ملفات .down.sql | SPEC-MIG متحقق |
| 2.3 | أدوات مشتركة: حقول التدقيق + public_id UUIDv7 + نوع timestamptz UTC | helpers في `database/schema` |
| 2.4 | Transaction helper (الكل أو لا شيء) + اختبار rollback | SPEC-TXN متحقق |
| 2.5 | py_0001_create_tenants | جدول tenants + slug فريد |
| 2.6 | py_0002_create_users + مواءمة جداول Better Auth | users بـ password_hash [VERIFY CL-01] |
| 2.7 | sy_0003_create_memberships | فريد (tenant_id,user_id) |
| 2.8 | sy_0004_create_sessions | sessions بـ active_tenant_id |
| 2.9 | py_0005_create_roles + sy_0006_create_permissions | RBAC tables |
| 2.10 | sy_0300_create_audit_logs (الأعمدة المدموجة) | append-oriented |
| 2.11 | seed: الأدوار والصلاحيات الافتراضية | sy_0900/0901 |
| 2.12 | اختبارات تكامل على Postgres حقيقي (قيود + ترحيلات + rollback) | كلها خضرا |

**Exit:** الترحيلات بتشتغل up وdown · القيود متحقق منها · اختبار rollback ناجح · لا float في أي حساب مالي.
**المخاطر:** R1 · R4 (سكريبت التسمية) · R3.

---

### 🔹 Phase 3 — Authentication  ·  `release/1.3` · `feature/1.3.1-authentication` · **L**
**الهدف:** مصادقة آمنة عبر Better Auth بجلسات كوكيز، وتشفير bcrypt عبر AuthService.
**Entry:** Phase 2 Exit متحقق · CL-01 وCL-02 محسومين.

| ID | المهمة | Deliverable |
|---|---|---|
| 3.1 | Better Auth + Drizzle adapter | الإعداد مربوط بالـ DB |
| 3.2 | AuthService: bcrypt cost 12 + توثيق التمليح + حد 72 بايت | SPEC-AUTH متحقق |
| 3.3 | تسجيل + دخول + خروج | endpoints شغالة |
| 3.4 | تأكيد الإيميل + إعادة تعيين الباسورد خلف EmailPort + Console adapter | بدون مزود بريد حقيقي |
| 3.5 | إدارة الجلسات + إلغاؤها + كوكيز آمنة + trusted origins | HttpOnly/Secure/SameSite |
| 3.6 | middleware المصادقة + rate limit المدمج لمسارات Auth | مسارات محمية |
| 3.7 | اختبارات Auth | كلها خضرا |

**Exit:** تسجيل/دخول/خروج شغالين · بيانات غلط مرفوضة · الجلسات بتتلغي · مسارات محمية.
**المخاطر:** R1 · R8.

---

### 🔹 Phase 4 — Authorization  ·  `release/1.4` · `feature/1.4.1-authorization` · **M**
**الهدف:** RBAC + صلاحيات resource:action بمنع افتراضي ومنع تصعيد الصلاحيات.
**Entry:** Phase 3 Exit متحقق.

| ID | المهمة | Deliverable |
|---|---|---|
| 4.1 | تعريف الصلاحيات (resource:action بالجمع) والأدوار الخمسة | كتالوج مركزي |
| 4.2 | Permission evaluator (deny by default) | SPEC-AUTHZ متحقق |
| 4.3 | authorization middleware | حماية على مستوى المسار |
| 4.4 | منع التصعيد + حماية آخر Owner + نقل الملكية | قواعد مفروضة في الخدمة |
| 4.5 | تسجيل التغييرات الحساسة في audit_logs | listener على الأحداث |
| 4.6 | اختبارات الصلاحيات (≥ 95%) | كلها خضرا |

**Exit:** طلبات غير مصرّح بيها مرفوضة · الأدوار مفروضة · محاولات التصعيد بتفشل · تغطية منطق الصلاحيات ≥ 95%.
**المخاطر:** R7.

---

### 🔹 Phase 5 — Multi-Tenancy  ·  `release/1.4` · `feature/1.4.2-multi-tenancy` · **L**
**الهدف:** عزل مستأجرين بطبقة تطبيق إلزامية، وإدارة أعضاء ودعوات.
**Entry:** Phase 4 Exit متحقق.

| ID | المهمة | Deliverable |
|---|---|---|
| 5.1 | tenant-context middleware (X-Tenant-Id + active_tenant_id) | SPEC-TENANT متحقق |
| 5.2 | Data Access Layer بيحقن tenant_id تلقائياً | لا استعلام بدون فلتر |
| 5.3 | إنشاء tenant + membership + owner في معاملة واحدة | الكل أو لا شيء |
| 5.4 | دعوات الأعضاء: إنشاء/قبول/انتهاء/إلغاء | tokens بمدة صلاحية |
| 5.5 | إدارة الأعضاء: تغيير الدور والإزالة | بحماية آخر Owner |
| 5.6 | اختبارات عزل المستأجرين cross-tenant | كلها خضرا |
| 5.7 | تقييم RLS مع Neon pooling وتوثيق القرار | ADR بنتيجة التقييم |

**Exit:** حدود المستأجرين مفروضة · أي وصول cross-tenant بيفشل · العضوية متحقق منها.
**المخاطر:** R3 · R7.

---

### 🔹 Phase 6 — Core API Modules  ·  `release/1.5` · `feature/1.5.1-core-modules` · **L–XL**
**الهدف:** موديولات الـ API الأساسية بتحقق ومصادقة وصلاحيات وتوثيق OpenAPI.
**Entry:** Phase 5 Exit متحقق.

| ID | المهمة | Deliverable |
|---|---|---|
| 6.1 | Pagination/filter/sort helpers (cursor) | SPEC-PAGE متحقق |
| 6.2 | users: me + تعديل البروفايل + تغيير الباسورد + قائمة الجلسات وإلغاؤها | SPEC-USERS متحقق |
| 6.3 | tenants: تفاصيل + تعديل + إعدادات | CRUD بصلاحيات |
| 6.4 | roles + permissions endpoints | قراءة وإدارة |
| 6.5 | settings (tenant_id,key فريد) | SPEC-SETTINGS متحقق |
| 6.6 | audit-logs: قراءة + فلترة + Pagination | SPEC-AUDIT متحقق |
| 6.7 | api-keys: hash فقط + scopes + انتهاء + إلغاء | SPEC-APIKEY متحقق |
| 6.8 | OpenAPI + Scalar (`/openapi.json` و`/docs`) | SPEC-OPENAPI متحقق |
| 6.9 | اختبارات API شاملة | كلها خضرا |

**Exit:** CRUD شغّال · التحقق مفروض · الصلاحيات مفروضة · `/openapi.json` و`/docs` مطابقين للتنفيذ.
**المخاطر:** R6 · R7.

---

### 🔹 Phase 7 — Basic Hardening & Release  ·  `release/1.6` · `chore/1.6.1-hardening` · **M**
**الهدف:** تأمين أساسي واختبارات أمنية وإغلاق أول إصدار.
**Entry:** Phase 6 Exit متحقق.

| ID | المهمة | Deliverable |
|---|---|---|
| 7.1 | مراجعة security headers وCORS وحدود الطلبات | تقرير مراجعة |
| 7.2 | اختبارات أمنية: SQLi وcross-tenant وتصعيد صلاحيات وmalformed وoversized | tests/security |
| 7.3 | فحص الاعتماديات (bun audit) وفحص الأسرار | سكريبت في scripts/security |
| 7.4 | توثيق الأمان والمخاطر المتبقية | docs/security |
| 7.5 | مراجعة نهائية وCHANGELOG وTag الإصدار | v1.6.0 |

**Exit:** اختبارات الأمان الحرجة بتعدّي · لا ثغرات حرجة في الاعتماديات · الإعدادات الأمنية موثّقة · tag للإصدار.
**المخاطر:** R5 · R8.

---

## 4. خطة الفروع والإصدارات (Git Tree Numbering)

```
main
 └── develop (1)
      ├── release/1.1  → P0 + P1   (Tag: v1.1.0)
      ├── release/1.2  → P2        (Tag: v1.2.0)
      ├── release/1.3  → P3        (Tag: v1.3.0)
      ├── release/1.4  → P4 + P5   (Tag: v1.4.0)
      ├── release/1.5  → P6        (Tag: v1.5.0)
      └── release/1.6  → P7        (Tag: v1.6.0)
```
- الـ Tree IDs **إرشادية**: قبل أي فرع افحص `git branch -a` وخد الرقم التالي الفعلي. الأرقام المحجوزة متتعادش.
- فروع Dependabot (لو اتفعّل) خارج قاعدة الترقيم لأنها بتتولّد تلقائياً.
- Hotfix من `main` يبدأ بـ `0.x`. لا Force Push على `main/develop/release/*` بدون تأكيد.

---

## 5. Quality Gates (بوابات الجودة)

| البوابة | متى | الشرط |
|---|---|---|
| **G0 — Task** | آخر كل مهمة | typecheck + lint + tests للمهمة |
| **G1 — Module** | آخر كل موديول | DoD (SPECKIT Part 10) كامل |
| **G2 — Phase** | آخر كل مرحلة | كل المهام ✅ + Exit Criteria + لا Blockers |
| **G3 — Release** | قبل Tag | build + coverage (80% عام / 95% صلاحيات) + CHANGELOG + مراجعة وثائق |
| **G4 — Pre-merge** | قبل أي Merge | Checklist AI_INSTRUCTIONS §14 |

---

## 6. نقاط القرار (Decision Checkpoints)

| الـ ID | القرار | لازم يتحسم قبل | المسؤول | الحالة |
|---|---|---|---|---|
| CL-04 | توافق Bun مع المكتبات | Phase 1 | AI (فحص) ثم المستخدم | مفتوح |
| CL-03 | جدوى سكريبت تسمية الترحيلات و`.down.sql` | 2.2 | AI (فحص) ثم المستخدم | مفتوح |
| CL-01 | Better Auth مع مفاتيح SERIAL | 2.6 و3.1 | AI (فحص) ثم المستخدم | مفتوح |
| CL-02 | Better Auth مع bcrypt مخصص | 3.2 | AI (فحص) ثم المستخدم | مفتوح |
| CL-05 | BullMQ ولا RabbitMQ | وقت تفعيل الـ Queue (B-2) | المستخدم | مؤجّل |

---

## 7. سجل المخاطر (Risk Register)

| # | الخطر | الاحتمال | الأثر | التخفيف | المالك |
|---|---|---|---|---|---|
| R1 | Better Auth مش بيدعم SERIAL أو bcrypt مخصص بالشكل المتوقع | متوسط | عالي | فحص في Phase 0/2 + بدائل موثّقة قبل القرار | AI |
| R2 | مكتبة مش متوافقة مع Bun (postgres/bcrypt/pino) | متوسط | عالي | تقرير 0.1 + اختبار تكامل قبل الاعتماد | AI |
| R3 | سلوك Neon pooling مع المعاملات وRLS | متوسط | عالي | تقييم 5.7 قبل أي ادعاء عزل بـ RLS | AI |
| R4 | سكريبت تسمية الترحيلات هش مع تحديثات drizzle-kit | متوسط | متوسط | عزله في `scripts/db` + اختبار + ADR | AI |
| R5 | تضارب مصادر الوثائق يسبب إعادة عمل | عالي | متوسط | الأسبقية (AI_INSTRUCTIONS §8) + سؤال مبكر | AI |
| R6 | Over-engineering مبكر | متوسط | متوسط | قاعدة Backlog + نطاق ADR-014 | AI |
| R7 | ثغرة في Data Access Layer تسرّب بيانات مستأجر | منخفض | حرج | اختبارات 5.6 إلزامية + مراجعة كل استعلام | AI |
| R8 | rate limit بالذاكرة مش بيصلح لأكتر من instance | عالي | متوسط | موثّق كقيد لحد B-1 | AI |
| R9 | الـ repo الفعلي مختلف عن الافتراضات | عالي | متوسط | Inspect First + `[VERIFY]` | AI |

---

## 8. تقدير الجهد وقياس التقدّم

| Phase | الجهد | ملاحظات |
|---|---|---|
| 0 | S–M | Repo Analysis & Setup |
| 1 | M | Project Foundation |
| 2 | L | Database Foundation |
| 3 | L | Authentication |
| 4 | M | Authorization |
| 5 | L | Multi-Tenancy |
| 6 | L–XL | Core API Modules |
| 7 | M | Basic Hardening & Release |

التقدّم بيتقاس في `PROJECT_TRACKER.md › Progress Dashboard` (✅ فقط بيتحسب).

---

## 9. Backlog / أفكار مؤجلة (متتنفّذش دلوقتي)

القائمة الكاملة والـ IDs (`B-1…B-18`) في `PROJECT_TRACKER.md › BACKLOG`. أي بند بيدخل الخطة بقرار المستخدم وبمرحلة جديدة (E6).

---

## 10. إدارة التغيير في الخطة

```markdown
1. تغيير ترتيب/نطاق المراحل = بموافقة المستخدم فقط، ويتسجّل في ARCHITECTURE › ADR + TRACKER › CHANGE LOG.
2. مهمة جديدة في مرحلة قديمة بتاخد الرقم التالي (مش بتتحشر في النص). IDs متتعادش.
3. مهمة > 8 دقايق بتتقسم في TRACKER › DETAILED TASKS LOG مش هنا.
4. حالة التنفيذ ممنوعة في الملف ده.
```