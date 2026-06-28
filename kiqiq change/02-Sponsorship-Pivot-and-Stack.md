# KiqIQ → club-sponsorship platform (the pivot)

The full recommended build is in `KiqIQ-Sponsorship-Platform-Stack.docx` (this folder). This file is the one-page orientation.

## The new product

KiqIQ pivots from a football-prediction/betting product to a platform that **helps UK football clubs win sponsors**. Core surfaces:

- Club profiles (clubs are organisations with several staff).
- A sponsor directory.
- In-app messaging between clubs and sponsors.
- Brokered matching (right sponsors for each club by sector, budget, locality).
- A gated resources library (sponsorship guides, pitch-deck templates, contract checklists).
- **Done-for-you automated sponsor outreach** — personalised emails at scale, reply tracking, follow-ups.

**Monetisation:** clubs pay a subscription for resources + automated outreach (meter outreach volume as a usage component).

## Three things that make this harder than a normal directory (they drive the stack)

1. **Two-sided platform with org accounts** — clubs (orgs, multi-staff) and sponsors (individual accounts) are different account types.
2. **An outreach engine** — deliverability + workflow problem, not CRUD. This is the defensible core and the #1 technical risk.
3. **Matching** — embeddings + search, not hand-coded filters.

## Recommended greenfield stack (one pick per layer)

- **Core:** Next.js 16 + Vercel; Tailwind v4 + shadcn/ui; React Hook Form + Zod.
- **Data/search/matching:** Supabase Postgres + Drizzle ORM; Typesense (faceted/typo-tolerant search); pgvector + embeddings (matching).
- **Accounts/billing:** Clerk **Organizations** (club = org); Stripe Billing (tiers + metered outreach).
- **Outreach engine (the differentiator):** Inngest (durable multi-step workflows — do *not* hand-roll with cron+setTimeout); Smartlead/Instantly → Amazon SES at volume (cold-outreach deliverability, on a **separate sending domain** from transactional email); Claude via Vercel AI SDK (personalised copy + reply drafts).
- **Content/comms/media:** Sanity (resources CMS); Supabase Realtime + Postgres for in-app messaging (graduate to Stream Chat only if chat becomes central); Cloudflare R2 (logos, media kits, decks — zero egress fees).
- **Observability/tooling:** PostHog + Sentry; Biome, Vitest, Playwright; GitHub Actions CI.

## Suggested build order

Phases 1–2 = a shippable paid product (clubs pay for profiles + resources). Phases 3–4 = the outreach engine + matching that justify a higher tier. Phase 5 = deepen engagement (messaging, etc.). Don't wire every tool on day one.

**Rough launch run-rate:** ~£100–180/mo before outreach volume grows; outreach sending and Typesense are the lines that scale first.

## What carries over from the old stack vs what's new

- **Keep (as patterns/accounts, rebuilt greenfield):** Next.js + Vercel, Supabase Postgres, Clerk, Stripe, PostHog, Sentry, Claude.
- **Drop:** all live sports-data (API-Football / TheStatsAPI), prediction/odds/Poisson engines, value-bets/trap-games/geo-gating, the football `/ask` intent system, **and all existing email flows** (none are wanted — rebuild transactional email only when the new product needs it, and keep cold-outreach mail on a separate domain).
- **Add:** Clerk Organizations, Typesense, pgvector matching, Inngest, Smartlead/SES outreach (separate domain), Sanity, Cloudflare R2, Drizzle.

## Open decision: greenfield vs. fork

The stack doc recommends **greenfield**. Decide explicitly whether to start a fresh repo or fork the existing app. Most of the football-specific code (predictions, odds, fixtures, geo-gating, betting surfaces) is dead weight for the new product, which argues for greenfield with selective copy-over of auth/billing/email plumbing. See `03-Missing-and-TODO.md`.
