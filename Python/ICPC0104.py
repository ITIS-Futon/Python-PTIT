def snn(xau):
    so = []
    link = ""
    for i in xau:
        if(i.isdigit()):
            link += i
        else:
            if link:
                so.append(int(link))
                link = ""
    if link:
        so.append(int(link))
    return min(so)

t = int(input())
while t:
    xau = input()
    print(snn(xau))
    t -= 1