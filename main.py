"""
For Bilan Ishlashni Ko'rib Chiqamiz
For - Uchun
"""



Mehmonlar = ['Diyorbek', 'Elbek', 'John', 'Abdusattor']
for Mehmon in Mehmonlar:
    print("Assalomu Alaykum", Mehmon)
    print("Hayr", Mehmon)


Davomiga Xabar Qo'shish

Mehmonlar = ['Diyorbek', 'Elbek', 'John', 'Abdusattor']
for Mehmon in Mehmonlar:
    print(f"Hurmatli Mehmonlar {Mehmon} Sizni Yangi Yilda Kutib Qolamiz")


Range - Sonlarni Ketma Ketligini Rivojlantiradi


Sonlar Bilan Ishlash

Sonlar = list(range(1,24))
for Son in Sonlar:
      print(f"{Son} Ning Darajasi {Son **2} Ga Teng")


Append Qo'shish

Sonlar = list(range(24))
Sonlar_Kvadrati = []
for Son in Sonlar:
    Sonlar_Kvadrati.append(Son **2)    # Append - Qiymat Qo'shish

print(Sonlar)
print(Sonlar_Kvadrati)




Input Orqali Foydalanuvchidann Ma'lumot Olish  Input - "KIRITISH" Ma'lumot Olishda Yordamlashadi

Dostlar = []
print("10 Eng Yaqin Do'stingizni Ismini Kiriting ")
for n in range(10):
    Dostlar.append(input(f"{n+1} - Kiriting"))
    print(Dostlar)




