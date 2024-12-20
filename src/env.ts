/* eslint-disable no-console */
/* eslint-disable node/no-process-env */
import type { ZodError } from "zod";

import { z } from "zod";

const envSchema = z.object({
  NODE_ENV: z.enum(["development", "test", "production"]).default("development"),
  PORT: z.coerce.number().positive().max(65536, `PORT should be >= 0 and < 65536`),
  LOG_LEVEL: z.enum(["fatal", "error", "warn", "info", "debug", "trace", "silent"]),
  DATABASE_URL: z
    .string({
      description: "DB Connection string",
      required_error: "😱 You forgot to add Database URL",
    })
    .min(5),
  DATABASE_AUTH_TOKEN: z.string().optional(),
});

const parsedEnv = envSchema.safeParse({
  PORT: process.env.PORT,
  NODE_ENV: process.env.NODE_ENV,
  LOG_LEVEL: process.env.LOG_LEVEL,
  DATABASE_URL: process.env.DATABASE_URL,
  DATABASE_AUTH_TOKEN: process.env.DATABASE_AUTH_TOKEN,
});

function prettyPrintErrors(errors: ZodError) {
  const formattedError = errors.flatten().fieldErrors;
  Object.entries(formattedError).forEach(([key, value]) => {
    console.log(`${key}:`);
    if (Array.isArray(value)) {
      value.forEach((errorMessage: string) => {
        console.log(`  - ${errorMessage}`);
      });
    }
  });
}

if (!parsedEnv.success) {
  console.log("------------------------------------------------");
  console.log("There is an error with the environment variables");
  console.log("------------------------------------------------");
  console.log(prettyPrintErrors(parsedEnv.error));
  process.exit(1);
}

const env = parsedEnv.data;

export default env;
