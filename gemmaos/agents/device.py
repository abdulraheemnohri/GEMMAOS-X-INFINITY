from gemmaos.agents.base import BaseAgent
from typing import Dict, Any

class DeviceAgent(BaseAgent):
    """
    Device Agent: Controls hardware and system settings.
    """
    def __init__(self):
        super().__init__(name="DeviceAgent")
        self.settings = {
            "wifi": True,
            "bluetooth": False,
            "brightness": 50,
            "volume": 70,
            "power_mode": "balanced"
        }

    def reason(self, task: Dict[str, Any]) -> str:
        intent = task.get("intent")
        if "wifi" in intent:
            return "set_wifi"
        if "brightness" in intent:
            return "set_brightness"
        return "unknown_action"

    def act(self, action: str, params: Dict[str, Any] = None) -> bool:
        if action == "set_wifi":
            state = params.get("state", True)
            self.settings["wifi"] = state
            print(f"WiFi set to {state}")
            return True
        if action == "set_brightness":
            level = params.get("level", 50)
            self.settings["brightness"] = level
            print(f"Brightness set to {level}")
            return True
        return False
