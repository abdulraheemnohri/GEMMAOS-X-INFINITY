from typing import Dict, Any, List

class AIProtectionGuard:
    """
    Tier 28: Risk Mitigation
    Human-in-the-loop for destructive actions and hallucination detection.
    """
    def __init__(self):
        self.destructive_actions = ["delete", "format", "wipe", "reset", "send_payment"]

    def verify_proposal(self, proposal: Dict[str, Any]) -> bool:
        """Checks for hallucinations or high-risk actions."""
        # 1. Destructive check
        for action in proposal.get("actions", []):
            if any(da in str(action).lower() for da in self.destructive_actions):
                print(f"Guardrails: High-risk action detected in proposal '{proposal.get('name')}'. Human review REQUIRED.")
                return False

        # 2. Confidence check
        if proposal.get("confidence", 0) < 0.8:
            print(f"Guardrails: Low confidence ({(proposal.get('confidence', 0)*100):.1f}%) detected. Blocking auto-execution.")
            return False

        return True

    def scan_generated_code(self, code: str) -> List[str]:
        """Static analysis for common vulnerabilities or hallucinations in AI code."""
        issues = []
        if "eval(" in code or "exec(" in code:
            issues.append("Dynamic code execution detected (eval/exec)")
        if "os.system(" in code:
            issues.append("Direct shell command execution detected")
        return issues
