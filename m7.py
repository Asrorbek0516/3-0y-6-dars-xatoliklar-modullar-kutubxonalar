import os

joriy_papka = os.getcwd()
print(f"Dastur ishga tushgan papka: {joriy_papka}")

fayllar_royxati = os.listdir(joriy_papka)

print("\nPapkadagi fayllar va papkalar ro'yxati:")
for i in fayllar_royxati:
    print(i)
