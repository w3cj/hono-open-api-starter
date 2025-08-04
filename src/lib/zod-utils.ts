import type { z } from "@hono/zod-openapi";
import type { z as z4 } from "zod/v4";

export function toZodV4SchemaTyped<T extends z4.ZodTypeAny>(
  schema: T,
) {
  return schema as unknown as z.ZodType<z4.infer<T>>;
}
