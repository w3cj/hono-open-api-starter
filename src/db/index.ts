import { drizzle } from "drizzle-orm/libsql";

import env from "@/env.ts";

import * as schema from "./schema.ts";

const db = drizzle({
  connection: {
    url: env.DATABASE_URL,
    authToken: env.DATABASE_AUTH_TOKEN,
  },
  casing: "snake_case",
  schema,
});

export default db;
