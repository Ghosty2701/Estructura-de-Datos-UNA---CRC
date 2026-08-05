from Ej02json import guardar_json, leer_json
from Ej02yaml import guardar_yaml, leer_yaml
from Ej02XML import guardar_xml, leer_xml

datos = [
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Luis", "edad": 25}
]

guardar_json(datos, "personas.json")
guardar_yaml(datos, "personas.yaml")
guardar_xml(datos, "personas.xml")

print(leer_json("personas.json"))
print(leer_yaml("personas.yaml"))
print(leer_xml("personas.xml"))