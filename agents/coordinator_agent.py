
from typing import List, Dict, Any
from agents.base_agent import Agent

class CoordinatorAgent(Agent):
    def __init__(self, name: str, agents: List[Agent]):
        super().__init__(name)
        self.agents = {agent.name: agent for agent in agents}

    def receive(self, task: Dict[str, Any]) -> Dict[str, Any]:
        print(f"[{self.name}] Starting coordination...")

        parse_result = self.agents["LanguageAgent"].receive(task)
        plan_result = self.agents["PlanningAgent"].receive(parse_result)

        print(f"[{self.name}] Final itinerary:")
        for item in plan_result.get("schedule", []):
            print(" -", item)

        return plan_result
