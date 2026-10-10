# PLAN__Bun-hono-api-starter.md

# Enterprise-Grade Bun + Hono API Starter

**Version:** 1.0.0  
**Architecture:** Modular Monolith / API-First / Cloud-Ready  
**Runtime:** Bun  
**Framework:** Hono  
**Language:** TypeScript  
**Database:** PostgreSQL  
**ORM:** Drizzle ORM  
**Validation:** Zod  
**Authentication:** Better Auth  
**Authorization:** RBAC + Permission-Based Access Control  
**Cache & Queue:** Redis + BullMQ (subject to Bun compatibility validation)  
**API Documentation:** OpenAPI 3.1  
**Development Environment:** GitHub Codespaces  
**Database Hosting:** Neon PostgreSQL  
**Deployment:** Docker / Managed Cloud  
**Testing:** Bun Test + Integration Tests + E2E Tests  
**Observability:** OpenTelemetry + Structured Logging  
**Security:** Defense in Depth / OWASP ASVS / Secure by Default

---

# 1. Project Vision

## 1.1 Objective

Build a professional, secure, scalable, maintainable, production-oriented backend starter using:

- Bun
- Hono
- TypeScript
- PostgreSQL
- Drizzle ORM
- Zod
- Better Auth
- Redis
- OpenAPI
- Docker

The project must provide a complete backend foundation suitable for:

1. SaaS applications.
2. CRM systems.
3. ERP systems.
4. E-commerce applications.
5. Mobile application backends.
6. Enterprise dashboards.
7. Multi-tenant platforms.
8. Subscription-based platforms.
9. Internal business applications.
10. Third-party API platforms.

The final result must be a reusable backend starter rather than an application tied to one business domain.

## 1.2 Engineering Philosophy

The architecture must follow these principles:

1. Security by default.
2. Strong type safety.
3. Modular architecture.
4. Separation of concerns.
5. Explicit dependency management.
6. Minimal unnecessary complexity.
7. Production-oriented configuration.
8. Testability.
9. Observability.
10. Maintainability.
11. Scalability.
12. Developer experience.
13. API consistency.
14. Database integrity.
15. Infrastructure portability.
16. Predictable error handling.
17. Secure multi-tenancy.
18. Least privilege.
19. Fail-safe defaults.
20. Defense in depth.

Performance must never be prioritized over correctness, security, or data integrity.

---

# 2. Instructions for the AI Coding Agent

## 2.1 Primary Mission

You are acting as a senior software architect, backend engineer, database architect, DevSecOps engineer, and quality assurance engineer.

Your responsibility is to implement the project described in this document.

Do not generate a collection of disconnected examples.

Build a coherent, executable, tested, documented application.

## 2.2 Mandatory Rules

The AI agent MUST:

1. Inspect the repository before making changes.
2. Identify existing files and dependencies.
3. Avoid overwriting working code unnecessarily.
4. Create a detailed implementation checklist.
5. Execute the project in clearly defined phases.
6. Use TypeScript strict mode.
7. Avoid `any` unless absolutely necessary and justified.
8. Validate all external input.
9. Never trust client-provided authorization data.
10. Never expose internal errors to API clients.
11. Never hardcode secrets.
12. Never log passwords, tokens, session cookies, or API keys.
13. Implement automated tests for critical functionality.
14. Implement database migrations.
15. Document environment variables.
16. Use consistent naming conventions.
17. Use structured error handling.
18. Keep controllers thin.
19. Keep business logic in services.
20. Keep database queries in repositories.
21. Implement dependency injection where useful without creating unnecessary abstraction.
22. Avoid circular dependencies.
23. Validate compatibility between Bun and every selected dependency.
24. Prefer maintained libraries with active communities.
25. Document technical decisions.
26. Run formatting, linting, type checking, and tests after each phase.
27. Never claim a feature is complete without verifying its behavior.
28. Never silently ignore failed tests.
29. Never disable security controls merely to make tests pass.
30. Never deploy automatically without explicit authorization.

## 2.3 Dependency Policy

Before installing a dependency:

- Check its official documentation.
- Verify its current stable version.
- Check Bun compatibility.
- Review maintenance activity.
- Review known security advisories.
- Avoid deprecated packages.
- Prefer stable releases.
- Pin dependencies using the lockfile.
- Document important architectural dependencies.

Do not invent package APIs.

If the latest documentation differs from this plan, use the supported API and document the deviation.

---

# 3. Technology Stack

## 3.1 Core Backend

| Component | Technology |
|---|---|
| Runtime | Bun |
| HTTP Framework | Hono |
| Language | TypeScript |
| Validation | Zod |
| API Schema | OpenAPI 3.1 |
| API Documentation | Scalar |
| Database | PostgreSQL |
| ORM | Drizzle ORM |
| Authentication | Better Auth |
| Password Hashing | Maintained secure library / Better Auth defaults |
| Authorization | RBAC + Permissions |
| Logging | Pino |
| Metrics | OpenTelemetry |
| Error Tracking | Sentry (optional) |
| Cache | Redis |
| Background Jobs | BullMQ or verified Bun-compatible alternative |
| Email | Resend / SMTP Adapter |
| Object Storage | S3-Compatible Storage |
| Testing | Bun Test |
| Containers | Docker |
| CI/CD | GitHub Actions |
| Development | GitHub Codespaces |

## 3.2 Supporting Libraries

Evaluate the latest compatible versions of:

- `@hono/zod-validator`
- `@hono/zod-openapi`
- `@scalar/hono-api-reference`
- `drizzle-orm`
- `drizzle-kit`
- `postgres`
- `zod`
- `better-auth`
- `pino`
- `ioredis`
- `bullmq`
- `@opentelemetry/api`
- `@opentelemetry/sdk-node`
- `@opentelemetry/instrumentation`
- `@aws-sdk/client-s3`
- `@aws-sdk/s3-request-presigner`

Only install packages that are actually used.

---

# 4. System Architecture

## 4.1 Architecture Style

Use a modular monolith architecture.

The architecture must allow modules to be extracted into independent services later without requiring a complete rewrite.

Avoid introducing microservices during the initial implementation.

## 4.2 Layered Architecture

Each business module should follow:

```text
HTTP Request
     |
     v
Hono Middleware
     |
     v
Authentication
     |
     v
Authorization
     |
     v
Input Validation
     |
     v
Controller
     |
     v
Application Service
     |
     v
Domain Logic
     |
     v
Repository
     |
     v
Drizzle ORM
     |
     v
PostgreSQL
```

## 4.3 Dependency Direction

Dependencies must flow inward.

Controllers may depend on services.

Services may depend on repositories through interfaces when appropriate.

Repositories may depend on Drizzle.

Domain logic must not depend on Hono.

Avoid importing HTTP-specific objects inside domain services.

## 4.4 Module Independence

Each module must:

- Own its business logic.
- Define its public interface.
- Encapsulate persistence operations.
- Expose routes through a dedicated router.
- Define validation schemas.
- Contain relevant tests.
- Avoid directly manipulating another module's internal tables.

Cross-module operations should use explicit services.

---

# 5. Project Directory Structure

Create the following structure, adjusting only when required for a documented engineering reason.

