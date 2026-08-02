import sys

num1 = int(sys.argv[1])
tot = 1

for i in range(1, num1 + 1):
    tot *= i
print (f"El factorial de {num1} es {tot}")