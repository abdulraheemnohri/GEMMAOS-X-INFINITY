from gemmaos.agents.base import BaseAgent
from typing import Dict, Any, List

class SecurityAgent(BaseAgent):
    """
    Tier 7.2.4: Security Agent
    Purpose: Threat detection and privacy protection.
    """
    def __init__(self):
        super().__init__(name="SecurityAgent")
        self.threat_logs: List[Dict[str, Any]] = []

    def reason(self, task: Dict[str, Any]) -> str:
        intent = task.get("intent", "")
        if "scan" in intent:
            return "scan_app"
        if "firewall" in intent or "block" in intent:
            return "set_firewall_rule"
        return "unknown_action"

    def act(self, action: str, params: Dict[str, Any] = None) -> bool:
        if action == "scan_app":
            package = params.get("package", "unknown")
            # Mock scanning logic
            is_malicious = "malware" in package.lower()
            print(f"Scanning {package}... Result: {'Threat Detected' if is_malicious else 'Clean'}")
            if is_malicious:
                self.threat_logs.append({"package": package, "type": "malware"})
            return not is_malicious

        if action == "set_firewall_rule":
            app = params.get("app", "unknown")
            block = params.get("block", True)
            print(f"Firewall: {'Blocking' if block else 'Allowing'} internet for {app}")
            return True

        return False

    def get_security_status(self) -> Dict[str, Any]:
        return {
            "threats_detected": len(self.threat_logs),
            "status": "Safe" if not self.threat_logs else "Action Required"
        }
