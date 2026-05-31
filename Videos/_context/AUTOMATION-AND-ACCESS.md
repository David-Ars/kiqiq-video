# Automation and access (minimal manual)

Goal: you do as little as possible. Claude runs the pipeline. You pick the player, approve twice, and keep two things connected.

## Who does what

| Step | Run by |
|------|--------|
| Daily API-Football pull | Automated on your PC (scheduled task, registered once). Claude reads the data from the shared folder. |
| Competitive scan (YouTube) | Claude, through Claude in Chrome (YouTube transcript panels + your free VidIQ web account) |
| Research and fact sheet | Claude, from the archive plus web verification |
| Angle and thesis | Claude proposes. YOU approve (gate 1). |
| Art style | Claude (the angle decides it) |
| Charts | Claude |
| Script | Claude drafts, AI-writing-tells swept |
| Narration audio | Claude writes the script; `tts.py` renders it with your ElevenLabs key |
| AI imagery | Claude, through the Gemini image tool |
| Video assembly (stills, audio, motion text) | Claude, ffmpeg/moviepy |
| Thumbnail, titles, description, tags | Claude |
| Final cut review | YOU approve (gate 2) |
| Upload and disclosure | Claude drives YouTube Studio in your Chrome. You confirm publish. |

Your manual footprint per video: pick the player, approve the angle, approve the final cut, confirm publish. Plus the one-time key setup below. You can waive either gate and I run straight through.

## Why a few steps touch your machine or browser

The sandbox cannot reach ElevenLabs, Gemini or YouTube over the network (all blocked). So images go through the Gemini tool (no sandbox network needed), web actions go through your connected Chrome, and ElevenLabs runs as a small local script with your key. Everything else runs in the sandbox.

## Accesses to set up now

1. ElevenLabs API key. elevenlabs.io, sign in, top-right profile menu, "API Keys" (or Settings, API Keys), create a key, copy it. Save it into a file named `elevenlabs.key` in `Videos/_system/` (Notepad, paste, save; if Windows adds `.txt`, that is fine, the script accepts it). That is all I need to render narration with `tts.py`.
2. Keep Chrome connected and logged in. The Claude in Chrome extension is already connected. Stay signed into your YouTube channel, your free VidIQ account and ElevenLabs in that browser so I can drive the scan, the VidIQ trend/idea research and the upload. VidIQ runs on the free tier through the browser, so there is no paid MCP and no extra key.
3. API-Football daily pull. Confirm the scheduled task is registered (run `_system/register_daily_pull.ps1` once if not). It already works.

Already in place, no setup: Chrome connected, Gemini image tool, Inter fonts, the KiqIQ logo, the chart and thumbnail engine.

## Optional later

- YouTube Data API (OAuth) if you ever prefer API upload over the Chrome route. Not needed now.
- Inter Black font drop-in for slightly heavier thumbnail text.
