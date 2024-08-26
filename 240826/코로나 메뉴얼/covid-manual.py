p = input(). split()
q = input(). split()
r = input(). split()

p1, p2 = p[0], int(p[1])
q1, q2 = q[0], int(q[1])
r1, r2 = r[0], int(r[1])

if (p1 == 'Y') and (p2 >= 37):
    result_p = 1
else:
    result_p = 0

if (q1 == 'Y') and (q2 >= 37):
    result_q = 1
else:
    result_q = 0

if (r1 == 'Y') and (r2 >= 37):
    result_r = 1
else:
    result_r = 0

if (result_p + result_q + result_r >= 2):
    print("E")
else:
    print("N")