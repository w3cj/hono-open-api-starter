import { config } from "dotenv";
import { expand } from "dotenv-expand";
import { defineConfig } from "drizzle-kit";
import path from "node:path";

import env from "@/env-runtime";

expand(config({
  path: path.resolve(
    process.cwd(),
    // eslint-disable-next-line node/no-process-env
    process.env.NODE_ENV === "test" ? ".env.test" : ".env",
  ),
}));

export default defineConfig({
  schema: "./src/db/schema.ts",
  out: "./src/db/migrations",
  dialect: "turso",
  casing: "snake_case",
  dbCredentials: {
    url: env.DATABASE_URL,
    authToken: env.DATABASE_AUTH_TOKEN,
  },
});
