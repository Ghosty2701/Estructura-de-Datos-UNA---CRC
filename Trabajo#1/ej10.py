import sys

num1 = int(sys.argv[1])
tot = 0

for i in range(1, num1 + 1):
    tot += i
print (f"La suma de los numeros del 1 al {num1} es {tot}")