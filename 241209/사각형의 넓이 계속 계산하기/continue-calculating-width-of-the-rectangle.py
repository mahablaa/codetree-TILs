while True:
    arr = input(). split()
    w, d = int(arr[0]), int(arr[1])
    name = arr[2]
    area = w*d
    print(area)
    if name == 'C':
        break