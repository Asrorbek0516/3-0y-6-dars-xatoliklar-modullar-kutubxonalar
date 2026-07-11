import random


son = random.randint(1,100)
count = 0
while count<5:
    try:
        count += 1
        taxmin = int(input(f"{count}-urinish: Son kiriting (1-100): "))
    except ValueError:
        print("Iltimos son kiriting! ")
        continue

    if son == taxmin:
        print(f"Tabriklaymiz! {count} ta urinishda topdingiz!")
        break

    elif taxmin > son:
        print("Kichikroq!")
    else:
        print("Kattaroq!")

else:
    print(f"Imkoniyat tugadio! Topa olmadingiz oylagan son {son}")
    