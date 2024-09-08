arr = input(). split()
a, b = int(arr[0]), int(arr[1])


num = a
while num <= b:
    print(num, end = " ")
    if num % 2 == 0:
        num += 3
    else:
        num *= 2