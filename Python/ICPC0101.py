n = int(input())
day = list(map(int, input().split()))
i = 0
while i < len(day) - 1:
    if(day[i] + day[i+1]) % 2 == 0:
        day.pop(i)
        #luc nay ptu tai i+1 da tro thanh ptu tai i
        day.pop(i)
        if i > 0: i -= 1
    else: i += 1
print(len(day))
