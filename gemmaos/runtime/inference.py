from enum import Enum
from typing import Dict, Any, List

class Hardware(Enum):
    CPU = "CPU"
    GPU = "GPU"
    NPU = "NPU"
    DSP = "DSP"

class InferenceBackend(Enum):
    LITERT = "LiteRT"
    MEDIAPIPE = "MediaPipe"
    ONNX = "ONNX"
    MLC = "MLC"
    LLAMA_CPP = "llama.cpp"

def detect_hardware() -> Dict[str, bool]:
    """Mock hardware detection."""
    return {
        "CPU": True,
        "GPU": True,
        "NPU": False, # Assume NPU not available in sandbox
        "DSP": False
    }

def route_inference(model: str, input_size: int, latency_requirement: int, power_budget: str) -> Hardware:
    """
    Routes inference to the best available hardware based on requirements.

    Logic from PRD:
    - critical power budget and DSP available -> DSP
    - latency < 100ms and NPU available -> NPU
    - input > 4096 and GPU available -> GPU
    - fallback -> CPU
    """
    available = detect_hardware()

    if power_budget == "critical" and available.get("DSP"):
        return Hardware.DSP

    if latency_requirement < 100 and available.get("NPU"):
        return Hardware.NPU

    if input_size > 4096 and available.get("GPU"):
        return Hardware.GPU

    return Hardware.CPU

class ModelManager:
    """Manages AI models, updates, and quantization."""
    def __init__(self):
        self.loaded_models: Dict[str, Any] = {}

    def load_model(self, model_id: str, hardware: Hardware):
        print(f"Loading {model_id} on {hardware.value}...")
        self.loaded_models[model_id] = {"status": "loaded", "hardware": hardware}

    def benchmark(self, model_id: str) -> Dict[str, float]:
        return {"tokens_per_sec": 45.0, "latency_ms": 120.0}
