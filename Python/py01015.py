t = int(input())
while t:
    so = input()
    check = 1
    for i in range(0, len(so)-1, 1):
        if int(so[i]) > int(so[i+1]):
            check = 0
            break
    if check == 1: print("YES")
    else: print("NO")
    t -= 1