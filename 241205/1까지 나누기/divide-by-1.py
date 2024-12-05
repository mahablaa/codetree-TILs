n = int(input())

div = n
for i in range(1, n):
    div //= i
    if div <= 1:
        print(i)
        break