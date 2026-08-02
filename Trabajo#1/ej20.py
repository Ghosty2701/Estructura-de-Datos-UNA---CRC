import sys

archivo = sys.argv[1]

lineas = 0
palabras = 0
caracteres = 0

with open(archivo, "r") as f:
    for linea in f:
        lineas += 1
        palabras += len(linea.split())
        caracteres += len(linea)

print(f"Líneas: {lineas}")
print(f"Palabras: {palabras}")
print(f"Caracteres: {caracteres}")