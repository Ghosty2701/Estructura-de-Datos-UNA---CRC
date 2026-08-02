import sys
import random
import string

long = int(sys.argv[1])

caracteres = string.ascii_letters + string.digits

contrasena = ""

for i in range(long):
    contrasena += random.choice(caracteres)

print(f"La contraseña generada es: {contrasena}")