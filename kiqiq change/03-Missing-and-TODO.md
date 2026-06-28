# Missing things + TODO for the new laptop

The point of this folder is so the new machine *understands* KiqIQ. But understanding isn't the same as having the working files. This is the gap list: what is **not** in this folder and must be brought across or decided, ordered by how badly it blocks work.

## A. Must be brought across manually (not in this folder)

These cannot be copied here from this session — they live in repos/services this folder has no access to.

1. **The app source code repo** — `C:\Users\david\Documents\Kiqiq\kiqiq` (remote `github.com/David-Ars/kiqiq`). This is the entire live website: all `src/`, `docs/`, `supabase/migrations/`, `package.json`, config. On the new laptop, `git clone` it (cleaner than copying `node_modules`). Without this, "current site structure" is only documented, not present.
2. **`.env.local` / secrets** — never in git. Includes at minimum: Clerk keys, Stripe keys + webhook secret, Supabase URL + service key, Resend key, Sentry DSN, PostHog key, `DATA_PROVIDER=thestatsapi` + TheStatsAPI key, the (to-be-removed) `API_FOOTBALL_KEY`, `PREVIEW_ACCESS_PASSWORD` + `PREVIEW_ACCESS_TOKEN`, `KIQIQ_LIFETIME_PRO_CLERK_IDS`. **Action:** export the full env from Vercel (Production/Preview/Dev) and from local `.env.local`; move them via a password manager / secure channel, not email or git.
3. **`docs/` folder from the app repo** — the canonical written decisions referenced throughout memory but not present here:
   - `docs/AI-WRITING-TELLS.md` (applies to all KiqIQ text)
   - `docs/PRICING-AND-PACKAGES.md` + `docs/PRICING-IMPLEMENTATION-PLAN.md`
   - `docs/ENV-VARIABLES.md`
   - `docs/GAMBLING-LAW-CONSULTATION-BRIEF.md`
   - `docs/BLOG-CANNIBALISATION-AUDIT.md`, `docs/BETTING-PAIRS-AUDIT.md`, `docs/ASK-NEXT-STEPS.md`, `docs/ASK-PERFECTION-PLAN.md`, `docs/AI-CONTEXT-COVERAGE-REVIEW.md`
4. **Supabase project access** — DB lives in the cloud (free tier). Bring the project ref + service role key; the schema is reproducible from `supabase/migrations/` in the repo.
5. **Service-account logins** — Vercel, Supabase, Clerk, Stripe, Resend, PostHog, Sentry, the domain registrar (Hostinger), GitHub. Make sure the new laptop's browser/CLI is signed into all of them.
6. **Local toolchain** — Node (version that builds Next 16), npm, git, the Vercel CLI, and (note) David's shell is **Windows PowerShell, Spanish locale** — use `;` not `&&`.

## B. Decisions to make before the pivot build starts

1. **Greenfield vs fork.** The stack doc recommends greenfield. Decide and write it down. Recommendation: greenfield repo, copy over only auth/billing/email/Sentry/PostHog plumbing; leave all football/prediction/betting code behind.
2. **What happens to the live football site?** Keep it running during the pivot, sunset it, or 301 it to the new product? This affects domain usage (`kiqiq.com`), SEO equity from the 222-article blog, and existing paying subscribers.
3. **Existing subscribers + Stripe.** There are live Stripe subscriptions (and David's lifetime-Pro row). Decide migration/refund/grandfathering before repointing the domain.
4. **Domain + email.** `kiqiq.com` is the transactional sender (Resend, verified). The outreach engine needs a **separate** sending domain for cold email — pick and register it early (warmup takes weeks).
5. **Blog/SEO equity.** 222 evergreen articles rank. Decide whether any are repurposed for the sponsorship audience or retired with redirects.
6. **New name/positioning check.** Confirm "KiqIQ" still fits a B2B club-sponsorship product, or whether a sub-brand is wanted. (Spelling is always **KiqIQ**.)

## C. Gaps in this handover bundle itself (nice-to-have, not blocking)

- This folder documents the app from memory + the two stack docx files; it does **not** contain a file-by-file map of `src/`. If you want that, generate a directory tree + route list from the cloned repo on the new laptop.
- No screenshots of the current UI are included. If a visual record of the old product is wanted before sunset, capture key pages.
- No copy of the Supabase schema is included here (it's reproducible from migrations in the repo).

## D. First moves on the new laptop (suggested order)

1. Sign into all services (section A.5).
2. `git clone` the app repo; restore `.env.local` from the password manager.
3. `npm install`, build, and run locally to confirm the old site still works as a reference.
4. Read the `docs/` files listed in A.3 — they are the binding written decisions.
5. Make the greenfield-vs-fork and old-site-fate decisions (section B).
6. Start the pivot build per the phase order in `02-Sponsorship-Pivot-and-Stack.md`.
