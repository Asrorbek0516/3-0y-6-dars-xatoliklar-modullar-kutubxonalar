try:
    parol = input("Parol kiriting: ")
    if len(parol) < 6:
        raise ValueError("Parol juda qisqa!")  # o'z xatongizni chiqarish
    else:
        print("Parol qabul qilindi!")
except ValueError as e:
    print("Xato:", e)
