
from agents.language_agent import LanguageAgent
from agents.planning_agent import PlanningAgent
from agents.coordinator_agent import CoordinatorAgent

def main():
    language_agent = LanguageAgent("LanguageAgent")
    planning_agent = PlanningAgent("PlanningAgent")
    coordinator = CoordinatorAgent("CoordinatorAgent", [language_agent, planning_agent])

    user_query = "Plan a day trip to Paris with museum visits and lunch, return by 7 PM."
    result = coordinator.receive({"query": user_query})

if __name__ == "__main__":
    main()
