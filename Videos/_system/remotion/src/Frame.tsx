import React from "react";
import { AbsoluteFill } from "remotion";
import { Preset, CHANNEL_MARK } from "./theme";

// Fixed KiqIQ frame: accent border, wordmark bottom-left on a navy chip,
// footer source line. Never changes per video. Sits above the scene.
export const Frame: React.FC<{ p: Preset; source?: string }> = ({ p, source = "official records, verified" }) => (
  <AbsoluteFill style={{ pointerEvents: "none" }}>
    <div style={{ position: "absolute", inset: 24, border: `4px solid ${p.accent}` }} />
    <div style={{ position: "absolute", left: 56, bottom: 56, background: "#0B1F3A",
      border: `2px solid ${p.accent}`, borderRadius: 14, padding: "10px 22px" }}>
      <span style={{ color: p.accent, fontFamily: p.font, fontWeight: 900, fontSize: 34 }}>{CHANNEL_MARK}</span>
    </div>
  </AbsoluteFill>
);
