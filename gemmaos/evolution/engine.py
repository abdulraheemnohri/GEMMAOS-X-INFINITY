from typing import Dict, Any, List

class EvolutionEngine:
    """
    Tier 3.3: Evolution Engine
    Generates automations from discovered patterns and optimizes workflows.
    """
    def __init__(self, discovery_engine, automation_studio):
        self.discovery_engine = discovery_engine
        self.automation_studio = automation_studio
        self.pending_proposals: List[Dict[str, Any]] = []

    def evaluate_patterns(self, logs: List[Dict[str, Any]]):
        """Analyzes logs via discovery engine and generates proposals."""
        patterns = self.discovery_engine.mine_temporal_patterns(logs)
        for pattern in patterns:
            if pattern.get("confidence", 0) > 0.85:
                proposal = self.propose_automation(pattern["pattern_id"])
                self.pending_proposals.append(proposal)

    def propose_automation(self, pattern_id: str) -> Dict[str, Any]:
        """Generates a structured proposal for the user."""
        # Mapping pattern IDs to concrete automation definitions
        if pattern_id == "daily_morning":
            return {
                "id": "prop_morning_routine",
                "name": "Morning Routine",
                "trigger_type": "time",
                "trigger_params": {"time": "08:30"},
                "actions": [
                    {"type": "launch_app", "params": {"app": "email"}},
                    {"type": "launch_app", "params": {"app": "calendar"}}
                ],
                "confidence": 0.95
            }
        return {"id": "unknown", "confidence": 0}

    def accept_proposal(self, proposal_id: str):
        """On user approval, deploys the automation to the Studio."""
        for prop in self.pending_proposals:
            if prop["id"] == proposal_id:
                self.automation_studio.create_workflow(
                    name=prop["name"],
                    trigger_type=prop["trigger_type"],
                    trigger_params=prop["trigger_params"],
                    actions=prop["actions"]
                )
                self.pending_proposals.remove(prop)
                return True
        return False
