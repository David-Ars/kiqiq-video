## Repository (read first)

This folder is the **KiqIQ video system** and is its OWN git repository, separate from the Next.js app. Do NOT push it to the app's remote `github.com/David-Ars/kiqiq` (that is the app at `Documents\Kiqiq\kiqiq`). This repo's remote is the dedicated video repo (e.g. `github.com/David-Ars/kiqiq-video`). The two are unrelated projects; never cross-push. The API-Football archive (`Videos/_data/`), `node_modules/`, and key files are git-ignored.

## File I/O (read first)

Read and write episode files (working-doc.md, fact-sheet.md, episode JSON, scripts) with the Read/Write/Edit tools, NOT bash `cat`/heredoc. The sandbox bash mount can lag or show a file truncated when it is actually complete (e.g. a fact sheet that "ends at F8"): trust the Read tool, which is authoritative for the real files, and never act on or "repair" an apparent truncation seen only in bash. Files created by bash (including Python tooling like `thumb.py`/`example_charts.py`) may not sync to the real folder; for charts and thumbnails, render them, then verify they appear in the episode folder, and if the mount has not synced, write the deliverable into the outputs area and surface it with present_files. Use bash for computation, not for delivering files the user must see.

## How to Navigate This Project

Read relevant context file inside the /_context/ before any task. This is the brand knowledge that shapes every output.

Check /_skills/ to find and invoke the right project-specific skill for the task first before using any global skills. If similar skills exist that serve same purpose, the project-specific skills should override and be prioritized.

Save outputs to the /output subfolder of the relevant channel. Use /input for source materials.

# KiqIQ Constitution & Style Guide

## 1. Brand & Identity
- **Spelling:** ALWAYS KiqIQ.
