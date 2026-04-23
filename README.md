# SecureCodeRAG

**AI-Powered Secure Code Analysis with Retrieval-Augmented Generation**

SecureCodeRAG is a hybrid security analysis tool that combines static code analysis with RAG (Retrieval-Augmented Generation) to detect vulnerabilities and provide AI-powered explanations with security best practices.

---
## Problem Statement & Engineering Intent (Spec)

**The Problem:** Traditional static code analyzers flag vulnerabilities but fail to teach developers how to fix them. Conversely, purely prompting an LLM for code fixes often leads to hallucinations or non-standard security advice.

**The Intent:** Build a hybrid, production-ready tool that bridges this gap. The system must:
1. Use static analysis for fast, deterministic vulnerability detection.
2. Use Retrieval-Augmented Generation (RAG) to ground AI explanations strictly in official OWASP documentation.
3. Be built with a modern, type-safe stack (**TypeScript/React** frontend, **Python/FastAPI** backend).
4. Be designed for cloud-native deployment with **Docker** containerisation and automated **CI/CD** pipelines.

This intent-first approach ensures the AI acts as a reliable educational tool rather than a black box, while the underlying architecture mirrors modern, containerised enterprise applications.

## Features

- **Static Analysis**: Pattern-based detection of common vulnerabilities (SQL Injection, Command Injection, XSS, Path Traversal)
- **AI-Powered Explanations**: LLM-generated security insights backed by OWASP documentation
- **RAG Architecture**: Retrieves relevant security documentation to provide context-aware explanations
- **Real-time Analysis**: Fast feedback on code security issues
- **Confidence Scoring**: Each finding includes a confidence level based on static analysis and retrieved evidence
- **Modern UI**: Clean React + TypeScript interface with syntax highlighting

---

##  Architecture

```
┌─────────────────┐
│   React UI      │
│  (TypeScript)   │
└────────┬────────┘
         │
         │ HTTP/JSON
         │
┌────────▼────────┐
│   FastAPI       │
│   Backend       │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
┌───▼───┐ ┌──▼──────┐
│Static │ │   RAG   │
│Scanner│ │ Engine  │
└───────┘ └──┬──────┘
             │
      ┌──────┴──────┐
      │             │
┌─────▼─────┐ ┌────▼────┐
│Vector DB  │ │  LLM    │
│  (FAISS)  │ │ (GPT-4) │
└───────────┘ └─────────┘
```

---

## Quick Start

### Prerequisites

- **Python 3.11+**
- **Node.js 18+**
- **OpenAI API Key** (optional for dummy mode)

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/Mac (use this if project is edited on Github Codespaces)
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` file:**
   ```bash
   cd app
   ```
   Create `.env` with:
   ```
   OPENAI_API_KEY=sk-your-key-here
   LLM_MODEL=gpt-4o-mini
   EMBEDDING_MODEL=text-embedding-3-small
   ```

5. **Initialise vector store (one-time):**
   ```bash
   python -m app.vectorstore.ingest
   ```

6. **Run the backend:**
   ```bash
   cd ..
   uvicorn app.main:app --reload --port 8000
   ```

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Run the development server:**
   ```bash
   npm run dev
   ```

4. **Open browser:**
   ```
   http://localhost:5173
   ```

---
## CI/CD and Docker
* Continuous Integration (CI) is set up via GitHub Actions to automatically lint, type-check, and test both backend and frontend on pushes and pull requests.

* Continuous Deployment (CD) will be added once the project is finalised and ready for production.

* Docker files exist for backend and frontend to enable future containerised builds. The project is not yet fully dockerised or composed, so you can continue development locally without affecting workflows.

## Usage

1. **Paste your code** into the editor
2. **Click "Analyse Code"**
3. **Review detected vulnerabilities** with:
   - Line number and code snippet
   - Severity and confidence score
   - AI-generated explanation
   - Secure coding recommendations
   - Related OWASP/CWE references

### Example

```python
# Vulnerable Code
String id = request.getParameter("id");
String sql = "SELECT * FROM orders WHERE id = " + id;
Statement stmt = conn.createStatement();
stmt.executeQuery(sql);

