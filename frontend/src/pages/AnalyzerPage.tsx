import { useState } from "react";
import { analyzeCode } from "../api/analyzer";
import type { AnalysisResult } from "../types/analysis";

import CodeEditor from "../components/CodeEditor";
import VulnerabilityList from "../components/VulnerabilityList";
import ExplanationPanel from "../components/ExplanationPanel";

export default function AnalyzerPage() {
  const [code, setCode] = useState("");
  const [results, setResults] = useState<AnalysisResult[]>([]);
  const [loading, setLoading] = useState(false);

  async function handleAnalyze() {
    setLoading(true);
    try {
      const data = await analyzeCode(code);
      setResults(data.results);
    } catch (err) {
      alert("Analysis failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ padding: "1.5rem" }}>
      <h1>Secure Code Review AI</h1>

      <CodeEditor value={code} onChange={setCode} />

      <button onClick={handleAnalyze} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze Code"}
      </button>

      <VulnerabilityList results={results} />

      <ExplanationPanel results={results} />
    </div>
  );
}
