/**
 * @file        : src/alias/libs.ts
 * @description : المكتبات الخارجية الداعمة — عميل PostgreSQL وPino وBetter Auth وbcrypt. الاستيراد دايماً من `@a` مش مباشرة (ADR-010).
 * @updated     : [
 *   { "date": "2026-10-10", "version": "1.0.0", "by": ["Arena Agent"], "comment": "إنشاء الملف" }
 * ]
 */

// ─────────────────────────────────────────────
// 🐘 postgres.js — عميل PostgreSQL (مش Turso/libSQL، ADR-002)
// ─────────────────────────────────────────────
export { default as postgres } from 'postgres';
export type { Sql as PostgresSql } from 'postgres';

// ─────────────────────────────────────────────
// 📝 Pino — لوجز JSON على stdout (ADR-020)
// ─────────────────────────────────────────────
export { pino } from 'pino';
export type { Logger } from 'pino';

// ─────────────────────────────────────────────
// 🔐 Better Auth — الهوية والجلسات فقط (ADR-006 · ADR-009)
// minimal mode بدون Kysely؛ الربط بـ Drizzle adapter هيتأكد في 3.1 (CL-01)
// ─────────────────────────────────────────────
export { betterAuth } from 'better-auth/minimal';
export type { BetterAuthOptions } from 'better-auth/minimal';

// ─────────────────────────────────────────────
// 🔒 bcrypt — التشفير من خلال AuthService فقط، cost 12 (ADR-008 · CL-02)
// ─────────────────────────────────────────────
export { default as bcrypt } from 'bcrypt';
