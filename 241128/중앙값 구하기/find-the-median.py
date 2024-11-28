arr = input(). split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

if (a-b)*(a-c) < 0:
    print(a)
elif (b-a)*(b-c) < 0:
    print(b)
else:
    print(c)