```text
bun-hono-api-starter/
│
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   ├── security.yml
│   │   └── release.yml
│   ├── dependabot.yml
│   └── CODEOWNERS
│
├── .devcontainer/
│   └── devcontainer.json
│
├── .vscode/
│   ├── extensions.json
│   └── settings.json
│
├── docs/
│   ├── architecture/
│   ├── api/
│   ├── database/
│   ├── deployment/
│   ├── security/
│   ├── testing/
│   ├── runbooks/
│   └── adr/
│
├── scripts/
│   ├── db/
│   ├── security/
│   ├── maintenance/
│   └── setup/
│
├── src/
│   │
│   ├── app.ts
│   ├── server.ts
│   │
│   ├── config/
│   │   ├── env.ts
│   │   ├── app.config.ts
│   │   ├── database.config.ts
│   │   ├── redis.config.ts
│   │   └── security.config.ts
│   │
│   ├── core/
│   │   ├── errors/
│   │   ├── exceptions/
│   │   ├── responses/
│   │   ├── constants/
│   │   ├── types/
│   │   ├── interfaces/
│   │   └── utils/
│   │
│   ├── database/
│   │   ├── client.ts
│   │   ├── schema/
│   │   ├── migrations/
│   │   ├── seeds/
│   │   └── transactions/
│   │
│   ├── infrastructure/
│   │   ├── cache/
│   │   ├── queue/
│   │   ├── storage/
│   │   ├── email/
│   │   ├── logging/
│   │   ├── telemetry/
│   │   ├── rate-limit/
│   │   └── cryptography/
│   │
│   ├── middleware/
│   │   ├── authentication.ts
│   │   ├── authorization.ts
│   │   ├── tenant-context.ts
│   │   ├── rate-limit.ts
│   │   ├── request-id.ts
│   │   ├── security-headers.ts
│   │   ├── error-handler.ts
│   │   ├── request-logger.ts
│   │   └── idempotency.ts
│   │
│   ├── modules/
│   │   │
│   │   ├── auth/
│   │   ├── users/
│   │   ├── organizations/
│   │   ├── tenants/
│   │   ├── roles/
│   │   ├── permissions/
│   │   ├── sessions/
│   │   ├── api-keys/
│   │   ├── subscriptions/
│   │   ├── billing/
│   │   ├── files/
│   │   ├── notifications/
│   │   ├── webhooks/
│   │   ├── audit-logs/
│   │   ├── feature-flags/
│   │   ├── settings/
│   │   └── health/
│   │
│   ├── routes/
│   │   ├── index.ts
│   │   └── v1.ts
│   │
│   ├── jobs/
│   │   ├── workers/
│   │   ├── processors/
│   │   └── schedules/
│   │
│   └── openapi/
│       ├── registry.ts
│       ├── schemas/
│       └── security.ts
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── e2e/
│   ├── security/
│   ├── performance/
│   ├── fixtures/
│   └── helpers/
│
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── docker-compose.dev.yml
│
├── drizzle.config.ts
├── bunfig.toml
├── tsconfig.json
├── package.json
├── .env.example
├── .gitignore
├── .dockerignore
├── README.md
├── SECURITY.md
├── CONTRIBUTING.md
├── CHANGELOG.md
└── PLAN__Bun-hono-api-starter.md
```

## 5.1 Internal Module Structure

Use a consistent module structure.

Example:

```text
modules/users/
├── users.routes.ts
├── users.controller.ts
├── users.service.ts
├── users.repository.ts
├── users.schema.ts
├── users.types.ts
├── users.permissions.ts
└── index.ts
```

Create additional files only when necessary.

Avoid excessive fragmentation.

---

# 6. Application Configuration

## 6.1 Environment Variables

All environment variables must be validated using Zod.

The application must fail during startup when required configuration is invalid.

Required configuration categories:

### Application

```env
NODE_ENV=development
APP_NAME=bun-hono-api
APP_VERSION=1.0.0
HOST=0.0.0.0
PORT=3000
API_PREFIX=/api
API_VERSION=v1
LOG_LEVEL=info
```

### Database

```env
DATABASE_URL=
DATABASE_POOL_MAX=10
DATABASE_CONNECTION_TIMEOUT=10000
```

### Authentication

```env
BETTER_AUTH_SECRET=
BETTER_AUTH_URL=http://localhost:3000
```

### Security

```env
CORS_ALLOWED_ORIGINS=http://localhost:5173
TRUST_PROXY=false
```

### Redis

```env
REDIS_URL=
```

### Email

```env
EMAIL_PROVIDER=
EMAIL_FROM=
RESEND_API_KEY=
```

### Storage

```env
STORAGE_PROVIDER=
S3_BUCKET=
S3_REGION=
S3_ENDPOINT=
S3_ACCESS_KEY_ID=
S3_SECRET_ACCESS_KEY=
```

### Observability

```env
OTEL_SERVICE_NAME=bun-hono-api
OTEL_EXPORTER_OTLP_ENDPOINT=
SENTRY_DSN=
```

### Application Features

```env
ENABLE_API_DOCS=true
ENABLE_REGISTRATION=true
ENABLE_EMAIL_VERIFICATION=true
ENABLE_MULTI_TENANCY=true
ENABLE_BILLING=false
ENABLE_BACKGROUND_JOBS=false
```

## 6.2 Configuration Requirements

The implementation must:

1. Parse configuration once during startup.
2. Export typed configuration objects.
3. Reject invalid production configuration.
4. Prevent accidental logging of secrets.
5. Support local development configuration.
6. Support container-based environments.
7. Support cloud deployment.
8. Document every variable.
9. Avoid insecure production defaults.
10. Require explicit configuration for security-sensitive features.

Feature flags must never replace server-side authorization.

---

# 7. Database Architecture

## 7.1 PostgreSQL

Use PostgreSQL as the primary transactional database.

Development may use Docker PostgreSQL.

Production may use Neon PostgreSQL or another managed PostgreSQL provider.

## 7.2 ORM

Use Drizzle ORM.

Requirements:

- Strongly typed schemas.
- Explicit relations.
- Reusable query helpers.
- Database migrations.
- Transaction support.
- Query parameterization.
- Pagination.
- Filtering.
- Sorting.
- Index management.
- Constraint management.

## 7.3 Database Naming Conventions

Use:

```text
snake_case
```

Examples:

```text
users
organizations
organization_members
roles
permissions
role_permissions
api_keys
audit_logs
```

## 7.4 Common Table Fields

Business tables should include appropriate fields such as:

```text
id
created_at
updated_at
deleted_at
```

Not every table requires soft deletion.

Add soft deletion only when there is a documented business requirement.

## 7.5 Primary Keys

Prefer UUID-based identifiers.

Use UUIDv7 where supported consistently by the application and database tooling.

Alternatively use UUIDv4.

Do not expose sequential internal identifiers when that would create avoidable information disclosure.

UUIDs do not replace authorization checks.

## 7.6 Database Constraints

Implement:

- Primary keys.
- Foreign keys.
- Unique constraints.
- Check constraints.
- Not-null constraints.
- Appropriate indexes.
- Referential integrity.
- Transaction boundaries.

Never rely exclusively on application validation.

## 7.7 Database Migrations

Use Drizzle Kit.

Requirements:

