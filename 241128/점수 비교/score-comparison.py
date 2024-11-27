Arr = input(). split()
Brr = input(). split()
math_A, eng_A = int(Arr[0]), int(Arr[1])
math_B, eng_B = int(Brr[0]), int(Brr[1])

if math_A > math_B and eng_A > eng_B:
    print(1)
else:
    print(0)