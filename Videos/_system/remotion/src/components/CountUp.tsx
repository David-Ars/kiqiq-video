import React from "react";
import { interpolate, useCurrentFrame } from "remotion";
import { FONT } from "../theme";

export const CountUp: React.FC<{
  value: number; duration?: number; prefix?: string; suffix?: string;
  color?: string; size?: number; font?: string;
}> = ({ value, duration = 30, prefix = "", suffix = "", color, size = 120, font = FONT }) => {
  const frame = useCurrentFrame();
  const v = interpolate(frame, [0, duration], [0, value], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const shown = Number.isInteger(value) ? Math.round(v).toLocaleString() : v.toFixed(1);
  return <span style={{ color, fontSize: size, fontWeight: 900, fontFamily: font }}>{prefix}{shown}{suffix}</span>;
};