1. Version-controlled migrations.
2. Reproducible database schema.
3. Migration validation in CI.
4. Separate development and production workflows.
5. No destructive production migrations without review.
6. Document rollback and recovery procedures.
7. Backup before high-risk schema changes.
8. Avoid applying migrations automatically on every application startup.

## 7.8 Transactions

Use transactions for operations such as:

- Organization creation.
- Membership changes.
- Billing state changes.
- Subscription updates.
- Multi-table writes.
- Permission assignments.
- Idempotent financial operations.

Transactions must be short-lived.

Never hold database transactions open during external network requests.

## 7.9 Database Performance

Implement:

- Connection pooling.
- Pagination limits.
- Query timeouts.
- Appropriate indexes.
- Query performance monitoring.
- Slow query logging where supported.
- Prevention of N+1 queries.
- Bounded result sets.

Connection pool configuration must account for the selected Neon connection endpoint and deployment concurrency.

---

# 8. Authentication System

## 8.1 Authentication Provider

Use Better Auth.

Integrate Better Auth with PostgreSQL and Drizzle using supported adapters.

Do not manually recreate functionality already provided securely by Better Auth.

## 8.2 Authentication Features

Implement:

1. User registration.
2. Email/password login.
3. Logout.
4. Email verification.
5. Password reset.
6. Session management.
7. Session revocation.
8. Secure cookies.
9. Account status management.
10. Login rate limiting.
11. Security event logging.
12. Password change.
13. Session invalidation following sensitive account changes.

## 8.3 Optional Authentication Features

Design extensibility for:

- Google OAuth.
- GitHub OAuth.
- Microsoft OAuth.
- Passkeys.
- TOTP multi-factor authentication.
- Backup recovery codes.
- Enterprise SSO.

Do not enable external identity providers until their credentials and callback URLs are configured.

## 8.4 Password Security

Use a maintained password hashing implementation.

Prefer Argon2id when supported appropriately.

If Better Auth uses another secure supported hashing mechanism, follow its documented integration.

Never use:

- MD5.
- SHA-1.
- Unsalted hashes.
- Reversible password encryption.

## 8.5 Session Security

Requirements:

- HttpOnly cookies.
- Secure cookies in production.
- Appropriate SameSite policy.
- Session expiration.
- Session revocation.
- Session rotation where supported and appropriate.
- CSRF protection for cookie-authenticated state-changing operations.
- No session tokens in URLs.
- No secrets in browser-accessible storage by default.

Cross-origin authentication must be deliberately designed and tested.

---

# 9. Authorization System

## 9.1 Authorization Model

Implement:

**RBAC + Permission-Based Authorization**

Support authorization based on:

- User.
- Organization.
- Membership.
- Role.
- Permission.
- Resource ownership.
- Tenant context.

## 9.2 Default Roles

Define initial organization roles:

```text
owner
admin
manager
member
viewer
```

Platform administration must be separate from organization administration.

A tenant owner must never automatically become a platform administrator.

## 9.3 Permission Naming

Use:

```text
resource:action
```

Examples:

```text
users:read
users:create
users:update
users:delete

organizations:read
organizations:update

members:invite
members:remove

roles:read
roles:manage

billing:read
billing:manage

audit_logs:read
```

## 9.4 Authorization Requirements

The system must:

1. Deny access by default.
2. Validate permissions server-side.
3. Validate resource ownership.
4. Enforce tenant boundaries.
5. Reject unauthorized cross-tenant access.
6. Prevent privilege escalation.
7. Prevent users from assigning permissions they do not possess.
8. Protect ownership transfers.
9. Prevent accidental removal of the last organization owner.
10. Log sensitive permission changes.

## 9.5 Authorization Testing

Test:

- Unauthenticated access.
- Unauthorized access.
- Missing permissions.
- Cross-tenant access.
- Privilege escalation attempts.
- Resource ownership checks.
- Role assignment.
- Role revocation.
- Organization ownership transfer.

---

# 10. Multi-Tenancy Architecture

## 10.1 Multi-Tenancy Strategy

Implement shared-database, shared-schema multi-tenancy.

Use an explicit tenant or organization identifier for tenant-owned records.

## 10.2 Tenant Isolation

Every tenant-owned query must enforce tenant isolation.

Never trust:

```text
organization_id
tenant_id
```

provided by the client without verifying membership and authorization.

## 10.3 Tenant Context

Create tenant-context middleware.

The middleware must:

1. Authenticate the user.
2. Resolve the selected organization.
3. Verify active organization membership.
4. Resolve effective permissions.
5. Attach trusted tenant context to the request.
6. Reject invalid or unauthorized tenant selection.

## 10.4 PostgreSQL Row-Level Security

Evaluate PostgreSQL Row-Level Security as an additional isolation boundary.

If enabled:

- Define explicit tenant policies.
- Use transaction-scoped tenant context.
- Prevent connection-pool context leakage.
- Test pooled connections.
- Verify compatibility with Neon.
- Ensure application roles cannot bypass RLS unintentionally.

Do not claim that tenant isolation is protected by RLS unless policies are enabled and tested.

## 10.5 Multi-Tenant Data Rules

Tenant-owned tables must use tenant identifiers consistently.

Where appropriate, enforce tenant-safe composite foreign keys.

Do not rely only on application-level filters.

---

# 11. User Management

Implement a complete user management module.

Features:

- Current user profile.
- Update profile.
- Change password.
- Email verification status.
- Account activation/deactivation.
- Account suspension.
- Session listing.
- Session revocation.
- Account deletion workflow.
- Data export workflow.
- Account security events.

Administrative endpoints must require explicit permissions.

Never expose password hashes or authentication secrets.

---

# 12. Organization Management

Implement:

- Organization creation.
- Organization details.
- Organization settings.
- Organization update.
- Membership management.
- Member invitations.
- Invitation acceptance.
- Invitation expiration.
- Invitation revocation.
- Member removal.
- Member role changes.
- Ownership transfer.
- Organization suspension.
- Organization deletion workflow.

Prevent unauthorized access to other organizations.

---

# 13. API Design

## 13.1 API Versioning

Use:

```text
/api/v1
```

Example endpoints:

```http
GET    /api/v1/health
GET    /api/v1/users/me

GET    /api/v1/organizations
POST   /api/v1/organizations

GET    /api/v1/organizations/:id
PATCH  /api/v1/organizations/:id

GET    /api/v1/organizations/:id/members
POST   /api/v1/organizations/:id/invitations

GET    /api/v1/roles
GET    /api/v1/permissions

GET    /api/v1/audit-logs
```

Better Auth endpoints may use their documented route structure.

## 13.2 Response Structure

Use a consistent success response.

Example:

```json
{
  "success": true,
  "data": {
    "id": "example-id"
  },
  "meta": {
    "requestId": "request-id"
  }
}
```

Use a consistent error response.

Example:

```json
{
  "success": false,
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "The requested resource was not found."
  },
  "meta": {
    "requestId": "request-id"
  }
}
```

Preserve standard HTTP semantics.

Do not force third-party authentication callbacks or webhook protocols into an incompatible response format.

## 13.3 HTTP Status Codes

Use appropriate codes:

```text
200 OK
201 Created
202 Accepted
204 No Content
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
409 Conflict
422 Unprocessable Content
429 Too Many Requests
500 Internal Server Error
503 Service Unavailable
```

## 13.4 Pagination

