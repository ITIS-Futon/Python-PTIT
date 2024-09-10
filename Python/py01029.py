import math

def gcd(a, b):
    if a % b == 0: return b
    while(b != 0):
        r = a % b
        a = b
        b = r
    return a

def dao(n):
    m = n[::-1]
    return m

t = int(input())
while t:
    n = input()
    m = dao(n)
    n = int(n)
    m = int(m)
    if (gcd(n, m) == 1): print("YES")
    else: print("NO")
    t -= 1