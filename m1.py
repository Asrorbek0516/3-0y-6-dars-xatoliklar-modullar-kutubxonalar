import math
son = int(input("Son kiriting: "))
try:
    if son > 0:
        print(f"{son} ning kvadrat ildizi = {math.sqrt(son)}")
    else:
        raise ValueError("Manfiy sonning ildizi yuq!")
        
except ValueError as V:
    print(V)