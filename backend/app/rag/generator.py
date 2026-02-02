from app.core.llm import get_llm
from .prompts import SYSTEM_PROMPT

llm = get_llm()

def generate_explanation(vuln, docs):
    context = "\n".join(d.page_content for d in docs)

    prompt = f"""
{SYSTEM_PROMPT}

Vulnerability:
{vuln['type']} (Line {vuln['line']})

Evidence:
{context}

Explain:
- What the vulnerability is
- Why it is dangerous
- Secure fix (code example)
"""

    return llm.predict(prompt)
