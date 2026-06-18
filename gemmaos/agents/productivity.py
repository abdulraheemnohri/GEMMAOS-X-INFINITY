from gemmaos.agents.base import BaseAgent
from typing import Dict, Any, List

class ProductivityAgent(BaseAgent):
    """
    Productivity Agent: Task and schedule management.
    """
    def __init__(self):
        super().__init__(name="ProductivityAgent")
        self.tasks: List[Dict[str, Any]] = []
        self.notes: List[Dict[str, Any]] = []

    def reason(self, task: Dict[str, Any]) -> str:
        intent = task.get("intent", "")
        if "note" in intent:
            return "create_note"
        if "task" in intent or "todo" in intent:
            return "create_task"
        return "unknown_action"

    def act(self, action: str, params: Dict[str, Any] = None) -> bool:
        if action == "create_note":
            note = {
                "title": params.get("title", "Untitled Note"),
                "content": params.get("content", ""),
                "tags": params.get("tags", [])
            }
            self.notes.append(note)
            print(f"Note created: {note['title']}")
            return True

        if action == "create_task":
            task = {
                "title": params.get("title", "Untitled Task"),
                "due_date": params.get("due_date"),
                "priority": params.get("priority", "medium")
            }
            self.tasks.append(task)
            print(f"Task created: {task['title']}")
            return True

        return False
