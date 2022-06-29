

""" Online bozor loyihasi: """

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


""" QR code  yaratish dastur: """

# import qrcode
#
# m = "instagram.com/muzaf_lv"
# qrcode.make(m).save('insta.jpg')
#






""" Pythonda kalkulyator dasturi: """

# print(" -=-=- Kalkulator -=-=- ")
# natija = 0
# ishora = ''
# while True:
#     son1 = int(input(" <1> sonni kiriting: "))
#     son2 = int(input(" <2> sonni kiriting: "))
#     print(""" 
#         Shartlardan birini tanlang:
#         1, qo'shish,
#         2, ayirish,
#         3, ko'payitirish,
#         4, bo'lish,
#      """)
#     user = int(input(" Kiriting>>> "))
#     if user == 1:
#         natija = son1 + son2
#         ishora = '+'
#     elif user == 2:
#         natija = son1 - son2
#         ishora = '-'
#     elif user == 3:
#         natija = son1 * son2
#         ishora = '*'
#     elif user == 4:
#         natija = son1 // son2
#         ishora = '/'
#     else:
#         print(f" Kechirasiz, menuda bunday son mavjud emas! Qayta urinib ko'ring ")
#         continue
#     print(f"Natija: {son1} {ishora} {son2} = {natija} ")










# import random
""" son topish o'yini: """
# print("\n\nSalom son topish o'yiniga hush kelibsiz \nMen 1-dan 20-gacha son o'yladim topaolasizmi?")
# kompyuter = random.randint(1,20)
# n = 0
# while True:
#     son = int(input(f"Son kiriting: "))
#     n += 1
#     if kompyuter == son:
#         print(f"Tabriklayman siz javobini topdingiz {n}-marta urindingiz: ")
#         murojat = input('Yana oynaymizmi? ha/yoq>>> ')
#         if murojat == "ha":
#             continue
#         else:
#             print("Xayr! o'yinimiz tugadi")
#             break
#     elif kompyuter < son:
#         print("Xato!, siz yuborgan raqam katta ")
#     else:
#         print("Xato!, siz kiritgan raqam kichik ")





""" Son topish o'yini 2-qism """

# import random
# boshi = 1
# ohiri = 30
# n = 0
# while True:
#     son = random.randint(boshi, ohiri)
#     user = input(f" {son} tengmi (t), kattami (+), kichikmi (-): ")
#     n += 1
#     if user == "t":
#         print(f"men topdim urinishlar soni: {n}")
    
#     elif user == "+":
#         boshi = son + 1
          
#     elif user == "-":
#         ohiri = son - 1










# """ login project """
# user = [
#     {"username":'user', "id":'5556555', "password":'1555'}
# ]
# print("\nAssalomu Alaykum ro'yxatdan o'tish bo'limiga hush kelibsiz!\nMenudan o'zingizga kerakli bo'limni tanlang:")
# def main():
#     def login():
#         username = input("Foydalanuvchi ismi: ")
#         password = input("Foydalanuvchi kodi: ")
#         for users in user:
#             if users['username'] == username and users['password'] == password: 
#                 print("Tabriklaymiz Akkauntga kirdingiz!")
#                 break
#             else:
#                 print("Xato! login va parolingizni o'ylab qayta urining:")
#                 login()
    

#     def create():
#         username = input("Yangi foydalanuvchi logini: ")
#         password = input("Yangi parol: ")
#         id_kod = input("Yangi ID: ")

#         new_account = {"username": username, "id": id_kod, "password": password}
#         user.append(new_account)
#         print(user)
#         print("Ro'yxatdan o'tdingiz")
#         main()
    
#     print("1 - akkauntga kirish: ")
#     print("2 - yangi akkaunt yaratish: ")
#     kirish = int(input(">>> "))
#     if kirish == 1:
#         login()
#     else:
#         create()
# main()











# """ Matematika o'yini """
# import random

# def menu():

