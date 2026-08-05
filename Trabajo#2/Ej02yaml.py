import yaml

def guardar__yaml(data, route):
    with open(route, 'w') as f:
        yaml.dump(data, f)
        
def leer__yaml(route):
    with open(route, 'r') as f:
        return yaml.safe_load(f)