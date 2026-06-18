from abc import ABC, abstractmethod
from typing import Dict, Any, List

class BaseAgent(ABC):
    """
    Base architecture for all AI agents:
    - Perception Layer
    - Reasoning Layer (Gemma 4 E2B)
    - Action Layer
    - Memory Layer
    """
    def __init__(self, name: str):
        self.name = name
        self.memory: List[Dict[str, Any]] = []

    def perceive(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Process sensor and system state."""
        return context

    @abstractmethod
    def reason(self, perceived_state: Dict[str, Any]) -> str:
        """Plan actions using LLM."""
        pass

    @abstractmethod
    def act(self, plan: str) -> Any:
        """Execute tools/actions."""
        pass

    def record_memory(self, interaction: Dict[str, Any]):
        self.memory.append(interaction)

class AgentRuntime:
    """Manages agent lifecycle and inter-agent communication."""
    def __init__(self):
        self.agents: Dict[str, BaseAgent] = {}

    def register_agent(self, agent: BaseAgent):
        self.agents[agent.name] = agent

    def dispatch(self, agent_name: str, task: Dict[str, Any]):
        if agent_name in self.agents:
            return self.agents[agent_name].reason(task)
        return "Agent not found"
