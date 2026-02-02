export interface Vulnerability {
  type: string;
  line: number;
  snippet: string;
  owasp: string;
}

export interface Confidence {
  score: number;
  level: "High" | "Medium" | "Low";
}

export interface AnalysisResult {
  vulnerability: Vulnerability;
  metadata?: {
    owasp?: string;
    cwe?: string;
    description?: string;
  };
  confidence: Confidence;
  explanation: string;
  sources: Record<string, any>[];
}

export interface AnalysisResponse {
  results: AnalysisResult[];
}
