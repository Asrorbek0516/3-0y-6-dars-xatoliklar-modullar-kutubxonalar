from random import randint

import math

sonlar = [randint(1,100) for i in range(10)]
print(sonlar)
print(sum(sonlar))

ortacha = sum(sonlar)/len(sonlar)

print(f"{ortacha} yaxlitlangan natija: {math.floor(ortacha)}")