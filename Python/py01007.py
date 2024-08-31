t = int(input())
while t:
    n, x, m = map(float, input().split())
    cnt = 0
    while n < m:
        cnt += 1
        n = n + n*x/100
    print(cnt)
    t -= 1