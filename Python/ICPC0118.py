def Zodiac(d, m):
    if(21 <= d <= 31 and m == 3) or (1 <= d <= 19 and m == 4):
        return "Bach Duong"
    if(20 <= d <= 30 and m == 4) or (1 <= d <= 20 and m == 5):
        return "Kim Nguu"
    if(21 <= d <= 31 and m == 5) or (1 <= d <= 20 and m == 6):
        return "Song Tu"
    if(21 <= d <= 30 and m == 6) or (1 <= d <= 22 and m == 7):
        return "Cu Giai"
    if(23 <= d <= 31 and m == 7) or (1 <= d <= 22 and m == 8):
        return "Su Tu"
    if(23 <= d <= 31 and m == 8) or (1 <= d <= 22 and m == 9):
        return "Xu Nu"
    if(23 <= d <= 30 and m == 9) or (1 <= d <= 22 and m == 10):
        return "Thien Binh"
    if(23 <= d <= 31 and m == 10) or (1 <= d <= 22 and m == 11):
        return "Thien Yet"
    if(23 <= d <= 30 and m == 11) or (1 <= d <= 21 and m == 12):
        return "Nhan Ma"
    if(22 <= d <= 31 and m == 12) or (1 <= d <= 19 and m == 1):
        return "Ma Ket"
    if(20 <= d <= 31 and m == 1) or (1 <= d <= 18 and m == 2):
        return "Bao Binh"
    if(19 <= d <= 29 and m == 2) or (1 <= d <= 20 and m == 3):
        return "Song Ngu"

t = int(input())
while t:
    d, m = map(int, input().split())
    print(Zodiac(d, m))
    t -= 1