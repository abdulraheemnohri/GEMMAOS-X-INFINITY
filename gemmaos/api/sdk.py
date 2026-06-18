from gemmaos.agents.base import BaseAgent
from typing import Dict, Any

class GemmaSDK:
    """
    Developer SDK for extending GemmaOS capabilities.
    """
    def __init__(self, runtime):
        self.runtime = runtime

    def register_custom_agent(self, agent_instance: BaseAgent):
        """Registers a 3rd party agent into the OS runtime."""
        print(f"SDK: Registering custom agent '{agent_instance.name}'")
        self.runtime.register_agent(agent_instance)

    def get_system_status(self) -> Dict[str, Any]:
        """Provides high-level system metrics to agents."""
        return {
            "os_version": "Infinity v1.0",
            "api_level": 42,
            "ai_active": True
        }
