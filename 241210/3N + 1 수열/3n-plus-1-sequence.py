N = int(input())

cnt = 0
while True:
    if N == 1:
        break

    if N%2 == 0:
        N //= 2
        cnt += 1
    else:
        N = N*3 + 1
        cnt += 1

print(cnt)
