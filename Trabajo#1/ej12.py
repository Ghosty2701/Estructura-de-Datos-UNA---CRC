import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        print(i)
