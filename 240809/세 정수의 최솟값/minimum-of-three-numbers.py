arr = input(). split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if a < b:
    b = a
else:
    a = b

if a <= c:
    print(a)
else:
    print(c)