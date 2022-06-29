
# talaba = {'ismi':'muzaffar murodov',  'yili':2000,  'yoshi':25 }
# talaba['lavozim'] = 'dasturchi'
# talaba['kursi'] = 3

# print(f" {talaba['ismi'].title()}, tug'ilgan yili {talaba['yili']}, {talaba['yoshi']}-yoshda,\
# {talaba['lavozim']}, {talaba['kursi']}-kursda oqiydi ")

# print(talaba)



# 3 misol

# kerakli = {
#     "integer": "Butun son",
#     "float": "O'nlik son",
#     "string": "Matn",
#     "list": "Ro'yxat",
#     "tuple": "O'zgarmas ro'yxat",
# }

# kalit = input("Kalit so'z kiriting:").lower()
# tarjima = kerakli.get(kalit)
# if tarjima == None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")




# viloyatlar = {
#     'alisher':'surxondaryo',
#     'aziz':'toshkent',
#     'madina':'namangan',
#     'xusnidiin':'qashqadaryo'
# }
# print(viloyatlar)


# viloyat = viloyatlar.get('nur', 'bunday ism mavjud emas')
# print(viloyat)








# telefonlar = {'sarvar':'nokia',
#               'behruz':'iphone',  
#               'alisher':'redmi-10',  
#               'sirojiddin':'samsung',
#               'muzaffar':'iphone',
#               'asliddin':'redmi-10'
#               }

# print("Do'stlarim quyidagi telefon modellarni ishlatishadi! ")    
# for dostlarim in set(telefonlar.values()):
#     print(dostlarim)


# print(mahsulotlar.values())

# menu = {
#     "osh": 20000,
#     "lag'mon": 22000,
#     "non": 4000,
#     "choy": 5000,
#     "shashlik": 12000,
#     "somsa": 6000,
#     "tabaka": 15000,
# }

# print("3 ta taom buyurtma bering.")
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom:").lower())

# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {buyurtma} yo'q.")


# moshina = {'modeli':'kia', 'yili':2020}
# for kalit, qiymat in moshina.items():
#     print(f" Kalit: {kalit} ")
#     print(f" Qiymat: {qiymat} ")




# moshina = {'modeli':'ferrai ',  'rangi':'qizil', 'yili':2020}

# # yangi qiymat qo'shish
# moshina['narhi'] = 22000
# moshina['karobka'] = 'avto'

# # qiymatni yangilash
# moshina['yili'] = 2022
# moshina['modeli'] = 'Gm'

# print(moshina)



# moshina = {}
# # print(moshina)


# moshina['modeli'] = 'KIA'
# moshina['rang'] = 'qora'
# moshina['yurgan_km'] = 78000
# # print(moshina)


# talaba = {'ismi':'qobil', 'fam':'karimov', 't_yili':1995, 'viloyati':'samarqand'}
# print(talaba)


# del talaba['viloyati'] 
# print(talaba)




# telefonlar = {
#     'Fazliddin':'Samarqand', 
#     'Zubaydullo':'Surxandaryo', 
#     'Alisher':'Toshkent', 
#     'Doston':'Fargona',
#     'Anvar':'Namangan',
#     }

# telefon = telefonlar['habibullo']
# print(f" {telefon} ")




# # alohida chiqarish
# avtolar = {
#     'alisher':'ferrari',
#     'fazliddin':'malibu',
#     'suhrob':'captiva',
#     'azizbek':'spark',
#     }
# bozorlik = ['olma', 'alisher', 'banan', 'suhrob']
# for avto in avtolar:
#     if avto in bozorlik:
#         print(f" {avto.title()}, {avtolar[avto]}-so'm ")
    




# # tartiblab chiqarish
# avtolar = {
#     'b':'ferrari',
#     'c':'malibu',
#     'a':'captiva',
#     'd':'spark',
#     'a':'spark',
#     }
# print("dukondagi mahsulot")    
# for avto in avtolar:
#     print(avto.title())






# viloyatlar = {
#     'Fazliddin':'Samarqand', 
#     'Zubaydullo':'Surxandaryo', 
#     'Alisher':'Toshkent', 
#     'Doston':'Fargona',
#     'Anvar':'Namangan',
#     }







# royxat = {
#     'banan':21000,
#     'olma':15000,
#     'anor':25000,
#     'olcha':30000,
#     'gilos':14000
# }
# buyurtma = ['banan', 'olma', 'ananas', 'shaftoli']
# for mijoz in royxat:
#     if mijoz not in buyurtma:
#         print(f" Iltimos, {mijoz.title()}'ni dukoningizga ham olib keling ")
#     else:
#         print(f" {mijoz.title()} bor, narhi {royxat[mijoz]}-so'm ")





doslarim = {
    'alisher':'redmi',
    'husniddin':'iphone',
    'doston':'samsung',
    'fazliddin':'redmi',
    'odil':'samsung',
    'mansur':'realme',
    'anvar':'iphone',
    'bobur':'iphone'
}
print()
for dostlar in sorted(doslarim):
    print(dostlar.title())







