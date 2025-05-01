technicians = [
    {"name": "Tech A", "location": "San Francisco", "services": ["engine repair", "electrical"]},
    {"name": "Tech B", "location": "Los Angeles", "services": ["plumbing", "engine repair"]},
]

def find_technicians(location, service_needed):
    return [
        tech for tech in technicians if tech['location'] == location and service_needed in tech['services']
    ]
