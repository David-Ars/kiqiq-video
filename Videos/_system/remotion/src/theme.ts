// KiqIQ brand theme for the video layer. Mirrors _system/brand.py presets so
// charts and motion match the stills. CONSTANTS never change per video; the
// preset (chosen by the angle) does.

export const CHANNEL_MARK = "KiqIQ";
export const FONT = "Inter, system-ui, sans-serif";

export type Preset = {
  bg: string; panel: string; text: string; muted: string; grid: string;
  neutral: string; accent: string; accentD: string; accent2: string;
  font: string; labelDarkOnAccent: boolean;
};

export const PRESETS: Record<string, Preset> = {
  data_native: { bg:"#0B1F3A", panel:"#102A4C", text:"#EAF2FA", muted:"#8AA0B8", grid:"#1C3656",
    neutral:"#33445C", accent:"#29C5F6", accentD:"#1A8FBC", accent2:"#8B5CF6", font:FONT, labelDarkOnAccent:true },
  blueprint: { bg:"#0A2540", panel:"#0E2E4E", text:"#EAF2FA", muted:"#7FA8C9", grid:"#1E4B73",
    neutral:"#284E73", accent:"#29C5F6", accentD:"#1A8FBC", accent2:"#9AD8F2", font:FONT, labelDarkOnAccent:true },
  engraving: { bg:"#EFE7D3", panel:"#E7DCC2", text:"#231C12", muted:"#6E5F49", grid:"#C9BC9E",
    neutral:"#B8A98A", accent:"#7B2D26", accentD:"#54201B", accent2:"#3F5740", font:"Georgia, 'Times New Roman', serif", labelDarkOnAccent:false },
  deco: { bg:"#11100C", panel:"#1A1812", text:"#F3ECD9", muted:"#B9A77C", grid:"#2A2517",
    neutral:"#3A3320", accent:"#C8A24A", accentD:"#8C6F2E", accent2:"#B9A77C", font:"Georgia, serif", labelDarkOnAccent:true },
  faded: { bg:"#15171C", panel:"#1C1F26", text:"#C9CDD4", muted:"#6B7280", grid:"#23262E",
    neutral:"#33373F", accent:"#5B7A99", accentD:"#3E5670", accent2:"#7C6F86", font:FONT, labelDarkOnAccent:false },
  pop: { bg:"#101418", panel:"#1A2030", text:"#FFFFFF", muted:"#8A93A6", grid:"#232A3A",
    neutral:"#333B4D", accent:"#FFC400", accentD:"#C99A00", accent2:"#29C5F6", font:FONT, labelDarkOnAccent:true },
};

export const getPreset = (name: string): Preset => PRESETS[name] ?? PRESETS.data_native;
