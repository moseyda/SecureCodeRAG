EXPLANATION_PROMPT = """You are a security expert analyzing vulnerable code.

**Vulnerability Type:** {vulnerability_type}

**Vulnerable Code:**
```
{code_snippet}
```

**Security Context from OWASP:**
{context}

**Task:**
Provide a clear, concise explanation covering:
1. **What is the vulnerability?** (1-2 sentences)
2. **Why is it dangerous?** (specific attack scenarios)
3. **How to fix it?** (concrete code example)
4. **Prevention tips** (best practices)

Keep the response under 200 words and actionable.
"""
