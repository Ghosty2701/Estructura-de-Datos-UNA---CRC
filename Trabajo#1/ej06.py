import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])

if num1 < num3 and num2 < num3:
    print (f"El numero {num3} es el mayor")
elif num1 < num2 and num2 > num3:
    print (f"El numero {num2} es el mayor")
else:
    print (f"El numero {num1} es el mayor")
    
    