
try:
    a,b = map(int,input("sonlarni kiriting: ").split())
    print(a/b)

except ZeroDivisionError:
    print("0 ga bo'lib bolmaydi!")
except ValueError:
    print("Iltimos son kiriting!")