from gemmaos.agents.base import BaseAgent
from typing import Dict, Any, List

class MediaAgent(BaseAgent):
    """
    Tier 7.2.5: Media Agent
    Purpose: Content creation and editing.
    """
    def __init__(self):
        super().__init__(name="MediaAgent")
        self.projects: List[Dict[str, Any]] = []

    def reason(self, task: Dict[str, Any]) -> str:
        intent = task.get("intent", "")
        if "generate" in intent and "image" in intent:
            return "generate_image"
        if "edit" in intent:
            return "edit_media"
        if "audio" in intent or "podcast" in intent:
            return "process_audio"
        return "unknown_action"

    def act(self, action: str, params: Dict[str, Any] = None) -> bool:
        if action == "generate_image":
            prompt = params.get("prompt", "GemmaOS Logo")
            print(f"MediaAgent: Generating image with SDXL Turbo: {prompt}")
            self.projects.append({"type": "image", "prompt": prompt})
            return True

        if action == "edit_media":
            file = params.get("file", "image.png")
            instruction = params.get("instruction", "Apply Neural Glass style")
            print(f"MediaAgent: Editing {file} - {instruction}")
            return True

        if action == "process_audio":
            print("MediaAgent: Running Whisper/Piper for audio processing...")
            return True

        return False
