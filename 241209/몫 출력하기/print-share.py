cnt = 0
while True:
    n = int(input())
    if n%2 == 1:
        continue
    elif n%2 == 0:
        print(n//2)
        cnt += 1

    if n%2==0 and cnt == 3:
        break