n = int(input())

sum_val = 0
for _ in range(n):
    k = int(input())
    sum_val += k

avg = sum_val/n
print(f"{sum_val} {avg:.1f}")
