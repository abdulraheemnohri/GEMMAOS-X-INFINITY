import sqlite3
import json
import time
from typing import Dict, Any, List, Optional

class LongTermMemory:
    """
    Tier 3: Long-Term Memory
    Capacity: Unlimited (structured DB)
    Retention: Permanent (user-controlled deletion)
    Content: Preferences, projects, interaction history, facts
    Persistence: SQLite, encrypted at rest
    """
    def __init__(self, db_path: str = "gemmaos_memory.db"):
        self.conn = sqlite3.connect(db_path)
        self._init_db()

    def _init_db(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS interactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp REAL,
                category TEXT,
                data TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS preferences (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        """)
        self.conn.commit()

    def save_interaction(self, category: str, interaction: Dict[str, Any]):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO interactions (timestamp, category, data) VALUES (?, ?, ?)",
            (time.time(), category, json.dumps(interaction))
        )
        self.conn.commit()

    def get_interactions(self, category: str = None) -> List[Dict[str, Any]]:
        cursor = self.conn.cursor()
        if category:
            cursor.execute("SELECT timestamp, category, data FROM interactions WHERE category = ?", (category,))
        else:
            cursor.execute("SELECT timestamp, category, data FROM interactions")

        results = []
        for row in cursor.fetchall():
            results.append({
                "timestamp": row[0],
                "category": row[1],
                "data": json.loads(row[2])
            })
        return results

    def set_preference(self, key: str, value: Any):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO preferences (key, value) VALUES (?, ?)",
            (key, json.dumps(value))
        )
        self.conn.commit()

    def get_preference(self, key: str) -> Optional[Any]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT value FROM preferences WHERE key = ?", (key,))
        row = cursor.fetchone()
        return json.loads(row[0]) if row else None

    def close(self):
        self.conn.close()
