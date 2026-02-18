export interface AnalysisResult {
  type: string;
  severity: string;
  line: number;
  code: string; // Backend sends 'code', was mapped to 'snippet' conceptually
  explanation: string;
  confidence: number; // Backend sends a float/number, not an object
  // output from backend does not include 'metadata' or 'sources' objects as per previous interface
  // explicitly adding optional fields if they might be added later or to avoid strict breaking if backend changes partially
  cwe?: string;
  owasp?: string;
  category?: string;
  sources?: Array<{ source: string;[key: string]: any }>;
}

export interface AnalysisResponse {
  vulnerabilities: AnalysisResult[];
  total_vulnerabilities: number;
  summary?: string;
}