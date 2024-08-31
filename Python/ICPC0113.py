import math

def tn(n):
    m = 0
    while n > 0:
        a = n % 10
        m = m*10 + a
        n //= 10
    return m

def prime(n):
    if n < 2: return 0
    for i in range(2, int(math.sqrt(n))+1, 1):
        if(n % i == 0): return 0
    return 1

t = int(input())
while t:
    res = []
    n = int(input())
    for i in range(2, n+1, 1):
        if(prime(i)):
            if(i != tn(i) and prime(tn(i)) == 1):
                if(tn(i) < n):
                    res.append(tn(i))
                res.append(i)
    for i in res:
        if(res.count(i) > 1): res.remove(i)
    for i in res:
        print(i, end = " ")
    print()
    t -= 1