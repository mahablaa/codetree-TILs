cnt = 0
sum_val = 0

for _ in range (10):
    n = int(input())
    if n >= 0 and n <= 200:
        cnt += 1
        sum_val += n

avg = sum_val/cnt
print(f"{sum_val} {avg:.1f}")
