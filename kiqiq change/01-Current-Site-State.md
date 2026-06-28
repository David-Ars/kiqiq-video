# KiqIQ — current site state (handover snapshot)

Prepared 28 June 2026 for the move to the new laptop. This is the reference the new machine needs to understand what KiqIQ is *today*, before the sponsorship pivot rebuild begins. Everything here describes the **existing live product** (the football-intelligence site at kiqiq.com). The new direction is covered in `02-Sponsorship-Pivot-and-Stack.md`.

> Source note: this snapshot is compiled from project memory and the two stack documents in this folder. The actual application source code is **not** in this folder (see `03-Missing-and-TODO.md` for where it lives and what must be brought across).

---

## 1. What KiqIQ is today

> **Reality check (28 June 2026, per David):** **Nothing is live except the homepage and the blog.** There are **no subscribers**. All other surfaces (`/ask`, football, value-bets, trap-games, fantasy, calculators, live match views, pricing/checkout) and all email flows are **not in active use** and are being stripped out for the pivot. The football-product detail below is recorded as *what exists in the codebase* so the new laptop knows what's there to remove or salvage — not as a running service.

KiqIQ's domain is **https://kiqiq.com** (custom domain — not the old `kiqiq.vercel.app` staging URL). What's actually live to the public is the **homepage + the evergreen blog**. The rest of the football-intelligence build (AI analyst, betting-edge tools, fantasy, calculators) exists in the repo but is being retired as part of the pivot.

## 2. Tech stack (existing app)

Full detail is in `KiqIQ-Tech-Stack.docx`. Summary, verified against `package.json` and `.env.local` on 28 June 2026:

- **Framework:** Next.js 16 + React 19 (App Router, Server Components), internationalised routes (`[locale]`).
- **Hosting:** Vercel (Pro) — edge, cron, CDN.
- **Database:** Supabase — **free tier** (Postgres + storage). First likely paid step is Supabase Pro when free DB limits hit.
- **Auth:** Clerk — **free tier**, email-only signup + CAPTCHA + disposable-email blocklist. David refuses Clerk Pro (phone signup is Pro-only).
- **Payments:** Stripe (Billing + subscriptions), Svix for webhook verification.
- **AI `/ask` layer:** hybrid Anthropic Claude + OpenAI. Note: route.ts still used gpt-4o-mini at the time of the pricing plan; Haiku migration was the gating step for the new pricing.
- **Rate limiting:** in-memory fallback — **Upstash Redis is NOT provisioned** (no keys set).
- **Email:** Resend was wired for transactional email (welcome, digest, contact-form), sender domain `kiqiq.com` verified. **All email flows are being deleted** (see §5) — none should remain active.
- **Monitoring/analytics:** Sentry (free tier), PostHog, Vercel Speed Insights.
- **Football data:** API-Football (was the live provider) → **migrated to `DATA_PROVIDER=thestatsapi`** in production (2026-05-09). API-Football was code-retired 2026-05-10 **but `API_FOOTBALL_KEY` is still set in `.env.local` and Vercel**, so live pulls can still happen — remove the key from both to guarantee zero pulls.

**Real fixed cost today: ~£19/mo** (Vercel + domain). Everything else is on free tiers. The ~£195/mo Spanish autónomo cuota is a personal founder cost, not part of the platform.

## 3. Key shipped architecture (so nothing gets "re-fixed" blindly)

