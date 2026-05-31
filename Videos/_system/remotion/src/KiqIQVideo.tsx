import React from "react";
import { AbsoluteFill, Audio, Img, Series, interpolate, staticFile, useCurrentFrame } from "remotion";
import { getPreset } from "./theme";
import { Frame } from "./Frame";
import { BarChart } from "./components/BarChart";
import { StatCard } from "./components/StatCard";
import { KineticText } from "./components/KineticText";
import { LogoSting } from "./components/LogoSting";
import { EpisodeProps } from "./schema";

export type { Scene, EpisodeProps } from "./schema";

const KenBurns: React.FC<{ src: string }> = ({ src }) => {
  const frame = useCurrentFrame();
  const scale = interpolate(frame, [0, 240], [1, 1.12], { extrapolateRight: "clamp" });
  return <Img src={staticFile(src)} style={{ width: "100%", height: "100%", objectFit: "cover", transform: `scale(${scale})` }} />;
};

export const KiqIQVideo: React.FC<EpisodeProps> = ({ preset, source, audioSrc, music, musicVolume, scenes }) => {
  const p = getPreset(preset);
  return (
    <AbsoluteFill style={{ backgroundColor: p.bg }}>
      {audioSrc && <Audio src={staticFile(audioSrc)} />}
      {musicVolume !== 0 && (
        <Audio src={staticFile(music ?? `music_${preset}.mp3`)} volume={musicVolume ?? 0.12} loop />
      )}
      <Series>
        {scenes.map((s, i) => (
          <Series.Sequence durationInFrames={s.durationInFrames} key={i}>
            <AbsoluteFill style={{ backgroundColor: p.bg }}>
              {s.sfx && <Audio src={staticFile(s.sfx)} volume={0.6} />}
              {s.type === "sting" && <LogoSting p={p} />}
              {s.type === "title" && (
                <div style={{ position: "absolute", inset: 0, padding: "0 110px", display: "flex",
                  flexDirection: "column", justifyContent: "center" }}>
                  {s.lines.map((l, j) => (
                    <KineticText key={j} color={p.text} size={86} weight={900} delay={j * 6} font={p.font}>{l}</KineticText>
                  ))}
                  {s.sub && <KineticText color={p.muted} size={34} weight={500} delay={s.lines.length * 6}
                    font={p.font} style={{ marginTop: 24 }}>{s.sub}</KineticText>}
                </div>
              )}
              {s.type === "bar" && <BarChart p={p} title={s.title} sub={s.sub} data={s.data} max={s.max} />}
              {s.type === "stat" && <StatCard p={p} title={s.title} stats={s.stats} />}
              {s.type === "image" && (
                <AbsoluteFill>
                  <KenBurns src={s.src} />
                  {s.caption && (
                    <div style={{ position: "absolute", left: 100, bottom: 130, color: p.text,
                      fontFamily: p.font, fontSize: 40, fontWeight: 800, background: "#0008", padding: "10px 20px" }}>
                      {s.caption}
                    </div>
                  )}
                </AbsoluteFill>
              )}
            </AbsoluteFill>
          </Series.Sequence>
        ))}
      </Series>
      <Frame p={p} source={source} />
    </AbsoluteFill>
  );
};
