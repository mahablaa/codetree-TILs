score_a = input(). split()
score_b = input(). split()
math_a = int(score_a[0])
eng_a = int(score_a[1])
math_b = int(score_b[0])
eng_b = int(score_b[1])

if math_a>math_b and eng_a>eng_b:
    print(1)
else:
    print(0)