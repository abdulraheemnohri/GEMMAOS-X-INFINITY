from typing import Dict, Any, List

class AIFirewall:
    """
    Tier 15.2: AI Firewall
    App-specific internet access control and tracker blocking.
    """
    def __init__(self):
        self.app_rules: Dict[str, bool] = {} # True = Allowed, False = Blocked
        self.blocked_trackers: List[str] = ["ad.tracker.com", "analytics.net"]

    def set_app_rule(self, package_name: str, allow_internet: bool):
        """Sets network access rule for a specific app."""
        print(f"Firewall: {'Allowing' if allow_internet else 'Blocking'} internet for {package_name}")
        self.app_rules[package_name] = allow_internet
        return True

    def scan_network_request(self, package_name: str, url: str) -> bool:
        """AI-powered DNS/Traffic analysis."""
        # 1. Check app-specific rule
        if not self.app_rules.get(package_name, True):
            print(f"Firewall: Blocked request from {package_name} (internet disabled)")
            return False

        # 2. Check tracker list
        for tracker in self.blocked_trackers:
            if tracker in url:
                print(f"Firewall: Blocked tracker request to {url} from {package_name}")
                return False

        return True

    def suggest_rules(self, app_list: List[str]):
        """AI suggest rules based on app type (e.g. calculator doesn't need net)."""
        print("Firewall: AI Analysis - Suggesting blocks for offline-only utility apps.")
        suggestions = []
        for app in app_list:
            if "calculator" in app.lower() or "clock" in app.lower():
                suggestions.append(app)
        return suggestions
