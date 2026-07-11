try:
    yosh = int(input("Yoshingizni kiriting: "))
    if yosh < 0 or yosh > 120:
        raise ValueError("Yosh noto'g'ri kiritildi!")
    else:
        print("Yosh:", yosh)
except ValueError as e:
    print("Xatolik:", e)
finally:
    print("Tekshiruv tugadi")
