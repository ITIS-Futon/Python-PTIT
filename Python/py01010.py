t = int(input())
while t:
    n = input()
    dau = n[0:2]
    cuoi = n[len(n)-2:len(n)]
    if(dau == cuoi): print("YES")
    else: print("NO")
    t -= 1