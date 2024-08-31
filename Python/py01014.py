a, k, n = map(int, input().split())
    # a + b <= n
    # (a + b) % k == 0
    # giả sử a = k.q1 + r1
    #        b = k.q2 + r2
    # => a+b = k(q1 + q2) + (r1 + r2)
    # vậy chỉ cần chứng minh (r1+r2)%k == 0
    # nếu r1 = 0 (tức a % k == 0) => r2 = 0 => b % k == 0
    # nếu r1 != 0: giả sử r1 + r2 = k 
    # => r2 = k - r1
    # => b%k = k - r1
    # => tìm được b
    # => kết hợp đk a + b <= n => dãy các b cần tìm
# res = []
res = set()
r1 = a % k
r2 = k - r1
    # for i in range(0, n-a+1, 1):
    #     if(i % k == r2): 
    #         res.add(i)
for i in range(r2, n-a+1, k):
    res.add(i)
    # res.append(i)
if(len(res) != 0):
    for i in res:
        print(i, end = " ")
else: print(-1)

    # t -= 1