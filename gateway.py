class AISecurityGateway:
    def __init__(self):
        self.attack_patterns = [
            "ignore previous instructions",
            "reveal system prompt",
            "bypass security",
            "act as admin",
            "override rules"
        ]

        self.sensitive_keywords = [
            "password", "api key", "confidential",
            "private data", "internal system"
        ]

    def calculate_risk(self, text):
        score = 0
        detected = []

        for pattern in self.attack_patterns:
            if pattern in text.lower():
                score += 3
                detected.append(pattern)

        for word in self.sensitive_keywords:
            if word in text.lower():
                score += 2
                detected.append(word)

        return score, detected

    def decision(self, score):
        if score >= 5:
            return "BLOCKED"
        elif score >= 3:
            return "FLAGGED"
        return "ALLOWED"

    def process(self, text):
        score, detected = self.calculate_risk(text)
        return {
            "input": text,
            "risk_score": score,
            "decision": self.decision(score),
            "detected": detected
        }
