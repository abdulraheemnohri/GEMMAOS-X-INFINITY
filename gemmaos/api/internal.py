import json
from typing import Dict, Any

class LocalAIEndpoint:
    """
    Tier 6.3: Internal RESTful Local API
    Interface for AI agents to query the Knowledge Vault and System Settings.
    """
    def __init__(self, vault, settings):
        self.vault = vault
        self.settings = settings

    def handle_request(self, method: str, path: str, payload: Dict[str, Any] = None) -> str:
        """Simulates internal API routing."""
        print(f"Internal API: {method} {path}")

        if path == "/vault/search":
            query = payload.get("query", "")
            results = self.vault.semantic_search(query)
            return json.dumps({"status": "success", "results": results})

        if path == "/settings/get":
            key = payload.get("key", "")
            value = self.settings.get_setting(key)
            return json.dumps({"status": "success", "value": value})

        if path == "/system/status":
            return json.dumps({
                "status": "success",
                "cpu_load": 15.0,
                "ai_active": True,
                "version": "GemmaOS Infinity 1.0"
            })

        return json.dumps({"status": "error", "message": "Not Found"})
