arr = input(). split()

a = int(arr[0])
b = int(arr[1])

if a < 90:
    print(0)
elif b >= 95:
    print(100000)
elif b >= 90:
    print(50000)
else:
    print(0)