import React from "react";
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { Preset, CHANNEL_MARK } from "../theme";

// Native KiqIQ logo sting (no Lottie). Animates the wordmark: a spring scale-in,
// a fade, and a fade-out at the tail. Use one scene at the open and one at the
// close. To use the actual logo image instead of the wordmark, drop
// logo_transparent.png into public/ and swap the <span> for an <Img>.
export const LogoSting: React.FC<{ p: Preset }> = ({ p }) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const pop = spring({ frame, fps, config: { damping: 200 } });
  const scale = interpolate(pop, [0, 1], [0.7, 1]);
  const fadeIn = interpolate(frame, [0, 10], [0, 1], { extrapolateRight: "clamp" });
  const fadeOut = interpolate(frame, [durationInFrames - 12, durationInFrames], [1, 0], { extrapolateLeft: "clamp" });
  const opacity = Math.min(fadeIn, fadeOut);
  return (
    <AbsoluteFill style={{ backgroundColor: p.bg, justifyContent: "center", alignItems: "center" }}>
      <span style={{ color: p.accent, fontFamily: p.font, fontWeight: 900, fontSize: 160,
        transform: `scale(${scale})`, opacity }}>
        {CHANNEL_MARK}
      </span>
    </AbsoluteFill>
  );
};
