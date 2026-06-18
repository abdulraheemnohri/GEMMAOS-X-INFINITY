import time
from typing import List, Dict, Any

class MemoryConsolidator:
    """
    Tier 5.2: Memory Consolidation
    Nightly process: compress Session Memory into Long-Term/Semantic memory.
    """
    def __init__(self, session_memory, long_term_memory, knowledge_vault):
        self.session_memory = session_memory
        self.long_term_memory = long_term_memory
        self.knowledge_vault = knowledge_vault

    def run_nightly_consolidation(self):
        """Processes and clears session memory."""
        print("Consolidation: Starting nightly memory optimization...")
        history = self.session_memory.get_session_history()

        if not history:
            print("Consolidation: No new session data found.")
            return

        # 1. Summarize and Save to Long-Term
        summary = self._summarize_session(history)
        self.long_term_memory.save_interaction("session_summary", {"summary": summary})

        # 2. Extract Knowledge for Vault
        self._extract_to_vault(history)

        # 3. Clear Session Memory
        self.session_memory.history = []
        print("Consolidation: Nightly process complete.")

    def _summarize_session(self, history: List[Dict[str, Any]]) -> str:
        """Mocked summarization of the day's activities."""
        return f"User performed {len(history)} tasks today across various agents."

    def _extract_to_vault(self, history: List[Dict[str, Any]]):
        """Identifies key facts/files to move to semantic knowledge."""
        for item in history:
            if item.get("important", False):
                self.knowledge_vault.ingest_content(
                    content=item.get("content", ""),
                    content_type="fact",
                    metadata={"source": "session_consolidation"}
                )