#     birinchimi = True
#     while True:
#         if birinchimi:
#             tanlov = input("""O'zingizga kerakli darajani tanlang:
#                      1. OSON,
#                      2. O'RTA,
#                      3. QIYIN,
#                      4, ortga...
#                  1 va 4 oralig'idagi son kiriting.
#                  Kiriting>>> """)
#             birinchimi = False
#         else:
#             tanlov = input("Xato, 1 va 4 oralig'idagi son kiriting. ")

#         if tanlov.isdigit() and int(tanlov) in range(1, 5):
#             return int(tanlov)



# tanlov = menu()
# if tanlov == 1:
#     takror = 5
#     for j in range(takror):
#         pass
#         amallar = random.choice(["+", "-", "*", "/"])
#         masala = None
#         javob = None
#         for son in range(2):
#             a = random.randint(1, 10)
#             if son == 0:
#                 masala = str(a)
#                 javob = a
#             else:
#                 masala += f" {amallar} {a} "
#                 if amallar == "+":
#                     javob += a
#                 elif amallar == "-":
#                     javob -= a
#                 elif amallar == "*":
#                     javob *= a
#                 if amallar == "/":
#                     javob = round(javob / a, 2)
#         natija = input(f" Misolni javobini yozing: {masala} =  ")
#         if float(natija) == javob:
#             print(" Javob to'g'ri!")
#         else:
#             print(f" Xato, to'g'ri javob: {javob}")



# elif tanlov == 2:
#     print("O'rta o'yin")

# elif tanlov == 3:
#     print("Qiyin o'yin")

# elif tanlov == 4:
#     print("Chiqish")
    








""" login registartion: """
# from cmath import log


# user = [
#     {"username":'test', "id":'4545445', "password":'4455'}
# ]

# print("\n\nAssalomu Alaykum ro'yxatdan o'tish bo'limiga hush kelibsiz\nMenu'dan kerakli bo'limni tanlang:")

# def main():
#     def login():
#         username = input("Foydalanuvchi nomi: ")
#         password = input("Foydalanuvchi kodi: ")
#         for users in user:
#             if users['username'] == username and users['password'] == password:
#                 print("Tabriklaymiz siz akkauntga kirdingiz! ")
#                 break
#             else:
#                 print("Xato! login va parolni o'ylab qayta kiriting:")
#                 login()
                
#     def create():
#         username = input("Yangi login kiriting: ")
#         password = input("Yangi parol kiriting: ")
#         id_raqam = input("Yangi ID kiriting: ")
        
#         new_user = {"username":username, "id":id_raqam, "password":password}
#         user.append(new_user)
#         print(user)
#         print("Siz ro'yxatdan o'tdingiz!")
#         login()

#     print(" ---menu--- ")
#     print("1 - kirish:")
#     print("2 - ro'yxatdan o'tish:")
#     javob = int(input("Kiriting>>>  "))

#     if javob == 1:
#         login()
#     elif javob == 2:
#         create()
# main()






""" Quduq qaychi o'yini """


import random
print("\n\n\n\n")
print("Assalomu Alaykum kompyuter bilan << quduq-qaychi-qog'oz >> o'yiniga hush kelibsiz")
print("O'yinni boshlash uchun shartlardan birini tanlang:\n ")
variantlar = ["quduq", "qaychi", "qogoz"]
k = 0
f = 0
d = 0
for i in range(5):
    komp = random.choice(variantlar)
    user = input(f"Varyantni tanlang: {variantlar}\n>>> ")
    if komp == "quduq" and user == "qaychi" or komp == "qogoz" and user == "quduq" or komp == "qaychi" and user == "qogoz": 
        print("Kompyuter yutdi!")
        k += 1
    elif komp == user:
        print("Durrang!")
        d += 1
    else:
        print("Siz yutdingiz!")
        f += 1
    print(f"(Kompyuter) {komp}:{user} (Foydanaluvchi)\n ")
print(f"Hisoblar: (kompyuter) {k}:{f} (foydalanuvchi)\nDurranglar soni {d} ")





