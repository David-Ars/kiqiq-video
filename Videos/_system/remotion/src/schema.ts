import { z } from "zod";

// Zod schema for a KiqIQ episode. This is the single source of truth for the
// shape of episodes/<slug>.json. Remotion uses it to (1) show editable controls
// in the studio at gate 2 and (2) fail loudly if an episode's props are malformed
// instead of rendering a broken video. The component prop types below are
// inferred from this schema, so the schema and the types can never drift apart.

const barItem = z.object({
  label: z.string(),
  value: z.number(),
  highlight: z.boolean().optional(),
});

const statItem = z.object({
  value: z.number(),
  label: z.string(),
  suffix: z.string().optional(),
  highlight: z.boolean().optional(),
});

// Optional per-scene one-shot sound effect: a file in public/, played at the
// scene's start (a soft tick as a count-up lands, a low whoosh on a reveal).
const sfx = z.string().optional();

const titleScene = z.object({
  type: z.literal("title"),
  durationInFrames: z.number().int().positive(),
  lines: z.array(z.string()),
  sub: z.string().optional(),
  sfx,
});

const barScene = z.object({
  type: z.literal("bar"),
  durationInFrames: z.number().int().positive(),
  title: z.string().optional(),
  sub: z.string().optional(),
  data: z.array(barItem),
  max: z.number().optional(),
  sfx,
});

const statScene = z.object({
  type: z.literal("stat"),
  durationInFrames: z.number().int().positive(),
  title: z.string().optional(),
  stats: z.array(statItem),
  sfx,
});

const imageScene = z.object({
  type: z.literal("image"),
  durationInFrames: z.number().int().positive(),
  src: z.string(),
  caption: z.string().optional(),
  sfx,
});

// The KiqIQ logo sting: a short branded bumper. Rendered natively in Remotion
// from the logo in public/ (no Lottie dependency). Use one at the open and one
// at the close.
const stingScene = z.object({
  type: z.literal("sting"),
  durationInFrames: z.number().int().positive(),
  sfx,
});

export const sceneSchema = z.discriminatedUnion("type", [
  titleScene,
  barScene,
  statScene,
  imageScene,
  stingScene,
]);

export const episodeSchema = z.object({
  subject: z.string(),
  preset: z.enum(["data_native", "blueprint", "engraving", "deco", "faded", "pop"]),
  source: z.string().optional(),
  audioSrc: z.string().optional(),
  // Optional low background music bed (a file in public/). Keep it quiet:
  // musicVolume defaults to 0.12 so it sits well under the narration.
  music: z.string().optional(),
  musicVolume: z.number().min(0).max(1).optional(),
  scenes: z.array(sceneSchema).min(1),
});

export type Scene = z.infer<typeof sceneSchema>;
export type EpisodeProps = z.infer<typeof episodeSchema>;
