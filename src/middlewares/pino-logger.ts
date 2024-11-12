import { pinoLogger as logger } from "hono-pino";
import pino from "pino";
import pretty from "pino-pretty";

import env from "@/env.ts";

export function pinoLogger() {
  return logger({
    // @ts-expect-error pino is a node library / types not compatible
    pino: pino({
      level: env.LOG_LEVEL || "info",
    }, env.NODE_ENV === "production" ? undefined : pretty()),
    http: {
      reqId: () => crypto.randomUUID(),
    },
  });
}
