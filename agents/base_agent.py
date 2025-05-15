
from typing import Dict, Any

class Agent:
    def __init__(self, name: str):
        self.name = name

    def receive(self, task: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError()
