import math

def prime(n):
    if n < 2: return 0
    for i in range(2, int(math.sqrt(n)), 1):
        if n % i == 0: return 0
    return 1

t = int(input())
while t:
    n = int(input())
    print(1, end = "")
    for i in range(2, int(math.sqrt(n)), 1):
        if(prime(i) == 1 and n % i == 0):
            print(" *", end = " ")
            cnt = 0
            while(n % i == 0):
                cnt += 1
                n /= i
            print(i, end = "^")
            print(cnt, end = "")
    if prime(n):
        print(" *", int(n), end = "^1")
    print()
    t -= 1