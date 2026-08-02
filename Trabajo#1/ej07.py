import sys

num1 = int(sys.argv[1])

if num1 >= 90:
    print(f"La nota es una A")
elif num1 >= 80 and num1 < 90:
    print(f"La nota es una B de Basura")
elif num1 >= 70 and num1 < 80:
    print(f"La nota es una C")
elif num1 >= 60 and num1 < 70:
    print(f"La nota es una D")
else:
    print(f"La nota es una F")
 