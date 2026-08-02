import sys

palabra = sys.argv[1]

final = ""

for i in range(len(palabra) - 1, -1, -1):
    final += palabra[i]
print(final)
if palabra.lower() == final.lower():
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")


