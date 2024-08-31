t = int(input())
while t:
    s1 = input()
    check = 1   
    for i in range(1, len(s1), 1):
        if(abs(ord(s1[i]) - ord(s1[i-1]))) != abs(ord(s1[-i]) - ord(s1[-i-1])):
            check = 0
    if check: print("YES")
    else: print("NO")
    t -= 1