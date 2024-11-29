arr = input(). split()
a, b = int(arr[0]), int(arr[1])

n = a
while n <= b:
    print(n, end = " ")
    if n%2 == 1:
        n *= 2
    else:
        n += 3