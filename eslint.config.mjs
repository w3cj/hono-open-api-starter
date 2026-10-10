/**
 * @file        : eslint.config.mjs
 * @description : ESLint flat config للـ Backend — قواعد TypeScript الصارمة، وحماية استيرادات `@a` (ADR-010)، وتنسيق Prettier بلا تعارض.
 * @updated     : [
 *   { "date": "2026-10-10", "version": "1.0.0", "by": ["Arena Agent"], "comment": "إنشاء الملف" }
 * ]
 */

import js from '@eslint/js';
import globals from 'globals';
import tseslint from 'typescript-eslint';
import prettier from 'eslint-config-prettier';

// ─────────────────────────────────────────────
// 🔒 المكتبات الخارجية — استيرادها لازم يمر من `@a` بس (ADR-010)
// ─────────────────────────────────────────────
const externalLibraries = [
  'bcrypt',
  'better-auth',
  'drizzle-orm',
  'hono',
  'pino',
  'postgres',
  'zod',
];

const restrictedImportMessage =
  'المكتبات الخارجية بتتستورد من `@a` بس (ADR-010) — عدّل الاستيراد لأ `@a`، أو صدّر الاسم في src/alias لو جديد.';

const tsFiles = ['**/*.ts', '**/*.mts', '**/*.cts'];

export default tseslint.config(
  // ─── 🧹 نطاق الفحص ───
  {
    ignores: [
      'node_modules/**',
      'dist/**',
      'coverage/**',
      'docs/**',
      'scripts/**',
    ],
  },

  // ─── 📦 ملفات JS/MJS (إعدادات وأدوات) ───
  {
    files: ['**/*.js', '**/*.mjs', '**/*.cjs'],
    languageOptions: {
      globals: { ...globals.node },
    },
    rules: {
      ...js.configs.recommended.rules,
      eqeqeq: ['error', 'always'],
      'no-eval': 'error',
      'no-new-func': 'error',
      'no-unused-vars': [
        'error',
        {
          argsIgnorePattern: '^_',
          varsIgnorePattern: '^_',
          caughtErrorsIgnorePattern: '^_',
          destructuredArrayIgnorePattern: '^_',
          ignoreRestSiblings: true,
        },
      ],
    },
  },

  // ─── 🧠 TypeScript — قواعد صارمة ───
  ...tseslint.configs.recommended.map((config) => ({
    ...config,
    files: tsFiles,
  })),
  {
    files: tsFiles,
    rules: {
      'no-undef': 'off',
      'no-unused-vars': 'off',
      '@typescript-eslint/no-explicit-any': 'error',
      '@typescript-eslint/no-unused-vars': [
        'error',
        {
          argsIgnorePattern: '^_',
          varsIgnorePattern: '^_',
          caughtErrorsIgnorePattern: '^_',
          destructuredArrayIgnorePattern: '^_',
          ignoreRestSiblings: true,
        },
      ],
      '@typescript-eslint/consistent-type-imports': [
        'error',
        { prefer: 'type-imports', fixStyle: 'separate-type-imports' },
      ],
      'no-restricted-imports': [
        'error',
        {
          patterns: [
            {
              group: externalLibraries.flatMap((lib) => [lib, `${lib}/**`]),
              message: restrictedImportMessage,
            },
          ],
        },
      ],
      eqeqeq: ['error', 'always'],
      'no-eval': 'error',
      'no-new-func': 'error',
    },
  },

  // ─── 🔓 ملفات الـ alias نفسها مسموح لها تستورد المكتبات مباشرة (ADR-010) ───
  {
    files: ['src/alias/**/*.ts'],
    rules: {
      'no-restricted-imports': 'off',
    },
  },

  // ─── 🎨 Prettier عشان يطفّي القواعد المتعارضة على التنسيق ───
  prettier,

  // ─── 🔁 قواعد إلزامية بعد Prettier — `curly` بيتصنّف special عندهم وبيتسدّد، والقواعد بتطلبه بصيغة "all" (ARCHITECTURE §18) ───
  {
    rules: {
      curly: ['error', 'all'],
    },
  },
);
