import sys
import random

num1 = int(sys.argv[1])
tot = 0
mayor = 0

for i in range(num1):
    numr = random.randint(1, 100)
    tot += numr
    if numr > mayor:
        mayor = numr
print(f"El promedio es: {tot/num1} \nEl numero mayor es: {mayor}")