- **3-tier prediction resolver** (`src/lib/fixture-prediction.ts`): odds-consensus → api-football model → baseline 45/27/28 safety net. Fixes the historic "every fixture shows 45%" bug. Backed by 4 layers of observability (Tier-2 fallback, "Odds TBC" UI placeholder, `/admin/system-health` coverage row, Sentry breadcrumbs+alerts). The redundancy is intentional — do not strip it.
- **Live match data** via `getMatchSlate()` in `src/lib/match-slate.ts` drives `/football`, `/value-bets`, `/trap-games`, `/insights/this-weekend`, `/football/predictions`, `/football/[league]`. Static `src/lib/fixtures.ts` only still backs the per-slug pre-match detail pages.
- **Live match view** at `/football/live/[fixtureId]` — Sofascore-style header + `MatchStatsPanel` + Poisson scoreline predictions (`src/lib/poisson.ts`). `FixtureRow.tsx` auto-routes live/finished fixtures here.
- **`/ask` AI assistant:** intent-based context injection, anti-hallucination guards, topic-carryover (always-on), markdown comparison + standings tables, follow-up coherence. Intent taxonomy with a classifier (`src/lib/ai-intent-classifier.ts`). **Trap:** `validIntents` whitelist silently drops any new intent not added to the list — adding an intent is a 4-file change.
- **Blog corpus:** 222+ evergreen articles, 7 pillars, curated hub at `/blog`, cluster-based related-article wiring, cannibalisation 301s in `next.config.ts`.
- **Geo-gating** (`src/lib/geo-gating.ts`): `/value-bets` and `/trap-games` restricted to the allow-listed markets; others redirect to `/licensing-jurisdictions`.

## 4. Business decisions from the football product (historical reference)

These governed the old football product. With nothing live but homepage + blog and no subscribers, most are **moot for the pivot** — kept here only so context isn't lost. The one item that still applies to all future work is the **writing standard** at the end.


- **Pricing (2026-05-25):** four tiers — Free (£0, 3 *lifetime* queries), Starter £9.99/100 (Haiku), Pro £19.99/200 (Sonnet), Pro Max £39.99/500 (Sonnet + selective Opus, hard cap 30 Opus/mo). Plus one-off week packs and top-ups. Hard loss-prevention controls are mandatory (Opus caps, spend kill-switch at 120% budget, one-pack-per-card/IP/30-day, strict 3-lifetime free tier). Canonical doc: `docs/PRICING-AND-PACKAGES.md`. **Declined (do not re-propose):** annual pre-pay, refer-a-friend, pause subscription, auto-billing trials.
- **Target market: 33 countries**, locked 2026-05-15 (`src/lib/geo-gating.ts` → `LAUNCH_SAFE_COUNTRIES`). No new market without engaged local legal counsel — competitor presence is *not* evidence of safety.
- **Data layer:** API-Football only (no StatsBomb/Opta/FBref). No affiliate-recruitment program (disclosed affiliate links in content are fine). Mobile app is post-web only.
- **Refunds:** none for used AI access; cancellation stops next renewal, access kept to period end. Stripe checkout has an explicit consent checkbox.
- **Writing standard:** the AI-writing-tells doc (`docs/AI-WRITING-TELLS.md` in the app repo) applies to **all** text — no em dashes, banned vocab list, no "not just X but Y", sentence-case headings.

## 5. Live status + what's being stripped (28 June 2026)

**Live to the public:** homepage + blog only. **No subscribers.** Stripe/pricing were never taken into real revenue.

Being removed for the pivot (exists in code, not wanted):

- **All email flows — delete these.** Welcome email, weekly digest / NotifyForm, contact-form sends, and any cron-driven mail. Remove the Resend integration and `RESEND_API_KEY`, the email templates, the NotifyForm/"Subscribe to digest" UI, and any webhook/cron that triggers mail. (This must be done in the app repo — not possible from this handover folder; see `03-Missing-and-TODO.md` §A.)
- All non-homepage/non-blog surfaces: `/ask`, `/football*`, `/value-bets`, `/trap-games`, `/insights`, fantasy, calculators, live match views, `/admin`.
- Stripe checkout + pricing pages, geo-gating, the AI cost-tracking and abuse-prevention machinery.

> Because the pivot is greenfield (see `02`), the cleanest route is to **not** carry these forward at all rather than delete them file-by-file in the old repo — keep the old repo as a read-only reference and build fresh. Confirm this in the greenfield-vs-fork decision.

## 6. Two separate repos — do not cross them

- **App:** `C:\Users\david\Documents\Kiqiq\kiqiq` → remote `github.com/David-Ars/kiqiq`. This is the live website (all `src/` code, `docs/`, `supabase/migrations/`).
- **Video/brand system:** `C:\Users\david\Documents\Claude\Projects\KiqIQ` (this folder's parent) → dedicated video repo. Separate project; never push one to the other's remote.

This `kiqiq change` folder lives inside the video-system folder and is a handover bundle, not a repo of its own.
