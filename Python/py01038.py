def sum(n):
    cnt = 0
    while(n % 7 != 0 and cnt <= 1000):
        cnt += 1
        n = str(n)
        m = int(n[::-1])
        n = int(n) + m
    return n

t = int(input())
while t:
    n = int(input())
    print(sum(n))
    t -= 1