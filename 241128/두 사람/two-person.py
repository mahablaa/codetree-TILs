arr = input(). split()
brr = input(). split()
age1 = int(arr[0])
sex1 = arr[1]
age2 = int(brr[0])
sex2 = brr[1]

if (sex1 == 'M' and age1 >= 19) or (sex2 == 'M' and age2 >= 19):
    print(1)
else:
    print(0)