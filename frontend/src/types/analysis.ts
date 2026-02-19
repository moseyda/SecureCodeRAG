export interface AnalysisResult {
  type: string;
  severity: string;
  line: number;
  code: string;
  explanation: string;
  confidence: number;
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