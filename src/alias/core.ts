/**
 * @file        : src/alias/core.ts
 * @description : استيرادات النواة — Hono وZod ومساعدات Drizzle. أي مكتبة خارجية جديدة بتتصدّر من هنا قبل أول استخدام (ADR-010).
 * @updated     : [
 *   { "date": "2026-10-10", "version": "1.0.0", "by": ["Arena Agent"], "comment": "إنشاء الملف" }
 * ]
 */

// ─────────────────────────────────────────────
// 🌐 Hono — الـ HTTP framework
// ─────────────────────────────────────────────
export { Hono } from 'hono';
export type { Context, MiddlewareHandler, Next } from 'hono';

// ─────────────────────────────────────────────
// ✅ Zod — التحقق من كل مدخل خارجي
// ─────────────────────────────────────────────
export { z } from 'zod';

// ─────────────────────────────────────────────
// 🗃️ Drizzle — المصنع والمساعدات (Postgres فقط، ADR-002)
// ─────────────────────────────────────────────
export { drizzle } from 'drizzle-orm/postgres-js';
export {
  and,
  asc,
  desc,
  eq,
  inArray,
  isNotNull,
  isNull,
  not,
  or,
  sql,
} from 'drizzle-orm';
