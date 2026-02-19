import "./index.css";
import { Composition } from "remotion";
import { MyComposition } from "./Composition";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="ASRComparatif"
        component={MyComposition}
        durationInFrames={150}
        fps={30}
        width={800}
        height={450}
      />
    </>
  );
};