Support cursor-based pagination for large datasets.

Offset pagination may be used for bounded administrative views.

Enforce maximum page sizes.

## 13.5 Filtering and Sorting

Implement:

- Allowed filter fields.
- Allowed sort fields.
- Validated query parameters.
- Stable sorting.
- Pagination metadata.

Never interpolate client-controlled SQL identifiers directly.

## 13.6 API Documentation

Generate OpenAPI documentation from typed route definitions where practical.

Provide:

```text
/openapi.json
/docs
```

Disable or restrict interactive documentation in production when appropriate.

Document authentication requirements, request examples, response schemas, and error codes.

---

# 14. Input Validation

Use Zod.

Validate:

- Request bodies.
- Query parameters.
- Route parameters.
- Headers where relevant.
- Environment variables.
- External webhook payloads.
- Background job payloads.

Use strict schemas where appropriate.

Enforce:

- String length limits.
- Numeric bounds.
- Enum validation.
- Array size limits.
- File size limits.
- Allowed MIME types.
- Date validation.
- Identifier validation.

Unknown fields must not silently become privileged database attributes.

---

# 15. Security Architecture

## 15.1 Security Standards

Use the following as engineering references:

- OWASP ASVS.
- OWASP API Security Top 10.
- OWASP Cheat Sheet Series.
- CWE Top 25.

Document the selected ASVS verification level and applicable controls.

## 15.2 Security Headers

Configure relevant headers:

- X-Content-Type-Options.
- Referrer-Policy.
- Content-Security-Policy where HTML is served.
- Strict-Transport-Security in HTTPS production environments.
- Appropriate cache-control headers.

Do not apply browser-specific policies blindly to endpoints where they are irrelevant.

## 15.3 CORS

Requirements:

- Explicit allowed origins.
- No wildcard origins with credentialed requests.
- Controlled HTTP methods.
- Controlled request headers.
- Correct preflight handling.

CORS is not an authorization mechanism.

## 15.4 Rate Limiting

Implement distributed rate limiting for production deployments.

Protect:

- Login.
- Registration.
- Password reset.
- Email verification.
- Invitation endpoints.
- API key creation.
- Expensive API operations.
- Public API endpoints.

Use Redis-backed rate limiting where appropriate.

Document behavior during Redis outages.

Security-sensitive endpoints must fail safely.

## 15.5 SQL Injection Protection

Use parameterized queries.

Avoid constructing SQL using raw user input.

Review all raw SQL.

## 15.6 Cross-Site Scripting

Escape or sanitize untrusted content according to its output context.

Do not assume that JSON-only APIs eliminate all XSS risks.

## 15.7 CSRF Protection

Protect cookie-authenticated state-changing requests.

Follow Better Auth's documented CSRF and trusted-origin mechanisms.

Test cross-origin and same-site behavior.

## 15.8 SSRF Protection

If the server fetches user-provided URLs:

- Restrict supported protocols.
- Block internal and metadata endpoints.
- Validate redirects.
- Validate resolved IP addresses.
- Apply network restrictions.
- Enforce timeouts.
- Limit response sizes.

Prefer allowlisted destinations.

## 15.9 Request Size Limits

Enforce limits for:

- JSON bodies.
- Multipart uploads.
- Headers.
- Query strings.
- File uploads.

Reject oversized requests before expensive processing where possible.

## 15.10 Secure Error Handling

Never return:

- Stack traces.
- Database credentials.
- Internal connection strings.
- Access tokens.
- Password hashes.
- Internal infrastructure details.

Return a request identifier for troubleshooting.

## 15.11 Secrets Management

Requirements:

- No secrets in Git.
- No secrets in Docker images.
- No secrets in application logs.
- No secrets in client responses.
- Support secret rotation.
- Document revocation procedures.
- Use managed secrets in production.

## 15.12 Supply Chain Security

Implement:

- Lockfile enforcement.
- Dependency auditing.
- Dependabot.
- Secret scanning.
- Static analysis.
- Container vulnerability scanning.
- Minimal runtime container images.
- Non-root container execution.
- CI permission minimization.
- GitHub Actions pinned to immutable commit SHAs.

## 15.13 API Abuse Prevention

Protect against:

- Credential stuffing.
- Enumeration.
- Excessive resource consumption.
- Mass assignment.
- Broken object-level authorization.
- Broken function-level authorization.
- Replay attacks.
- Unbounded pagination.
- Excessive concurrency.

---

# 16. API Key Management

Implement API keys for server-to-server integrations.

Features:

1. Secure key generation.
2. Key prefix identification.
3. Store only secure key digests.
4. Show full keys only once.
5. Expiration.
6. Revocation.
7. Permission scopes.
8. Tenant association.
9. Last-used timestamps.
10. Audit logging.
11. Optional IP restrictions.
12. Key rotation support.

Never store API keys in plaintext.

API keys must not implicitly inherit unrestricted user privileges.

---

# 17. Redis Cache

## 17.1 Purpose

Use Redis for:

- Distributed rate limiting.
- Short-lived caching.
- Job coordination.
- Temporary tokens where appropriate.
- Distributed coordination where necessary.

## 17.2 Cache Architecture

Implement a cache abstraction.

Example interface:

```typescript
interface CacheService {
  get<T>(key: string): Promise<T | null>

  set<T>(
    key: string,
    value: T,
    ttlSeconds: number
  ): Promise<void>

  delete(key: string): Promise<void>
}
```

## 17.3 Cache Rules

- Use namespaced keys.
- Define TTLs.
- Avoid caching secrets.
- Avoid stale authorization decisions.
- Invalidate cache after relevant mutations.
- Include tenant identifiers in tenant-specific cache keys.
- Define cache failure behavior.

Cache must never become the sole source of truth for critical business data.

---

# 18. Background Jobs

## 18.1 Queue System

Evaluate BullMQ with Bun.

Verify compatibility through integration tests.

If compatibility problems exist, select a maintained Bun-compatible alternative and document the decision.

## 18.2 Job Types

Support:

- Sending emails.
- Processing uploads.
- Notification delivery.
- Webhook delivery.
- Data exports.
- Cleanup operations.
- Report generation.
- Scheduled maintenance.

## 18.3 Job Requirements

Implement:

- Retry policies.
- Exponential backoff.
- Idempotency.
- Job timeouts.
- Concurrency limits.
- Dead-letter handling or equivalent failed-job recovery.
- Structured logs.
- Operational monitoring.

Do not put sensitive information unnecessarily inside queue payloads.

## 18.4 Transactional Outbox

Implement the transactional outbox pattern for critical database-to-queue workflows.

Prevent situations where a database transaction succeeds but the corresponding critical event is permanently lost.

Document at-least-once delivery semantics.

Consumers must tolerate duplicate delivery.

---

# 19. Email System

Create an email provider abstraction.

Support:

- Resend.
- SMTP.
- Future providers.

Email templates:

- Welcome.
- Verify email.
- Reset password.
- Organization invitation.
- Security alert.
- Password changed.
- Subscription notification.

Requirements:

- Template rendering.
- Retry support.
- Delivery logging without exposing sensitive content.
- Rate limiting.
- Expiring action links.
- One-time-use sensitive tokens.

Never include passwords in emails.

---

# 20. File Storage

Use S3-compatible object storage.

