import {
    AbsoluteFill,
    interpolate,
    spring,
    useCurrentFrame,
    useVideoConfig,
} from "remotion";

export const TranslationAnim = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    // Animations setup
    const titleOpacity = interpolate(frame, [0, 15], [0, 1], {
        extrapolateRight: "clamp",
    });

    const frProgress = spring({
        frame: frame - 15, // Starts at frame 15
        fps,
        config: { damping: 14, stiffness: 60 },
    });

    const enProgress = spring({
        frame: frame - 40, // Translates after a brief pause
        fps,
        config: { damping: 14, stiffness: 60 },
    });

    // Flow from left to right idea
    const frY = interpolate(frProgress, [0, 1], [30, 0]);
    const frOpacity = frProgress;

    const enY = interpolate(enProgress, [0, 1], [-30, 0]);
    const enOpacity = enProgress;

    const arrowProgress = spring({
        frame: frame - 30, // Arrow appears between FR and EN
        fps,
        config: { damping: 14, stiffness: 60 },
    });

    const arrowOpacity = arrowProgress;
    const arrowScale = interpolate(arrowProgress, [0, 1], [0.8, 1]);

    return (
        <AbsoluteFill
            style={{
                backgroundColor: "white", // White background
                fontFamily: "'Inter', 'SF Pro Display', system-ui, sans-serif",
                justifyContent: "center",
                alignItems: "center",
            }}
        >
            {/* Header */}
            <div
                style={{
                    position: "absolute",
                    top: 80,
                    opacity: titleOpacity,
                    fontSize: 48,
                    fontWeight: 800,
                    color: "#0F172A", // Slate 900
                    display: "flex",
                    alignItems: "center",
                    gap: 16,
                }}
            >
                <div
                    style={{
                        width: 40,
                        height: 40,
                        backgroundColor: "#22c55e", // Using a green accent for LibreTranslate 
                        borderRadius: 8,
                        display: "flex",
                        justifyContent: "center",
                        alignItems: "center",
                        color: "white",
                        fontSize: 24
                    }}
                >
                    LT
                </div>
                LibreTranslate
            </div>

            {/* Main Content Area: Horizontal layout */}
            <div style={{ display: "flex", alignItems: "center", gap: 60 }}>

                {/* French Block */}
                <div
                    style={{
                        opacity: frOpacity,
                        transform: `translateY(${frY}px)`,
                        display: "flex",
                        flexDirection: "column",
                        gap: 12,
                        width: 400,
                    }}
                >
                    <span style={{ fontSize: 24, fontWeight: 700, color: "#94A3B8" }}>FR </span>
                    <div
                        style={{
                            padding: "32px 40px",
                            backgroundColor: "white",
                            borderRadius: 24,
                            boxShadow: "0 20px 40px rgba(0,0,0,0.05)",
                            borderLeft: "8px solid #FF7E22", // Orange
                            minHeight: 120,
                            display: "flex",
                            alignItems: "center"
                        }}
                    >
                        <span style={{ fontSize: 36, fontWeight: 600, color: "#334155", lineHeight: 1.4 }}>
                            Bonjour, comment allez-vous ?
                        </span>
                    </div>
                </div>

                {/* Translation Arrow */}
                <div
                    style={{
                        opacity: arrowOpacity,
                        transform: `scale(${arrowScale})`,
                        fontSize: 64,
                        color: "#CBD5E1"
                    }}
                >
                    ➔
                </div>

                {/* English Block */}
                <div
                    style={{
                        opacity: enOpacity,
                        transform: `translateY(${enY}px)`,
                        display: "flex",
                        flexDirection: "column",
                        gap: 12,
                        width: 400,
                    }}
                >
                    <span style={{ fontSize: 24, fontWeight: 700, color: "#94A3B8", textAlign: "right" }}> EN</span>
                    <div
                        style={{
                            padding: "32px 40px",
                            backgroundColor: "white",
                            borderRadius: 24,
                            boxShadow: "0 20px 40px rgba(0,0,0,0.05)",
                            borderRight: "8px solid #FAC130", // Yellow
                            minHeight: 120,
                            display: "flex",
                            alignItems: "center"
                        }}
                    >
                        <span style={{ fontSize: 36, fontWeight: 600, color: "#334155", lineHeight: 1.4 }}>
                            Hello, how are you?
                        </span>
                    </div>
                </div>

            </div>
        </AbsoluteFill>
    );
};
