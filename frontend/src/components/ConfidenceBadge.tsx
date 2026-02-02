import type { Confidence } from "../types/analysis";

export default function ConfidenceBadge({
  confidence
}: {
  confidence: Confidence;
}) {
  return (
    <span style={{ marginLeft: "0.5rem" }}>
      [{confidence.level} – {confidence.score}]
    </span>
  );
}
