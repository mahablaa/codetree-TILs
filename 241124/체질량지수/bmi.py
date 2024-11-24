arr = input(). split()
h, w = int(arr[0]), int(arr[1])

b = (10000 * w) / (h ** 2)

print(int(b*10 // 10))
if b*100 // 10 >= 25:
    print("Obesity")