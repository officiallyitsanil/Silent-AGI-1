
from typing import Dict, Any
from agents.base_agent import Agent

class LanguageAgent(Agent):
    def receive(self, task: Dict[str, Any]) -> Dict[str, Any]:
        print(f"[{self.name}] Parsing input query...")
        query = task.get("query", "").lower()
        subtasks = {
            "visit": ["Louvre", "Orsay"],
            "lunch_time": "1 PM",
            "restaurant": "Le Gourmet",
            "return_time": "7 PM",
            "start_location": "Hotel"
        }
        return {"subtasks": subtasks}
