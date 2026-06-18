import time
from typing import Dict, Any, List

class DataSyncManager:
    """
    Tier 16.2: Offline Mesh Network
    Local collaboration and data synchronization between GemmaOS devices.
    """
    def __init__(self, mesh_node):
        self.mesh_node = mesh_node
        self.sync_queue: List[Dict[str, Any]] = []

    def queue_for_sync(self, category: str, data: Dict[str, Any]):
        """Queues local changes for broadcast to peers."""
        self.sync_queue.append({
            "timestamp": time.time(),
            "category": category,
            "data": data
        })

    def sync_with_peers(self):
        """Simulates data exchange over the mesh."""
        peers = self.mesh_node.discover_peers()
        if not peers:
            return False

        print(f"Sync: Synchronizing {len(self.sync_queue)} items with {len(peers)} peers...")
        for peer_id in peers:
            for item in self.sync_queue:
                self.mesh_node.send_message(peer_id, f"SYNC:{item['category']}")

        self.sync_queue = []
        return True

    def handle_incoming_sync(self, source_id: str, payload: str):
        """Processes incoming data from peers."""
        print(f"Sync: Received data from {source_id}: {payload}")
        return True
