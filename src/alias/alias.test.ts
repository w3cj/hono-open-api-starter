/**
 * @file        : src/alias/alias.test.ts
 * @description : اختبارات سطح `@a` — بتتأكد إن المكتبات الخارجية بتوصل شغالة من الـ alias بس (ADR-010)، وكمان بتأكد إن مسارات `@a` و`@/*` بتشتغل وقت الاختبار.
 * @updated     : [
 *   { "date": "2026-10-10", "version": "1.0.0", "by": ["Arena Agent"], "comment": "إنشاء الملف" }
 * ]
 */

import { describe, expect, test } from 'bun:test';

import {
  Hono,
  and,
  bcrypt,
  betterAuth,
  desc,
  drizzle,
  eq,
  inArray,
  isNotNull,
  isNull,
  not,
  or,
  pino,
  postgres,
  sql,
  z,
} from '@a';
import { Hono as HonoFromSrcPath } from '@/alias/core';

describe('سطح @a العام', () => {
  test('المكتبات والمساعدات المطلوبة كلها متاحة من @a', () => {
    // بنراجع السطح كله في حاوية واحدة: أي اسم اتشال من الـ alias هيوقع الاختبار ده
    const exportedSurface = [
      Hono,
      z,
      drizzle,
      postgres,
      pino,
      betterAuth,
      bcrypt,
      eq,
      and,
      or,
      not,
      sql,
      desc,
      inArray,
      isNull,
      isNotNull,
    ];

    for (const item of exportedSurface) {
      expect(item).toBeDefined();
    }

    // المساعدات لازم تبقى callable عشان م umiejęش يتبدل بقيم فاضية
    expect(typeof eq).toBe('function');
    expect(typeof sql).toBe('function');
  });

  test('مسار @a ومسار @/* بيوصلوا لنفس الوحدة', () => {
    // لو tsconfig paths اتكسرت، الاستيراد التاني هيقع أو هيجيب نسخة تانية
    expect(HonoFromSrcPath).toBe(Hono);
  });
});

describe('سلوك المكتبات عبر الـ alias', () => {
  test('Hono بيرد على طلب HTTP بشكل سليم', async () => {
    const app = new Hono();
    app.get('/health', (context) => context.json({ status: 'ok' }));

    const response = await app.request('/health');

    expect(response.status).toBe(200);
    expect(await response.json()).toEqual({ status: 'ok' });
  });

  test('Zod بيقبل البيانات السليمة ويرفض الغلط', () => {
    const schema = z.object({ name: z.string().min(1) });

    expect(schema.safeParse({ name: 'bun' }).success).toBe(true);
    expect(schema.safeParse({ name: '' }).success).toBe(false);
  });

  test('bcrypt وbetterAuth وصلوا بواجهاتهم المطلوبة', () => {
    expect(typeof bcrypt.hash).toBe('function');
    expect(typeof bcrypt.compare).toBe('function');
    expect(typeof betterAuth).toBe('function');
  });
});
