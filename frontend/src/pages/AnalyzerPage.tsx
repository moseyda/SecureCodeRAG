import { useState } from "react";
import { analyzeCode } from "../api/analyzer";
import type { AnalysisResult } from "../types/analysis";
import { Shield, Search, Loader2, Trash2, ShieldCheck } from "lucide-react";

import CodeEditor from "../components/CodeEditor";
import Modal from "../components/Modal";
import AnalysisResults from "../components/AnalysisResults";
import Toast from "../components/Toast";

import styles from "./AnalyzerPage.module.css";

interface ToastMessage {
  id: number;
  type: "success" | "error" | "info";
  message: string;
}

export default function AnalyzerPage() {
  const [code, setCode] = useState("");
  const [results, setResults] = useState<AnalysisResult[]>([]);
  const [loading, setLoading] = useState(false);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [toasts, setToasts] = useState<ToastMessage[]>([]);

  const addToast = (message: string, type: "success" | "error" | "info" = "info") => {
    const id = Date.now();
    setToasts((prev) => [...prev, { id, type, message }]);
    setTimeout(() => {
      setToasts((prev) => prev.filter((t) => t.id !== id));
    }, 4000);
  };

  const removeToast = (id: number) => {
    setToasts((prev) => prev.filter((t) => t.id !== id));
  };

  async function handleAnalyze() {
    if (!code.trim()) {
      addToast("Please enter code to analyze", "error");
      return;
    }

    setLoading(true);
    setIsModalOpen(true);
    setResults([]);

    try {
      const data = await analyzeCode(code);
      const safeResults = Array.isArray(data?.vulnerabilities) ? data.vulnerabilities : [];
      setResults(safeResults);

      if (safeResults.length === 0) {
        addToast("No vulnerabilities detected!", "success");
      } else {
        addToast(`Found ${safeResults.length} vulnerability(ies)`, "info");
      }
    } catch (err) {
      addToast("Analysis failed. Please try again.", "error");
      setIsModalOpen(false);
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  const handleClear = () => {
    setCode("");
    setResults([]);
    addToast("Code cleared", "info");
  };

  const handleCloseModal = () => {
    if (!loading) {
      setIsModalOpen(false);
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <div className={styles.headerContent}>
          <div className={styles.logo}>
            <Shield size={40} className={styles.logoIcon} />
            <h1>SecureCodeRAG</h1>
          </div>
          <p className={styles.subtitle}>
            AI-Powered Security Code Review with RAG
          </p>
        </div>
      </div>

      <div className={styles.mainContent}>
        <CodeEditor value={code} onChange={setCode} />

        <div className={styles.controls}>
          <button
            onClick={handleAnalyze}
            disabled={loading || !code.trim()}
            className={styles.analyzeBtn}
          >
            {loading ? (
              <>
                <Loader2 size={18} className={styles.spinner} /> Analyzing...
              </>
            ) : (
              <>
                <Search size={18} /> Analyze Code
              </>
            )}
          </button>

          <button
            onClick={handleClear}
            disabled={loading || !code.trim()}
            className={styles.clearBtn}
          >
            <Trash2 size={18} /> Clear
          </button>
        </div>
      </div>

      <Modal
        isOpen={isModalOpen}
        onClose={handleCloseModal}
        title="Security Analysis Results"
        icon={<ShieldCheck size={24} />}
      >
        <AnalysisResults results={results} isLoading={loading} />
      </Modal>

      <div className={styles.toastContainer}>
        {toasts.map((toast) => (
          <Toast
            key={toast.id}
            message={toast.message}
            type={toast.type}
            onClose={() => removeToast(toast.id)}
          />
        ))}
      </div>
    </div>
  );
}