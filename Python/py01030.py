import math

def gcd(a, b):
    if a % b == 0: return b
    while(b != 0):
        r = a % b
        a = b
        b = r
    return a

n, k = map(int, input().split())
dem = 0
for i in range(10**(k-1), 10**k - 1):
    if(gcd(i, n) == 1): 
        dem += 1
        print(i, end = " ")
    if(dem == 10): 
        print()
        dem = 0