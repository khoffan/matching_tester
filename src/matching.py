from math import radians, sin, cos, sqrt, atan2

def match_requesters_responder(requesters, responder):
    # Initialize each requester's current proposal index to 0
    current_proposal = {requester: 0 for requester in requesters}
    
    # Initialize the responder's current match to None
    current_match = None
    
    while current_match is None:
        # For each requester, propose to the responder at their current proposal index
        for requester in requesters:
            proposal_responder = requester.preference_list[current_proposal[requester]]
            if proposal_responder == responder:
                # The responder accepts the proposal
                current_match = (requester, responder)
                break
            elif (proposal_responder.location == responder.location
                  or haversine(proposal_responder.location, responder.location) <= requester.time):
                # The responder rejects the proposal and updates their preference to the new requester
                if current_match is None or calculate_travel_time(proposal_responder.location, responder.location) < calculate_travel_time(current_match[0].location, current_match[1].location):
                    current_match = (requester, proposal_responder)
        
        # If the responder has rejected a proposal, move on to the next highest-ranked requester
        if current_match is None:
            proposal_requester = max(requesters, key=lambda r: r.preference_list.index(responder))
            current_proposal[proposal_requester] += 1
    
    return current_match

def haversine(location1, location2):
    # Calculate the great-circle distance between two points on the Earth's surface
    earth_radius = 6371  # km
    lat1, lon1 = radians(location1[0]), radians(location1[1])
    lat2, lon2 = radians(location2[0]), radians(location2[1])
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return earth_radius * c

def calculate_travel_time(location1, location2):
    # Calculate the travel time between two locations proportional to their distance
    travel_speed = 50  # km/h
    return haversine(location1, location2) / travel_speed * 60  # minutes

def find_closest_responder(requester, responders):
    # Find the closest responder to the requester based on distance
    closest_responder = None
    min_distance = float('inf')
    
    for responder in responders:
        distance = haversine(requester.location, responder.location)
        if distance < min_distance:
            closest_responder = responder
            min_distance = distance
    
    return closest_responder
