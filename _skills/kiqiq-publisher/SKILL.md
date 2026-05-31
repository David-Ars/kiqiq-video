---
name: kiqiq-publisher
description: Run final QC, AI disclosure and the YouTube upload. Triggers: publish, upload to YouTube, run the final QC.
---

# KiqIQ publisher and QC

## How Claude runs this
- Claude runs this step autonomously. The player comes from the kiqiq-produce run or the request; if missing, take the active episode under `Videos/output/`, and ask David only if the player is genuinely unclear. Create the episode folder from `Videos/output/_EPISODE-TEMPLATE/` if it does not exist.
- Obey the three hard rules in `Videos/_context/VIDEO-CHANNEL-BRIEF.md`: verify and log every stat (flag league-only vs all-comps); competitor videos are leads only, never copied; player imagery keeps the face abstract and non-literal (identity via build, hair, kit, posture, context, never an exact face or the name), team imagery uses no single face and no real crest or sponsor logo, plain kit.
- Apply the writing-tells doc to all text: `C:\Users\david\Documents\Kiqiq\kiqiq\docs\AI-WRITING-TELLS.md`. No em dashes, no flagged vocabulary, sentence-case headings.
- Update only this step's sections of `working-doc.md` / `fact-sheet.md`. Work without step-by-step narration; report the result.

## What Claude does

Claude runs the final check and the upload. SOP Role 8.

Run working-doc section 10 QC and `Videos/_context/AI-SAFEGUARDS-CHECKLIST.md`. Confirm every figure traces to a fact-sheet ID and no real footage was used. Drive YouTube Studio in David's connected Chrome to upload and set the title, description, tags and thumbnail, and tick the altered-or-synthetic-content disclosure if any image could read as realistic. This is GATE 2: get David's go before the final publish click.

On the upload, also set up these growth items (all in YouTube Studio via Chrome):
- **Subtitles.** Upload an accurate `.srt` built from the narration script and its timings (we own the script, so captions are near-free); improves accessibility, retention and search. Save it as `<slug>/script/<slug>.srt`.
- **End screen.** Add an end screen over the last ~20 seconds: subscribe element plus a next-video/playlist element, to drive session time.
- **Thumbnail A/B test.** Load the 2-3 thumbnails the packager produced into YouTube's Test & Compare so the platform picks the winner.
- **Playlists.** Add the video to the right thematic playlist (by league, era or position); create the playlist if it does not exist.
- **Post-publish retention loop.** A few days after publishing, pull the video's retention curve and audience-retention key moments from Studio, note where viewers drop, and write those lessons into the episode's working-doc section 10 so the scriptwriter can act on them next time.

## Next step (always end with this)

Do ONLY this step. When it finishes, STOP. Do not begin the next skill or any other step yourself. End the reply by telling David exactly what to run next, and wait:

> Next: run the episode is published. Start the next video with **kiqiq-researcher** (scan + fact sheet), then **kiqiq-produce** — input: the new player.
