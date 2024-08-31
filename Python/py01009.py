xau = input()
hoa = 0
thg = 0
for i in str(xau):
    if (i.isupper() == 1): hoa += 1
    if (i.islower() == 1): thg += 1
if(hoa <= thg): print(xau.lower())
else: print(xau.upper())