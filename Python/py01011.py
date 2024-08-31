def tn(n):
    m = 0
    while n > 0:
        a = n % 10
        m = m*10 + a
        n //= 10
    return m

def check(i):
    cnt = 0
    while i > 0:
        a = i % 10
        if a % 2 != 0: return 0
        i //= 10
        cnt += 1
    return cnt % 2 == 0

t = int(input())
while t:
    n = int(input())
    for i in range(22, n+1, 1):
        if(check(i) == 1 and i == tn(i)): 
            print(i, end = " ")
    print()
    t -= 1