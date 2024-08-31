import math

def prime(n):
    n = int(n)
    if (n < 2): return 0
    if (n == 2) or (n == 3): return 1
    if (n % 2 == 0) or (n % 3 == 0): return 0
    for i in range(5, int(math.sqrt(n)), 6):
        if (n % i == 0) or (n % (i+2) == 0): return 0
    return 1

# N là số nguyên tố; đảo ngược các chữ số của N cũng là một số nguyên tố; 
# tổng các chữ số của N là một số nguyên tố
# mỗi chữ số của N cũng là một số nguyên tố. 

def reverse(n):
    n = n[::-1]
    return n

t = int(input())
while t:
    n = input()
    check = 0
    sum = 0
    if(prime(n) == 1 and prime(reverse(n)) == 1): check = 1
    for i in str(n):
        if (prime(i)): sum += int(i)
        else: 
            check = 0
            break
    if (check == 0): print("No")
    else: print("Yes")
    t -= 1