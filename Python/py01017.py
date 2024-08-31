t = int(input())
while t:
    xbd = input()
    xmh = []
    cnt = 1
    for i in range(1, len(xbd), 1):
        if(xbd[i-1] == xbd[i]):
            cnt += 1
        else: 
            xmh.append(cnt)
            xmh.append(xbd[i-1])
            cnt = 1
    # if(xbd[len(xbd)-1] != xbd[len(xbd)-2]):
    #     xmh.append(cnt)
    #     xmh.append(xbd[-1])
    # else:
    xmh.append(cnt)
    xmh.append(xbd[-1])     
    for i in xmh:
        print(i, end = "")
    print()
    t -= 1