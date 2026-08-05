import json

def guardar__json(data, route):
    with open(route, 'w') as f:
        json.dump(data, f, indent=4)
        
def leer__json(route):
    with open(route, 'r') as f:
        return json.load(f)