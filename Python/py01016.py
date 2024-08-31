t = int(input())
while t:
    xmh = input()
    xbd = []
    for i in range(0, len(xmh), 1):
        if xmh[i].isdigit(): 
            for j in range(1, int(xmh[i])+1, 1):
                xbd.append(xmh[i-1])
    for i in xbd:
        print(i, end = "")
    print()
    t -= 1