# Remarka Lab · Monitor — production setup runbook (lab.remarka.biz)

Path A: internal tool, whole site behind Caddy Basic Auth on a Hetzner CX23
(2 vCPU / 4 GB / swap 2 GB, Falkenstein/EU). All commands run **on the server as
`massimo`** (member of the `docker` group). Copy-paste as-is.

Related: `docs/server-hetzner.md` (server facts), `docs/deploy-ssh.md` (SSH).

---

## 0. Layout on the server

The code is already cloned at `~/remarka-lab` (a git repo; the platform lives in
the `sitelens` subfolder). These three deploy files live in this repo
(`deploy/remarka-lab/`): `docker-compose.prod.yml`, `Caddyfile`,
`.env.prod.template`. **Put them next to the platform's base compose**, i.e.
inside `~/remarka-lab/sitelens/`, and run compose from there.

```bash
cd ~/remarka-lab/sitelens

# Copy the three deploy files in (adjust the source path to wherever you fetched
# this studio repo on the server; scp from your Mac also works).
cp /path/to/studio/deploy/remarka-lab/docker-compose.prod.yml .
cp /path/to/studio/deploy/remarka-lab/Caddyfile .
cp /path/to/studio/deploy/remarka-lab/.env.prod.template .

ls -1 docker-compose.yml docker-compose.prod.yml Caddyfile .env.prod.template
```

From now on every compose command is:

```bash
docker compose -f docker-compose.yml -f docker-compose.prod.yml <cmd>
```

---

## 1. Create `.env` from the template

```bash
cd ~/remarka-lab/sitelens
cp .env.prod.template .env
```

Generate a DB password and paste it into **both** `POSTGRES_PASSWORD` and the
`DATABASE_URL` in `.env`:

```bash
openssl rand -base64 24 | tr -d '/+='
```

Then edit `.env` and fill:
- `POSTGRES_PASSWORD` and the password inside `DATABASE_URL` (same value);
- `ANTHROPIC_API_KEY` (direct key from console.anthropic.com);
- optional integration keys (GSC / Yandex / PSI) if used now — otherwise leave
  blank and add later.

```bash
nano .env      # or vim
chmod 600 .env
```

---

## 2. Generate the Basic Auth hash and put it in the Caddyfile

Pick a username + password for the whole site, then hash the password:

```bash
docker run --rm caddy:2-alpine caddy hash-password --plaintext 'YOUR-STRONG-PASSWORD'
```

Copy the printed `$2a$...` bcrypt hash. Edit `Caddyfile` and replace the
placeholder line under `basic_auth` with your username + hash:

```
	basic_auth {
		youruser $2a$14$....your-real-hash....
	}
```

> The placeholder in the file is the hash for the password `changeme` — it will
> NOT protect anything real. Replace it.

---

## 3. (One-time) confirm DNS points at the server

Caddy needs `lab.remarka.biz` → `178.105.192.76` resolving before it can get a
Let's Encrypt cert over HTTP-01.

```bash
dig +short lab.remarka.biz    # should print 178.105.192.76
```

If it does not yet resolve, wait for the A-record to propagate before step 5.

---

## 4. Patch the web Dockerfile to accept the build-arg (REQUIRED, one line pair)

`NEXT_PUBLIC_API_URL` is inlined by Next.js at **build** time. The platform's
`apps/web/Dockerfile` does not yet declare the ARG, so the build-arg from the
override would be ignored and the bundle would fall back to `localhost:3001`
(the app would be broken in the browser). Add two lines to the **build** stage,
right **before** the `RUN pnpm --filter @sitelens/web build` line:

```bash
cd ~/remarka-lab/sitelens
# Insert ARG + ENV just before the web build step:
sed -i 's#^RUN pnpm --filter @sitelens/web build#ARG NEXT_PUBLIC_API_URL\nENV NEXT_PUBLIC_API_URL=$NEXT_PUBLIC_API_URL\nRUN pnpm --filter @sitelens/web build#' apps/web/Dockerfile

# Verify it now looks like this:
grep -n -A0 'NEXT_PUBLIC_API_URL\|pnpm --filter @sitelens/web build' apps/web/Dockerfile
```

Expected result (the three lines, in order):

```
ARG NEXT_PUBLIC_API_URL
ENV NEXT_PUBLIC_API_URL=$NEXT_PUBLIC_API_URL
RUN pnpm --filter @sitelens/web build
```

> This edits the on-server clone only (it's a git checkout — `git diff` shows the
> change; it survives until you `git checkout`/`git pull`). See "Updating" for
> re-applying after a pull.

