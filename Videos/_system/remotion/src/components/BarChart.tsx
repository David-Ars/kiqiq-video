import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { Preset } from "../theme";
import { CountUp } from "./CountUp";

export type Bar = { label: string; value: number; highlight?: boolean };

export const BarChart: React.FC<{ p: Preset; title?: string; sub?: string; data: Bar[]; max?: number }> =
({ p, title, sub, data, max }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const top = max ?? Math.max(...data.map((d) => d.value)) * 1.12;
  return (
    <div style={{ position: "absolute", inset: 0, padding: "90px 100px", fontFamily: p.font }}>
      {title && <div style={{ color: p.text, fontSize: 52, fontWeight: 800 }}>{title}</div>}
      {sub && <div style={{ color: p.muted, fontSize: 26, marginTop: 8 }}>{sub}</div>}
      <div style={{ marginTop: 60, display: "flex", flexDirection: "column", gap: 40 }}>
        {data.map((d, i) => {
          const grow = spring({ frame: frame - 10 - i * 6, fps, config: { damping: 200 } });
          const w = interpolate(grow, [0, 1], [0, (d.value / top) * 100]);
          const col = d.highlight ? p.accent : p.neutral;
          const lab = d.highlight ? (p.labelDarkOnAccent ? p.bg : p.text) : p.text;
          return (
            <div key={i}>
              <div style={{ color: p.text, fontSize: 30, marginBottom: 10 }}>{d.label}</div>
              <div style={{ position: "relative", height: 64 }}>
                <div style={{ position: "absolute", inset: 0, background: p.grid, opacity: 0.25 }} />
                <div style={{ position: "absolute", top: 0, left: 0, bottom: 0, width: `${w}%`,
                  background: col, display: "flex", alignItems: "center", justifyContent: "flex-end", paddingRight: 18 }}>
                  <span style={{ color: lab, fontWeight: 800, fontSize: 28 }}>
                    <CountUp value={d.value} duration={20} size={28} font={p.font} color={lab} />
                  </span>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
