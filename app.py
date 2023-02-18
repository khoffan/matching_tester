from src.matching import match_requesters_responder,find_closest_responder

class Requester:
    def __init__(self,name,location,time,preference_list):
        self.name = name
        self.location = location
        self.time = time
        self.preference_list = preference_list        

class Responder:
    def __init__(self,name,location):
        self.name = name
        self.location = location
        
requester1 = Requester('Requester 1', (52.5200, 13.4050), 30, [Responder('Responder A', (52.5160, 13.3779)), Responder('Responder B', (52.5200, 13.4050)), Responder('Responder C', (52.5147, 13.3466))])
requester2 = Requester('Requester 2', (52.5072, 13.3903), 20, [Responder('Responder A', (52.5160, 13.3779)), Responder('Responder C', (52.5147, 13.3466)), Responder('Responder B', (52.5200, 13.4050))])
requester3 = Requester('Requester 3', (52.4862, 13.4286), 60, [Responder('Responder C', (52.5147, 13.3466)), Responder('Responder B', (52.5200, 13.4050)), Responder('Responder A', (52.5160, 13.3779))])
responders = [Responder('Responder A', (52.5160, 13.3779)), Responder('Responder B', (52.5200, 13.4050)), Responder('Responder C', (52.5147, 13.3466))]

matches = []

for requester in [requester1,requester2,requester3]:
    match = match_requesters_responder([requester],find_closest_responder(requester,responders))
    matches.append(match)

for match in matches:
    print(f'{match[0].name} match with {match[1].name}')