import type { Confidence } from "../types/analysis";
import styles from "./ConfidenceBadge.module.css";

export default function ConfidenceBadge({
  confidence
}: {
  confidence: Confidence;
}) {
  const getColorClass = (level: string) => {
    switch (level.toLowerCase()) {
      case "critical":
        return styles.critical;
      case "high":
        return styles.high;
      case "medium":
        return styles.medium;
      case "low":
        return styles.low;
      default:
        return styles.info;
    }
  };

  return (
    <span className={`${styles.badge} ${getColorClass(confidence.level)}`}>
      <span className={styles.level}>{confidence.level}</span>
      <span className={styles.score}>{(confidence.score * 100).toFixed(0)}%</span>
    </span>
  );
}