Possible providers:

- AWS S3.
- Cloudflare R2.
- MinIO for local development.

Implement:

1. Private file uploads.
2. Signed upload URLs.
3. Signed download URLs.
4. File size limits.
5. MIME type validation.
6. Extension allowlists.
7. Randomized storage keys.
8. Tenant isolation.
9. Upload expiration.
10. Metadata storage.
11. File deletion.
12. Optional malware scanning.

Do not trust client-provided MIME types alone.

For sensitive files, require an appropriate scanning or quarantine workflow before making files available.

---

# 21. Notification System

Implement an extensible notification architecture.

Channels:

- Email.
- In-app notifications.
- Webhooks.

Future channels:

- SMS.
- Push notifications.

Features:

- Notification preferences.
- Read/unread status.
- Delivery status.
- Retry support.
- Tenant awareness.
- Templates.
- Pagination.

---

# 22. Webhooks

## 22.1 Outgoing Webhooks

Implement:

- Endpoint registration.
- Event subscriptions.
- Secret generation.
- Payload signing.
- Delivery attempts.
- Retry policies.
- Delivery history.
- Endpoint disabling.
- Replay tooling for authorized administrators.

## 22.2 Incoming Webhooks

Requirements:

- Verify signatures.
- Validate timestamps when supported.
- Protect against replay attacks.
- Enforce payload limits.
- Process idempotently.
- Acknowledge according to provider requirements.
- Queue expensive processing.

Do not assume webhook delivery is exactly once.

## 22.3 Webhook Security

Use HMAC signatures or provider-defined verification.

Use constant-time comparison for secret-derived signatures.

Protect against SSRF when delivering outgoing webhooks to configurable destinations.

---

# 23. Billing and Subscriptions

## 23.1 Billing Architecture

Create a payment-provider abstraction.

Initial recommended provider:

**Stripe**

Do not implement custom credit card storage or processing.

## 23.2 Billing Features

Design support for:

- Plans.
- Prices.
- Subscriptions.
- Trials.
- Billing customers.
- Checkout sessions.
- Customer portal.
- Subscription changes.
- Cancellation.
- Renewal.
- Payment status.
- Billing history.
- Webhook synchronization.

## 23.3 Billing Security

Requirements:

- Verify provider webhook signatures.
- Use idempotency keys.
- Prevent duplicate processing.
- Never trust subscription status supplied by clients.
- Keep local billing state synchronized with provider events.
- Reconcile inconsistent records.
- Handle out-of-order webhook delivery.

## 23.4 Billing Isolation

Each billing customer must belong to a verified tenant or organization.

Prevent cross-tenant access to billing records.

## 23.5 Billing Feature Flag

Billing must remain disabled until configured.

Do not create fake production payment flows.

---

# 24. Audit Logging

## 24.1 Audit Events

Record security-sensitive operations.

Examples:

- Login.
- Logout.
- Password changes.
- Role changes.
- Permission changes.
- Organization ownership transfer.
- API key creation.
- API key revocation.
- User suspension.
- Subscription changes.
- Sensitive settings changes.

## 24.2 Audit Log Schema

Include appropriate fields:

```text
id
actor_id
organization_id
action
resource_type
resource_id
ip_address
user_agent
request_id
metadata
created_at
```

## 24.3 Audit Requirements

- Append-oriented design.
- Restricted write access.
- Restricted read access.
- Sensitive data redaction.
- Retention configuration.
- Pagination and filtering.
- Tamper-resistance strategy.

For stronger integrity guarantees, consider exporting audit events to append-only external storage.

Do not describe ordinary database audit rows as tamper-proof.

---

# 25. Feature Flags

Implement server-side feature flags.

Support:

- Global flags.
- Environment-specific flags.
- Tenant-specific flags.
- Percentage rollout where justified.

Requirements:

- Safe defaults.
- Typed definitions.
- Audit changes.
- No sensitive information exposure.
- No authorization bypass.

Feature flags are not permission checks.

---

# 26. Observability

## 26.1 Structured Logging

Use structured JSON logs.

Include:

- Timestamp.
- Log level.
- Service name.
- Environment.
- Request ID.
- Trace ID when available.
- Route identifier.
- Response status.
- Request duration.

Avoid sensitive payload logging.

## 26.2 Distributed Tracing

Use OpenTelemetry where runtime support is verified.

Trace:

- Incoming HTTP requests.
- Database queries where supported.
- Redis operations.
- Background jobs.
- External API calls.

Use sampling and avoid storing sensitive attributes.

## 26.3 Metrics

Expose or export:

- Request rate.
- Error rate.
- Request latency.
- Database query latency.
- Active database connections.
- Queue depth.
- Job failures.
- Cache hit rate.
- Authentication failures.

## 26.4 Health Checks

Implement:

```text
/health/live
/health/ready
```

Liveness must not fail merely because an optional external dependency is temporarily unavailable.

Readiness should reflect whether the instance can serve its required functionality.

Do not disclose infrastructure details publicly.

---

# 27. Error Handling

Create a centralized error system.

Example error categories:

```text
ValidationError
AuthenticationError
AuthorizationError
NotFoundError
ConflictError
RateLimitError
DatabaseError
ExternalServiceError
InternalServerError
```

Map errors to appropriate HTTP status codes.

Use stable machine-readable error codes.

Implement:

- Request ID correlation.
- Structured error logging.
- Safe client-facing messages.
- Error cause preservation internally.
- Unexpected exception handling.

Do not suppress unexpected failures.

---

# 28. Idempotency

Implement idempotency support for operations requiring duplicate-request protection.

Examples:

- Billing operations.
- Organization provisioning.
- External event processing.
- Critical resource creation.

Requirements:

- Idempotency keys.
- Request fingerprinting.
- Tenant scoping.
- Atomic persistence.
- Concurrent request protection.
- Defined expiration.
- Safe response replay.

Do not use an in-memory-only implementation in horizontally scaled production environments.

---

# 29. Testing Strategy

## 29.1 Testing Layers

Implement:

1. Unit tests.
2. Integration tests.
3. End-to-end tests.
4. Authorization tests.
5. Tenant isolation tests.
6. Security regression tests.
7. Migration tests.
8. Background job tests.
9. Webhook tests.
10. Performance smoke tests.

## 29.2 Unit Tests

Test:

- Domain services.
- Validation schemas.
- Permission evaluation.
- Utility functions.
- Error mapping.
- Business rules.

## 29.3 Integration Tests

Use a real PostgreSQL database.

Test:

- Drizzle queries.
- Migrations.
- Transactions.
- Constraints.
- Authentication integration.
- Tenant isolation.
- Redis integration when applicable.

## 29.4 E2E Tests

Test complete flows:

```text
Register
→ Verify Email
→ Login
→ Create Organization
→ Invite Member
→ Accept Invitation
→ Assign Role
→ Access Protected Resource
→ Revoke Access
→ Confirm Access Denied
```

## 29.5 Security Tests

Test:

- SQL injection attempts.
- Unauthorized resource access.
- Cross-tenant access.
- Role escalation.
- Invalid session handling.
- Expired tokens.
- Rate limiting.
- CSRF protection.
- Malformed input.
- Oversized requests.
- Webhook signature validation.
- Duplicate webhook processing.

## 29.6 Test Coverage

