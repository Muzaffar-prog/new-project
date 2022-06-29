# Funkisyida xatoliklar tartibi:
# def my_func(name, lastname): 
#     """ Userdan ism va familiyasini bitta qilib chiqaruvchi funksiya """
#     print(f"Userning ismi: {name.title()} ")
#     print(f"Userning familiyasi: {lastname.title()} ")

# my_func(1997, 'olimov') 


# # Funksiyaga bir nechta argument uzatish:
# def age(name, age):
#     print(f"Do'stim: {name.title()} {2022-age}-yoshda")

# age(age=2000, name='fazliddin')  # ketma-ketlik joyini almashtirib qo'ysak xatolik beradi



# Standart qiymat berish:
# def yosh(yil,): 
#     print(f"Siz {yil-hozirgi_yil} yoshdasiz")

# yosh(1995)


""" 2 misol funksiya va qiymat """

# Funksiyadan oddiy qiymat qaytarish:
# def full_name(name, lastname):
#     """Toliq isma qaytaruvchi funksiya"""
#     toliq_ism = f"{name} {lastname}"
#     return toliq_ism # return qiymatni qaytaradi

# shaxs1 = full_name('akbar', 'halilov')
# shaxs2 = full_name('nurullo', 'shukurov')
# shaxs3 = full_name('husan', 'zikirov')
# print(shaxs1, shaxs2, shaxs3)



# ixtiyoriy argumentlar misoli:
# def full_name(ism, fam, fakultet=''):
#     if fakultet: # otasining_ismi mavjudligini tekshiramiz
#         full_name = f"{ism} {fam} {fakultet}"
#     else:
#         full_name = f"{ism} {fam} "
#     return full_name

# shaxs1 = full_name('akbar', 'halilov')
# shaxs2 = full_name('nurullo', 'shukurov', 'backend dasturchi')
# print(f' Bugungi darsga kelgan dasturchilar ismi: {shaxs1}, va \n kechikib kelgan dasturchi: {shaxs2} ')






# def xisoblash(min,max):
#     sonlar = [] # bo'sh ro'yxat
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar

# print(xisoblash(0,20))
# print(xisoblash(10,31))



# print(" Online bozordagi telefonlar ro'yxatini tuzamiz:")
# telefonlar_bush=[] 
# while True:
#     print("\nKo'rsatilgan ma'lumotlarni kiriting\n ",end='')
#     kompaniya=input("Ishlab chiqaruvchi komp: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
#     telefonlar_bush.append(telefonlar(kompaniya, model, rangi, korobka, yili, narhi))
#     javob = input(" Yana telefon qo'shasizmi?  'ha' | 'yoq' : ")
#     if javob == 'yoq':
#         break



# """ Funksiya haqida dars loyihalari: """

# def salomlashuv():
#     print('Assalomu Alaykum')

# salomlashuv()


# def salomBer(name):
#     """ Bu funksiya foydalanuvchi ismini qabul qilib usha ismga salom beruvchi funksiya """
#     print(f"Salom, {name} ")

# salomBer()








# def salom_ber():
#     print("Salom")
    
# salom_ber()



# def my_func():
#     print('Voliykum assalom')

# my_func()







# def my_func(name, yoshi):
#     """ Bu funksiyamiz ism qabul qilib unga salom beradi """
#     print(f"Assalomu Alaykum hurmatli, {name} yoshi: {yoshi} ")

# my_func("olimjon", 25)
# my_func(yoshi=25, name="Olimjon")






# def yoshni_chiqar(ismi, yoshi, hozirgi_yil=2022):
#     """ Foydalanuvchining ismini va yoshini chiqaruvchi func """
#     print(f"Talabaning ismi: {ismi.title()} yoshi: {hozirgi_yil - yoshi}")


# yoshni_chiqar("fazliddin", 1998)
# yoshni_chiqar("odiljon", 1998, 2022)

















""" Funksiya darsi 2-qism """

# def full_name(name, firstname, age, s_qiymat=5):
#     """ Userning to'liq ismini qabul qiluvchi funksiya: """
#     print(f" Userning ismi: {name} ")
#     print(f" Userning familyasi: {firstname} ")
#     print(f" Userning yoshi: {age} ") 

# full_name("Alimjon", "Allamov" )





""" return """
# def moshina(nomi, rangi, yili):
#     moshinalar = f" {nomi}, {rangi}, {yili} "
#     return moshinalar

# moshina1 = moshina('Malibu', 'Qora', 2022)
# moshina2 = moshina('Captiva', 'Oq', 2017)