---

## 5. Build and start

Pre-flight: confirm the two compose files merge cleanly (checks the `!reset`
tag support and .env interpolation; prints the merged config or an error):

```bash
cd ~/remarka-lab/sitelens
docker compose -f docker-compose.yml -f docker-compose.prod.yml config --quiet && echo "COMPOSE CONFIG OK"
```

Expect `COMPOSE CONFIG OK`. If it errors, stop and report the message. Then:

```bash
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build
```

First build is slow (Chromium in the worker image, full pnpm install). Watch it:

```bash
docker compose -f docker-compose.yml -f docker-compose.prod.yml ps
docker compose -f docker-compose.yml -f docker-compose.prod.yml logs -f caddy
```

Caddy will log the cert issuance for `lab.remarka.biz`. Give it up to a minute
after DNS is live.

---

## 6. Verify

```bash
# Health check through Caddy (Basic Auth required). Expect: {"status":"ok",...}
curl -u youruser:YOUR-STRONG-PASSWORD https://lab.remarka.biz/health

# Without credentials you should get 401:
curl -i https://lab.remarka.biz/health | head -n 1     # HTTP/2 401
```

Then open `https://lab.remarka.biz` in a browser, enter the Basic Auth
user/password, and confirm the dashboard loads. Create a test project and start
a crawl — the live progress bar uses the WebSocket (`wss://.../ws/...`); if it
updates in real time, the `/ws` routing and the baked `NEXT_PUBLIC_API_URL` are
correct.

---

## Diagnostics

```bash
cd ~/remarka-lab/sitelens
BASE="-f docker-compose.yml -f docker-compose.prod.yml"

# All containers + health status
docker compose $BASE ps

# Logs (pick a service): caddy | web | api | worker | db | redis
docker compose $BASE logs -f api
docker compose $BASE logs --tail=200 worker

# Memory use per container (watch the worker under a crawl)
docker stats --no-stream

# Is the DB schema present? (api runs `prisma db push` on start)
docker compose $BASE exec db psql -U sitelens -d sitelens -c '\dt' | head
```

### TLS / cert problems
- Cert not issued → check DNS (`dig +short lab.remarka.biz`) and that ports
  80/443 are open (`sudo ufw status`); Caddy needs 80 reachable for HTTP-01.
- `docker compose $BASE logs caddy` shows ACME errors verbatim.

### Browser can log in but API calls fail / point at localhost
- The web image was built without the build-arg. Re-do **step 4**, then
  rebuild **only web** with no cache:
  ```bash
  docker compose $BASE build --no-cache web && docker compose $BASE up -d web
  ```

### OOM (out of memory) — worker gets killed
The worker (Chromium + 2 concurrent crawl jobs) is the memory hog and is capped
at 1 GB. If `docker compose $BASE logs worker` shows it being OOM-killed, or a
crawl kills other services:
1. Lower **BullMQ crawl concurrency 2 → 1** in
   `apps/worker/src/workers/crawl-worker.ts` (the `concurrency: 2` in
   `createCrawlWorker`), then rebuild the worker:
   ```bash
   docker compose $BASE build worker && docker compose $BASE up -d worker
   ```
2. And/or lower the **per-crawl HTTP concurrency** when starting a crawl (crawl
   settings `concurrency`, default 5) and keep `renderJs` off (Chromium is only
   spawned when JS-rendering is enabled).
3. The box has 2 GB swap as a cushion, but swap-thrashing is slow — prefer
   lowering concurrency.

---

## Updating (new code from git)

```bash
cd ~/remarka-lab
git pull                         # updates the whole clone incl. sitelens/
cd sitelens

# Re-apply the web Dockerfile patch if the pull reverted it (step 4). Check:
grep -q 'ARG NEXT_PUBLIC_API_URL' apps/web/Dockerfile || echo "RE-APPLY STEP 4"

# Rebuild + restart
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build

# Clean up old images occasionally
docker image prune -f
```

> `prisma db push` runs automatically on every api start and syncs the schema.
> There are **no Prisma migrations** in this project (see "db push vs migrate"
> in `README.md`), so schema changes from a pull are applied on restart. For a
> destructive schema change `db push` will refuse and the api container will
> fail to start — back up first (see `backup.sh`) and read the api logs.

---

## Cabinet (client portal, K1)

Separate app (`apps/cabinet`), same server, same Postgres — see
`docs/piano-cabinet-k1.md` for the full design. Public client login at
**`cab.remarka.biz`**, deliberately NOT behind Basic Auth (the app does its
own auth: magic-link email → server-side session cookie). Adds one container
(`cabinet`, 384M limit) and one Caddy site block; `lab.remarka.biz` and its
Basic Auth are untouched.

