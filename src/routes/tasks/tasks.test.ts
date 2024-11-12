/* eslint-disable ts/ban-ts-comment */
import { testClient } from "hono/testing";
import * as HttpStatusPhrases from "stoker/http-status-phrases";
import { ZodIssueCode } from "zod";
import { expect } from "@std/expect";

import env from "@/env.ts";
import { ZOD_ERROR_CODES, ZOD_ERROR_MESSAGES } from "@/lib/constants.ts";
import createApp from "@/lib/create-app.ts";

import router from "./tasks.index.ts";
import { removeTestDb, startTestDB, stopTestDB } from "@/lib/test-helpers.ts";

if (env.NODE_ENV !== "test") {
  throw new Error("NODE_ENV must be 'test'");
}

const client = testClient(createApp().route("/", router));

Deno.test("tasks routes", async (t) => {
  await removeTestDb();
  const testDbProcess = await startTestDB();
  await t.step("post /tasks validates the body when creating", async () => {
    const response = await client.tasks.$post({
      // @ts-expect-error test-data
      json: {
        done: false,
      },
    });
    expect(response.status).toBe(422);
    if (response.status === 422) {
      const json = await response.json();
      expect(json.error.issues[0].path[0]).toBe("name");
      expect(json.error.issues[0].message).toBe(ZOD_ERROR_MESSAGES.REQUIRED);
    }
  });

  const id = "1";
  const name = "Learn vitest";

  await t.step("post /tasks creates a task", async () => {
    const response = await client.tasks.$post({
      json: {
        name,
        done: false,
      },
    });
    expect(response.status).toBe(200);
    if (response.status === 200) {
      const json = await response.json();
      expect(json.name).toBe(name);
      expect(json.done).toBe(false);
    }
  });

  await t.step("get /tasks lists all tasks", async () => {
    const response = await client.tasks.$get();
    expect(response.status).toBe(200);
    if (response.status === 200) {
      const json = await response.json();
      expect(Array.isArray(json)).toBe(true);
      expect(json.length).toBe(1);
    }
  });

  await t.step("get /tasks/{id} validates the id param", async () => {
    const response = await client.tasks[":id"].$get({
      param: {
        id: "wat",
      },
    });
    expect(response.status).toBe(422);
    if (response.status === 422) {
      const json = await response.json();
      expect(json.error.issues[0].path[0]).toBe("id");
      expect(json.error.issues[0].message).toBe(
        ZOD_ERROR_MESSAGES.EXPECTED_NUMBER,
      );
    }
  });

  await t.step("get /tasks/{id} returns 404 when task not found", async () => {
    const response = await client.tasks[":id"].$get({
      param: {
        id: "999",
      },
    });
    expect(response.status).toBe(404);
    if (response.status === 404) {
      const json = await response.json();
      expect(json.message).toBe(HttpStatusPhrases.NOT_FOUND);
    }
  });

  await t.step("get /tasks/{id} gets a single task", async () => {
    const response = await client.tasks[":id"].$get({
      param: {
        id,
      },
    });
    expect(response.status).toBe(200);
    if (response.status === 200) {
      const json = await response.json();
      expect(json.name).toBe(name);
      expect(json.done).toBe(false);
    }
  });

  await t.step(
    "patch /tasks/{id} validates the body when updating",
    async () => {
      const response = await client.tasks[":id"].$patch({
        param: {
          id,
        },
        json: {
          name: "",
        },
      });
      expect(response.status).toBe(422);
      if (response.status === 422) {
        const json = await response.json();
        expect(json.error.issues[0].path[0]).toBe("name");
        expect(json.error.issues[0].code).toBe(ZodIssueCode.too_small);
      }
    },
  );

  await t.step("patch /tasks/{id} validates the id param", async () => {
    const response = await client.tasks[":id"].$patch({
      param: {
        id: "wat",
      },
      json: {},
    });
    expect(response.status).toBe(422);
    if (response.status === 422) {
      const json = await response.json();
      expect(json.error.issues[0].path[0]).toBe("id");
      expect(json.error.issues[0].message).toBe(
        ZOD_ERROR_MESSAGES.EXPECTED_NUMBER,
      );
    }
  });

  await t.step("patch /tasks/{id} validates empty body", async () => {
    const response = await client.tasks[":id"].$patch({
      param: {
        id,
      },
      json: {},
    });
    expect(response.status).toBe(422);
    if (response.status === 422) {
      const json = await response.json();
      expect(json.error.issues[0].code).toBe(ZOD_ERROR_CODES.INVALID_UPDATES);
      expect(json.error.issues[0].message).toBe(ZOD_ERROR_MESSAGES.NO_UPDATES);
    }
  });

  await t.step(
    "patch /tasks/{id} updates a single property of a task",
    async () => {
      const response = await client.tasks[":id"].$patch({
        param: {
          id,
        },
        json: {
          done: true,
        },
      });
      expect(response.status).toBe(200);
      if (response.status === 200) {
        const json = await response.json();
        expect(json.done).toBe(true);
      }
    },
  );

  await t.step(
    "delete /tasks/{id} validates the id when deleting",
    async () => {
      const response = await client.tasks[":id"].$delete({
        param: {
          id: "wat",
        },
      });
      expect(response.status).toBe(422);
      if (response.status === 422) {
        const json = await response.json();
        expect(json.error.issues[0].path[0]).toBe("id");
        expect(json.error.issues[0].message).toBe(
          ZOD_ERROR_MESSAGES.EXPECTED_NUMBER,
        );
      }
    },
  );

  await t.step("delete /tasks/{id} removes a task", async () => {
    const response = await client.tasks[":id"].$delete({
      param: {
        id,
      },
    });
    expect(response.status).toBe(204);
  });

  await stopTestDB(testDbProcess);
});
