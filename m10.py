import datetime

bugun = datetime.datetime.today().weekday()

if bugun == 0:
    print("Bugun dushanba, dam olish vaqti emas!")
elif bugun == 5:
    print("Bugun shanba, dam oling!")
elif bugun == 6:
    print("Bugun yakshanba, dam oling!")
else:
    print("Bugun ish kuni!")
