#
# while True:
#     print(" \n\n\n😊Online dukonimizga xush kelibsiz!"
#           " Dasturni ishlatish uchun surovlarga javob bering:👇 ")
#
#     komp_narxi = int(input(" 👉Kompyuter narxini kriting: "))
#     komp_nomi = input(" 👉Kompyuter nomini kiriting: ")
#     pul_miqdor = int(input(" 👉Sotib olish uchun qancha pulingiz bor: "))
#
#     if komp_narxi <= pul_miqdor:
#         print("----------MENU-------------")
#         print(f" \nSiz {komp_nomi}, kompyuterini sotib olishingiz mumkun! narhi {komp_narxi}$ ")
#         print(" 💻Sotib olish uchun <1> ni bosing: ")
#         print(" ❌Bekor qilish uchun <2> ni bosing: ")
#
#         mijoz = int(input("Sizning tanlovingiz>>> "))
#         if mijoz == 1:
#             print(f"💻Tabriklaymiz siz {komp_nomi}, ni sotib oldingiz qaytimingizni oling: {komp_narxi-pul_miqdor}$ ")
#         elif mijoz == 2:
#             print("❌To'lov bekor qilindi XAYR!!!")
#             break
#         else:
#             print("📌Dasturni amalga oshirish uchun <1> yoki <2> ni kiritish shart! ")
#             continue
#     else:
#         print(f" Kechirasiz, Siz {komp_nomi.title()}'ni sotib olishingiz uchun sizda {komp_narxi - pul_miqdor}$ yetmaydi! ")
#

import qrcode

manzil = "telegram.me/muzafchik"
qrcode.make(manzil).save("qrmanzil.jpg")

