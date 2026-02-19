import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

/*
 * Accuracy = 100 - WER (%) on FLEURS benchmark
 * Voxtral: 960ms delay
 */
const MODELS = [
  { name: "Voxtral Mini 4B", fr: 94.32, en: 95.66, zh: 92.1, color: "#3B82F6" },
  { name: "Qwen3-ASR 1.7B", fr: 92.8, en: 96.65, zh: 97.2, color: "#8B5CF6" },
];

const FLOOR = 85;
const CEIL = 100;
const BAR_HEIGHT = 200;

const BarPair = ({
  model,
  index,
}: {
  model: (typeof MODELS)[0];
  index: number;
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const delay = index * 8;

  const makePct = (val: number) =>
    ((val - FLOOR) / (CEIL - FLOOR)) * BAR_HEIGHT;

  const frProgress = spring({
    frame: frame - delay,
    fps,
    config: { damping: 14, stiffness: 50 },
  });
  const enProgress = spring({
    frame: frame - delay - 4,
    fps,
    config: { damping: 14, stiffness: 50 },
  });
  const zhProgress = spring({
    frame: frame - delay - 8,
    fps,
    config: { damping: 14, stiffness: 50 },
  });

  const frH = makePct(model.fr) * frProgress;
  const enH = makePct(model.en) * enProgress;
  const zhH = makePct(model.zh) * zhProgress;

  const labelOpacity = interpolate(frame, [delay + 15, delay + 25], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const renderBar = (val: number, height: number, flag: string, progress: number) => (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 6 }}>
      <span
        style={{
          fontSize: 18,
          fontWeight: 800,
          color: model.color,
          opacity: labelOpacity,
          fontVariantNumeric: "tabular-nums",
        }}
      >
        {val.toFixed(1)}%
      </span>
      <div
        style={{
          width: 48,
          height: BAR_HEIGHT,
          backgroundColor: "#F1F5F9",
          borderRadius: 10,
          display: "flex",
          flexDirection: "column",
          justifyContent: "flex-end",
          overflow: "hidden",
        }}
      >
        <div
          style={{
            width: "100%",
            height: height,
            backgroundColor: model.color,
            borderRadius: 10,
            opacity: flag === "🇨🇳" ? 1 : (flag === "🇬🇧" ? 0.85 : 0.7),
          }}
        />
      </div>
      <span style={{ fontSize: 14, fontWeight: 600, color: "#64748B" }}>{flag}</span>
    </div>
  );

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        flex: 1,
      }}
    >
      <div style={{ display: "flex", gap: 8, alignItems: "flex-end", height: BAR_HEIGHT + 40 }}>
        {renderBar(model.fr, frH, "🇫🇷", frProgress)}
        {renderBar(model.en, enH, "🇬🇧", enProgress)}
        {renderBar(model.zh, zhH, "🇨🇳", zhProgress)}
      </div>

      <div
        style={{
          marginTop: 18,
          fontSize: 20,
          fontWeight: 800,
          color: "#0F172A",
          textAlign: "center" as const,
          letterSpacing: "-0.5px",
        }}
      >
        {model.name}
      </div>
    </div>
  );
};

export const MyComposition = () => {
  return (
    <AbsoluteFill
      style={{
        backgroundColor: "white",
        padding: "50px 60px 40px",
        fontFamily: "'Inter', 'SF Pro Display', system-ui, sans-serif",
        flexDirection: "row",
        alignItems: "flex-end",
        justifyContent: "center",
        gap: 50,
      }}
    >
      {MODELS.map((m, i) => (
        <BarPair key={m.name} model={m} index={i} />
      ))}
    </AbsoluteFill>
  );
};
