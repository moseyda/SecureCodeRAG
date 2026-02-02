import re

# SQL Injection patterns
SQLI_PATTERNS = [
    r"SELECT .* FROM .* WHERE .*=\s*['\"]?\s*\+",
    r"execute\(.+\+.+\)",
    r"cursor\.execute\([^,)]*\+",
    r"executemany\([^,)]*\+",
]

# Command Injection patterns
CMD_INJECTION_PATTERNS = [
    r"os\.system\(",
    r"subprocess\.call\(",
    r"subprocess\.run\(",
    r"subprocess\.Popen\(",
    r"eval\(",
    r"exec\(",
]

# XSS patterns
XSS_PATTERNS = [
    r"innerHTML\s*=",
    r"document\.write\(",
    r"\.html\(.+\+",
]

# Path Traversal patterns
PATH_TRAVERSAL_PATTERNS = [
    r"open\(.+\+",
    r"file\(.+\+",
]

def detect_vulnerabilities(code: str) -> list[dict[str, str | int]]:
    findings: list[dict[str, str | int]] = []
    lines = code.split("\n")

    for i, line in enumerate(lines):
        # Check SQL Injection
        for pattern in SQLI_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                findings.append({
                    "type": "SQL Injection",
                    "line": i + 1,
                    "snippet": line.strip(),
                    "owasp": "A03:2021"
                })
        
        # Check Command Injection
        for pattern in CMD_INJECTION_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                findings.append({
                    "type": "Command Injection",
                    "line": i + 1,
                    "snippet": line.strip(),
                    "owasp": "A03:2021"
                })
        
        # Check XSS
        for pattern in XSS_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                findings.append({
                    "type": "XSS",
                    "line": i + 1,
                    "snippet": line.strip(),
                    "owasp": "A07:2021"
                })
        
        # Check Path Traversal
        for pattern in PATH_TRAVERSAL_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                findings.append({
                    "type": "Path Traversal",
                    "line": i + 1,
                    "snippet": line.strip(),
                    "owasp": "A01:2021"
                })
    
    return findings