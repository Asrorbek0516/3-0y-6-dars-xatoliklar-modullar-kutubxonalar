sonlar = []

while len(sonlar) < 3:
    try:
        son = int(input("Son kiriting: "))
        sonlar.append(son)
    except ValueError:
        print("Xato, son kiriting!")

print("Kiritilgan sonlar ro'yxati:", sonlar)
