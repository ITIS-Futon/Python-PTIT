import math

def prime(n):
    if n < 2: return 0
    for i in range(2, int(math.sqrt(n)), 1):
        if (n % i == 0): return 0
    return 1

def gcd(a, b):
    if(b == 0): return a
    return gcd(b, a%b)

t = int(input())
while t:
    n = int(input())
    k = 0
    for i in range(1, n, 1): 
        if(gcd(i, n) == 1): k += 1
    if prime(k): print("YES")
    else: print("NO")
    t -= 1