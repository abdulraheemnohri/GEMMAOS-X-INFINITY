import time
from typing import Dict, Any, List

class DigitalTwin:
    """
    Tier 4: Digital Twin System
    Lightweight behavioral model encoding user patterns.
    """
    def __init__(self):
        self.behavior_weights: Dict[str, float] = {
            "work_focus": 0.5,
            "social_activity": 0.5,
            "entertainment_preference": 0.5
        }
        self.daily_activity_sequence: List[str] = []

    def update_model(self, recent_actions: List[Dict[str, Any]]):
        """Updates behavioral weights based on recent actions."""
        for action in recent_actions:
            app = action.get("app", "")
            if app in ["slack", "email", "teams"]:
                self.behavior_weights["work_focus"] = min(1.0, self.behavior_weights["work_focus"] + 0.05)
            elif app in ["youtube", "netflix", "spotify"]:
                self.behavior_weights["entertainment_preference"] = min(1.0, self.behavior_weights["entertainment_preference"] + 0.05)

        print(f"Digital Twin updated. Work Focus: {self.behavior_weights['work_focus']:.2f}")

    def predict_next_action(self, context: Dict[str, Any]) -> str:
        """Predicts the most likely next action based on current state and model."""
        hour = context.get("hour", 0)
        if 8 <= hour <= 10 and self.behavior_weights["work_focus"] > 0.6:
            return "open_work_apps"
        if hour >= 20 and self.behavior_weights["entertainment_preference"] > 0.6:
            return "open_media_apps"
        return "wait"

    def get_user_state(self) -> str:
        """Determines the current high-level user state."""
        if self.behavior_weights["work_focus"] > 0.8:
            return "deep_work"
        return "normal"
