import env from "@/env.ts";

export const removeTestDb = async () => {
  try {
    const cleanUp = new Deno.Command("rm", {
      cwd: Deno.cwd(),
      args: ["test.db", "test.db-shm", "test.db-wal"],
    }).spawn();
    await cleanUp.status;
    // deno-lint-ignore no-empty
  } catch {}
};

export const startTestDB = async (): Promise<Deno.ChildProcess> => {
  const testDbProcess = new Deno.Command("turso", {
    args: ["dev", "-p", "8181", "--db-file", "test.db"],
  }).spawn();
  // wait for process to spin up before pushing schema
  await new Promise((resolve) => setTimeout(resolve, 1000));

  const pushDB = new Deno.Command("deno", {
    args: ["task", "db:push:test"],
  }).spawn();
  await pushDB.status;

  return new Promise((resolve) => {
    const healthCheck = async () => {
      try {
        const response = await fetch(env.DATABASE_URL, {
          method: "POST",
          body: JSON.stringify({ "statements": ["select * from tasks"] }),
        });
        const json = await response.json();
        if (json[0].results) {
          console.log("DB available!");
          resolve(testDbProcess);
        } else {
          setTimeout(healthCheck, 1000);
        }
      } catch {
        console.log("Waiting for DB...");
        setTimeout(healthCheck, 1000);
      }
    };

    healthCheck();
  });
};

export const stopTestDB = (testDbProcess: Deno.ChildProcess) => {
  return new Promise((resolve) => {
    const cleanup = async () => {
      console.log("Cleaning up...");
      try {
        testDbProcess.kill();
        await testDbProcess.status;
        // deno-lint-ignore no-empty
      } catch {}
      await removeTestDb();
      resolve(true);
    };

    setTimeout(cleanup, 500);
  });
};
