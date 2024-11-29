arr = input(). split()
a, b = int(arr[0]), int(arr[1])

c = a//b
print(f"{c}.", end ="")

i = a*10
for _ in range(20):
    print(i//b, end="")
    i = i%b*10