export interface Vulnerability {
  type: string;
  line: number;
  snippet: string;
  owasp: string;
}

export interface Confidence {
  score: number;
  level: "Critical" | "High" | "Medium" | "Low";
}

export interface VulnerabilityMetadata {
  severity?: "Critical" | "High" | "Medium" | "Low";
  category?: string;
  cwe?: string;
  owasp?: string;
  description?: string;
}

export interface AnalysisResult {
  vulnerability: Vulnerability;
  metadata?: VulnerabilityMetadata;
  confidence: Confidence;
  explanation: string;
  sources: Array<{ source: string; [key: string]: any }>;
}

export interface AnalysisResponse {
  results: AnalysisResult[];
}