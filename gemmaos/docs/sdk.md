# GemmaOS X Infinity Developer SDK

## Creating a Custom AI Agent

1. Inherit from `gemmaos.agents.base.BaseAgent`.
2. Implement `reason(task)` to return action names.
3. Implement `act(action, params)` to execute tools.

## Example
```python
from gemmaos.agents.base import BaseAgent

class MyAgent(BaseAgent):
    def reason(self, task):
        return "my_action"

    def act(self, action, params):
        print("Executing custom action")
        return True
```

## System APIs
- `MemoryAPI`: Access Tier 1-5 memory.
- `MeshAPI`: Local peer communication.
- `PerceptionAPI`: Real-time sensor data.

## Research & Creator Studio APIs

### ResearchStudio
- `analyze_topic(topic)`: Semantic analysis of local vault.
- `generate_report(synthesis, format)`: PDF/Markdown report generation.

### CreatorStudio
- `create_project(type, prompt)`: Generate media content.
- `apply_style_transfer(file, style)`: Edit media with AI filters.

## Community Integration
- `share_workflow(workflow, privacy)`: Shared automation with the mesh.
