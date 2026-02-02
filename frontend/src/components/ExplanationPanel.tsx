import type { AnalysisResult } from "../types/analysis";

export default function ExplanationPanel({
  results
}: {
  results: AnalysisResult[];
}) {
  if (results.length === 0) return null;

  return (
    <div>
      <h2>Explanation & Secure Fix</h2>
      {results.map((r, idx) => (
        <div key={idx} style={{ marginBottom: "1rem" }}>
          <h3>{r.vulnerability.type}</h3>
          <p>{r.explanation}</p>
        </div>
      ))}
    </div>
  );
}
