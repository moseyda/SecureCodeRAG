import type { AnalysisResult } from "../types/analysis";
import { Lightbulb, BookOpen, FileText, AlertTriangle } from "lucide-react";
import styles from "./ExplanationPanel.module.css";

export default function ExplanationPanel({
  results
}: {
  results: AnalysisResult[];
}) {
  if (results.length === 0) return null;

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h2><Lightbulb size={20} /> Explanation & Secure Fix</h2>
      </div>

      <div className={styles.content}>
        {results
          .filter(vuln => vuln && vuln.type)
          .map((vuln, idx) => (
            <div key={idx} className={styles.card}>
              <div className={styles.cardHeader}>
                <h3>
                  <AlertTriangle size={18} className={styles.titleIcon} />
                  {vuln.type}
                </h3>
                {vuln.severity && (
                  <span className={`${styles.severity} ${styles[vuln.severity.toLowerCase()]}`}>
                    {vuln.severity}
                  </span>
                )}
              </div>

              <div className={styles.explanation}>
                <p>{vuln.explanation}</p>
              </div>

              {vuln.sources && vuln.sources.length > 0 && (
                <div className={styles.sources}>
                  <h4><BookOpen size={16} /> Sources</h4>
                  <ul>
                    {vuln.sources.map((source: any, idx: number) => (
                      <li key={idx}>
                        <FileText size={14} />
                        <span>{source.source}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          ))}
      </div>
    </div>
  );
}