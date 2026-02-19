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
  { name: "Voxtral Mini 4B", fr: 100 - 5.68, en: 100 - 4.34, color: "#3B82F6" },
  { name: "Qwen3-ASR 1.7B", fr: 100 - 5.5, en: 100 - 3.35, color: "#8B5CF6" },
  { name: "Kyutai STT 1B", fr: 100 - 9.7, en: 100 - 8.3, color: "#10B981" },
];

const FLOOR = 88;
const CEIL = 100;
const BAR_HEIGHT = 220;

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

  const frH = makePct(model.fr) * frProgress;
  const enH = makePct(model.en) * enProgress;

  const labelOpacity = interpolate(frame, [delay + 15, delay + 25], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        flex: 1,
      }}
    >
      {/* Bars + values */}
      <div style={{ display: "flex", gap: 10, alignItems: "flex-end", height: BAR_HEIGHT + 40 }}>
        {/* FR bar */}
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 6 }}>
          <span
            style={{
              fontSize: 20,
              fontWeight: 800,
              color: model.color,
              opacity: labelOpacity,
              fontVariantNumeric: "tabular-nums",
            }}
          >
            {model.fr.toFixed(1)}%
          </span>
          <div
            style={{
              width: 56,
              height: BAR_HEIGHT,
              backgroundColor: "#F1F5F9",
              borderRadius: 12,
              display: "flex",
              flexDirection: "column",
              justifyContent: "flex-end",
              overflow: "hidden",
            }}
          >
            <div
              style={{
                width: "100%",
                height: frH,
                backgroundColor: model.color,
                borderRadius: 12,
                opacity: 0.75,
              }}
            />
          </div>
          <span style={{ fontSize: 15, fontWeight: 600, color: "#64748B" }}>🇫🇷</span>
        </div>

        {/* EN bar */}
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 6 }}>
          <span
            style={{
              fontSize: 20,
              fontWeight: 800,
              color: model.color,
              opacity: labelOpacity,
              fontVariantNumeric: "tabular-nums",
            }}
          >
            {model.en.toFixed(1)}%
          </span>
          <div
            style={{
              width: 56,
              height: BAR_HEIGHT,
              backgroundColor: "#F1F5F9",
              borderRadius: 12,
              display: "flex",
              flexDirection: "column",
              justifyContent: "flex-end",
              overflow: "hidden",
            }}
          >
            <div
              style={{
                width: "100%",
                height: enH,
                backgroundColor: model.color,
                borderRadius: 12,
              }}
            />
          </div>
          <span style={{ fontSize: 15, fontWeight: 600, color: "#64748B" }}>🇬🇧</span>
        </div>
      </div>

      {/* Model name */}
      <div
        style={{
          marginTop: 14,
          fontSize: 18,
          fontWeight: 700,
          color: "#1E293B",
          textAlign: "center" as const,
          lineHeight: 1.3,
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
