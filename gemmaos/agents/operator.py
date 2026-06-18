from gemmaos.agents.base import BaseAgent
from typing import Dict, Any, List

class OperatorAgent(BaseAgent):
    """
    Tier 8: AI Operator Mode
    UI Automation with safety constraints and semantic representation.
    """
    def __init__(self, vision_subsystem):
        super().__init__(name="OperatorAgent")
        self.vision = vision_subsystem
        self.action_history: List[Dict[str, Any]] = []

    def reason(self, task: Dict[str, Any]) -> str:
        intent = task.get("intent", "")
        if "click" in intent or "tap" in intent:
            return "tap_element"
        if "type" in intent:
            return "type_text"
        if "scroll" in intent:
            return "scroll_screen"
        return "unknown_action"

    def act(self, action: str, params: Dict[str, Any] = None) -> bool:
        """Executes UI action with safety verification."""
        # 8.4 Safety Constraints check
        if not self._verify_safety(action, params):
            print(f"Operator: Safety violation blocked action '{action}'")
            return False

        print(f"Operator: Executing '{action}' with params {params}")
        self.action_history.append({"action": action, "params": params})

        # 8.3 Task Execution Flow: Perception -> Action -> Verification
        screen_state = self.vision.analyze_screenshot(b"dummy_frame")
        if self._verify_execution(action, screen_state):
            return True
        return False

    def _verify_safety(self, action: str, params: Dict[str, Any]) -> bool:
        """Prevents interaction with sensitive apps without biometric auth."""
        target = params.get("element_text", "").lower()
        sensitive_targets = ["bank", "password", "confirm payment", "delete account"]
        for st in sensitive_targets:
            if st in target:
                return False
        return True

    def _verify_execution(self, action: str, screen_state: Dict[str, Any]) -> bool:
        """Simulates screenshot verification after critical actions."""
        print("Operator: Verifying execution via vision feedback...")
        return True

    def get_semantic_ui(self) -> Dict[str, Any]:
        """Fusion: Accessibility Tree + Vision detections."""
        return self.vision.analyze_screenshot(b"current_frame")