# print(f" Birinchi moshina: {moshina1} \n Ikkinchi moshina: {moshina2} ")




""" ixtiyoriy argument """
# def telefonlar(nomi, yili, rangi=''):
#     if telefonlar:
#         telefon = f" {nomi} {yili} {rangi} "
#     else:
#         telefon = f" {nomi} {yili} {rangi} "
#     return telefon

# tel1 = telefonlar("Iphone", 2021, "Qora")
# tel2 = telefonlar("Samsung", 2014)

# print(f"Birinchi telefon: {tel1} \nIkkinchi telefon: {tel2} ")






""" funksiya ichidi bo'sh lug'at """

# def telefonlar(kompaniya, model, rangi, korobka, narhi,  yili=None):
#     telefon = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'narh':narhi,
#             'yil':yili
#             }
#     return telefon

# phone1 = telefonlar('Redmi', '10-pro', 'black', 'yoq', 2020)
# phone2 = telefonlar('Iphone', '13-pro max', 'yashil', 'bor', 2022, 1400)
# print(f" yili Ma'lum: {phone2}\n yili Noma'lum: {phone1} ")





# """ funksiya ichida ro'yxat """
# def sonlar(min, max):
#     son = []
#     while min < max:
#         son.append(min)
#         min += 1
#     return son

# print(sonlar(1,21))





# def moshinalar(nomi, rangi, narhi, yili, karobkasi=''):
#     if moshinalar:
#         moshina = f" {nomi} {rangi} {narhi} {yili} {karobkasi} "
#     else:
#         moshina = f" {nomi} {rangi} {narhi} {yili}  "
#     return moshina

# moshina1 = moshinalar("Tesla", "qora", 50000, 2022, "avto")
# moshina2 = moshinalar("Kia", "oq", 30000, 2021, )

# print(f" Karobkasi ma'lum: {moshina1} ")
# print(f" Karobkasi noma'lum: {moshina2} ")





# def telefonlar(kompaniya, model, rangi, narhi, operatovka, yili=None):
#     telefon = {
#         'kompaniya':kompaniya,
#         'model':model,
#         'rang':rangi,
#         'narh':narhi,
#         'operatovka':operatovka,
#         'yili':yili
#         }
#     return telefon

# phone1 = telefonlar("apple", "Iphone 12", 'qora', 800, 128, 2020)
# phone2 = telefonlar("apple", "Iphone 12", 'qora', 800, 128, )
# print(phone1)
# print(phone2)





# *args sonlar bilan ishlashi:
# def sonlar(*son):
#     return son

# print(sonlar(5 * 5))




# def ismlar(ismi, familya, **qolgan_malumot):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#     qolgan_malumot['ismi'] = ismi
#     qolgan_malumot['familya'] = familya
#     return qolgan_malumot

# ism1 = ismlar("Alisher", "Sattarov", otasining_ismi="Narimon o'g'li", t_yil=1998)
# ism2 = ismlar("Behruz", "Gaffarov", fakultet='Informatika', yoshi=23)
# print(ism1)
# print(ism2)






# lambda funksiyasi haqida:
# son = lambda a, b : a * b
# print(son(5, 6))

# # 2 misol
# son = lambda a : a + 10
# print(son(5)) 


# from math import sqrt # modullar ichidan ildiz chaqirildi:

# number = list(range(11))
# ildiz = list(map(sqrt, number))
# print(number)
# print(ildiz)



# # map() va lambda ishlashi:
# son = list(range(1, 11))
# kv = list(map(lambda x : x * x, son))
# print(kv)


# son = list(range(1, 11))
# def kv(x):
#     return x*x

# print(list(map(kv, son)))









# def moshina(*ism):
#     """ bu ismlar haqida malumot qaytaradi: """
#     return ism

# moshina1 = moshina("Malibu", 2022, "avto")
# print(moshina1)





# def moshina(nomi, rangi):
#     """ bu ismlar haqida malumot qaytaradi: """
#     m = f" {nomi} {rangi} "
#     return m

# moshina1 = moshina(nomi="KIA", rangi="Oq")
# print(moshina1)




# def dasturchi(ismi, **dev):
#     dev['ismi'] = ismi
#     return dev

# dasturchi1 = dasturchi("Olimjon", fam='Allamov', yoshi=24, sohasi="backend")
# print(dasturchi1)




# from math import sqrt

# number = list(range(1, 11))
# ildiz = list(map(sqrt, number))
# print(number)
# print(ildiz)





def salomlashuv():
    print("Assalomu Alaykum")
    


def ismlar(name, fam):
    print(f" {name} {fam} ")





