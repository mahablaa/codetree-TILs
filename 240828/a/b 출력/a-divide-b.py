arr = input(). split()
a, b = int(arr[0]), int(arr[1])
c = a//b
print(f"{c}.", end ="")

p = a%b

for i in range(1, 21):
    print(p*10//b, end = "")
    p = p*10%b