A = input(). split()
B = input(). split()

math_a, eng_a = int(A[0]), int(A[1])
math_b, eng_b = int(B[0]), int(B[1])

if math_a == math_b:
    print("A" if eng_a > eng_b else "B")
elif math_a > math_b:
    print("A")
else:
    print("B")