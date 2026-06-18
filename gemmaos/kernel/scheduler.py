from enum import Enum
from typing import Dict, Any, List

class ResourceType(Enum):
    CPU = "CPU"
    GPU = "GPU"
    NPU = "NPU"
    DSP = "DSP"

class AIResourceScheduler:
    """
    Tier 2.1: AI Resource Scheduler
    Manages task allocation across heterogeneous hardware (CPU/GPU/NPU/DSP).
    """
    def __init__(self):
        self.load_table: Dict[ResourceType, float] = {
            ResourceType.CPU: 10.0,
            ResourceType.GPU: 5.0,
            ResourceType.NPU: 0.0,
            ResourceType.DSP: 0.0
        }

    def schedule_task(self, task_type: str, requirements: Dict[str, Any]) -> ResourceType:
        """Determines the best hardware target for a given task."""
        print(f"Kernel: Scheduling {task_type}...")

        # Logic: NPU > GPU > CPU for AI tasks
        if task_type in ["inference", "embedding"] and self.load_table[ResourceType.NPU] < 80.0:
            target = ResourceType.NPU
        elif task_type in ["image_gen", "video_edit"] and self.load_table[ResourceType.GPU] < 85.0:
            target = ResourceType.GPU
        else:
            target = ResourceType.CPU

        self.load_table[target] += 5.0
        print(f"Kernel: Task scheduled on {target.value}")
        return target

    def get_load_report(self) -> Dict[str, float]:
        return {res.value: load for res, load in self.load_table.items()}
