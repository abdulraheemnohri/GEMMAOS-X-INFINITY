from typing import Dict, Any, List

class CreatorStudio:
    """
    Tier 14: AI Creator Studio
    Image, Video, and Audio generation front-end.
    """
    def __init__(self, media_agent):
        self.media_agent = media_agent
        self.gallery: List[Dict[str, Any]] = []

    def create_project(self, project_type: str, prompt: str):
        """Dispatches generation task to MediaAgent."""
        print(f"Creator Studio: Starting new {project_type} project...")
        success = self.media_agent.act(f"generate_{project_type}", {"prompt": prompt})
        if success:
            self.gallery.append({"type": project_type, "prompt": prompt, "status": "completed"})
            return True
        return False

    def list_gallery(self) -> List[Dict[str, Any]]:
        return self.gallery

    def apply_style_transfer(self, file_path: str, style: str):
        """Uses MediaAgent to edit existing content."""
        return self.media_agent.act("edit_media", {"file": file_path, "instruction": f"Apply {style} style"})
