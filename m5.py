from datetime import datetime

hozir = datetime.now()

formatlangan_sana = hozir.strftime("%d-%m-%Y")
print(formatlangan_sana) # Natija: 11.07.2026

formatlangan_vaqt = hozir.strftime("%Y/%m/%d %H:%M")
print(formatlangan_vaqt)
