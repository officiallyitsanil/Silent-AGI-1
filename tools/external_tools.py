
def get_museum_hours(museum_name: str) -> str:
    hours = {
        "Louvre": "9 AM - 6 PM",
        "Orsay": "9:30 AM - 6 PM",
        "Pompidou": "11 AM - 9 PM"
    }
    return hours.get(museum_name, "Closed")

def get_restaurant_availability(restaurant_name: str, time_slot: str) -> bool:
    available_slots = {
        "Le Gourmet": ["12 PM", "1 PM", "2 PM"],
        "Bistro Paris": ["12 PM", "1 PM"]
    }
    return time_slot in available_slots.get(restaurant_name, [])

def get_transport_time(from_loc: str, to_loc: str) -> int:
    mock_times = {
        ("Hotel", "Louvre"): 15,
        ("Louvre", "Orsay"): 20,
        ("Orsay", "Le Gourmet"): 10,
        ("Le Gourmet", "Hotel"): 25
    }
    return mock_times.get((from_loc, to_loc), 30)
