
from typing import Dict, Any
from agents.base_agent import Agent
from tools.external_tools import get_museum_hours, get_restaurant_availability, get_transport_time

class PlanningAgent(Agent):
    def receive(self, task: Dict[str, Any]) -> Dict[str, Any]:
        subtasks = task.get("subtasks", {})
        print(f"[{self.name}] Planning itinerary...")

        schedule = []
        current_location = subtasks.get("start_location", "Hotel")
        current_time_hr = 9

        for museum in subtasks.get("visit", []):
            transport_time = get_transport_time(current_location, museum)
            arrival_time = current_time_hr + transport_time / 60
            museum_hours = get_museum_hours(museum)
            visit_duration = 2

            schedule.append(
                f"Travel from {current_location} to {museum} (takes {transport_time} min), arrive around {int(arrival_time)} AM"
            )
            schedule.append(
                f"Visit {museum} (open {museum_hours}) from {int(arrival_time)} AM to {int(arrival_time + visit_duration)} AM"
            )

            current_time_hr = arrival_time + visit_duration
            current_location = museum

        restaurant = subtasks.get("restaurant", "Le Gourmet")
        lunch_time = subtasks.get("lunch_time", "1 PM")
        lunch_hr = int(lunch_time.split()[0])
        available = get_restaurant_availability(restaurant, lunch_time)
        if available:
            transport_time = get_transport_time(current_location, restaurant)
            arrival_time = current_time_hr + transport_time / 60
            schedule.append(
                f"Travel from {current_location} to {restaurant} (takes {transport_time} min), arrive around {int(arrival_time)} AM"
            )
            schedule.append(f"Lunch at {restaurant} at {lunch_time}")
            current_time_hr = max(arrival_time, lunch_hr) + 1
            current_location = restaurant
        else:
            schedule.append(f"Restaurant {restaurant} not available at {lunch_time}, please choose another time/place.")

        return_time_str = subtasks.get("return_time", "7 PM")
        return_hr = int(return_time_str.split()[0]) + 12
        transport_time = get_transport_time(current_location, subtasks.get("start_location", "Hotel"))
        latest_departure_time = return_hr - transport_time / 60

        schedule.append(f"Travel back to Hotel (takes {transport_time} min), should depart by {int(latest_departure_time)} PM to arrive by {return_time_str}")

        return {"schedule": schedule}
