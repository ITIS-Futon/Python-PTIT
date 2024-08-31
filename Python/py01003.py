def lam_tron(n):
    p = 10
    while n >= p:
        n = (n + p // 2) // p * p 
        # n + p // 2 để n là int/ll thay vì float/double
        # // p * p để làm tròn các lớp đơn vị
        p *= 10
    return n

t = int(input())
while t:
    n = int(input())
    print(lam_tron(n))
    t -= 1

 