```

**Result:**
- Command Injection (Line 2)
- Confidence: High (1.0)
- Explanation: Direct execution of user input without validation...
- Fix: Use `subprocess` with argument lists instead

---

##  Configuration

### Backend Configuration (`backend/app/.env`)

```env
GEMINI_API_KEY=AI*****
LLM_MODEL=gemini-2.0-flash
EMBEDDING_MODEL=models/embedding-001

# Optional
PROJECT_NAME=SecureCodeRAG
```

### Frontend Configuration

Edit `frontend/src/api/analyzer.ts` to change API endpoint:

```typescript
const API_BASE = "http://localhost:8000/api";
```

---

##  Testing Without OpenAI

The system includes a **DummyLLM** for testing without an API key:

- Simply don't set `OPENAI_API_KEY`
- The backend will use mock responses
- Perfect for development and testing

---

##  Supported Vulnerabilities

| Vulnerability Type | Pattern Detection | OWASP Category |
|-------------------|-------------------|----------------|
| SQL Injection | String concatenation in queries | A03:2021 |
| Command Injection | `os.system()`, `exec()`, `eval()` | A03:2021 |
| XSS | `innerHTML`, `document.write()` | A07:2021 |
| Path Traversal | Unsanitised file paths | A01:2021 |

*More patterns can be added in `backend/app/security/static_scan.py`*

---

## 📁 Project Structure

```
SecureCodeRAG/
├─ .github/
│  └─ workflows/
│     └─ ci.yml
├─ backend/
│  ├─ app/
│  │  ├─ api/
│  │  │  └─ analyze.py
│  │  ├─ core/
│  │  │  ├─ config.py
│  │  │  ├─ embeddings.py
│  │  │  └─ llm.py
│  │  ├─ rag/
│  │  │  ├─ generator.py
│  │  │  ├─ prompts.py
│  │  │  └─ retriever.py
│  │  ├─ schemas/
│  │  │  ├─ request.py
│  │  │  └─ response.py
│  │  ├─ security/
│  │  │  ├─ confidence.py
│  │  │  ├─ static_scan.py
│  │  │  └─ vulnerability_map.py
│  │  └─ main.py
│  ├─ data/
│  │  └─ owasp_docs/
│  │     ├─ A01_Broken_Authentication.txt
│  │     ├─ A02_Cryptographic_Failures.txt
│  │     ├─ A03_SQL_Injection.txt
│  │     ├─ A05_Broken_Access_Control.txt
│  │     └─ A07_XSS.txt
│  ├─ Dockerfile
│  └─ requirements.txt
├─ frontend/
│  ├─ public/
│  │  └─ vite.svg
│  ├─ src/
│  │  ├─ api/
│  │  │  └─ analyzer.ts
│  │  ├─ assets/
│  │  │  └─ react.svg
│  │  ├─ components/
│  │  ├─ pages/
│  │  └─ types/
│  ├─ Dockerfile
│  ├─ nginx.conf
│  ├─ package.json
│  └─ package-lock.json
├─ docker-compose.yml
└─ README.md

```

---

## Contributing

Contributions are welcome! Areas for improvement:

- [ ] Add more vulnerability patterns
- [ ] Support additional programming languages
- [ ] Improve confidence scoring algorithm
- [ ] Add automated testing
- [ ] Create VS Code extension
- [ ] Add GitHub Actions CI/CD

---

## License

MIT License - To be obtained...

---

## ⚠️ Disclaimer

This tool is for **educational and testing purposes**. It should complement, not replace, comprehensive security audits and manual code reviews. Always follow security best practices and consult security professionals for production systems.

---

## Acknowledgments

- **OWASP** for security documentation
- **LangChain** for RAG framework
- **FastAPI** and **React** for the tech stack
- **OpenAI** for LLM capabilities

---

## Contact

For questions or feedback, reach out on LinkedIn (www.linkedin.com/in/moseyda).

---

**Made with ❤️ for secure coding practices**
