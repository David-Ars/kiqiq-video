import React from "react";
import { Composition } from "remotion";
import { KiqIQVideo } from "./KiqIQVideo";
import { episodeSchema, EpisodeProps } from "./schema";
import example from "./example-episode.json";

const FPS = 30;

export const RemotionRoot: React.FC = () => (
  <Composition
    id="KiqIQVideo"
    component={KiqIQVideo}
    schema={episodeSchema}
    fps={FPS}
    width={1920}
    height={1080}
    defaultProps={example as EpisodeProps}
    calculateMetadata={({ props }) => ({
      durationInFrames: props.scenes.reduce((a, s) => a + s.durationInFrames, 0),
    })}
  />
);