Target high coverage for critical business and security logic.

A reasonable initial target is:

```text
Overall coverage: >= 80%
Critical authorization logic: >= 95%
```

Coverage percentages do not replace meaningful tests.

## 29.7 Test Isolation

Each test must be repeatable.

Use:

- Dedicated test databases.
- Deterministic fixtures.
- Database cleanup.
- Controlled time.
- Mocked external services where appropriate.

Never run destructive tests against production databases.

---

# 30. Performance Engineering

## 30.1 Goals

Optimize for:

- Predictable latency.
- Efficient database access.
- Controlled memory usage.
- Stable throughput.
- Resource efficiency.

## 30.2 Benchmarking

Use a suitable load-testing tool such as:

- k6.
- autocannon.

Measure:

- Requests per second.
- p50 latency.
- p95 latency.
- p99 latency.
- Error rate.
- CPU usage.
- Memory usage.
- Database connection usage.

## 30.3 Performance Rules

- Benchmark before optimizing.
- Avoid unnecessary ORM queries.
- Use appropriate indexes.
- Use connection pooling.
- Bound concurrency.
- Limit request payload sizes.
- Prevent unbounded result sets.
- Avoid blocking the event loop.
- Offload expensive background work.

Do not declare the application capable of supporting a specific number of users without representative load tests.

---

# 31. Docker Architecture

## 31.1 Dockerfile

Create a production-oriented Dockerfile.

Requirements:

- Multi-stage build where beneficial.
- Pinned base image versions.
- Minimal runtime dependencies.
- Non-root execution.
- Health-check compatibility.
- Proper signal handling.
- No embedded secrets.
- Small image size.
- Reproducible dependency installation.

## 31.2 Docker Compose

Provide local services:

```text
api
postgres
redis
worker
```

Optional:

```text
minio
mailpit
```

Workers and optional services should be configurable through Docker Compose profiles.

## 31.3 Container Security

Implement:

- Least privilege.
- Non-root execution.
- Read-only filesystem where feasible.
- Resource limits.
- Graceful shutdown.
- Appropriate restart policies.
- Minimal Linux capabilities.

---

# 32. GitHub Codespaces

Create:

```text
.devcontainer/devcontainer.json
```

Requirements:

- Bun installed.
- Recommended VS Code extensions.
- PostgreSQL access.
- Redis access.
- Port forwarding.
- Environment setup.
- Development scripts.
- Reproducible tooling.

The environment must support opening the repository and starting development with minimal manual setup.

Never place production credentials in devcontainer configuration.

---

# 33. GitHub Actions CI/CD

## 33.1 CI Pipeline

On pull requests and protected branch pushes:

1. Checkout repository.
2. Install pinned Bun version.
3. Install dependencies using frozen lockfile.
4. Run formatting checks.
5. Run linting.
6. Run TypeScript checks.
7. Run unit tests.
8. Run integration tests.
9. Validate database migrations.
10. Run security checks.
11. Build the application.
12. Build the Docker image.

## 33.2 Security Pipeline

Implement:

- Dependency scanning.
- Secret scanning.
- Static analysis.
- Container scanning.
- Dependency update automation.

## 33.3 Deployment Pipeline

Deployment must require authorization.

Production deployment should support:

- Environment protection rules.
- Deployment approvals.
- Migration review.
- Rollback procedures.
- Health verification.
- Post-deployment smoke tests.

## 33.4 Supply Chain Requirements

Use:

- Minimal GitHub token permissions.
- Immutable action references.
- Protected branches.
- Required CI checks.
- Reviewed dependency updates.
- Artifact integrity verification where practical.

---

# 34. Deployment Architecture

## 34.1 Recommended Initial Production Architecture

```text
                  Internet
                     |
                     v
               CDN / WAF
                     |
                     v
               Load Balancer
                     |
                     v
              Bun + Hono API
                     |
          +----------+-----------+
          |          |           |
          v          v           v
      PostgreSQL    Redis     Object Storage
        Neon       Managed      S3/R2
          |
          v
      Backups / PITR
```

Background workers should run as separate processes or services where required.

## 34.2 Production Requirements

- HTTPS.
- Managed secrets.
- Database backups.
- Health checks.
- Horizontal scaling strategy.
- Graceful shutdown.
- Centralized logging.
- Monitoring.
- Error tracking.
- Resource limits.
- Secure network configuration.
- Disaster recovery documentation.

## 34.3 Deployment Providers

Support standard Docker deployment.

Potential providers:

- Fly.io.
- Railway.
- Render.
- AWS.
- Google Cloud.
- Azure.

Provider-specific implementation should be optional.

Avoid vendor lock-in where practical.

---

# 35. Backup and Disaster Recovery

## 35.1 Backup Requirements

Document:

- Database backup schedule.
- Backup retention.
- Point-in-time recovery availability.
- Backup encryption.
- Restore procedures.
- Access restrictions.

## 35.2 Recovery Objectives

Define:

```text
RPO: Recovery Point Objective
RTO: Recovery Time Objective
```

Do not invent guaranteed RPO or RTO values.

Select objectives based on business requirements and provider capabilities.

## 35.3 Recovery Testing

Perform restore tests in isolated environments.

Backups are not considered operationally verified until restoration has been tested.

---

# 36. Data Privacy and Retention

Implement configurable retention policies for:

- Audit logs.
- Application logs.
- Expired sessions.
- Invitations.
- Temporary tokens.
- Uploaded files.
- Deleted accounts.
- Background job records.

Provide workflows for:

- Personal data export.
- Account deletion.
- Data anonymization where appropriate.
- Retention enforcement.

Document legal and regulatory assumptions.

Do not claim GDPR, SOC 2, HIPAA, or other regulatory compliance merely because technical controls exist.

---

# 37. Developer Experience

## 37.1 Required Commands

Provide scripts for:

```bash
bun run dev
bun run start
bun run build

bun run lint
bun run format
bun run typecheck

bun run test
bun run test:unit
bun run test:integration
bun run test:e2e

bun run db:generate
bun run db:migrate
bun run db:seed

bun run docker:up
bun run docker:down
```

Adjust command names if required, but document them consistently.

## 37.2 Development Requirements

- Fast startup.
- Hot reload.
- Clear error messages.
- Reproducible environment.
- Easy database reset for development.
- Example API requests.
- Automatic API documentation.
- Seed data.
- Minimal onboarding steps.

---

# 38. Documentation

Create professional documentation.

## 38.1 README

Include:

1. Project overview.
2. Features.
3. Architecture.
4. Requirements.
5. Quick start.
6. Environment configuration.
7. Database setup.
8. Running tests.
9. Running Docker.
10. API documentation.
11. Authentication setup.
12. Deployment.
13. Troubleshooting.

## 38.2 Architecture Documentation

Document:

- Architecture decisions.
- Module responsibilities.
- Database relationships.
- Authentication flow.
- Authorization flow.
- Tenant isolation.
- Background job architecture.
- Security boundaries.

## 38.3 ADRs

Use Architecture Decision Records.

Examples:

```text
ADR-001: Use Bun
ADR-002: Use Hono
ADR-003: Use PostgreSQL
ADR-004: Use Drizzle ORM
ADR-005: Use Better Auth
ADR-006: Use Modular Monolith
ADR-007: Multi-Tenant Isolation Strategy
ADR-008: Redis and Background Jobs
```

