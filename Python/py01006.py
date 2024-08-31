t = int(input())
while t:
    n = input()
    check = 0
    for i in str(n):
        if (i == "4" or i == "7"): check = 1
        else: 
            check = 0
            break
    if (check == 1): print("YES")
    else: print("NO")
    t -= 1