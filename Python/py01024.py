def tcs(a):
    sum = 0
    a = int(a)
    while a > 0:
        b = a % 10
        sum += b
        a //= 10
    return sum

def check(a):
    for i in range(0, len(a), 1):
        if( abs(int(a[i]) - int(a[i-1])) == 2 or abs(int(a[i]) - int(a[i+1])) == 2):
            return 1
    return 0

t = int(input())
while t:
    n = input()
    if(len(n) >= 3):
        if tcs(n) % 10 == 0 and check(n) == 1: print("YES")
        else: print("NO")
    t -= 1