---

# 39. Implementation Roadmap

The AI agent must implement the system incrementally.

Do not attempt to generate the entire project in one uncontrolled operation.

## Phase 0 — Repository Analysis

Tasks:

- Inspect repository.
- Identify existing code.
- Check available tooling.
- Validate package compatibility.
- Identify architecture decisions.
- Create implementation checklist.

Deliverables:

- Repository assessment.
- Dependency compatibility report.
- Implementation checklist.

Acceptance criteria:

- Existing code is understood.
- No unnecessary files are overwritten.
- Major compatibility risks are documented.

## Phase 1 — Project Foundation

Implement:

- Bun.
- Hono.
- TypeScript.
- Project structure.
- Environment validation.
- Error handling.
- Request IDs.
- Structured logging.
- Health endpoints.
- Development scripts.

Acceptance criteria:

- Server starts successfully.
- Environment validation works.
- Health endpoint responds.
- Type checking passes.
- Basic tests pass.

## Phase 2 — Database Foundation

Implement:

- PostgreSQL integration.
- Drizzle ORM.
- Database schemas.
- Migration system.
- Connection configuration.
- Transaction helpers.
- Database integration tests.

Acceptance criteria:

- Migrations run successfully.
- Database connectivity works.
- Integration tests pass.
- Constraints are verified.

## Phase 3 — Authentication

Implement:

- Better Auth.
- Registration.
- Login.
- Logout.
- Email verification.
- Password reset.
- Session management.
- Secure cookie configuration.
- Authentication tests.

Acceptance criteria:

- Authentication flows work.
- Invalid credentials are rejected.
- Sessions can be revoked.
- Sensitive endpoints are protected.

## Phase 4 — Authorization

Implement:

- Roles.
- Permissions.
- Permission evaluation.
- Authorization middleware.
- Privilege escalation protection.
- Authorization tests.

Acceptance criteria:

- Unauthorized requests are rejected.
- Role permissions are enforced.
- Privilege escalation attempts fail.

## Phase 5 — Multi-Tenancy

Implement:

- Organizations.
- Memberships.
- Invitations.
- Tenant context.
- Tenant isolation.
- Cross-tenant security tests.

Acceptance criteria:

- Tenant boundaries are enforced.
- Cross-tenant resource access fails.
- Organization membership is validated.

## Phase 6 — Core API Modules

Implement:

- Users.
- Organizations.
- Roles.
- Permissions.
- Settings.
- Audit logs.
- API keys.

Acceptance criteria:

- CRUD operations work.
- Validation is enforced.
- Authorization is enforced.
- API documentation is generated.

## Phase 7 — Infrastructure Services

Implement:

- Redis.
- Distributed rate limiting.
- Cache abstraction.
- Queue integration.
- Background workers.
- Email abstraction.
- Storage abstraction.

Acceptance criteria:

- Redis integration works.
- Rate limits are enforced.
- Jobs process reliably.
- Retry behavior is tested.

## Phase 8 — Advanced Platform Features

Implement:

- Notifications.
- Webhooks.
- Feature flags.
- Idempotency.
- Transactional outbox.
- Billing integration behind a disabled-by-default feature flag.

Acceptance criteria:

- Webhook signatures are verified.
- Duplicate events are handled.
- Failed jobs can be recovered.
- Billing cannot operate without valid configuration.

## Phase 9 — Security Hardening

Implement and verify:

- Security headers.
- CORS.
- CSRF protection.
- Rate limiting.
- Request size limits.
- Authorization regression tests.
- Secret scanning.
- Dependency scanning.
- Container hardening.

Acceptance criteria:

- Critical security tests pass.
- No known unmitigated critical dependency vulnerabilities remain.
- Security configuration is documented.
- Sensitive information is not exposed.

## Phase 10 — Observability

Implement:

- Structured logging.
- Tracing.
- Metrics.
- Error monitoring integration.
- Health checks.
- Operational dashboards documentation.

Acceptance criteria:

- Requests can be correlated.
- Errors are observable.
- Sensitive values are redacted.

## Phase 11 — Testing and Performance

Implement:

- Unit tests.
- Integration tests.
- E2E tests.
- Security tests.
- Load testing.
- Performance baseline documentation.

Acceptance criteria:

- Test suites pass.
- Performance results are documented.
- Bottlenecks are identified.
- No unsupported performance claims are made.

## Phase 12 — Deployment and Release

Implement:

- Docker.
- Docker Compose.
- Codespaces.
- GitHub Actions.
- Production environment documentation.
- Backup procedures.
- Deployment runbooks.
- Release checklist.

Acceptance criteria:

- Docker image builds.
- Container runs as non-root.
- CI passes.
- Deployment procedure is documented.
- Rollback procedure is documented.

---

# 40. Definition of Done

A feature is complete only when:

1. Code is implemented.
2. Types are correct.
3. Input is validated.
4. Authorization is enforced.
5. Errors are handled.
6. Relevant tests exist.
7. Tests pass.
8. Documentation is updated.
9. Security considerations are reviewed.
10. The feature integrates with the application.
11. No unrelated functionality is broken.
12. Known limitations are documented.

Do not use placeholder implementations and describe them as finished.

---

# 41. Production Readiness Checklist

Before declaring the starter production-ready, verify:

## Application

- [ ] Application starts successfully.
- [ ] Environment validation works.
- [ ] Graceful shutdown works.
- [ ] Errors are handled centrally.
- [ ] Request IDs are generated.
- [ ] API documentation is accurate.

## Database

- [ ] Migrations work.
- [ ] Transactions work.
- [ ] Foreign keys are enforced.
- [ ] Indexes are reviewed.
- [ ] Database connections are bounded.
- [ ] Backup and restore procedures are documented.

## Authentication

- [ ] Login works.
- [ ] Registration works.
- [ ] Email verification works.
- [ ] Password reset works.
- [ ] Session revocation works.
- [ ] Cookie security is verified.
- [ ] CSRF protections are tested.

## Authorization

- [ ] Permissions are enforced.
- [ ] Roles are enforced.
- [ ] Privilege escalation is prevented.
- [ ] Tenant boundaries are enforced.
- [ ] Cross-tenant tests pass.

## Security

- [ ] CORS is restricted.
- [ ] Rate limiting works.
- [ ] Secrets are protected.
- [ ] Sensitive logs are redacted.
- [ ] Request size limits work.
- [ ] Dependency scanning passes.
- [ ] Container scanning is performed.
- [ ] Critical vulnerabilities are resolved or formally risk-accepted.

## Infrastructure

- [ ] Docker builds successfully.
- [ ] CI passes.
- [ ] Health checks work.
- [ ] Logs are structured.
- [ ] Metrics are available.
- [ ] Graceful shutdown is verified.
- [ ] Recovery procedures are documented.

---

# 42. Additional Engineering Requirements

## 42.1 Graceful Shutdown

The application must gracefully handle termination signals.

Requirements:

- Stop accepting new requests.
- Allow active requests to complete within a timeout.
- Close database connections.
- Close Redis connections.
- Stop workers safely.
- Flush logs and telemetry where supported.

## 42.2 Timeouts

Configure appropriate timeouts for:

