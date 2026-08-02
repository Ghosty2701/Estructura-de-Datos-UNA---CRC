import sys

palabra = sys.argv[1]

contador = 0

for letra in palabra:
    if letra in "aeiouAEIOU":
        contador += 1
print(f"La palabra '{palabra}' tiene {contador} vocales.")