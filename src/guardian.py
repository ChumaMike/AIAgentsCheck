import re

class EdgeGuardian:
    def __init__(self):
        # We define "Toxic" patterns or PII (Personally Identifiable Information)
        self.pii_patterns = {
            "EMAIL": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
            "PHONE": r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b",
            "SSN": r"\b\d{3}-\d{2}-\d{4}\b"
        }

    def sanitize(self, text: str) -> str:
        """
        Scans text and REDACTS any found PII.
        """
        clean_text = text
        redacted_count = 0

        for label, pattern in self.pii_patterns.items():
            matches = re.findall(pattern, clean_text)
            for match in matches:
                clean_text = clean_text.replace(match, f"[{label}_REDACTED]")
                redacted_count += 1
        
        if redacted_count > 0:
            print(f"🛡️ GUARDIAN ACTION: Redacted {redacted_count} sensitive items.")
        
        return clean_text

    def check_safety(self, prompt: str) -> bool:
        """
        Simple check to prevent 'Jailbreaks' or malicious prompts.
        """
        unsafe_keywords = ["hack", "exploit", "ignore instructions", "system override"]
        if any(keyword in prompt.lower() for keyword in unsafe_keywords):
            print("🚨 GUARDIAN ALERT: Malicious prompt detected.")
            return False
        return True