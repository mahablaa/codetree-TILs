arr1 = input(). split()
arr2 = input(). split()
arr3 = input(). split()
d1, d2, d3 = arr1[0], arr2[0], arr3[0]
t1, t2, t3 = int(arr1[1]), int(arr2[1]), int(arr3[1])

if (d1 == 'Y' and t1 >= 37) and (d2 == 'Y' and t2 >= 37):
    print("E")
elif (d1 == 'Y' and t1 >= 37) and (d3 == 'Y' and t3 >= 37):
    print("E")
elif (d2 == 'Y' and t2 >= 37) and (d3 == 'Y' and t3 >= 37):
    print("E")
else:
    print("N")