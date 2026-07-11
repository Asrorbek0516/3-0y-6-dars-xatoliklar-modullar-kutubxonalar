from datetime import datetime

hozir = datetime.now()

tugilgan_yil = int(input("Tugilgan yilingizni kiriting: "))

hozirgi_year = hozir.year

yosh = hozirgi_year - tugilgan_yil

print(f"Siz {yosh} yoshdasiz")