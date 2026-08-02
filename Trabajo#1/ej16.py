import sys

palabra = sys.argv[1]

final = ""

for i in range(len(palabra) - 1, -1, -1):
    final += palabra[i]
    
print(final)



