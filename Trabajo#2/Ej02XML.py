import xml.etree.ElementTree as ET

def guardar__xml(data, route):
    root = ET.Element("personas")
    for persona in data:
        nodo = ET.subelement(root, "persona")
        for key, value in persona.items():
            camp = ET.subelement(nodo, key)
            camp.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(route, encoding="utf-8", xml_declaration=True)


def leer__xml(route):
    tree = ET.parse(route)
    root = tree.getroot()
    data = []
    for node in root:
        persona = {child.tag: child.text for child in node}
        data.append(persona)
    return data
    