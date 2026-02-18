import re
from typing import List, Dict
from app.security.vulnerability_map import VULNERABILITY_PATTERNS

class StaticScanner:
    """Scans code for security vulnerabilities using regex patterns"""
    
    def __init__(self):
        self.patterns = VULNERABILITY_PATTERNS
    
    def scan(self, code: str) -> List[Dict]:
        """
        Scan code for vulnerabilities
        
        Args:
            code: Source code string to analyze
            
        Returns:
            List of vulnerabilities found
        """
        vulnerabilities = []
        lines = code.split('\n')
        
        for vuln_type, pattern_info in self.patterns.items():
            pattern = pattern_info['pattern']
            severity = pattern_info['severity']
            
            for line_num, line in enumerate(lines, start=1):
                if re.search(pattern, line, re.IGNORECASE):
                    vulnerabilities.append({
                        'type': vuln_type,
                        'severity': severity,
                        'line': line_num,
                        'code': line.strip()
                    })
        
        return vulnerabilities
