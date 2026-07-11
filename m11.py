import random


son = random.randint(1,100)
count = 0
while count<5:
  
    count += 1
    taxmin = int(input(f"{count}-urinish: Son kiriting (1-100): "))
    if son == taxmin:
        print(f"Tabriklaymiz! {count} ta urinishda topdingiz!")
        break

    elif taxmin > son:
        print("Kichikroq!")
    else:
        print("Kattaroq!")

else:
    print(f"Imkoniyat tugadio! Topa olmadingiz oylagan son {son}")
    


# import random

# # Kompyuter tasodifiy son tanlaydi
# son = random.randint(1, 100)

# # Foydalanuvchiga 5 ta imkoniyat
# imkoniyat = 5

# for urinish in range(1, imkoniyat + 1):
#     taxmin = int(input(f"{urinish}-urinish: Son kiriting (1-100): "))

#     if taxmin == son:
#         print(f"Tabriklaymiz! {urinish} ta urinishda topdingiz!")
#         break
#     elif taxmin > son:
#         print("Kichikroq!")
#     else:
#         print("Kattaroq!")

# # Agar foydalanuvchi topa olmasa
# else:
#     print(f"Imkoniyat tugadi. Son {son} edi.")
