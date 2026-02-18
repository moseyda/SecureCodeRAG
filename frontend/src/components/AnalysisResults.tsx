import type { AnalysisResult } from "../types/analysis";
import { ShieldAlert, ShieldCheck, AlertTriangle, CheckCircle } from "lucide-react";
import VulnerabilityList from "./VulnerabilityList";
import ExplanationPanel from "./ExplanationPanel";
import styles from "./AnalysisResults.module.css";

interface Props {
  results: AnalysisResult[];
  isLoading: boolean;
}

export default function AnalysisResults({ results, isLoading }: Props) {
  if (isLoading) {
    return (
      <div className={styles.loading}>
        <div className={styles.spinner}></div>
        <p>Analyzing your code for vulnerabilities...</p>
        <span className={styles.subtext}>This may take a few seconds</span>
      </div>
    );
  }

  if (results.length === 0) {
    return (
      <div className={styles.noVulnerabilities}>
        <ShieldCheck size={64} className={styles.successIcon} />
        <h3>No Vulnerabilities Detected</h3>
        <p>Your code appears to be secure based on our analysis.</p>
        <div className={styles.tips}>
          <h4><CheckCircle size={16} /> Security Tips</h4>
          <ul>
            <li>Continue following secure coding practices</li>
            <li>Keep dependencies up to date</li>
            <li>Perform regular security audits</li>
          </ul>
        </div>
      </div>
    );
  }

const criticalCount = results.filter(r => r.severity?.toLowerCase() === "critical").length;
const highCount = results.filter(r => r.severity?.toLowerCase() === "high").length;
const mediumCount = results.filter(r => r.severity?.toLowerCase() === "medium").length;
const lowCount = results.filter(r => r.severity?.toLowerCase() === "low").length;


  return (
    <div className={styles.container}>
      <div className={styles.summary}>
        <div className={styles.summaryHeader}>
          <ShieldAlert size={24} />
          <h3>Analysis Summary</h3>
        </div>
        <div className={styles.stats}>
          <div className={`${styles.stat} ${styles.critical}`}>
            <span className={styles.statCount}>{criticalCount}</span>
            <span className={styles.statLabel}>Critical</span>
          </div>
          <div className={`${styles.stat} ${styles.high}`}>
            <span className={styles.statCount}>{highCount}</span>
            <span className={styles.statLabel}>High</span>
          </div>
          <div className={`${styles.stat} ${styles.medium}`}>
            <span className={styles.statCount}>{mediumCount}</span>
            <span className={styles.statLabel}>Medium</span>
          </div>
          <div className={`${styles.stat} ${styles.low}`}>
            <span className={styles.statCount}>{lowCount}</span>
            <span className={styles.statLabel}>Low</span>
          </div>
        </div>
      </div>

      <div className={styles.resultsContent}>
        <VulnerabilityList results={results} />
        <ExplanationPanel results={results} />
      </div>
    </div>
  );
}