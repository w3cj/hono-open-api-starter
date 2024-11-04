# Hono Open API Starter

A starter template for building fully documented type-safe JSON APIs with Hono and Open API.

> A new version of drizzle was released since the video showing this starter was made. See the [drizzle-v0.35 branch](https://github.com/w3cj/hono-open-api-starter/tree/drizzle-v0.35) and [this commit](https://github.com/w3cj/hono-open-api-starter/commit/92525ff84fb2a247c8245cc889b2320d7b3b6e2c) for the changes required to use drizzle v0.35

> For a cloudflare specific template, see the [cloudflare branch](https://github.com/w3cj/hono-open-api-starter/tree/cloudflare) on this repo and the [cloudflare-drizzle-v0.35 branch](https://github.com/w3cj/hono-open-api-starter/tree/cloudflare-drizzle-v0.35)

> For other deployment examples see the [hono-node-deployment-examples](https://github.com/w3cj/hono-node-deployment-examples) repo

- [Hono Open API Starter](#hono-open-api-starter)
  - [Included](#included)
  - [Setup](#setup)
  - [Code Tour](#code-tour)
  - [Endpoints](#endpoints)
  - [References](#references)

## Included

- Structured logging with [pino](https://getpino.io/) / [hono-pino](https://www.npmjs.com/package/hono-pino)
- Documented / type-safe routes with [@hono/zod-openapi](https://github.com/honojs/middleware/tree/main/packages/zod-openapi)
- Interactive API documentation with [scalar](https://scalar.com/#api-docs) / [@scalar/hono-api-reference](https://github.com/scalar/scalar/tree/main/packages/hono-api-reference)
- Convenience methods / helpers to reduce boilerplate with [stoker](https://www.npmjs.com/package/stoker)
- Type-safe schemas and environment variables with [zod](https://zod.dev/)
- Single source of truth database schemas with [drizzle](https://orm.drizzle.team/docs/overview) and [drizzle-zod](https://orm.drizzle.team/docs/zod)
- Testing with [vitest](https://vitest.dev/)
- Sensible editor, formatting and linting settings with [@antfu/eslint-config](https://github.com/antfu/eslint-config)

## Setup

Clone this template without git history

```sh
npx degit w3cj/hono-open-api-starter my-api
cd my-api
```

Create `.env` file

```sh
cp .env.example .env
```

Install dependencies

```sh
pnpm install
```

Create sqlite db / push schema

```sh
pnpm drizzle-kit push
```

Run

```sh
pnpm dev
```

Lint

```sh
pnpm lint
```

Test

```sh
pnpm test
```

## Code Tour

Base hono app exported from [app.ts](./src/app.ts). Local development uses [@hono/node-server](https://hono.dev/docs/getting-started/nodejs) defined in [index.ts](./src/index.ts) - update this file or create a new entry point to use your preferred runtime.

Typesafe env defined in [env.ts](./src/env.ts) - add any other required environment variables here. The application will not start if any required environment variables are missing

See [src/routes/tasks](./src/routes/tasks/) for an example Open API group. Copy this folder / use as an example for your route groups.

- Router created in [tasks.index.ts](./src/routes/tasks/tasks.index.ts)
- Route definitions defined in [tasks.routes.ts](./src/routes/tasks/tasks.routes.ts)
- Hono request handlers defined in [tasks.handlers.ts](./src/routes/tasks/tasks.handlers.ts)
- Group unit tests defined in [tasks.test.ts](./src/routes/tasks/tasks.test.ts)

All app routes are grouped together and exported into single type as `AppType` in [app.ts](./src/app.ts) for use in [RPC / hono/client](https://hono.dev/docs/guides/rpc).

## Endpoints

| Path               | Description              |
| ------------------ | ------------------------ |
| GET /doc           | Open API Specification   |
| GET /reference     | Scalar API Documentation |
| GET /tasks         | List all tasks           |
| POST /tasks        | Create a task            |
| GET /tasks/{id}    | Get one task by id       |
| PATCH /tasks/{id}  | Patch one task by id     |
| DELETE /tasks/{id} | Delete one task by id    |

## References

- [What is Open API?](https://swagger.io/docs/specification/v3_0/about/)
- [Hono](https://hono.dev/)
  - [Zod OpenAPI Example](https://hono.dev/examples/zod-openapi)
  - [Testing](https://hono.dev/docs/guides/testing)
  - [Testing Helper](https://hono.dev/docs/helpers/testing)
- [@hono/zod-openapi](https://github.com/honojs/middleware/tree/main/packages/zod-openapi)
- [Scalar Documentation](https://github.com/scalar/scalar/tree/main/?tab=readme-ov-file#documentation)
  - [Themes / Layout](https://github.com/scalar/scalar/blob/main/documentation/themes.md)
  - [Configuration](https://github.com/scalar/scalar/blob/main/documentation/configuration.md)
