import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { FONT } from "../theme";

export const KineticText: React.FC<{
  children: React.ReactNode; delay?: number; color?: string; size?: number;
  weight?: number; font?: string; style?: React.CSSProperties;
}> = ({ children, delay = 0, color, size = 56, weight = 800, font = FONT, style }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const o = spring({ frame: frame - delay, fps, config: { damping: 200 } });
  const y = interpolate(o, [0, 1], [26, 0]);
  return (
    <div style={{ opacity: o, transform: `translateY(${y}px)`, color, fontSize: size,
      fontWeight: weight, fontFamily: font, lineHeight: 1.1, ...style }}>{children}</div>
  );
};
