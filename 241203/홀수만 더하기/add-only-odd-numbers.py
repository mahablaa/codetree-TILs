n = int(input())
sum_val = 0

for _ in range (n):
    k = int(input())
    if k%2==1 and k%3==0:
        sum_val += k

print(sum_val)