- HTTP requests.
- Database operations.
- Redis operations.
- External API calls.
- Background jobs.
- File uploads.

Avoid unlimited execution times.

## 42.3 External Service Resilience

Implement where appropriate:

- Bounded retries.
- Exponential backoff.
- Retry jitter.
- Circuit breaking.
- Concurrency limits.
- Request cancellation.
- Failure classification.

Do not retry non-idempotent operations blindly.

## 42.4 Database Schema Evolution

Use backward-compatible migration strategies.

For breaking schema changes, prefer:

```text
Expand
→ Migrate Data
→ Deploy Compatible Code
→ Contract
```

Avoid changes that require simultaneous deployment of every application instance.

## 42.5 Security Review Before Release

Review:

- Authentication.
- Authorization.
- Tenant isolation.
- File upload handling.
- Webhook verification.
- Secrets handling.
- SQL query safety.
- Logging.
- Dependency vulnerabilities.
- Infrastructure permissions.

Document unresolved risks.

---

# 43. Future Extensions

Design the architecture to support future additions without implementing unnecessary complexity immediately.

Potential extensions:

- GraphQL API.
- WebSocket gateway.
- Server-Sent Events.
- Real-time notifications.
- Advanced search.
- Elasticsearch or OpenSearch.
- AI integrations.
- Workflow automation.
- Advanced analytics.
- Usage-based billing.
- Enterprise SSO.
- SCIM provisioning.
- Internationalization.
- Data residency.
- Advanced compliance controls.
- Dedicated-tenant database deployment.

Future support does not mean these features must be implemented in the initial release.

---

# 44. AI Agent Execution Protocol

The AI agent must follow this protocol throughout implementation.

## Step 1 — Inspect

Inspect the existing repository and identify its current state.

## Step 2 — Plan

Create a phase-specific task checklist.

Identify:

- Files to create.
- Files to modify.
- Dependencies required.
- Tests required.
- Security considerations.
- Acceptance criteria.

## Step 3 — Implement

Implement only the current phase.

Use actual functioning code.

Avoid placeholder logic.

## Step 4 — Verify

Run:

```bash
bun run typecheck
bun run lint
bun run test
```

Also run relevant integration and migration checks.

## Step 5 — Review

Review:

- Correctness.
- Security.
- Type safety.
- Maintainability.
- Error handling.
- Database integrity.
- Tenant isolation.
- Documentation.

## Step 6 — Report

At the end of every phase, report:

```text
Phase:
Status:

Implemented Features:
- ...

Created Files:
- ...

Modified Files:
- ...

Dependencies Added:
- ...

Tests Executed:
- ...

Test Results:
- ...

Security Checks:
- ...

Known Limitations:
- ...

Next Phase:
- ...
```

## Step 7 — Continue

Proceed to the next phase only after the current phase meets its acceptance criteria.

If a blocker exists, report it clearly.

Do not fabricate successful test results.

---

# 45. Final Deliverables

The completed project must include:

1. Functional Bun + Hono application.
2. Strict TypeScript configuration.
3. PostgreSQL integration.
4. Drizzle ORM schemas and migrations.
5. Better Auth integration.
6. Secure authentication workflows.
7. RBAC and permission enforcement.
8. Multi-tenant architecture.
9. User management.
10. Organization management.
11. API key management.
12. Redis integration.
13. Distributed rate limiting.
14. Background job infrastructure.
15. Email provider abstraction.
16. Object storage integration.
17. Notification architecture.
18. Webhook infrastructure.
19. Optional billing integration.
20. Audit logging.
21. Feature flags.
22. OpenAPI documentation.
23. Structured logging.
24. Error monitoring integration.
25. Health endpoints.
26. Automated tests.
27. Security regression tests.
28. Docker configuration.
29. GitHub Codespaces configuration.
30. GitHub Actions CI/CD.
31. Deployment documentation.
32. Backup and recovery documentation.
33. Architecture documentation.
34. Security documentation.
35. Developer onboarding documentation.

---

# 46. Final Success Criteria

The project succeeds when:

- A developer can clone the repository and start the application using documented commands.
- The application can connect to PostgreSQL.
- Authentication works securely.
- Authorization rules are enforced.
- Tenant isolation is verified through automated tests.
- Database migrations are reproducible.
- Critical operations are protected against duplicate execution.
- Sensitive information is protected.
- Automated tests execute successfully.
- The Docker image builds and runs.
- CI validates changes.
- API documentation matches the implementation.
- Infrastructure failures are handled predictably.
- The application is observable.
- Production deployment procedures are documented.
- Security limitations and operational risks are explicitly recorded.

The goal is not to maximize the number of dependencies or features.

The goal is to produce a cohesive, reliable, secure, extensible backend foundation that developers can understand, operate, and maintain.

---

# 47. Final Instruction to the AI Coding Agent

**Build this project as a real, maintainable software system.**

Do not treat this document as a request for pseudocode or disconnected code snippets.

Implement features incrementally.

Verify compatibility with the current Bun, Hono, Drizzle ORM, Better Auth, and PostgreSQL ecosystems.

Prioritize:

1. Security.
2. Correctness.
3. Data integrity.
4. Maintainability.
5. Testability.
6. Operational reliability.
7. Performance.
8. Developer experience.

Avoid unnecessary architectural complexity.

Never substitute assumptions for verification.

Never report tests as passing unless they were actually executed.

Do not claim production readiness without evidence.

**Begin with Phase 0: Repository Analysis.**


هذه الخطة تتجاوز Starter بسيطًا؛ فهي مواصفات لبناء **Backend Platform Foundation** يمكن إعادة استخدامها في مشاريع متعددة.

هناك ثلاث نقاط أنصحك بالاهتمام بها أثناء التنفيذ:

**1. لا تطلب من AI تنفيذ المشروع كله دفعة واحدة.** حجم المواصفات كبير، ومحاولة تنفيذها في جلسة واحدة قد تنتج ملفات كثيرة دون تكامل حقيقي. الأفضل أن يلتزم بالمراحل الـ13، مع اختبار كل مرحلة قبل الانتقال إلى التالية.

**2. لا تجعل جميع الخدمات شرطًا لتشغيل المشروع محليًا.** ينبغي أن يعمل الـAPI الأساسي باستخدام Bun وPostgreSQL فقط، ثم تُفعّل Redis والبريد والتخزين والمدفوعات حسب الحاجة. هذا يقلل التعقيد ويجعل الـStarter أكثر قابلية لإعادة الاستخدام.

**3. أضف مستويين واضحين للتشغيل:** وضع `Core` يحتوي على API والمصادقة والمستخدمين والصلاحيات وقاعدة البيانات، ووضع `Full` يفعّل الخدمات الإضافية. ويمكن تنفيذ ذلك من خلال إعدادات واضحة وDocker Compose Profiles، وليس بالضرورة بنظام إضافات معقد.

**ترشيحي الأخير:** ابدأ بتنفيذ المراحل من 0 إلى 5 أولًا. عند اكتمالها واختبار المصادقة والصلاحيات وعزل المؤسسات، ستكون قد أنشأت أهم أساس أمني ومعماري للمشروع. بعد ذلك أضف بقية المكونات تدريجيًا، مع الاحتفاظ بهذه الخطة بوصفها المرجع الهندسي الرئيسي.