import { createClient } from "@libsql/client";
import { drizzle } from "drizzle-orm/libsql";

import type { Environment } from "@/env";

import * as schema from "./schema";

export function createDb(env: Environment) {
  const client = createClient({
    url: env.DATABASE_URL,
    authToken: env.DATABASE_AUTH_TOKEN,
  });

  const db = drizzle(client, {
    schema,
  });

  return { db, client };
}
