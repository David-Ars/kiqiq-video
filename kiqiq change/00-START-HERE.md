# KiqIQ change — start here

Handover bundle created 28 June 2026 for moving KiqIQ to the new laptop and pivoting it from a football-intelligence site into a **UK club-sponsorship platform**.

Read in this order:

1. **`01-Current-Site-State.md`** — what KiqIQ is *today*: structure, stack, shipped features, live business decisions, launch status, repo layout.
2. **`02-Sponsorship-Pivot-and-Stack.md`** — the new product and the recommended greenfield stack (one-page orientation over the docx).
3. **`03-Missing-and-TODO.md`** — what is **not** in this folder and must be brought across (app repo, secrets, `docs/`), plus the decisions to make before building.

Source documents (full detail):

- **`KiqIQ-Tech-Stack.docx`** — full review of the existing/old stack, costs, trade-offs.
- **`KiqIQ-Sponsorship-Platform-Stack.docx`** — full recommended new-build stack, layer by layer, with build phases and launch costs.

## The one-paragraph version

KiqIQ is a launched football-intelligence web app (Next.js 16 / Vercel / Supabase free tier / Clerk / Stripe / Claude+OpenAI) at **kiqiq.com**, fixed cost ~£19/mo. It's pivoting to a platform that helps UK clubs win sponsors — club profiles, sponsor directory, matching, in-app messaging, a gated resources library, and automated outreach, sold to clubs by subscription. The recommended path is a **greenfield** rebuild that keeps the auth/billing/email plumbing and the outreach engine (Inngest + Smartlead/SES + Clerk Organizations + pgvector matching) as the defensible core, and drops everything football-data/betting-specific.

## Two important reminders

- **Code and secrets are not in this folder.** The live app lives in a separate repo (`Documents\Kiqiq\kiqiq`) and `.env.local`/Vercel hold the keys. See `03-Missing-and-TODO.md` section A.
- **Spelling is always `KiqIQ`.**
