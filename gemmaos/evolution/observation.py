import time
from typing import List, Dict, Any

class ObservationEngine:
    """
    Tier 3.1: Observation Engine
    Continuous monitoring of app usage, battery, and system state.
    """
    def __init__(self):
        self.app_logs: List[Dict[str, Any]] = []
        self.battery_logs: List[Dict[str, Any]] = []

    def log_app_usage(self, app_name: str, duration: int):
        """Logs app usage event."""
        self.app_logs.append({
            "timestamp": time.time(),
            "app": app_name,
            "duration": duration
        })
        # Note: In a real system, we would prune logs older than 90 days here.

    def log_battery_level(self, level: int):
        """Logs battery level aggregate."""
        self.battery_logs.append({
            "timestamp": time.time(),
            "level": level
        })
        # Note: In a real system, we would prune logs older than 30 days here.

    def get_recent_activity(self) -> List[Dict[str, Any]]:
        """Returns the most recent app usage logs."""
        return self.app_logs[-10:]

    def get_behavioral_vector(self) -> Dict[str, Any]:
        """Summarizes recent behavior for the Pattern Discovery Engine."""
        return {
            "top_apps": self._get_top_apps(),
            "avg_battery_drain": self._calculate_drain()
        }

    def _get_top_apps(self) -> List[str]:
        # Mock summary
        return ["email", "slack", "chrome"]

    def _calculate_drain(self) -> float:
        return 0.5 # Mock drain rate
