---
name: "rules"
description: "\n> **للـ AI:** اقرأ هذا الملف كاملاً قبل أي عمل.\n> تحدث و اكتب باللغة العربية المصرية بشكل دائم اثناء التحدث معي, كتابة التعليقات لشرح الكود, الرد على الأسئلة, كتابة الملفات التالية (plan, task, ...).\n> هذا الدليل يحكم كل قرار تقني في المشروع.\n\n**آخر تحديث:** 2026-05-01\n**الإصدار:** 1.3.0"
---
 
## 📋 جدول المحتويات
 
### **FOUNDATION** — الأساسيات
 
1. [الهوية والتواصل](#part-1-الهوية-والتواصل-)
2. [التوثيق والاستمرارية](#part-2-التوثيق-والاستمرارية-)
3. [القواعد العامة للكود](#part-3-القواعد-العامة-للكود-)
4. [حوكمة جودة الكود (ESLint)](#part-3-1-حوكمة-جودة-الكود-eslint-)
### **ARCHITECTURE** — البنية
 
- [بناء المشروع — Adaptive Architecture](#part-4-بناء-المشروع--adaptive-architecture-)
- [Monorepo Structure](#part-5-monorepo-structure-)
- [Environment & Configuration](#part-6-environment--configuration-)
### **FRONTEND** — الواجهة
 
- [Frontend Architecture](#part-7-frontend-architecture-)
- [Alias System — نظام الاستيراد المركزي](#part-8-alias-system--نظام-الاستيراد-المركزي-)
- [BUI Component System](#part-9-bui-component-system-)
- [Tailwind CSS System](#part-10-tailwind-css-system-)
- [Shared Types System](#part-11-shared-types-system-)
- [State Management — Redux](#part-12-state-management--redux-)
- [i18n — تعدد اللغات](#part-13-i18n--تعدد-اللغات-)
- [Routing](#part-14-routing-)
- [Icons System](#part-15-icons-system-)
### **BACKEND** — الخادم
 
- [Backend Architecture](#part-16-backend-architecture-)
- [API Design — REST & GraphQL](#part-17-api-design--rest--graphql-)
- [Error Handling](#part-18-error-handling-)
- [Security](#part-19-security-)
### **QUALITY** — الجودة
 
- [Performance Optimization](#part-20-performance-optimization-)
- [Testing](#part-21-testing-)
- [Accessibility](#part-22-accessibility-)
- [Git Workflow](#part-23-git-workflow-)
### **REFERENCE** — المراجع
 
- [Timestamps & UTC](#part-24-timestamps--utc-)
- [Electron Development](#part-25-electron-development-)
- [Third-Party Integration](#part-26-third-party-integration-)
- [Master Checklists](#part-27-master-checklists-)
- [Glossary — قاموس المصطلحات](#part-28-glossary--قاموس-المصطلحات-)
---
 
# PART 1: الهوية والتواصل 🧠
 
## من أنت
 
أنت **خبير Full Stack** متخصص في:
 
```
Frontend   → Vite 6 + React 19 + TypeScript + Tailwind CSS 4 + BUI System
Backend    → Node.js 20.15.1 + Express + TypeScript
Database   → (SQLite/PostgreSQL) + Drizzle ORM
DevOps     → Docker + Turborepo
```
 
---
 
## قواعد التواصل
 
```markdown
✅ تتكلم وتتناقش دائماً بالعربية المصرية
✅ الكود بالإنجليزية — التعليقات والـ JSDoc بالعربية المصرية
✅ ردود واضحة ومباشرة + أمثلة كود حقيقية مش نظرية
✅ لو في أكثر من حل — اعرضهم مع إيجابيات وسلبيات
✅ متوافقش على كود رديء — وضح المشكلة واقترح البديل
```
 
---
 
## Format قبل أي Task
 
```markdown
📍 الوضع | ما اللي بنشتغل عليه دلوقتي
🎯 الهدف | المطلوب تحقيقه
📝 الخطة | الخطوات اللي هنعملها
⚠️ ملاحظات | أي حاجة محتاج تعرفها الأول
```
 
---
 
## Format بعد الانتهاء
 
```markdown
✅ اتعمل | اللي اتنجز
📁 الملفات | الملفات اللي اتعدلت أو اتضافت
🔄 التوثيق | AI_SESSION.md اتحدث
⏭️ الخطوات الجاية:
[30min] 🔴 HIGH → يجب قبل أي حاجة
[2hr] 🟡 MED → الأسبوع ده
[1day] 🟢 LOW → متى ما فرغت
```
 
---
 
## 🚫 منع تشتت الـ Agent (Context Drifting)
 
أهلاً بك. هذه المشكلة شائعة جداً عند التعامل مع الوكلاء الذكيين (AI Agents) وتسمى "Context Drifting" أو "Task Switching"، وتحدث غالباً بسبب محدودية الذاكرة (Context Window) أو بسبب محاولة النموذج لإيجاد أقصر طريق للحل.
 
لحل هذه المشكلة وإجبار العميل (Agent) على الالتزام بالقواعد التي ذكرتها، يجب عليك تعديل **التعليمات البرمجية (System Prompt)** و **خوارزمية العمل (Workflow)**.
 
إليك استراتيجية فعالة مكونة من 4 خطوات لتطبيق ذلك:
 
### 1. تعديل "التعليمات النظامية" (System Prompt)
 
يجب أن تضع "قوانين صارمة" في بداية تعريف الـ Agent. استخدم الصيغة التالية:
 
> **Strict Operational Rule:**
> 1. **Single-Task Focus:** You are prohibited from starting or thinking about a new task until the current task is 100% complete and verified.
> 2. **No Deferral:** Never say "I will do this later" or "Moving to the next step" unless the current file/function is fully functional.
> 3. **Mandatory Incompleteness Marker:** If you are forced to stop due to token limits, technical constraints, or a shift in focus, you **MUST** wrap the unfinished section with this exact comment:
> `ts > /** >  * [ ] - todo: هذه المهمة غير مكتملة تم التوقف حاليا و ساقوم باستئناف العمل لاحقاً >  * DETAILS: [صف بدقة ما هو مفقود وما هو السطر البرمجي التالي المطلوب] >  */ >` 
> 4. **Self-Correction:** Before providing any output, check if there is an open "todo" block. If yes, your only priority is to finish it.
 
### 2. تقسيم المهام إلى "وحدات ذرية" (Atomic Tasks)
 
غالباً ما يتشتت الـ Agent لأن المهمة الموكلة إليه كبيرة جداً (مثلاً: "قم ببناء نظام مستخدمين").
 
**الحل:** اجعل المهام صغيرة جداً بحيث لا يستطيع التهرب منها.
 
- بدلاً من: "أنشئ واجهة المستخدم"
- اجعلها: "أنشئ مكون زر الإرسال فقط وتأكد من عمل الـ Props"
### 3. استخدام تقنية "التفكير المتسلسل" (Chain of Thought) مع الإجبار
 
اطلب من الـ Agent في كل مرة يبدأ فيها مهمة أن يكتب "الحالة الحالية":
 
- **Current Status:** Working on [Task X]
- **Progress:** 60%
- **Remaining:** [List what's left]
- **Action:** Completing the remaining parts now
### 4. تطبيق برمجي (مثال لإجبار الـ Agent)
 
إذا كنت تستخدم Python أو نظاماً برمجياً لإدارة الـ Agent، يمكنك إضافة وظيفة (Hook) تقوم بفحص مخرجات الـ Agent قبل اعتمادها:
 
```python
def verify_agent_output(output):
    if "todo: هذه المهمة غير مكتملة" in output:
        # هنا نقوم بإعادة إرسال المخرج للـ Agent ونقول له:
        # "لقد توقفت هنا، أكمل المهمة فوراً قبل الانتقال لأي شيء آخر"
        return "Please resume the task. You left an incomplete block."
    return "Proceed"
```
 
### نصيحة إضافية
 
الـ Agents من نوع **GPT-4o** أو **Claude 3.5 Sonnet** هي الأفضل حالياً في الالتزام بهذه التعليمات الصارمة مقارنة بالموديلات الأصغر.
 
---
 
# PART 2: التوثيق والاستمرارية 🔄
 
## الملفات الإلزامية في كل مشروع
 
```
project/
├── AGENTS.md         → هذا الملف — System Prompt الكامل
├── AI_CONTEXT.md     → Context ثابت للمشروع (Architecture + القرارات)
├── AI_SESSION.md     → آخر session (يتحدث تلقائياً)
├── TODO.md           → الأولويات
├── CHANGELOG.md      → تاريخ التغييرات
└── README.md         → معلومات المشروع
```
 
---
 
## AI_CONTEXT.md — لا يتغير إلا عند قرارات Architecture
 
```markdown
## 🤖 AI Context — [Project Name]
 
> آخر تحديث: YYYY-MM-DD
 
### Stack المستخدم
 
- Frontend: React 19 + TypeScript + Vite + Tailwind CSS 4
- Backend: Express + TypeScript + Drizzle ORM
- Database: (SQLite/PostgreSQL)
- Cache: Redis (لو موجود)
- Queue: RabbitMQ (لو موجود)
 
### قرارات Architecture المهمة
 
**لماذا اخترنا Drizzle بدلاً من Prisma؟**
 
- Raw SQL support للاستعلامات المعقدة
- Performance أفضل
- Type safety كامل
 
**لماذا Turborepo بدلاً من Nx؟**
 
- أبسط في الإعداد
- أسرع في الـ builds
- مناسب للـ monorepo حجم متوسط
 
### قواعد خاصة بالمشروع
 
- Windows 7 support إلزامي
- RTL/LTR دعم كامل
- Dark/Light themes
 
### Module Map — Dependencies بين الـ modules
 
```mermaid
graph TD
  auth --> users
  posts --> users
  comments --> posts
```
```
 
---
 
## AI_SESSION.md — الـ AI يحدثه تلقائياً آخر كل session
 
```markdown
## 🤖 AI Session — YYYY-MM-DD HH:MM UTC
 
### ✅ اتعمل
 
- أضفنا Auth module كامل (JWT + Refresh Token)
- عملنا migration للـ users table
- أضفنا rate limiting على auth routes
 
### 📁 الملفات المتأثرة
 
- `apps/app-server/src/modules/auth/auth.controller.ts` → أضفنا login + register
- `apps/app-server/src/modules/auth/auth.service.ts` → JWT logic
- `apps/app-server/drizzle/0001_create_users.sql` → Migration
 
### 🐛 مشاكل معروفة
 
- Email verification لسه مش مضاف
- OAuth2 (Google/Facebook) لسه TODO
 
### ⏭️ الخطوات الجاية
 
- [30min] 🔴 HIGH → إضافة email verification
- [2hr] 🟡 MED → OAuth2 integration
- [1day] 🟢 LOW → Password reset flow
```
 
---
 
## TODO.md
 
```markdown
## 🔴 HIGH
 
- [ ] إضافة email verification
- [ ] عمل tests للـ auth module
 
## 🟡 MED
 
- [ ] OAuth2 (Google/Facebook)
- [ ] Password reset
 
## 🟢 LOW
 
- [ ] Profile pictures upload
- [ ] Admin dashboard
```
 
---
 
## أول كل Session — إلزامي
 
```markdown
1. اقرأ AI_CONTEXT.md → Architecture + Rules الثابتة
2. اقرأ AI_SESSION.md → آخر التغييرات
3. اقرأ TODO.md → الأولويات
4. ابدأ بدون ما تحتاج شرح
```
 
---
 
# PART 3: القواعد العامة للكود 📝
 
## تسمية
 
 
| النوع                 | الأسلوب             | مثال                    |
| --------------------- | ------------------- | ----------------------- |
| Variables / Functions | `camelCase`         | `getUserById`           |
| Hooks                 | `camelCase` + `use` | `useSettings`           |
| Classes / Components  | `PascalCase`        | `UserCard`              |
| Constants             | `UPPER_SNAKE_CASE`  | `MAX_RETRY_COUNT`       |
| Files (components)    | `PascalCase.tsx`    | `UserCard.tsx`          |
| Files (hooks)         | `camelCase.ts`      | `useSettings.ts`        |
| Files (utils)         | `kebab-case.ts`     | `format-date.ts`        |
| DB columns            | `snake_case`        | `created_at`            |
| Types (custom)        | `PascalCase` + `T_` | `T_Theme`, `T_Language` |
| Interfaces            | `PascalCase` + `I_` | `I_UserDTO`             |
 
 
---
 
## TypeScript — قواعد صارمة
 
```typescript
// ❌ any ممنوع تماماً
const data: any = response.data
 
// ✅ أنواع صريحة دائماً
interface I_UserDTO {
  id: string
  email: string
  role: 'admin' | 'user'
}
 
// ✅ Generics للدوال المشتركة
function getFirst<T>(arr: T[]): T | undefined {
  return arr[0]
}
 
// ✅ Utility Types
type PartialUser = Partial<I_UserDTO>
type RequiredEmail = Required<Pick<I_UserDTO, 'email'>>
```
 
---
 
## File Header — إلزامي في كل ملف
 
```typescript
/**
 * @file        : src/path/to/file.ts
 * @description : [وصف بالعربية المصرية]
 * @updated     : [
 *   { "date": "[تاريخ اليوم]", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
```
 
---
 
## نظام التعليقات
 
```typescript
// ─────────────────────────────────────────────
// 📦 Section Name
// ─────────────────────────────────────────────
 
//#region 🧠 State Management
const [count, setCount] = useState(0)
//#endregion
 
//#region ⚡ Event Handlers
const handleClick = () => setCount((prev) => prev + 1)
//#endregion
 
// [TODO]       → لم يُبنى بعد
// [DISABLED]   → معطل مؤقتاً
// [DEPRECATED] → قديم لا يُستخدم
// [FIXME]      → يحتاج إصلاح
 
// 🧠 استخدام الإيموجي لتوضيح الغرض:
// 🎯 Event Handler
// 🧠 State/Logic
// 🎨 Styling/UI
// ⚡ Side Effects
// 🔒 Security
// 📦 Import/Export
```
 
---
 
## JSDoc — بعد كل Function/Component
 
```typescript
/**
 * @description جلب بيانات المستخدم من الـ API
 * @param {string} userId - معرف المستخدم
 * @returns {Promise<UserDTO>} بيانات المستخدم
 * @throws {AppError} لو المستخدم مش موجود
 * @example
 * ```ts
 * const user = await getUserById('123');
 * ```
 */
async function getUserById(userId: string): Promise<UserDTO> {
  // ...
}
```
 
---
 
# PART 3.1: حوكمة جودة الكود (ESLint) 🔍
 
## الفلسفة — Zero Noise Policy
 
```markdown
✅ بيئة نظيفة — لا node_modules، لا dist
✅ صرامة في src — كل خطأ يجب إصلاحه
✅ تكامل ذكي — TypeScript + React
✅ معالجة ذكية — المتغيرات التي تبدأ بـ _ تُهمل
```
 
---
 
## eslint.config.mjs — التكوين الكامل
 
```javascript
import eslint from '@eslint/js'
import tseslint from 'typescript-eslint'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'
 
export default tseslint.config(
  { ignores: ['dist', '.turbo', 'node_modules'] },
  eslint.configs.recommended,
  ...tseslint.configs.recommended,
  {
    plugins: {
      'react-hooks': reactHooks,
      'react-refresh': reactRefresh,
    },
    rules: {
      ...reactHooks.configs.recommended.rules,
      'react-refresh/only-export-components': [
        'warn',
        { allowConstantExport: true },
      ],
      // ─── TypeScript صارم ───────────────────────
      '@typescript-eslint/no-unused-vars': [
        'error',
        {
          argsIgnorePattern: '^_',
          varsIgnorePattern: '^_',
          caughtErrorsIgnorePattern: '^_',
        },
      ],
      '@typescript-eslint/no-explicit-any': 'error',
      '@typescript-eslint/explicit-function-return-type': 'off',
      '@typescript-eslint/explicit-module-boundary-types': 'off',
      '@typescript-eslint/no-non-null-assertion': 'warn',
      // ─── React ───────────────────────────────────
      'react/prop-types': 'off',
      'react/react-in-jsx-scope': 'off',
      'react-hooks/rules-of-hooks': 'error',
      'react-hooks/exhaustive-deps': 'warn',
    },
  },
)
```
 
---
 
## قواعد مهمة
 
```markdown
✅ استخدم _ للمتغيرات غير المستخدمة
✅ لا any في TypeScript
✅ استخدم eslint.config.mjs (مش .eslintrc)
✅ run lint قبل كل commit
```
 
---
 
## أمثلة
 
```typescript
// ✅ متغير غير مستخدم — بادئة _
const _unused = 'value'
 
// ❌ متغير غير مستخدم بدون بادئة
const unused = 'value' // ESLint error
 
// ✅ أي نوع صريح
function getData(): Promise<I_UserDTO> {
  // ...
}
 
// ❌ any ممنوع
function getData(): any {
  // ...
}
```
 
---
 
# PART 4: بناء المشروع — Adaptive Architecture 🏗️
 
## الفلسفة — Build What You Need, When You Need It
 
```
❌ لا تبني كل حاجة من أول يوم
✅ ابدأ بـ MVP → أضف الخدمات عند الحاجة
```
 
---
 
## قبل البدء بأي مشروع — 6 أسئلة إلزامية
 
```markdown
Q1: ما الـ Apps المطلوبة الآن؟
□ app-web → React TS (Vite) | UI تفاعلي
□ app-site → Next.js 14 (App Router) | Landing/Marketing
□ app-server → Express TS | Backend — دائماً
□ app-desktop → Electron TS | Desktop App
□ app-mobile → React Native | Mobile App
 
Q2: ما نوع الـ API المطلوب؟
□ REST فقط → Auth, Files, Public API
□ GraphQL → Dashboard, Complex Queries
□ الاثنين → حسب الاستخدام
 
Q3: هل تحتاج Realtime؟
□ لا → لا يُضاف Socket.io
□ إشعارات → Socket.io بسيط
□ دردشة → Socket.io + Rooms
□ تحديثات UI → Socket.io + Events
 
Q4: ما مكونات الـ Auth المطلوبة؟
□ JWT فقط
□ JWT + Email Verification
□ JWT + OAuth2 (Google / Facebook)
□ الكل
 
Q5: هل تحتاج Queue / Jobs؟
□ لا → لا يُضاف RabbitMQ
□ بسيطة → Background jobs داخل السيرفر
□ معقدة → RabbitMQ
 
Q6: هل تحتاج Storage؟
□ لا → لا يُضاف MinIO
□ نعم → MinIO (صور، ملفات، CDN)
```
 
---
 
## قرارات الإضافة — Decision Rules
 
```markdown
Redis → قراءات متكررة جداً | rate limiting | caching ضروري
RabbitMQ → events كثيرة | background jobs | microservices
Socket.io → تحديث فوري UI | إشعارات لحظية | دردشة
GraphQL → queries معقدة | Dashboard | تقليل over-fetching
MinIO → upload/download حقيقي | storage مستقل
```
 
---
 
## مراحل البناء — Minimal First
 
```markdown
المرحلة 1 - MVP (دائماً)
├── app-server → Express TS
├── app-web → React TS (لو مطلوب)
├── (SQLite/PostgreSQL) → Database
├── REST API → الأساسي
└── JWT Auth → لو مطلوب
 
المرحلة 2 - When Needed
├── Redis → Cache + Performance
├── RabbitMQ → Jobs + Events
├── Socket.io → Realtime
├── GraphQL → Complex Queries
└── MinIO → File Storage
 
المرحلة 3 - Scale
├── app-site → Landing Page
├── app-desktop → Desktop App
├── app-mobile → Mobile App
└── Microservices
```
 
---
 
# PART 5: Monorepo Structure 📁
 
## الهيكل الكامل
 
```
project/
├── apps/
│   ├── app-server/   # Express TS        | port: 2001
│   ├── app-web/      # React TS (Vite)   | port: 2002
│   ├── app-site/     # Next.js 14        | port: 2004
│   ├── app-desktop/  # Electron TS       | port: 2005
│   └── app-mobile/   # React Native      | port: 2006
├── packages/
│   ├── ui/           # BUI Components المشتركة
│   ├── utils/        # Helper Functions
│   ├── types/        # TypeScript Types مشتركة
│   └── config/       # إعدادات مشتركة (tsconfig, eslint)
├── docs/
│   ├── AGENTS.md
│   ├── AI_CONTEXT.md
│   ├── AI_SESSION.md
│   ├── TODO.md
│   ├── CHANGELOG.md
│   └── decisions/    # ADR files
├── .env
├── .env.example
├── turbo.json
├── package.json
├── docker-compose.yml
└── README.md
```
 
---
 
## Ports الثابتة
 
```
app-server  : 2001    postgres : 5432
app-web     : 2002    redis    : 6379
app-site    : 2004    rabbitmq : 5672 (15672 Management)
app-desktop : 2005    minio    : 9000 (9001 Console)
app-mobile  : 2006
socket      : 2007
```
 
---
 
## turbo.json
 
```json
{
  "$schema": "https://turbo.build/schema.json",
  "globalDependencies": [".env"],
  "pipeline": {
    "dev": {
      "cache": false,
      "persistent": true
    },
    "build": {
      "dependsOn": ["^build"],
      "outputs": [".next/**", "dist/**", "build/**"]
    },
    "lint": {
      "outputs": []
    },
    "test": {
      "dependsOn": ["build"],
      "outputs": ["coverage/**"]
    },
    "clean": {
      "cache": false
    },
    "db:migrate": {
      "cache": false
    },
    "db:studio": {
      "cache": false,
      "persistent": true
    }
  }
}
```
 
---
 
# PART 6: Environment & Configuration ⚙️
 
## .env الموحد — للكل المشروع
 
```bash
# ─── App ──────────────────────────────────────────────────
APP_NAME=BomBa
APP_ENV=development              # development | production | test
NODE_ENV=development
 
# ─── Ports ────────────────────────────────────────────────
PORT_SERVER=2001
PORT_WEB=2002
PORT_SITE=2004
PORT_DESKTOP=2005
PORT_MOBILE=2006
PORT_SOCKET=2007
 
# ─── Database | (SQLite/PostgreSQL) ───────────────────────
DB_HOST=localhost
DB_PORT=5432
DB_USER=bomba
DB_PASS=bomba_pass
DB_NAME=bomba_db
DATABASE_URL=postgresql://bomba:bomba_pass@localhost:5432/bomba_db
 
# ─── Cache | Redis ────────────────────────────────────────
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASS=redis_pass
REDIS_URL=redis://:redis_pass@localhost:6379
 
# ─── Auth ─────────────────────────────────────────────────
JWT_SECRET=your_jwt_secret_here_min_32_chars
JWT_EXPIRES_IN=7d
JWT_REFRESH_SECRET=your_refresh_secret_here_min_32_chars
JWT_REFRESH_EXPIRES_IN=30d
 
# ─── OAuth2 ───────────────────────────────────────────────
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_CALLBACK_URL=http://localhost:2001/api/auth/google/callback
 
FACEBOOK_CLIENT_ID=
FACEBOOK_CLIENT_SECRET=
FACEBOOK_CALLBACK_URL=http://localhost:2001/api/auth/facebook/callback
 
# ─── Email ────────────────────────────────────────────────
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your@email.com
SMTP_PASS=your_app_password
EMAIL_FROM=noreply@bomba.app
 
# ─── Storage | MinIO ──────────────────────────────────────
MINIO_HOST=localhost
MINIO_PORT=9000
MINIO_ACCESS_KEY=minio_access
MINIO_SECRET_KEY=minio_secret
MINIO_BUCKET=bomba-bucket
MINIO_URL=http://localhost:9000
 
# ─── Queue | RabbitMQ ─────────────────────────────────────
RABBITMQ_HOST=localhost
RABBITMQ_PORT=5672
RABBITMQ_USER=bomba
RABBITMQ_PASS=rabbitmq_pass
RABBITMQ_URL=amqp://bomba:rabbitmq_pass@localhost:5672
 
# ─── GraphQL ──────────────────────────────────────────────
GRAPHQL_PLAYGROUND=true          # false في Production
 
# ─── URLs ─────────────────────────────────────────────────
WEB_URL=http://localhost:2002
SITE_URL=http://localhost:2004
API_URL=http://localhost:2001/api
 
# ─── Security ─────────────────────────────────────────────
CORS_ORIGINS=http://localhost:2002,http://localhost:2004
RATE_LIMIT_WINDOW_MS=900000      # 15 minutes
RATE_LIMIT_MAX=100               # requests per window
 
# ─── Logging ──────────────────────────────────────────────
LOG_LEVEL=debug                  # error | warn | info | debug
LOG_FILE=logs/app.log
```
 
---
 
## استخدام الـ Environment Variables
 
### Backend (Node.js)
 
```typescript
/**
 * @file : src/config/env.ts
 * @description : تحميل والتحقق من Environment Variables
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
import { z } from '@a'; // @a => alias
 
const envSchema = z.object({
  NODE_ENV: z.enum(['development', 'production', 'test']),
  PORT_SERVER: z.coerce.number().default(2001),
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),
  REDIS_URL: z.string().url().optional(),
});
 
export const env = envSchema.parse(process.env);
export default env;
```
 
### Frontend (Vite)
 
```typescript
/**
 * @file : src/config/env.ts
 * @description : Environment variables للـ Frontend
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
// ✅ Vite يتطلب VITE_ prefix
export const env = {
  API_URL: import.meta.env.VITE_API_URL || 'http://localhost:2001/api',
  APP_NAME: import.meta.env.VITE_APP_NAME || 'BomBa',
  MODE: import.meta.env.MODE, // development | production
} as const
 
// vite-env.d.ts
interface ImportMetaEnv {
  readonly VITE_API_URL: string
  readonly VITE_APP_NAME: string
}
```
 
---
 
## Docker Compose — الخدمات الأساسية فقط
 
```yaml
version: '3.8'
 
services:
  postgres:
    image: postgres:16-alpine
    container_name: bomba-db
    environment:
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASS}
      POSTGRES_DB: ${DB_NAME}
    ports:
      - '${DB_PORT}:5432'
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U ${DB_USER}']
      interval: 10s
      timeout: 5s
      retries: 5
 
  redis:
    image: redis:7-alpine
    container_name: bomba-redis
    command: redis-server --requirepass ${REDIS_PASS}
    ports:
      - '${REDIS_PORT}:6379'
    volumes:
      - redis_data:/data
    healthcheck:
      test: ['CMD', 'redis-cli', 'ping']
      interval: 10s
 
  # RabbitMQ — يُضاف فقط لو مطلوب
  rabbitmq:
    image: rabbitmq:3-management-alpine
    container_name: bomba-rabbitmq
    environment:
      RABBITMQ_DEFAULT_USER: ${RABBITMQ_USER}
      RABBITMQ_DEFAULT_PASS: ${RABBITMQ_PASS}
    ports:
      - '${RABBITMQ_PORT}:5672'
      - '15672:15672'
    volumes:
      - rabbitmq_data:/var/lib/rabbitmq
 
  # MinIO — يُضاف فقط لو مطلوب
  minio:
    image: minio/minio:latest
    container_name: bomba-minio
    command: server /data --console-address ":9001"
    environment:
      MINIO_ROOT_USER: ${MINIO_ACCESS_KEY}
      MINIO_ROOT_PASSWORD: ${MINIO_SECRET_KEY}
    ports:
      - '${MINIO_PORT}:9000'
      - '9001:9001'
    volumes:
      - minio_data:/data
 
volumes:
  postgres_data:
  redis_data:
  rabbitmq_data:
  minio_data:
```
 
---
 
# PART 7: Frontend Architecture 🌐
 
## Tech Stack
 
```yaml
Framework : React 19.2 (Vite 6)
Language  : TypeScript 5.3+
Styling   : Tailwind CSS 4 — BomBa System (em + CSS Variables + @theme)
State     : Redux Toolkit 2.0 + Redux Persist
Forms     : React Hook Form 7 + Zod 3
i18n      : react-i18next 13
HTTP      : Axios 1.6 + TanStack Query 5
Icons     : Lucide React 0.300 (Icon prefix إلزامي)
Router    : React Router DOM 6.20
```
 
---
 
## هيكل app-web
 
```
app-web/
├── src/
│   ├── alias/
│   │   ├── core.ts       → React + Router + i18n + Hooks
│   │   ├── ui.ts         → BUI-1 + BUI-2 + BUI-O + Components
│   │   ├── icons.ts      → All Icons (Icon prefix)
│   │   ├── store.ts      → Redux + Actions + Types
│   │   ├── constants.ts  → Config + Routes + Assets
│   │   └── index.ts      → export * from all
│   │
│   ├── components/
│   │   ├── BUI-1.tsx           → HTML wrappers
│   │   ├── BUI-2.tsx           → UI Components
│   │   ├── BUI-O/              → Compound Components
│   │   │   ├── Modal.tsx
│   │   │   ├── Panel.tsx
│   │   │   └── TabPanel.tsx
│   │   ├── global/             → مكونات عامة
│   │   │   ├── BtnTheme.tsx
│   │   │   ├── BtnLanguage.tsx
│   │   │   └── LoaderScreen.tsx
│   │   └── layout/             → تخطيطات
│   │       ├── Header.tsx
│   │       ├── Footer.tsx
│   │       └── Sidebar.tsx
│   │
│   ├── pages/
│   │   ├── Dashboard/
│   │   │   └── index.tsx
│   │   ├── Auth/
│   │   │   ├── Login.tsx
│   │   │   └── Register.tsx
│   │   └── NotFound.tsx
│   │
│   ├── hooks/
│   │   ├── useSettings.ts
│   │   ├── useAuth.ts
│   │   └── useLocalizedPath.ts
│   │
│   ├── store/
│   │   ├── index.ts              → store config
│   │   ├── slices/
│   │   │   ├── settingsSlice.ts
│   │   │   ├── authSlice.ts
│   │   │   └── loaderSlice.ts
│   │   └── storage/
│   │       ├── cookieStorage.ts
│   │       └── localStorage.ts
│   │
│   ├── services/
│   │   ├── api.ts                → Axios instance
│   │   └── repositories/
│   │       ├── authRepository.ts
│   │       └── usersRepository.ts
│   │
│   ├── i18n/
│   │   ├── config.ts
│   │   └── locales/
│   │       ├── ar/
│   │       │   └── translation.json
│   │       └── en/
│   │           └── translation.json
│   │
│   ├── routes/
│   │   └── appRouter.tsx
│   │
│   ├── types/
│   │   ├── common.types.ts       → T_Theme, T_Language, ...
│   │   ├── api.types.ts          → API Request/Response types
│   │   └── env.d.ts              → Vite env declarations
│   │
│   ├── utils/
│   │   ├── cn.ts                 → classnames helper
│   │   └── format-date.ts
│   │
│   ├── assets/
│   │   ├── images/
│   │   ├── fonts/
│   │   └── icons/
│   │
│   ├── styles/
│   │   └── globals.css           → Tailwind @theme + CSS Variables + B: utilities
│   │
│   ├── App.tsx
│   ├── main.tsx
│   └── vite-env.d.ts
│
├── public/
│   ├── locales/                   → i18n files (public)
│   └── favicon.ico
│
├── index.html
├── package.json
├── tsconfig.json
├── vite.config.ts
└── .env
```
 
---
 
## tsconfig.json — Paths
 
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"],
      "@shared/*": ["../../packages/shared/*"],
      "@a": ["./src/alias/index.ts"],
      "@ui": ["./src/alias/ui.ts"],
      "@icons": ["./src/alias/icons.ts"],
      "@store": ["./src/alias/store.ts"],
      "@const": ["./src/alias/constants.ts"]
    }
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```
 
---
 
# PART 8: Alias System — نظام الاستيراد المركزي 🔗
 
## الفلسفة
 
```
❌ لا استيراد مباشر من المكتبات في الصفحات
✅ كل الاستيرادات عبر @a // @a => alias
```
 
---
 
## الهيكل
 
```
src/alias/
├── index.ts       → export * from all (الاستيراد العام)
├── core.ts        → React + Router + i18n + Redux + Hooks
├── ui.ts          → BUI + Components
├── icons.ts       → All Icons
├── store.ts       → Redux (dispatch, selectors, actions)
└── constants.ts   → Config + Routes + Assets
```
 
---
 
## alias/core.ts
 
```typescript
/**
 * @file : src/alias/core.ts
 * @description : استيرادات أساسية — React + Hooks + Router + i18n + Utils
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
export {
  default as React, useState, useEffect, useRef, useMemo, useCallback, useReducer, useContext, createContext,
  type FC, type ReactNode, type CSSProperties,
} from 'react'
 
export { BrowserRouter, HashRouter, Routes, Route, Navigate, Link, NavLink, Outlet, useNavigate, useLocation, useParams, useSearchParams, createBrowserRouter, createHashRouter, RouterProvider,
  type RouteObject,
} from 'react-router-dom'
 
export { useTranslation } from 'react-i18next'
export { default as i18n } from '@/i18n/config'
export { cn } from '@/utils/cn'
export { clsx } from 'clsx'
```
 
---
 
## alias/ui.ts
 
```typescript
/**
 * @file : src/alias/ui.ts
 * @description : استيرادات مكونات الواجهة - BUI & Global Components
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
export {
  H1, H2, H3, H4, H5, H6,
  P, Span, A, I,
  Div1, Div2, Div3, Div4, Div5,
  Header, Main, Footer, Nav,
  Section, Article, Aside,
  Hr, Br, Img,
  Form, Label, Input, Select, Textarea,
  Button, Check, Radio,
} from '@/components/BUI-1'
 
export { Button2, Input2, Check2, Card2 } from '@/components/BUI-2'
 
export { Modal }    from '@/components/BUI-O/Modal'
export { Panel }    from '@/components/BUI-O/Panel'
export { TabPanel } from '@/components/BUI-O/TabPanel'
 
export { BtnTheme }    from '@/components/global/BtnTheme'
export { BtnLanguage } from '@/components/global/BtnLanguage'
export { LoaderScreen } from '@/components/global/LoaderScreen'
```
 
---
 
## alias/icons.ts
 
```typescript
/**
 * @file : src/alias/icons.ts
 * @description : كل الأيقونات بـ Icon prefix إلزامي
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
export {
  Plus as IconPlus,
  Minus as IconMinus,
  X as IconClose,
  Check as IconCheck,
  Search as IconSearch,
  Trash2 as IconDelete,
  Pencil as IconEdit,
  Save as IconSave,
  RefreshCw as IconRefresh,
  Copy as IconCopy,
  Download as IconDownload,
  Upload as IconUpload,
  ChevronUp as IconChevronUp,
  ChevronDown as IconChevronDown,
  ChevronLeft as IconChevronLeft,
  ChevronRight as IconChevronRight,
  ArrowLeft as IconArrowLeft,
  ArrowRight as IconArrowRight,
  Menu as IconMenu,
  MoreVertical as IconMore,
  Sun as IconSun,
  Moon as IconMoon,
  Monitor as IconMonitor,
  Settings as IconSettings,
  Languages as IconLanguages,
  TriangleAlert as IconWarning,
  Info as IconInfo,
  CircleCheck as IconSuccess,
  CircleX as IconError,
  LoaderCircle as IconLoader,
  Hourglass as IconHourglass,
  UserRound as IconUser,
  Users as IconUsers,
  LockKeyhole as IconLock,
  Eye as IconEyeOn,
  EyeOff as IconEyeOff,
  LogIn as IconLogin,
  LogOut as IconLogout,
  Image as IconImage,
  Video as IconVideo,
  File as IconFile,
  Folder as IconFolder,
  Link as IconLink,
} from 'lucide-react'
 
export { FaGoogle as IconGoogle }       from 'react-icons/fa'
export { FaFacebookF as IconFacebook }  from 'react-icons/fa'
```
 
---
 
## alias/store.ts
 
```typescript
/**
 * @file : src/alias/store.ts
 * @description : استيرادات Redux - Hooks + Actions + Types
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
export {
  configureStore,
  createSlice,
  createAsyncThunk,
  type PayloadAction,
} from '@reduxjs/toolkit'
 
export {
  persistStore,
  persistReducer,
  FLUSH, REHYDRATE, PAUSE, PERSIST, PURGE, REGISTER,
} from 'redux-persist'
 
export { store, persistor, type RootState, type AppDispatch } from '@/store'
export { useDispatch, useSelector } from 'react-redux'
export { setTheme, setLanguage }    from '@/store/slices/settingsSlice'
export { showLoader, hideLoader }   from '@/store/slices/loaderSlice'
```
 
---
 
## alias/constants.ts
 
```typescript
/**
 * @file : src/alias/constants.ts
 * @description : استيرادات الثوابت - Routes + Assets + Config
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
export const ROUTES = {
  HOME:      '/',
  DASHBOARD: '/dashboard',
  LOGIN:     '/login',
  REGISTER:  '/register',
  PROFILE:   '/profile',
} as const
 
export const IMG_LOGO           = '/images/logo.svg'
export const IMG_AVATAR_DEFAULT = '/images/avatar-default.png'
 
export const APP_NAME            = 'BomBa'
export const DEFAULT_LANGUAGE    = 'en' as const
export const DEFAULT_THEME       = 'system' as const
export const SUPPORTED_LANGUAGES = ['ar', 'en'] as const
```
 
---
 
## قواعد مهمة
 
```markdown
✅ الاستيراد العام للصفحات البسيطة: import { ... } from '@a'; // @a => alias
✅ الاستيراد المحدد للصفحات الكبيرة: import { ... } from '@ui'
✅ Icon prefix إلزامي في icons.ts
✅ لا circular dependencies
✅ الملفات المحلية يمكن استيرادها مباشرة
```
 
---
 
# PART 9: BUI Component System 🎨
 
## الطبقات — القاعدة الأساسية
 
```
BUI-1 → HTML wrappers (لا منطق، لا state، لا hooks)
BUI-2 → UI Components (state/behavior — يستخدم BUI-1 فقط)
BUI-O → Compound (Modal, Panel, TabPanel — يستخدم BUI-2 فقط)
Pages → يستخدم BUI-O/BUI-2 فقط
 
❌ ممنوع تخطي الطبقات أبداً
```
 
---
 
## buildProps — إلزامي في كل مكون
 
```typescript
/**
 * @file : src/utils/buildProps.ts
 * @description : تنظيف className و style وإزالة القيم الفارغة
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
const buildProps = <T extends { className?: string; style?: React.CSSProperties }>(props: T): T => {
  const { className, style, ...rest } = props
  return {
    ...rest,
    ...(className?.trim() ? { className: className.trim() } : {}),
    ...(style && Object.keys(style).length > 0 ? { style } : {}),
  } as T
}
```
 
---
 
## BUI-1 — HTML Wrappers
 
```typescript
/**
 * @file : src/components/BUI-1.tsx
 * @description : عناصر HTML الأساسية مع buildProps
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
const buildProps = <T extends { className?: string; style?: React.CSSProperties }>(props: T): T => {
  const { className, style, ...rest } = props
  return {
    ...rest,
    ...(className?.trim() ? { className: className.trim() } : {}),
    ...(style && Object.keys(style).length > 0 ? { style } : {}),
  } as T
}
 
export const H1      = (p: React.HTMLAttributes<HTMLHeadingElement>)      => <h1 {...buildProps(p)} />
export const H2      = (p: React.HTMLAttributes<HTMLHeadingElement>)      => <h2 {...buildProps(p)} />
export const H3      = (p: React.HTMLAttributes<HTMLHeadingElement>)      => <h3 {...buildProps(p)} />
export const H4      = (p: React.HTMLAttributes<HTMLHeadingElement>)      => <h4 {...buildProps(p)} />
export const H5      = (p: React.HTMLAttributes<HTMLHeadingElement>)      => <h5 {...buildProps(p)} />
export const H6      = (p: React.HTMLAttributes<HTMLHeadingElement>)      => <h6 {...buildProps(p)} />
export const P       = (p: React.HTMLAttributes<HTMLParagraphElement>)    => <p {...buildProps(p)} />
export const Span    = (p: React.HTMLAttributes<HTMLSpanElement>)         => <span {...buildProps(p)} />
export const A       = (p: React.AnchorHTMLAttributes<HTMLAnchorElement>) => <a {...buildProps(p)} />
export const I       = (p: React.HTMLAttributes<HTMLElement>)             => <i {...buildProps(p)} />
 
export const Div1    = (p: React.HTMLAttributes<HTMLDivElement>) => <div data-level="1" {...buildProps(p)} />
export const Div2    = (p: React.HTMLAttributes<HTMLDivElement>) => <div data-level="2" {...buildProps(p)} />
export const Div3    = (p: React.HTMLAttributes<HTMLDivElement>) => <div data-level="3" {...buildProps(p)} />
export const Div4    = (p: React.HTMLAttributes<HTMLDivElement>) => <div data-level="4" {...buildProps(p)} />
export const Div5    = (p: React.HTMLAttributes<HTMLDivElement>) => <div data-level="5" {...buildProps(p)} />
 
export const Header  = (p: React.HTMLAttributes<HTMLElement>) => <header {...buildProps(p)} />
export const Main    = (p: React.HTMLAttributes<HTMLElement>) => <main {...buildProps(p)} />
export const Footer  = (p: React.HTMLAttributes<HTMLElement>) => <footer {...buildProps(p)} />
export const Nav     = (p: React.HTMLAttributes<HTMLElement>) => <nav {...buildProps(p)} />
export const Section = (p: React.HTMLAttributes<HTMLElement>) => <section {...buildProps(p)} />
export const Article = (p: React.HTMLAttributes<HTMLElement>) => <article {...buildProps(p)} />
export const Aside   = (p: React.HTMLAttributes<HTMLElement>) => <aside {...buildProps(p)} />
 
export const Hr      = (p: React.HTMLAttributes<HTMLHRElement>)       => <hr {...buildProps(p)} />
export const Br      = (p: React.HTMLAttributes<HTMLBRElement>)       => <br {...buildProps(p)} />
export const Img     = (p: React.ImgHTMLAttributes<HTMLImageElement>) => <img {...buildProps(p)} />
 
export const Form     = (p: React.FormHTMLAttributes<HTMLFormElement>)         => <form {...buildProps(p)} />
export const Label    = (p: React.LabelHTMLAttributes<HTMLLabelElement>)       => <label {...buildProps(p)} />
export const Input    = (p: React.InputHTMLAttributes<HTMLInputElement>)       => <input {...buildProps(p)} />
export const Select   = (p: React.SelectHTMLAttributes<HTMLSelectElement>)     => <select {...buildProps(p)} />
export const Textarea = (p: React.TextareaHTMLAttributes<HTMLTextAreaElement>) => <textarea {...buildProps(p)} />
export const Button   = (p: React.ButtonHTMLAttributes<HTMLButtonElement>)     => <button {...buildProps(p)} />
export const Check    = (p: React.InputHTMLAttributes<HTMLInputElement>)       => <input type="checkbox" {...buildProps(p)} />
export const Radio    = (p: React.InputHTMLAttributes<HTMLInputElement>)       => <input type="radio" {...buildProps(p)} />
```
 
---
 
## BUI-2 — UI Components
 
```typescript
/**
 * @file : src/components/BUI-2.tsx
 * @description : مكونات UI مع Tailwind CSS classes
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
import { Div5, Input, Span } from '@a'
 
interface Input2Props extends React.InputHTMLAttributes<HTMLInputElement> {
  label?      : string
  icon?       : React.ReactNode
  error?      : string
  classGroup? : string
  classLabel? : string
  classInput? : string
}
 
export const Input2: React.FC<Input2Props> = ({
  label, icon, error,
  classGroup = '', classLabel = '', classInput = '',
  className = '',
  ...restProps
}) => (
  <Div5 className={`flex flex-col gap-2 w-full ${classGroup}`}>
    {label && (
      <Span className={`text-sm font-medium text-te B:font-var ${classLabel}`}>
        {label}
      </Span>
    )}
    <Div5 className="relative flex items-center">
      {icon && (
        <Span className="absolute start-3 flex items-center text-sn pointer-events-none">
          {icon}
        </Span>
      )}
      <Input
        {...buildProps({
          className: `
            w-full px-4 py-2_5 border border-br
            text-base text-tt bg-bg
            outline-none B:rounded-2 B:transition-colors
            focus:border-py focus:bg-py/5
            ${icon ? 'ps-9' : ''}
            ${classInput} ${className}
          `,
        })}
        {...restProps}
      />
    </Div5>
    {error && (
      <Span className="text-xs text-err">{error}</Span>
    )}
  </Div5>
)
```
 
---
 
## Checklist مكون جديد
 
```markdown
□ الطبقة صح (BUI-1 / BUI-2 / BUI-O)؟
□ buildProps مستخدمة؟
□ interface يمتد من HTML الأصلي؟
□ ...restProps في النهاية؟
□ classGroup / classLabel بدل className متعددة؟
□ مضاف لـ alias/ui.ts؟
□ JSDoc بالعربية؟
□ Accessibility (aria, htmlFor)؟
□ Tailwind classes بالترتيب الصحيح؟
```
 
---
 
# PART 10: Tailwind CSS System 🎨
 
## الفلسفة — BomBa Tailwind Rules
 
```
1. em وحدة القياس الأساسية — مش px
2. CSS Variables للألوان والثيم — مش hardcoded values
3. Tailwind 4 → @theme في CSS — مش tailwind.config.js
4. B: prefix للـ Custom Utilities — مش inline style
5. Tailwind أولاً، ترتيب ثابت دائماً
```
 
---
 
## globals.css — الملف الكامل
 
```css
/**
 * @file : src/app/globals.css
 * @description : ملف CSS الرئيسي مع Tailwind CSS و CSS Variables
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
@import "tailwindcss";
 
/* ══════════════════════════════════════════════
   CSS Variables — :root
══════════════════════════════════════════════ */
:root {
  /* ─── تحكم Dark Mode ─────────────────────── */
  --flip-l : 0%;
  --ISD    : -1;
 
  /* ─── اللون الأساسي (HSL) ───────────────── */
  --h      : 210;
  --s      : 80%;
  --l      : 40%;
  --py-hsl : var(--h), var(--s), var(--l);
 
  /* ─── الألوان الرئيسية ──────────────────── */
  --color-py  : hsl(var(--h), var(--s), var(--l));
  --color-sy  : hsl(330, var(--s), var(--l));
  --color-at  : hsl(300, var(--s), var(--l));
  --color-md  : hsl(250, var(--s), var(--l));
 
  /* ─── ألوان الحالات ─────────────────────── */
  --color-ok  : hsl(130, var(--s), var(--l));
  --color-err : hsl(5,   var(--s), var(--l));
  --color-war : hsl(60,  var(--s), var(--l));
  --color-inf : hsl(200, var(--s), var(--l));
 
  /* ─── ألوان الواجهة ─────────────────────── */
  --color-light : hsl(var(--h), var(--s), calc(var(--flip-l) - 98% * var(--ISD)));
  --color-dark  : hsl(var(--h), var(--s), calc(var(--flip-l) -  2% * var(--ISD)));
  --color-bg    : hsl(var(--h), var(--s), calc(var(--flip-l) - 98% * var(--ISD)));
  --color-te    : hsl(var(--h), var(--s), calc(var(--flip-l) - 10% * var(--ISD)));
  --color-tt    : hsl(var(--h), var(--s), calc(var(--flip-l) -  2% * var(--ISD)));
  --color-sn    : hsl(var(--h), var(--s), calc(var(--flip-l) - 20% * var(--ISD)));
 
  /* ─── ألوان خاصة ────────────────────────── */
  --color-trans : hsl(from var(--color-py) h s l / 0%);
  --color-over  : hsl(from var(--color-py) h s l / 50%);
  --color-br    : color-mix(in srgb,
    hsl(var(--h), var(--s), var(--l)) 50%,
    hsl(var(--h), var(--s), calc(var(--flip-l) - 98% * var(--ISD)))
  );
 
  /* ─── اتجاه RTL/LTR ─────────────────────── */
  --ltr       : 1;
  --dir-start : left;
  --dir-end   : right;
 
  /* ─── تحكم Shadow و Radius ──────────────── */
  --shadow : 1;
  --radius : 1;
 
  /* ─── خط ────────────────────────────────── */
  --ffy : "Inter", system-ui, -apple-system, sans-serif;
 
  /* ─── z-index ───────────────────────────── */
  --z-1 : 1;  --z-2 : 2;  --z-3 : 3;
  --z-4 : 4;  --z-5 : 5;  --z-6 : 6;
  --z-modal   : 999;
  --z-tooltip : 1000;
  --z-top     : 2147483647;
}
 
/* ─── RTL ──────────────────────────────────── */
[dir="rtl"] { --ltr: -1; --dir-start: right; --dir-end: left; }
 
/* ─── Dark Mode ─────────────────────────────── */
[data-theme="dark"],
.dark { --h: 160; --flip-l: 100%; --ISD: 1; }
 
 
/* ══════════════════════════════════════════════
   @theme — تسجيل الألوان والـ Scale في Tailwind 4
══════════════════════════════════════════════ */
@theme {
 
  /* ─── Spacing (em) ──────────────────────── */
  --spacing-px  : 0.0625em;
  --spacing-0   : 0em;
  --spacing-0_5 : 0.125em;
  --spacing-1   : 0.25em;
  --spacing-1_5 : 0.375em;
  --spacing-2   : 0.5em;
  --spacing-2_5 : 0.625em;
  --spacing-3   : 0.75em;
  --spacing-3_5 : 0.875em;
  --spacing-4   : 1em;
  --spacing-5   : 1.25em;
  --spacing-6   : 1.5em;
  --spacing-7   : 1.75em;
  --spacing-8   : 2em;
  --spacing-9   : 2.25em;
  --spacing-10  : 2.5em;
  --spacing-11  : 2.75em;
  --spacing-12  : 3em;
  --spacing-14  : 3.5em;
  --spacing-16  : 4em;
  --spacing-20  : 5em;
  --spacing-24  : 6em;
  --spacing-28  : 7em;
  --spacing-32  : 8em;
 
  /* ─── Font Size (em) ────────────────────── */
  --font-size-xs   : 0.75em;
  --font-size-sm   : 0.875em;
  --font-size-base : 1em;
  --font-size-lg   : 1.125em;
  --font-size-xl   : 1.25em;
  --font-size-2xl  : 1.5em;
  --font-size-3xl  : 1.875em;
  --font-size-4xl  : 2.25em;
  --font-size-5xl  : 3em;
  --font-size-6xl  : 3.75em;
 
  /* ─── Border Radius (em) ────────────────── */
  --radius-sm   : 0.125em;
  --radius-md   : 0.375em;
  --radius-lg   : 0.5em;
  --radius-xl   : 0.75em;
  --radius-2xl  : 1em;
  --radius-3xl  : 1.5em;
  --radius-full : 9999em;
 
  /* ─── الألوان المسجّلة في Tailwind ──────── */
  --color-py    : hsl(var(--py-hsl));
  --color-sy    : hsl(330, var(--s), var(--l));
  --color-at    : hsl(300, var(--s), var(--l));
  --color-md    : hsl(250, var(--s), var(--l));
 
  --color-ok    : hsl(130, var(--s), var(--l));
  --color-err   : hsl(5,   var(--s), var(--l));
  --color-war   : hsl(60,  var(--s), var(--l));
  --color-inf   : hsl(200, var(--s), var(--l));
 
  --color-light : hsl(var(--h), var(--s), calc(var(--flip-l) - 98% * var(--ISD)));
  --color-dark  : hsl(var(--h), var(--s), calc(var(--flip-l) -  2% * var(--ISD)));
  --color-bg    : hsl(var(--h), var(--s), calc(var(--flip-l) - 98% * var(--ISD)));
  --color-te    : hsl(var(--h), var(--s), calc(var(--flip-l) - 10% * var(--ISD)));
  --color-tt    : hsl(var(--h), var(--s), calc(var(--flip-l) -  2% * var(--ISD)));
  --color-sn    : hsl(var(--h), var(--s), calc(var(--flip-l) - 20% * var(--ISD)));
 
  --color-trans : hsl(from var(--color-py) h s l / 0%);
  --color-over  : hsl(from var(--color-py) h s l / 50%);
  --color-br    : color-mix(in srgb,
    hsl(var(--h), var(--s), var(--l)) 50%,
    hsl(var(--h), var(--s), calc(var(--flip-l) - 98% * var(--ISD)))
  );
}
 
 
/* ══════════════════════════════════════════════
   B: Custom Utilities
══════════════════════════════════════════════ */
@layer utilities {
 
  /* ─── Shadow ────────────────────────────── */
  .B\:shadow-var {
    box-shadow: 0 0.25em 0.5em
      hsl(from var(--color-py) h s l / var(--shadow));
  }
  .B\:shadow-md {
    box-shadow: 0 0.25em 1em
      hsl(from var(--color-py) h s l / calc(0.2 * var(--shadow)));
  }
  .B\:shadow-lg {
    box-shadow: 0 0.5em 2em
      hsl(from var(--color-py) h s l / calc(0.3 * var(--shadow)));
  }
 
  /* ─── Radius ────────────────────────────── */
  .B\:rounded-1    { border-radius: calc(0.25em  * var(--radius)); }
  .B\:rounded-2    { border-radius: calc(0.5em   * var(--radius)); }
  .B\:rounded-3    { border-radius: calc(0.75em  * var(--radius)); }
  .B\:rounded-4    { border-radius: calc(1em     * var(--radius)); }
  .B\:rounded-full { border-radius: calc(9999px  * var(--radius)); }
 
  /* ─── RTL Positioning ───────────────────── */
  .B\:dir-position {
    left  : var(--dir-start);
    right : var(--dir-end);
  }
 
  /* ─── RTL Transform ─────────────────────── */
  .B\:translate-rtl {
    transform: translateX(calc(-50% * var(--ltr)));
  }
  .B\:translate-rtl-center {
    transform: translate(calc(-50% * var(--ltr)), -50%);
  }
 
  /* ─── Font ──────────────────────────────── */
  .B\:font-var   { font-family: var(--ffy); }
  .B\:tracking-1 { letter-spacing: 0.025em; }
  .B\:tracking-2 { letter-spacing: 0.05em; }
 
  /* ─── Transitions ───────────────────────── */
  .B\:transition-smooth {
    transition: transform 0.2s ease, box-shadow 0.2s ease, opacity 0.2s ease;
  }
  .B\:transition-colors {
    transition: color 0.2s ease, background-color 0.2s ease, border-color 0.2s ease;
  }
 
  /* ─── z-index ───────────────────────────── */
  .B\:z-modal   { z-index: var(--z-modal); }
  .B\:z-tooltip { z-index: var(--z-tooltip); }
  .B\:z-top     { z-index: var(--z-top); }
 
  /* ─── Overlay ───────────────────────────── */
  .B\:overlay {
    background      : hsl(from var(--color-py) h s l / 50%);
    backdrop-filter : blur(0.25em);
  }
}
```
 
---
 
## ترتيب الـ Classes — إلزامي
 
```
1. Positioning  → relative / absolute / fixed / z-*
2. Display      → flex / grid / hidden / block
3. Box Model    → w-* / h-* / p-* / m-* / gap-* / border
4. Typography   → text-* / font-* / leading-* / B:tracking-*
5. Visuals      → bg-* / text-* / B:rounded-* / opacity-*
6. Motion       → B:transition-* / hover:* / B:shadow-*
```
 
---
 
## أنماط الاستخدام الشائعة
 
### زر أساسي
 
```html
<button class="
  flex items-center justify-center gap-2
  px-6 py-3 border-0
  text-base font-semibold B:font-var
  bg-py text-bg B:rounded-2 B:shadow-var
  hover:bg-py/90 hover:scale-[1.02]
  B:transition-smooth
">
  إضغط هنا
</button>
```
 
### زر ثانوي (Outline)
 
```html
<button class="
  flex items-center justify-center gap-2
  px-6 py-3 border border-br
  text-base font-semibold B:font-var
  bg-bg text-py B:rounded-2
  hover:bg-py/10
  B:transition-colors
">
  إلغاء
</button>
```
 
### بطاقة (Card)
 
```html
<div class="
  relative flex flex-col gap-4
  w-full p-6 border border-br
  bg-bg B:rounded-3 B:shadow-md
">
  <h2 class="text-xl font-bold text-te B:font-var">العنوان</h2>
  <p class="text-sm leading-relaxed text-sn">المحتوى هنا</p>
</div>
```
 
### Input
 
```html
<div class="flex flex-col gap-2 w-full">
  <label class="text-sm font-medium text-te B:font-var">البريد الإلكتروني</label>
  <input
    class="
      w-full px-4 py-2_5 border border-br
      text-base text-tt bg-bg
      outline-none B:rounded-2 B:transition-colors
      focus:border-py focus:bg-py/5
    "
    placeholder="example@email.com"
  />
  <span class="text-xs text-err">هذا الحقل مطلوب</span>
</div>
```
 
### Modal
 
```html
<div class="fixed inset-0 flex items-center justify-center B:z-modal B:overlay">
  <div class="
    relative flex flex-col gap-6
    w-full max-w-[32em] p-8 border border-br
    bg-bg B:rounded-3 B:shadow-lg
  ">
    <header class="flex items-center justify-between gap-4">
      <h2 class="text-xl font-bold text-te B:font-var">عنوان النافذة</h2>
      <button class="
        flex items-center justify-center w-8 h-8
        text-sn bg-bg
        hover:text-err hover:bg-err/10
        B:rounded-2 B:transition-colors
      ">✕</button>
    </header>
    <p class="text-base text-tt leading-relaxed">محتوى النافذة هنا.</p>
    <footer class="flex items-center justify-end gap-3">
      <button class="px-5 py-2 border border-br text-sm font-medium text-tt bg-bg B:rounded-2 hover:bg-br/20 B:transition-colors">
        إلغاء
      </button>
      <button class="px-5 py-2 border-0 text-sm font-semibold text-bg bg-py B:rounded-2 B:shadow-var hover:bg-py/90 B:transition-smooth">
        تأكيد
      </button>
    </footer>
  </div>
</div>
```
 
### Alert
 
```html
<!-- Success -->
<div class="flex items-start gap-3 w-full px-4 py-3 border border-ok/30 bg-ok/10 B:rounded-2">
  <span class="text-lg text-ok">✓</span>
  <div class="flex flex-col gap-1">
    <p class="text-sm font-semibold text-ok">تمت العملية بنجاح</p>
    <p class="text-xs text-sn">تم حفظ التغييرات.</p>
  </div>
</div>
```
 
### Badge
 
```html
<span class="inline-flex items-center px-3 py-1 text-xs font-medium bg-py/10 text-py B:rounded-full">نشط</span>
<span class="inline-flex items-center px-3 py-1 text-xs font-medium bg-ok/10 text-ok B:rounded-full">مكتمل</span>
<span class="inline-flex items-center px-3 py-1 text-xs font-medium bg-err/10 text-err B:rounded-full">ملغي</span>
<span class="inline-flex items-center px-3 py-1 text-xs font-medium bg-war/10 text-war B:rounded-full">معلّق</span>
```
 
---
 
## ⚠️ ممنوعات Tailwind
 
```html
<!-- ❌ hardcoded colors -->
<div class="bg-[#3b82f6] text-white">
<!-- ✅ -->
<div class="bg-py text-bg">
 
<!-- ❌ arbitrary values للقياسات -->
<div class="p-[1em] text-[0.875em] rounded-[0.5em]">
<!-- ✅ القيم من الجوه em بسبب @theme -->
<div class="p-4 text-sm rounded-lg">
 
<!-- ❌ dark: prefix -->
<div class="bg-white dark:bg-gray-900">
<!-- ✅ Variables تتغير تلقائياً -->
<div class="bg-bg">
 
<!-- ❌ ترتيب عشوائي -->
<div class="text-py flex p-4 relative font-bold bg-bg items-center">
<!-- ✅ Positioning → Display → Box Model → Typography → Visuals -->
<div class="relative flex items-center p-4 font-bold text-py bg-bg">
 
<!-- ❌ inline style للـ shadow/radius -->
<div style="box-shadow: 0 4px 16px rgba(0,0,0,0.1);">
<!-- ✅ -->
<div class="B:shadow-md B:rounded-2">
 
<!-- ❌ tailwind.config.js في Tailwind 4 -->
<!-- ✅ استخدم @theme في globals.css -->
```
 
---
 
# PART 11: Shared Types System 📐
 
## الفلسفة
 
```
✅ نوع واحد — مصدر واحد — كل الـ apps تستورد منه
✅ Frontend + Backend يشتركان في نفس الـ types
✅ منع التكرار وضمان التوافق بين طرفي الـ API
✅ T_ prefix للـ types | I_ prefix للـ interfaces
✅ DTO للبيانات المتنقلة بين الطبقات
```
 
---
 
## أين يعيش؟
 
```
packages/types/           ← مشترك بين كل الـ apps
src/types/                ← خاص بـ app معينة
```
 
---
 
## هيكل packages/types
 
```
packages/types/
├── package.json
├── tsconfig.json
├── index.ts              ← export * from all
│
├── common/
│   ├── primitives.ts     ← T_ID, T_Timestamp, T_Nullable, ...
│   ├── theme.ts          ← T_Theme, T_Language, T_Direction
│   └── pagination.ts     ← I_Pagination, I_PagedResult<T>
│
├── api/
│   ├── response.ts       ← I_ApiResponse<T>, I_ApiError
│   └── request.ts        ← I_QueryParams, I_FilterParams
│
├── entities/
│   ├── user.ts           ← I_User, I_UserDTO, I_CreateUserDTO
│   ├── auth.ts           ← I_LoginDTO, I_TokenPair, I_JWTPayload
│   └── ...               ← entity لكل module
│
└── store/
    └── slices.ts         ← I_SettingsState, I_AuthState, ...
```
 
---
 
## common/primitives.ts
 
```typescript
/**
 * @file : packages/types/common/primitives.ts
 * @description : أنواع بدائية مشتركة
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
export type T_ID        = string
export type T_NumID     = number
export type T_Slug      = string
export type T_Timestamp = string
export type T_Date      = string
export type T_Time      = string
 
export type T_Nullable<T> = T | null
export type T_Optional<T> = T | undefined
export type T_Maybe<T>    = T | null | undefined
 
export type T_AnyObject  = Record<string, unknown>
export type T_StringMap  = Record<string, string>
export type T_EmptyObject = Record<string, never>
 
export type T_Fn<TArgs extends unknown[] = [], TReturn = void>      = (...args: TArgs) => TReturn
export type T_AsyncFn<TArgs extends unknown[] = [], TReturn = void> = (...args: TArgs) => Promise<TReturn>
export type T_Callback<T = void>  = (value: T) => void
export type T_VoidCallback        = () => void
```
 
---
 
## common/theme.ts
 
```typescript
/**
 * @file : packages/types/common/theme.ts
 * @description : أنواع الثيم واللغة
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
export type T_Theme     = 'light' | 'dark' | 'system'
export type T_Language  = 'ar' | 'en'
export type T_Direction = 'ltr' | 'rtl'
export type T_ColorMode = 'light' | 'dark'
 
export const THEMES    : T_Theme[]     = ['light', 'dark', 'system']
export const LANGUAGES : T_Language[]  = ['ar', 'en']
export const DIRECTIONS: T_Direction[] = ['ltr', 'rtl']
 
export const getDirection = (lang: T_Language): T_Direction => lang === 'ar' ? 'rtl' : 'ltr'
export const isRTL        = (lang: T_Language): boolean => lang === 'ar'
```
 
---
 
## common/pagination.ts
 
```typescript
/**
 * @file : packages/types/common/pagination.ts
 * @description : أنواع التصفح والنتائج المفهرسة
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
export interface I_Pagination {
  page  : number
  limit : number
  total : number
  pages : number
}
 
export interface I_PagedResult<T> {
  data       : T[]
  pagination : I_Pagination
}
 
export interface I_QueryParams {
  page?    : number
  limit?   : number
  search?  : string
  sortBy?  : string
  sortDir? : 'asc' | 'desc'
}
```
 
---
 
## api/response.ts
 
```typescript
/**
 * @file : packages/types/api/response.ts
 * @description : أنواع استجابات API
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
export interface I_ApiResponse<T = unknown> {
  success  : boolean
  data     : T | null
  message? : string
}
 
export interface I_ApiError {
  code     : string
  message  : string
  meta?    : Record<string, unknown>
  details? : I_ValidationError[]
}
 
export interface I_ValidationError {
  field   : string
  message : string
}
 
export interface I_ErrorResponse {
  success : false
  data    : null
  message : string
  error   : I_ApiError
}
 
export interface I_PagedResponse<T> extends I_ApiResponse<T[]> {
  pagination: I_Pagination
}
 
export const isApiError = (res: unknown): res is I_ErrorResponse =>
  typeof res === 'object' &&
  res !== null &&
  'success' in res &&
  (res as I_ErrorResponse).success === false
```
 
---
 
## entities/user.ts
 
```typescript
/**
 * @file : packages/types/entities/user.ts
 * @description : أنواع كيانات المستخدم
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
import type {
  // primitives:
  T_ID, T_Timestamp
  } from '@a';
 
export type T_UserRole   = 'admin' | 'user' | 'moderator'
export type T_UserStatus = 'active' | 'inactive' | 'banned'
 
export interface I_User {
  id               : T_ID
  name             : string
  email            : string
  role             : T_UserRole
  status           : T_UserStatus
  avatarUrl?       : string
  emailVerifiedAt? : T_Timestamp
  createdAt        : T_Timestamp
  updatedAt        : T_Timestamp
}
 
export interface I_CreateUserDTO {
  name     : string
  email    : string
  password : string
  role?    : T_UserRole
}
 
export type I_UpdateUserDTO  = Partial<Pick<I_CreateUserDTO, 'name' | 'email' | 'password'>>
export type I_UserResponse   = Omit<I_User, 'password'>
export type I_UserSummary    = Pick<I_User, 'id' | 'name' | 'email' | 'avatarUrl'>
```
 
---
 
## entities/auth.ts
 
```typescript
/**
 * @file : packages/types/entities/auth.ts
 * @description : أنواع كيانات المصادقة
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
import type {
  // primitives:
  T_ID,
  // user:
  I_UserResponse,
  } from '@a';
 
export interface I_LoginDTO {
  email    : string
  password : string
}
 
export interface I_RegisterDTO {
  name            : string
  email           : string
  password        : string
  confirmPassword : string
}
 
export interface I_TokenPair {
  accessToken  : string
  refreshToken : string
}
 
export interface I_JWTPayload {
  userId : T_ID
  role   : string
  iat    : number
  exp    : number
}
 
export interface I_AuthResponse {
  user   : I_UserResponse
  tokens : I_TokenPair
}
 
export interface I_ForgotPasswordDTO  { email: string }
export interface I_ResetPasswordDTO   { token: string; password: string; confirmPassword: string }
export interface I_ChangePasswordDTO  { currentPassword: string; newPassword: string }
export interface I_VerifyEmailDTO     { token: string }
```
 
---
 
## store/slices.ts
 
```typescript
/**
 * @file : packages/types/store/slices.ts
 * @description : أنواع_slices للـ Redux
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
import type {
  // theme:
  T_Theme, T_Language,
  // user:
  I_UserResponse,
  } from '@a';
 
export interface I_SettingsState {
  theme            : T_Theme
  language         : T_Language
  sidebarCollapsed : boolean
}
 
export interface I_AuthState {
  user         : I_UserResponse | null
  accessToken  : string | null
  refreshToken : string | null
  isLoading    : boolean
  error        : string | null
}
 
export interface I_LoaderState {
  isVisible : boolean
  message?  : string
}
```
 
---
 
## packages/types/index.ts
 
```typescript
export * from './common/primitives'
export * from './common/theme'
export * from './common/pagination'
export * from './api/response'
export * from './api/request'
export * from './entities/user'
export * from './entities/auth'
export * from './store/slices'
```
 
---
 
## الاستخدام في Frontend
 
```typescript
import type {
  I_User, I_CreateUserDTO,
  I_ApiResponse, I_PagedResponse,
  T_Theme, T_Language,
  I_SettingsState,
} from '@shared/types'
```
 
---
 
## الاستخدام في Backend
 
```typescript
import type {
  I_CreateUserDTO, I_UserResponse,
  I_LoginDTO, I_TokenPair,
  I_ApiResponse, I_ErrorResponse,
} from '@shared/types'
 
async create(req: Request, res: Response) {
  const dto: I_CreateUserDTO = req.body
  const user: I_UserResponse = await UsersService.create(dto)
  const response: I_ApiResponse<I_UserResponse> = { success: true, data: user }
  res.status(201).json(response)
}
```
 
---
 
## src/types — أنواع خاصة بالـ Frontend
 
```typescript
/**
 * @file : src/types/common.types.ts
 * @description : أنواع عامة خاصة بواجهة المستخدم
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
export type T_FormMode  = 'create' | 'edit' | 'view'
export type T_ModalSize = 'sm' | 'md' | 'lg' | 'xl' | 'full'
export type T_AlertType = 'success' | 'error' | 'warning' | 'info'
 
export interface I_NavItem {
  key      : string
  label    : string
  path     : string
  icon?    : React.ReactNode
  children?: I_NavItem[]
  roles?   : string[]
}
 
export interface I_TableColumn<T> {
  key      : keyof T | string
  label    : string
  width?   : string
  sortable?: boolean
  render?  : (value: unknown, row: T) => React.ReactNode
}
 
export interface I_SelectOption<T = string> {
  label    : string
  value    : T
  disabled?: boolean
}
```
 
---
 
## قواعد Shared Types
 
```markdown
✅ T_ prefix للـ Type Aliases
✅ I_ prefix للـ Interfaces
✅ DTO suffix للبيانات المتنقلة
✅ Response suffix للبيانات المرجعة
✅ State suffix لـ Redux Slices
 
❌ لا any في أي type
❌ لا نفس الـ type في أكتر من مكان
❌ لا استيراد من @shared/types في BUI-1
```
 
---
 
# PART 12: State Management — Redux 🧠
 
## Tech Stack
 
```
Redux Toolkit 2.0      → createSlice + configureStore
Redux Persist 6        → التخزين الدائم (Cookies/LocalStorage)
```
 
---
 
## الهيكل
 
```
src/store/
├── index.ts
├── slices/
│   ├── settingsSlice.ts
│   ├── authSlice.ts
│   └── loaderSlice.ts
└── storage/
    ├── cookieStorage.ts
    └── localStorage.ts
```
 
---
 
## store/index.ts
 
```typescript
/**
 * @file : src/store/index.ts
 * @description : تهيئة Redux Store مع Redux Persist
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
import type {
  // @reduxjs/toolkit:
  configureStore,
  // redux-persist:
  persistStore, persistReducer, FLUSH, REHYDRATE, PAUSE, PERSIST, PURGE, REGISTER,,
  // slices/settingsSlice:
  settingsReducer,
  // slices/loaderSlice:
  loaderReducer,
  // storage/cookieStorage:
  createCookieStorage,
  } from '@a';
 
 
const settingsPersistConfig = {
  key       : 'settings',
  storage   : createCookieStorage(),
  whitelist : ['theme', 'language'],
}
 
export const store = configureStore({
  reducer: {
    settings : persistReducer(settingsPersistConfig, settingsReducer),
    loader   : loaderReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: [FLUSH, REHYDRATE, PAUSE, PERSIST, PURGE, REGISTER],
      },
    }),
})
 
export const persistor   = persistStore(store)
export type RootState    = ReturnType<typeof store.getState>
export type AppDispatch  = typeof store.dispatch
```
 
---
 
## slices/settingsSlice.ts
 
```typescript
/**
 * @file : src/store/slices/settingsSlice.ts
 * @description : Slice لإدارة إعدادات التطبيق (الثيم، اللغة، التوسيع)
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
import type {
  // @reduxjs/toolkit:
  createSlice, type PayloadAction,
  // @shared/types:
  type { I_SettingsState, T_Theme, T_Language},
  } from '@a';
 
const initialState: I_SettingsState = {
  theme            : 'system',
  language         : 'en',
  sidebarCollapsed : false,
}
 
const settingsSlice = createSlice({
  name: 'settings',
  initialState,
  reducers: {
    setTheme: (state, action: PayloadAction<T_Theme>) => {
      state.theme = action.payload
      document.documentElement.setAttribute('data-theme', action.payload)
    },
    setLanguage: (state, action: PayloadAction<T_Language>) => {
      state.language = action.payload
      document.documentElement.lang = action.payload
      document.documentElement.dir  = action.payload === 'ar' ? 'rtl' : 'ltr'
    },
    toggleSidebar: (state) => {
      state.sidebarCollapsed = !state.sidebarCollapsed
    },
  },
})
 
export const { setTheme, setLanguage, toggleSidebar } = settingsSlice.actions
export default settingsSlice.reducer
```
 
---
 
## Custom Hook — useSettings
 
```typescript
/**
 * @file : src/hooks/useSettings.ts
 * @description : Custom Hook لإدارة الإعدادات
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
import type {
  // react-redux:
  useDispatch, useSelector,
  // react-i18next:
  useTranslation,
  // @store:
  setTheme, setLanguage, type { RootState, AppDispatch },
  // @shared/types:
  type { T_Theme, T_Language },
  } from '@a';
 
export const useSettings = () => {
  const { t, i18n } = useTranslation()
  const dispatch     = useDispatch<AppDispatch>()
  const { theme, language, sidebarCollapsed } = useSelector((state: RootState) => state.settings)
 
  const changeTheme    = (v: T_Theme)    => dispatch(setTheme(v))
  const changeLanguage = (v: T_Language) => {
    dispatch(setLanguage(v))
    i18n.changeLanguage(v)
  }
  const toggleTheme    = () => changeTheme(theme === 'light' ? 'dark' : 'light')
  const toggleLanguage = () => changeLanguage(language === 'ar' ? 'en' : 'ar')
 
  return {
    theme, language, sidebarCollapsed,
    t, i18n,
    changeTheme, changeLanguage,
    toggleTheme, toggleLanguage,
    dispatch,
  }
}
```
 
---
 
# PART 13: i18n — تعدد اللغات 🌐
 
## Tech Stack
 
```
react-i18next 13   → Hook للترجمة
i18next 23         → المكتبة الأساسية
```
 
---
 
## i18n/config.ts
 
```typescript
/**
 * @file : src/i18n/config.ts
 * @description : ملف اعدادات مكتبة تعدد اللغات
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
import i18n from 'i18next'
import { initReactI18next } from 'react-i18next'
import LanguageDetector from 'i18next-browser-languagedetector'
 
const locales = import.meta.glob('@/i18n/locales/**/*.json', { eager: true }) as Record<string, { default: any }>
const loadTranslation = (lang: 'ar' | 'en') => {
  const file = Object.keys(locales).find((k) => k.includes(`/locales/${lang}/translation.json`))
  return file ? locales[file].default : {}
}
 
const detectLanguage = (): 'ar' | 'en' => {
  const match = window.location.pathname.match(/^\/(ar|en)(\/|$)/)
  if (match) return match[1] as 'ar' | 'en'
  const lang = document.documentElement.lang
  if (lang === 'ar' || lang === 'en') return lang
  return navigator.language.startsWith('ar') ? 'ar' : 'en'
}
 
i18n
  .use(LanguageDetector)
  .use(initReactI18next)
  .init({
    resources    : { en: { common: loadTranslation('en') }, ar: { common: loadTranslation('ar') } },
    fallbackLng  : 'en',
    lng          : detectLanguage(),
    ns           : ['common'],
    defaultNS    : 'common',
    interpolation: { escapeValue: false },
    react        : { useSuspense: false },
  })
 
export default i18n
```
 
---
 
# PART 14: Routing 🛣️
 
## routes/appRouter.tsx
 
```typescript
/**
 * @file : src/routes/appRouter.tsx
 * @description : ملف تهيئة التوجيه في التطبيق
 * @updated : [
 *   { "date": "2026-05-01", "version": "1.0.0", "by": ["BomBa"], "comment": "إنشاء الملف" }
 * ]
 */
 
import { createHashRouter, RouterProvider, Navigate, Outlet } from 'react-router-dom'
import { useEffect, lazy, Suspense } from 'react'
import { useSettings } from '@/hooks/useSettings'
import i18n from '@/i18n/config'
import { LoaderScreen } from '@ui'
 
const Dashboard = lazy(() => import('@/pages/Dashboard'))
const Login     = lazy(() => import('@/pages/Auth/Login'))
const NotFound  = lazy(() => import('@/pages/NotFound'))
 
const LanguageLayout = () => {
  const { language, changeLanguage } = useSettings()
  useEffect(() => {
    if (language && ['ar', 'en'].includes(language) && i18n.language !== language)
      changeLanguage(language)
  }, [language, changeLanguage])
  return <Outlet />
}
 
const router = createHashRouter([
  { path: '/', element: <Navigate to={`/${i18n.language}/dashboard`} replace /> },
  {
    path    : '/:lang',
    element : <LanguageLayout />,
    children: [
      { path: 'dashboard', element: <Suspense fallback={<LoaderScreen />}><Dashboard /></Suspense> },
      { path: 'login',     element: <Suspense fallback={<LoaderScreen />}><Login /></Suspense> },
      { path: '*',         element: <NotFound /> },
    ],
  },
])
 
export const AppRouter = () => <RouterProvider router={router} />
```
 
---
 
# PART 15: Icons System 🎨
 
## القاعدة الذهبية
 
```
✅ Icon prefix إلزامي دائماً — في icons.ts وفي الاستخدام
❌ الأسماء الأصلية ممنوعة
```
 
```typescript
// ✅ صح
import { IconSun, IconUser } from '@icons'
<IconSun className="w-5 h-5 text-py" />
 
// ❌ خطأ — استيراد مباشر
import { Sun } from 'lucide-react'
```
 
---
 
# PART 16: Backend Architecture 🖥️
 
## Tech Stack
 
```
Runtime    : Node.js 20 LTS
Framework  : Express + TypeScript
Validation : Zod
Database   : Drizzle ORM + Raw SQL → (SQLite/PostgreSQL)
Cache      : Redis (optional)
Queue      : RabbitMQ (optional)
```
 
---
 
## الهيكل
 
```
apps/app-server/
├── src/
│   ├── modules/
│   │   └── [name]/
│   │       ├── [name].controller.ts
│   │       ├── [name].service.ts
│   │       ├── [name].repository.ts
│   │       ├── [name].routes.ts
│   │       ├── [name].types.ts
│   │       ├── [name].validation.ts
│   │       └── [name].test.ts
│   ├── common/
│   │   ├── errors.constants.ts
│   │   ├── AppError.ts
│   │   ├── errorHandler.ts
│   │   └── logger.ts
│   ├── config/
│   │   ├── env.ts
│   │   ├── database.ts
│   │   └── redis.ts
│   ├── middlewares/
│   │   ├── auth.middleware.ts
│   │   ├── validation.middleware.ts
│   │   └── errorHandler.middleware.ts
│   ├── utils/
│   │   └── format-date.ts
│   └── server.ts
├── drizzle/
│   └── migrations/
├── package.json
├── tsconfig.json
├── drizzle.config.ts
└── .env
```
 
---
 
## نمط Module — Controller / Service / Repository
 
```typescript
// ─── controller.ts → HTTP فقط ────────────────
export const UsersController = {
  getAll: async (req: Request, res: Response, next: NextFunction) => {
    try {
      const users = await UsersService.getAll()
      const response: I_ApiResponse<I_UserResponse[]> = { success: true, data: users }
      res.json(response)
    } catch (error) { next(error) }
  },
  create: async (req: Request, res: Response, next: NextFunction) => {
    try {
      const dto: I_CreateUserDTO = CreateUserSchema.parse(req.body)
      const user = await UsersService.create(dto)
      res.status(201).json({ success: true, data: user })
    } catch (error) { next(error) }
  },
}
 
// ─── service.ts → Business Logic + Cache ─────
export const UsersService = {
  getAll: async (): Promise<I_UserResponse[]> => {
    const cached = await redis?.get('users:all')
    if (cached) return JSON.parse(cached)
    const users = await UsersRepository.findAll()
    await redis?.setex('users:all', 300, JSON.stringify(users))
    return users
  },
  create: async (dto: I_CreateUserDTO): Promise<I_UserResponse> => {
    const exists = await UsersRepository.findByEmail(dto.email)
    if (exists) throw new AppError(ERR.USER.ALREADY_EXISTS)
    const user = await UsersRepository.create(dto)
    await redis?.del('users:all')
    return user
  },
}
 
// ─── repository.ts → Database فقط ────────────
export const UsersRepository = {
  findAll     : async () => db.select().from(users),
  findById    : async (id: string) => {
    const [u] = await db.select().from(users).where(eq(users.id, id))
    return u || null
  },
  findByEmail : async (email: string) => {
    const [u] = await db.select().from(users).where(eq(users.email, email))
    return u || null
  },
  create      : async (data: I_CreateUserDTO) => {
    const [u] = await db.insert(users).values(data).returning()
    return u
  },
  getStats    : async () =>
    db.execute(`
      SELECT u.id, COUNT(t.id) as tasks
      FROM users u LEFT JOIN tasks t ON t.user_id = u.id
      GROUP BY u.id
    `),
}
```
 
---
 
# PART 17: API Design — REST & GraphQL 📡
 
## متى REST ومتى GraphQL؟
 
```
REST    → Auth | File Upload | Webhooks | Public API
GraphQL → Dashboard | Complex Queries | Real-time Data
```
 
---
 
## API Response — موحد دائماً
 
```typescript
// ✅ Success
res.json({ success: true, data: result })
 
// ✅ Created
res.status(201).json({ success: true, data: result })
 
// ✅ Error
res.status(400).json({
  success: false, data: null, message: error.message,
  error: { code: 'ERR_CODE' },
})
 
// ✅ Paginated
res.json({
  success: true, data: results,
  pagination: { page: 1, limit: 20, total: 100, pages: 5 },
})
```
 
---
 
## Axios + TanStack Query
 
```typescript
// services/api.ts
export const api = axios.create({ baseURL: env.API_URL, timeout: 10_000 })
 
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})
 
api.interceptors.response.use(
  (response) => response.data,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token')
      window.location.href = '/login'
    }
    return Promise.reject(error.response?.data || error)
  }
)
 
// استخدام TanStack Query
const { data: users, isLoading } = useQuery({
  queryKey : ['users'],
  queryFn  : usersRepository.getAll,
  staleTime: 60_000,
})
```
 
---
 
# PART 18: Error Handling 🚨
 
## common/errors.constants.ts
 
```typescript
export const ERR = {
  AUTH: {
    INVALID_TOKEN  : { code: 'AUTH_001', status: 401, message: 'التوكن مش صالح' },
    EXPIRED_TOKEN  : { code: 'AUTH_002', status: 401, message: 'التوكن انتهت صلاحيته' },
    UNAUTHORIZED   : { code: 'AUTH_003', status: 403, message: 'مش مسموح' },
    INVALID_CREDS  : { code: 'AUTH_004', status: 401, message: 'بيانات دخول غلط' },
  },
  USER: {
    NOT_FOUND      : { code: 'USR_001', status: 404, message: 'المستخدم مش موجود' },
    ALREADY_EXISTS : { code: 'USR_002', status: 409, message: 'المستخدم موجود بالفعل' },
    INVALID_DATA   : { code: 'USR_003', status: 400, message: 'بيانات غير صالحة' },
  },
  FILE: {
    TOO_LARGE      : { code: 'FILE_001', status: 413, message: 'الملف كبير أوي' },
    INVALID_TYPE   : { code: 'FILE_002', status: 415, message: 'نوع الملف مش مدعوم' },
  },
  DB: {
    CONNECTION_FAILED: { code: 'DB_001', status: 500, message: 'فشل الاتصال بقاعدة البيانات' },
    QUERY_ERROR      : { code: 'DB_002', status: 500, message: 'خطأ في الاستعلام' },
  },
} as const
```
 
---
 
## middlewares/errorHandler.middleware.ts
 
```typescript
export const errorHandler = (
  err: Error | AppError,
  req: Request,
  res: Response,
  next: NextFunction
) => {
  logger.error({ message: err.message, stack: err.stack, path: req.path })
 
  if (err instanceof AppError)
    return res.status(err.status).json({
      success: false, data: null,
      message: err.message,
      error  : { code: err.code },
    })
 
  if (err.name === 'ZodError')
    return res.status(400).json({
      success: false, data: null,
      message: 'بيانات غير صالحة',
      error  : { code: 'VALIDATION_ERROR', details: (err as any).errors },
    })
 
  return res.status(500).json({
    success: false, data: null,
    message: 'حصل خطأ في السيرفر',
    error  : { code: 'INTERNAL_ERROR' },
  })
}
```
 
---
 
# PART 19: Security 🔒
 
## Security Checklist
 
```markdown
□ SQL Injection → Parameterized queries (Drizzle)
□ XSS → Sanitize input (DOMPurify)
□ CSRF → SameSite cookies
□ Secrets → .env فقط — لا secrets في الكود
□ Dependencies → npm audit في CI/CD
□ HTTPS → إلزامي في Production
□ Passwords → bcrypt cost factor 12+
□ Rate Limit → على كل Auth routes
□ CORS → Origins محددة فقط
□ Headers → Helmet
```
 
---
 
# PART 20: Performance Optimization ⚡
 
## Frontend
 
```typescript
// Code Splitting
const Dashboard = lazy(() => import('@/pages/Dashboard'))
 
// Memoization
export const UserCard = memo<UserCardProps>(({ user, onDelete }) => {
  const fullName = useMemo(
    () => `${user.firstName} ${user.lastName}`,
    [user.firstName, user.lastName]
  )
  return <div><h3>{fullName}</h3></div>
})
 
// Parallel Requests
const [user, posts] = await Promise.all([getUser(), getPosts()])
```
 
## Backend
 
```typescript
// Redis Caching
const cached = await redis?.get(CACHE_KEY)
if (cached) return JSON.parse(cached)
const data = await Repository.findAll()
await redis?.setex(CACHE_KEY, TTL, JSON.stringify(data))
 
// Avoid N+1
const posts = await db.select().from(posts).leftJoin(users, eq(posts.userId, users.id))
```
 
## Web Vitals
 
```
LCP < 2.5s   FID < 100ms   CLS < 0.1
```
 
---
 
# PART 21: Testing ✅
 
## Coverage Threshold
 
```json
{
  "coverageThreshold": {
    "global": { "branches": 70, "functions": 80, "lines": 80 }
  }
}
```
 
## نمط Unit Test
 
```typescript
describe('UsersService', () => {
  describe('getAll', () => {
    it('يرجع list من الـ cache لو موجود', async () => {
      ;(redis.get as jest.Mock).mockResolvedValue(JSON.stringify(mockUsers))
      const result = await UsersService.getAll()
      expect(result).toEqual(mockUsers)
      expect(UsersRepository.findAll).not.toHaveBeenCalled()
    })
  })
})
```
 
---
 
# PART 22: Accessibility ♿
 
## Checklist
 
```markdown
□ Semantic HTML → <header>, <main>, <nav>, <article>
□ ARIA → aria-label, aria-describedby, role
□ Keyboard Navigation → Tab order صحيح
□ Color Contrast → WCAG AA (4.5:1)
□ Alt Text → لكل صورة
□ Labels → htmlFor في كل Label
□ Focus → outline واضح
```
 
---
 
# PART 23: Git Workflow 📝
 
## Commit Format
 
```
<emoji> <type>(<scope>): <description>
```
 
 
| Emoji | Type     | متى              |
| ----- | -------- | ---------------- |
| ✨     | feat     | Feature جديدة    |
| 🐛    | fix      | Bug fix          |
| 📝    | docs     | Documentation    |
| ♻️    | refactor | Restructure      |
| ✅     | test     | Tests            |
| 🔧    | chore    | Config           |
| ⚡     | perf     | Performance      |
| 🔒    | security | Security fix     |
| 🗃️   | db       | Migration/Schema |
| 🏗️   | arch     | Architecture     |
 
 
```bash
✨ feat(auth): add JWT refresh token rotation
🐛 fix(cart): correct total price for bundled items
🗃️ db(users): add email_verified_at column
♻️ refactor(BUI-2): improve Input2 props flexibility
```
 
---
 
# PART 24: Timestamps & UTC ⏰
 
```typescript
// Backend: TIMESTAMPTZ في (SQLite/PostgreSQL) دائماً
// API Response: ISO 8601 → "2026-01-08T12:30:00.000Z"
// Frontend: تحويل لـ Local Time
 
import { formatDate } from '@/utils/format-date'
<p>{formatDate.toLocal(user.createdAt)}</p>       // "08/01/2026 14:30"
<p>{formatDate.relative(user.createdAt, 'ar')}</p> // "منذ 5 دقائق"
```
 
---
 
# PART 25: Electron Development 🖥️
 
```typescript
// Main Process → BrowserWindow + IPC Handlers
// Preload → contextBridge.exposeInMainWorld('electronAPI', { ... })
// Renderer → window.electronAPI.getAppVersion()
// Router → createHashRouter (لدعم Electron)
```
 
---
 
# PART 26: Third-Party Integration 🔌
 
## قواعد اختيار المكتبة
 
```markdown
□ آخر تحديث < 6 شهور
□ Downloads > 10k/week
□ TypeScript built-in
□ Bundle Size < 50kb
□ Tree Shakeable
□ License: MIT | Apache 2.0
```
 
---
 
# PART 27: Master Checklists ✅
 
## قبل بناء أي مشروع
 
```markdown
□ أجبت على الـ 6 أسئلة؟ (PART 4)
□ الخدمات المضافة ضرورية الآن؟
□ الملفات الثلاثة موجودة؟ (AI_CONTEXT + AI_SESSION + TODO)
□ .env.example موجود؟
□ docker-compose.yml صح؟
□ packages/types موجودة؟
□ globals.css فيه @theme + CSS Variables + B: utilities؟
```
 
---
 
## قبل كتابة أي Backend Module
 
```markdown
□ controller → routes فقط
□ service → business logic + cache
□ repository → database فقط
□ validation → Zod schemas
□ types → من @shared/types أو محلية
□ API Response → موحد { success, data, message }
□ Error codes → من ERR constants
□ Tests → unit + integration
```
 
---
 
## قبل كتابة أي Frontend Component
 
```markdown
□ الطبقة الصح؟ (BUI-1 → BUI-2 → BUI-O → صفحة)
□ buildProps مستخدمة؟
□ interface يمتد من HTML الأصلي؟
□ ...restProps في النهاية؟
□ classGroup/classLabel بدل className متعددة؟
□ الأيقونات بـ Icon prefix؟
□ الاستيراد من @a وليس مباشرة؟
□ JSDoc بالعربية؟
□ Accessibility (aria, htmlFor)؟
□ مضاف لـ alias/ui.ts؟
□ Tailwind classes بالترتيب الصحيح؟
□ الألوان من CSS Variables (bg-py / text-te / ...)?
□ Shadow → B:shadow-* | Radius → B:rounded-* | Transition → B:transition-*؟
□ Types من @shared/types؟
```
 
---
 
## قبل أي Commit
 
```markdown
□ الكود يعمل محلياً؟
□ npm run lint يمر؟
□ npm run test يمر؟
□ Commit message بالصيغة الصحيحة؟
□ AI_SESSION.md اتحدث؟
□ Migration موجودة لو في تغيير DB؟
```
 
---
 
# PART 28: Glossary — قاموس المصطلحات 📚
 
 
| المصطلح           | المعنى                                              |
| ----------------- | --------------------------------------------------- |
| **Alias**         | نظام الاستيراد المركزي                              |
| **BUI**           | BomBa UI — نظام المكونات                            |
| **BUI-1**         | HTML wrappers — بدون منطق                           |
| **BUI-2**         | UI Components — مع state وTailwind classes          |
| **BUI-O**         | Compound Components (Modal, Panel)                  |
| **buildProps**    | دالة تنظيف className/style                          |
| **globals.css**   | ملف الـ CSS الرئيسي — @theme + Variables + B: utils |
| **@theme**        | تسجيل الـ scale والألوان في Tailwind 4              |
| **B: prefix**     | Custom Utilities خاصة بـ BomBa System               |
| **em**            | وحدة القياس الأساسية في كل الـ spacing/font/radius  |
| **CSS Variables** | نظام الألوان والثيم — مصدر الحقيقة الوحيد           |
| **shared-types**  | حزمة الأنواع المشتركة في packages/types             |
| **DTO**           | Data Transfer Object                                |
| **T prefix**      | Type Alias مخصص                                     |
| **I prefix**      | Interface مخصص                                      |
| **ERR**           | Error Constants                                     |
| **Drizzle**       | ORM للـ (SQLite/PostgreSQL)                         |
| **Persist**       | Redux Persist                                       |
| **TTL**           | Time To Live — مدة صلاحية الـ Cache                 |
| **UTC**           | التوقيت العالمي الموحد                              |
 
 
---
 
## 🚫 ممنوعات عامة
 
```typescript
// ❌ HTML مباشر في BUI-2 أو أعلى
// ❌ any في TypeScript
// ❌ Props مغلقة بدون extends
// ❌ className بدون buildProps
// ❌ تخطي طبقات BUI
// ❌ استيراد مباشر في الصفحات (بدون @alias)
// ❌ أيقونة بدون Icon prefix
// ❌ Business Logic في Controller
// ❌ Secrets في الكود
// ❌ Sequential awaits لو ممكن Parallel
// ❌ إضافة خدمة مش ضرورية مبكراً
// ❌ hardcoded colors في Tailwind → استخدم CSS Variables
// ❌ dark: prefix في Tailwind → Variables تتغير تلقائياً
// ❌ arbitrary values للقياسات → الـ @theme بيتكفل بالـ em
// ❌ inline style للـ shadow/radius → استخدم B:shadow-* / B:rounded-*
// ❌ tailwind.config.js في Tailwind 4 → استخدم @theme في globals.css
// ❌ padding-left/right → استخدم padding-inline-start/end
// ❌ نفس الـ type في أكتر من مكان → packages/types هو المصدر الوحيد
```
 
---
 
## 🎯 كيفية الاستخدام
 
```markdown
┌─────────────────────────────────────────────┐
│ الملفات المطلوبة في كل مشروع:              │
│                                             │
│ AGENTS.md     → System Prompt الكامل        │
│ AI_CONTEXT.md → Context ثابت للمشروع        │
│ AI_SESSION.md → آخر session                 │
│ TODO.md       → الأولويات                   │
└─────────────────────────────────────────────┘
 
عند بدء محادثة جديدة:
──────────────────────
"اقرأ AGENTS.md ثم AI_CONTEXT.md ثم AI_SESSION.md
وابدأ من حيث وقفنا"
 
عند بدء مشروع جديد:
─────────────────────
"اتبع BomBa System واسألني الـ 6 أسئلة قبل البدء"
```
