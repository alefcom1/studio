# deploy/remarka-lab

Production deployment config for **Remarka Lab · Monitor** (the SEO-monitoring
platform, ex-**SiteLens** — renamed because `site-lens.tech` was taken; code
identifiers such as the `sitelens` folder and the `sitelens_secret` placeholder
keep the old name upstream). Deployed as an **internal tool behind a password**
(path A) on the Hetzner CX23 at **`lab.remarka.biz`** (`178.105.192.76`, EU).

The platform is a monorepo: Next.js **web** + Fastify **api** + Node **worker**
(BullMQ, bundles Chromium) + **Postgres** (Prisma) + **Redis**. Source lives in
another repo, cloned on the server at `~/remarka-lab` (platform in `sitelens/`)
and treated as read-only from here.

## Architecture

```
                         ┌────────────────────────────────────────┐
 Browser ──HTTPS──▶ Caddy │ TLS (Let's Encrypt) + Basic Auth (all) │
 (Basic Auth)            └───────────┬───────────────┬────────────┘
                    /api/* /ws /health              everything else
                            │                          │
                            ▼                          ▼
                        api:3001  ◀── internal ──▶  web:3000
                       (Fastify)     Docker net     (Next.js)
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
              db:5432               redis:6379 ◀── worker (BullMQ + Chromium)
             (Postgres)              (queues)
```

- **Nothing is published to the host except Caddy's 80/443.** api/web ports are
  removed via `!reset` (Compose concatenates `ports`, and Docker's iptables
  bypass ufw, so removal — not loopback binding — is the safe choice). db/redis
  were never published; do **not** add `docker-compose.expose.yml` in prod.
- **Auth:** the app has none, so Caddy Basic Auth gates the whole site.
- **Same-origin:** `NEXT_PUBLIC_API_URL` is baked at build to
  `https://lab.remarka.biz`, so the browser calls its own origin for `/api` and
  `wss://…/ws`; `CORS_ORIGIN` is still pinned server-side as defense-in-depth.

## Files

| File                       | Purpose                                                        |
|----------------------------|----------------------------------------------------------------|
| `docker-compose.prod.yml`  | Override over the platform's base compose (secrets, no public ports, memory limits, healthchecks inherited, Caddy service, web build-arg). |
| `Caddyfile`                | TLS + Basic Auth + routing (`/api`,`/ws`,`/health`→api, rest→web); stub for adding `remarka.biz` WordPress later. |
| `.env.prod.template`       | All env vars as placeholders (no real secrets). Copy to `.env`. |
| `setup.md`                 | Step-by-step server runbook (as `massimo`), diagnostics, updating. |
| `backup.sh`                | Daily `pg_dump` → gzip, 14-day rotation, optional offsite scp, uptime-monitor note. |

## Run (short form — full runbook in `setup.md`)

```bash
cd ~/remarka-lab/sitelens
# copy the 4 files here, create .env, hash the Basic Auth password,
# patch apps/web/Dockerfile for the build-arg (setup.md step 4), then:
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build
```

## Memory budget (4 GB box, 2 GB swap)

| Service | Limit | Why |
|---------|-------|-----|
| worker  | 1024M | Chromium + up to 2 concurrent crawl jobs — the hog; capped so it can't kill the rest. |
| db      | 512M  | Postgres 16, small dataset + autovacuum. |
| api     | 512M  | Fastify + Prisma, I/O-bound. |
| web     | 512M  | Next.js standalone runtime, light. |
| redis   | 256M  | Queues + pub/sub only, not a data store. |
| caddy   | 128M  | Tiny Go binary. |
| **Σ**   | **~2.9G** | Leaves ~1 GB for the OS + FS cache; swap is a cushion, not a plan. Lowers room for future WordPress — revisit limits when it lands. |

If the worker OOMs: lower crawl concurrency 2→1 (see `setup.md` → Diagnostics).

## What the owner must supply

- **DB password** → `POSTGRES_PASSWORD` + inside `DATABASE_URL` (`.env`).
- **Basic Auth** user + `caddy hash-password` hash → `Caddyfile`.
- **`ANTHROPIC_API_KEY`** (direct; EU egress open, no proxy).
- **DNS**: `lab.remarka.biz` A-record → `178.105.192.76` (exists) must resolve
  before first start (Let's Encrypt HTTP-01).
- **OAuth (if used)**: register redirect URIs in Google / Yandex consoles:
  `https://lab.remarka.biz/api/integrations/{gsc,yandex}/callback`.

## Related docs

- `docs/server-hetzner.md` — server facts, SSH, rename note.
- `docs/deploy-ssh.md` — SSH runbook.

## db push vs migrate (known risk)

The project has **no Prisma migrations** (`packages/db/prisma/` has only
`schema.prisma`). The api container runs `prisma db push` on **every start**
(`apps/api/docker-entrypoint.sh`). This is kept as-is for this internal tool:
it's the only schema mechanism the project ships. Risks to know: `db push` runs
on each restart (idempotent when the schema is unchanged), and a **destructive**
schema change will make it refuse and the api container will fail to start —
back up (`backup.sh`) before pulling schema changes and check api logs. Moving to
authored migrations (`prisma migrate deploy`) would be the hardening step if this
ever becomes more than an internal tool.
