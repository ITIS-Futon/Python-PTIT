def giai_thua(n):
    gt = 1
    for i in range(2, n+1):
       gt *= i
    return gt

def sum_num(n):
    sum = 0
    for i in str(n):
        sum += giai_thua(int(i))
    return sum

t = int(input())
while t:
    n = input()
    if sum_num(n) == int(n): print("YES")
    else: print("NO")
    t -= 1