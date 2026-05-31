import React from "react";
import { Preset } from "../theme";
import { CountUp } from "./CountUp";
import { KineticText } from "./KineticText";

export type Stat = { value: number; label: string; suffix?: string; highlight?: boolean };

export const StatCard: React.FC<{ p: Preset; title?: string; stats: Stat[] }> = ({ p, title, stats }) => (
  <div style={{ position: "absolute", inset: 0, padding: "90px 100px", fontFamily: p.font,
    display: "flex", flexDirection: "column", justifyContent: "center" }}>
    {title && <KineticText color={p.text} size={52} weight={800} style={{ marginBottom: 70 }}>{title}</KineticText>}
    <div style={{ display: "flex", gap: 100, justifyContent: "center" }}>
      {stats.map((s, i) => (
        <div key={i} style={{ textAlign: "center" }}>
          <CountUp value={s.value} duration={28} suffix={s.suffix ?? ""} size={150}
            color={s.highlight ? p.accent : p.text} font={p.font} />
          <div style={{ color: p.muted, fontSize: 30, marginTop: 16 }}>{s.label}</div>
        </div>
      ))}
    </div>
  </div>
);
