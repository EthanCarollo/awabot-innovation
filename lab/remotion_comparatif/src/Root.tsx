import "./index.css";
import { Composition } from "remotion";
import { MyComposition } from "./Composition";
import { TranslationAnim } from "./Translation";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="ASRComparatif"
        component={MyComposition}
        durationInFrames={150}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="LibreTranslateGIF"
        component={TranslationAnim}
        durationInFrames={90}
        fps={30}
        width={1080}
        height={1080}
      />
    </>
  );
};
