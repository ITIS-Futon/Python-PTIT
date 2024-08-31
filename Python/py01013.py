import math

def gcd(a, b):
    if(a % b == 0): return b
    else:
        while b != 0:
            r = a % b
            a = b
            b = r
        return a

def prime(n):
    if n < 2: return 0
    for i in range(2, int(math.sqrt(n))+1, 1):
        if(n % i == 0): return 0
    return 1

def tcs(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum
t = int(input())
while t:
    a, b = map(int, input().split())
    ucln = gcd(a, b)
    if(prime(tcs(ucln)) == 1): print("YES")
    else: print("NO")
    t -= 1