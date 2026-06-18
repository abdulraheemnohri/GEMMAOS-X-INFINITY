import time
from typing import List, Dict, Any, Optional

class WorkingMemory:
    """
    Tier 1: Working Memory
    Capacity: 8K-32K tokens
    Retention: Current task only
    Content: Active conversation, current plan, immediate context
    Persistence: RAM only, cleared on task completion
    """
    def __init__(self, capacity: int = 32000):
        self.capacity = capacity
        self.content: List[Dict[str, Any]] = []
        self.current_task_id: Optional[str] = None

    def add_message(self, role: str, content: str):
        self.content.append({
            "role": role,
            "content": content,
            "timestamp": time.time()
        })
        # Simple token approximation: 1 token ~= 4 chars
        current_tokens = sum(len(m["content"]) // 4 for m in self.content)
        while current_tokens > self.capacity and self.content:
            self.content.pop(0)
            current_tokens = sum(len(m["content"]) // 4 for m in self.content)

    def clear(self):
        self.content = []
        self.current_task_id = None

    def get_context(self) -> List[Dict[str, Any]]:
        return self.content

class SessionMemory:
    """
    Tier 2: Session Memory
    Capacity: 128K tokens compressed
    Retention: Current user session (until device lock/timeout)
    Content: Conversation history, task history, temporary plans
    Persistence: RAM + encrypted swap, auto-purged after 4h
    """
    def __init__(self, capacity: int = 128000, purge_timeout: int = 14400):
        self.capacity = capacity
        self.purge_timeout = purge_timeout
        self.history: List[Dict[str, Any]] = []
        self.last_activity = time.time()

    def add_interaction(self, interaction: Dict[str, Any]):
        self._check_purge()
        self.history.append({
            **interaction,
            "timestamp": time.time()
        })
        self.last_activity = time.time()

        # Simple token approximation
        current_tokens = sum(len(str(i)) // 4 for i in self.history)
        while current_tokens > self.capacity and self.history:
            self.history.pop(0)
            current_tokens = sum(len(str(i)) // 4 for i in self.history)

    def _check_purge(self):
        if time.time() - self.last_activity > self.purge_timeout:
            self.history = []

    def get_session_history(self) -> List[Dict[str, Any]]:
        self._check_purge()
        return self.history
