# gps_routing.py
import random

def get_random_direction():
    directions = [
        "Head north",
        "Head south",
        "Turn left",
        "Turn right",
        "Continue straight"
    ]
    return random.choice(directions)

def get_route(start, end):
    # Generate a simulated route with random directions
    route_instructions = [f"Start from {start}."]
    for _ in range(5):  # Simulate 5 steps
        route_instructions.append(f"{get_random_direction()} for {random.randint(1, 20)} miles.")
    route_instructions.append(f"Arrive at {end}.")
    return route_instructions