### Prerequisites specific to Cabinet

1. **DNS**: `cab.remarka.biz` → `178.105.192.76` (A-record) must resolve
   BEFORE first start, same as step 3 above for `lab.remarka.biz`:
   ```bash
   dig +short cab.remarka.biz    # should print 178.105.192.76
   ```
2. **Brevo API key** (owner decision 16.07.2026 — EU region, GDPR). Get one
   at https://app.brevo.com after verifying the `remarka.biz` sending domain
   (SPF/DKIM/DMARC — Brevo's domain authentication page gives you the exact
   DNS records to add). Free tier (300 emails/day) is enough for magic-link
   volume. **Without a key**, the cabinet still starts and serves pages, but
   runs in **dev mode**: instead of emailing the login link, it logs the URL
   to the container's stdout — fine for a first smoke test, not for real
   clients (nobody actually receives a login link).

### Deploy Cabinet (after `lab.remarka.biz` is already running)

```bash
cd ~/remarka-lab/sitelens

# 1) Pull the branch with the cabinet app (or your normal update flow if
#    it has already been merged to the branch you deploy from).
cd ~/remarka-lab && git fetch origin && git checkout claude/cabinet-k1 && git pull
cd sitelens

# 2) Add the Cabinet variables to the EXISTING .env (do not overwrite it —
#    it already holds POSTGRES_PASSWORD/DATABASE_URL/etc from the lab.*
#    setup). Append, then edit in the real values:
cat >> .env <<'EOF'
CABINET_URL=https://cab.remarka.biz
BREVO_API_KEY=
EMAIL_FROM=no-reply@remarka.biz
MAGIC_TTL_MINUTES=15
SESSION_TTL_DAYS=7
EOF
nano .env      # fill BREVO_API_KEY (or leave empty for dev-mode smoke test first)

# 3) Confirm the merged compose config is still valid with the new service:
docker compose -f docker-compose.yml -f docker-compose.prod.yml config --quiet && echo "COMPOSE CONFIG OK"

# 4) Build and start ONLY the new pieces (cabinet + caddy reload for the new
#    site block) — this does not touch db/api/worker/web:
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build cabinet caddy

# 5) Watch the cert issuance for the new host:
docker compose -f docker-compose.yml -f docker-compose.prod.yml logs -f caddy
```

### Verify

```bash
BASE="-f docker-compose.yml -f docker-compose.prod.yml"

# Should return the login page (NO Basic Auth prompt, unlike lab.*):
curl -i https://cab.remarka.biz/login | head -n 1     # HTTP/2 200

# Container present and healthy, memory within the 384M cap:
docker compose $BASE ps cabinet
docker stats --no-stream cabinet

# Cab_* tables exist in the shared DB (created by prisma db push, additive —
# see piano-cabinet-k1.md §7.4 on why this is safe):
docker compose $BASE exec db psql -U sitelens -d sitelens -c '\dt' | grep cab_
```

### Onboard the first pilot client

Manual account creation (K1 has no self-service signup):

```bash
docker compose -f docker-compose.yml -f docker-compose.prod.yml \
  exec cabinet node_modules/.bin/tsx ../../packages/db/prisma/seed-cabinet.ts \
  --email cliente@esempio.it --client "Nome Cliente S.r.l." --locale it \
  --project "Sito aziendale"
```

(If running the seed from a dev machine against the prod DB instead, use
`pnpm --filter @sitelens/cabinet seed -- --email ... --client ... --locale
it` with `DATABASE_URL` pointed at the server — see
`packages/db/prisma/seed-cabinet.ts` header for both modes.)

Then send the client to `https://cab.remarka.biz/login` to request their
first magic link.

### Diagnostics specific to Cabinet

- `docker compose $BASE logs -f cabinet` — dev-mode magic-link logging shows
  up here (`[cabinet:email:dev-mode] ... would send magic link to ...`) if
  `BREVO_API_KEY` is empty; Brevo send failures also log here (never the raw
  token, only an HTTP status).
- If `cab.remarka.biz` doesn't get a cert: same TLS/cert troubleshooting as
  `lab.remarka.biz` above (DNS + ports 80/443).
- Memory: 384M is comfortable for Next standalone with no Chromium. If it
  ever needs headroom, see piano-cabinet-k1.md §7.3 for the fallback (320M
  floor, or trim elsewhere in the budget) — do not raise it without checking
  the box's total (currently 3328M summed limits on a 4 GB host).
