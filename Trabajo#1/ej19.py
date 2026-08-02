import sys

archivo = sys.argv[1]

with open(archivo, "w") as f:
    for palabra in sys.argv[2:]:
        f.write(palabra + "\n")