
# print(" Darsga kelgan dasturchilar ro'yxatini tuzamiz ")
# dasturchilar = []

# n=1 # Userni sanaydi
# while True:
#     savol = f" {n}-Bugungi darsda bor odamni ismini kiriting: "
#     ismlar = input(savol)
#     dasturchilar.append(ismlar)
#     savol2 = input(f" Yana ism qo'shasizmi || ha/yoq ")
#     if savol2 == 'ha':
#         n+=1
#         continue
#     else:
#         break

# print('Bugun darsga kelgan dasturchilar royxati:')
# for ismlar in dasturchilar:
#     print(ismlar.title())







# print()
# print()
# print()
# print()
# print()


# print(" Bugun darsdagilarni ismi va yoshini saqlaymiz!!! ")
# dasturchilar = {}
# ishora = True
# while ishora:
#     name = input("Bugun darsda bor dasturchini ismini kiriting>>> ")
#     age = input(f"{name.title()}-ning yoshini kiriting: ")
#     dasturchilar[name] = int(age)

#     savol = input(f" Yana ism qo'shasizmi || ha/yoq ")
#     if savol == 'yoq':
#         ishora = False
    
# print('\n Bugungi darsda bor dasturchilar ismi va yoshi: ')
# for name, age in dasturchilar.items():
#     print(f" {name.title()}-ning yoshi {age}-da ")





# # ro'yxatdagi elemntni o'chirish
# avtolar = ['nexia', 'malibu', 'gentra', 'nexia', 'captiva', 'nexia']
# while 'nexia' in avtolar:
#     avtolar.remove('nexia')
# print('\nBizning royxatda qolgan moshinalar: ', avtolar)




# # ro'yxatdan ro'yxatga element ko'chirish
# talabalar = ['alisher', 'nizom', 'odil']
# bahonlagan_talabar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f" {talaba} ning bahosini kiriting: ")
#     print(f" {talaba} baholandi! ")
#     bahonlagan_talabar[talaba] = baho

# print("Baholangan talabalar: ", bahonlagan_talabar)
# for kalit, qiymat in bahonlagan_talabar.items():
#     print(f" Ism: {kalit} ")
#     print(f" Bahosi: {qiymat} ")









# avtolar = ['nexia', 'malibu', 'gentra', 'nexia', 'captiva', 'matiz', 'spark', 'nexia']
# while 'nexia' in avtolar:
#     avtolar.remove('nexia')
# print(avtolar)





# ro'yxatdan ro'yxatga element ko'chirish
talabalar = ['habibullo', 'doniyor', 'saidbek', 'mustafo', 'suhrob', 'quvonchbek']
baholangan_talabar = {}

while talabalar:
    talaba = talabalar.pop()
    baho = input(f" {talaba.title()}'ning bahosini kiriting: ")
    print(f" {talaba.title()}-baholandi! ")
    baholangan_talabar[talaba] = baho

for ism, baho in baholangan_talabar.items():
    print(f" Talaba ismi: {ism} ")
    print(f" Talaba bahosi: {baho} ")




