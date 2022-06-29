





# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")







# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat<0:
#         continue
#     elif qiymat=='Exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")








# kitoblar = []
# print(" yaxshi ko'rgan kitoblaringizni ro'yxatini tuzamiz! ")
# n=1  # kitoblarni sanash uchun o'zgaruvchi 
# while True:
#     savol = f"{n} - kitobingizni kiriting>>> " 
#     kitob = input(savol)
#     kitoblar.append(kitob)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break




# print("Do'stlaringiz ro'yxati:")
# for kitob in kitoblar:
#     print(kitob.title())




# print(" Kursdoshlaringiz yoshini saqlovchi dastur! ")
# yaqinlar = {}
# ishora = True
# while ishora:
#     ism = input(" Kursdoshingizning ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     yaqinlar[ism] = int(yosh) # ism kalit, yosh qiymat
    
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False

# print("Kursdoshlaringiz ro'yxati!")
# for ism, yosh in yaqinlar.items():
#     print(f"{ism.title()} {yosh} yoshda")





# ismlar = ['alisher','asomiddin','behruz', 'alisher', 'nilufar', 'abdusattor', 'adham', 'fazliddin', 'alisher']
# while 'alisher' in ismlar: 
#     ismlar.remove('alisher') 
# print(ismlar)



# oquvchilar = ['alisher', 'odil', 'alimjon', 'nodirbek']
# baholangan_oquvchilar = {}
# while oquvchilar:
#     oquvchi = oquvchilar.pop()
#     baho = input(f"{oquvchi.title()}'ning bahosini kiriting: ")
#     print(f"{oquvchi.title()} baholandi")
#     baholangan_oquvchilar[oquvchi] = baho


# savol = "istalgan son kiriting \n(dasturni to\'xtatish uchun esa 'stop') buyrug'ini bosing "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'stop':
#         ishora = False
#     else:
#         print(float(qiymat)**3)
        



 

# son = 1
# while son <= 10:
#     print(son, end=', ')
#     son += 1
# print("Dastur tugadi!")





# print()
# print()
# print()

# print(" Kiritilgan sonning kvadratini chiqaruvchi dastur ")
# savol = "Istalgan son kiriting, (dasturni to'xtatish uchun esa 'stop' buyrug'ini yozing ) "
# qiymat = ''
# while qiymat != 'stop':
#     qiymat = input(savol)
#     if qiymat != 'stop':
#         print(float(qiymat)**2)
# print('dastur yakunlandi!')




# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(f" {float(qiymat) == 4} sizga kirish bepul ")
#     else:
#         print(f" {float(qiymat) == 10} sizga kirish 10000 ")

        




# while True:
#     yosh = input('Yoshingiz nechida ')
#     if int(yosh) >= 5:
#         print('sizga kirish bepul')
#     elif int(yosh) >= 15:
#         print('sizga kirish 6000 som ')
#     elif yosh == 'stop':
#         print('dastur tugadi')
#         break



"""" Ishora haqida misol """

# print("kiritilgan sonning kvadratini chiqarib beruvchi dastur")
# matn = "Istalgan son kiriting: "
# matn += "Dasturni toxtatish uchun esa ('exit' deb yozing)>>> "
# qiymat = True
# while qiymat:
#     qiymat = input(matn)
#     if qiymat == 'stop':
#         qiymat = False

#     else:
#         print(f" {qiymat}ning kvadrati: {int(qiymat)**2}")

# print('the')







""" break haqida misol """


# print('men kiritilgan ismga salom beruvchi dasturman!')
# salom = ' \n Ismingingizni kiriting: \n Dasturni toxtatish uchun esa stop buyrugini bosing>>> '

# while True:
#     savol = input(salom)
#     if savol == 'stop':
#         break
#     else:
#         print(f'Assalomu Alaykum,', savol)
# print('the end')




""" for yordamida break ishlashi """
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 11:
#         break
#     else:
#         print(f'{son} ning kubi {son**3}-ga teng! ')





""" contineu yordamida ishlatish """
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 11:
#         continue
#     else:
#         print(f'{son} ning kvadrati {son**2}-ga teng! ')





# """ son % bilan bolsinishi """
# son = 0 
# while son < 20:
#     son += 1
#     if son % 2 != 0:
#         continue
#     else:
#         print(son)





""" While 2 dars misollar """
# # while yordamida ro'yxatni toldirish

# print('darsga kemagan bollar')
# ismlar = []
# n = 1
# while True:
#     savol = f' {n}-kemagan bolani ismini kiriting: '
#     ism = input(savol)
#     ismlar.append(ism)

#     savol2 = input('yana ism qoshasizmi ha yoq')
#     n+=1
#     if savol2 == 'yoq':
#         break

# print('kemagan bollar ')
# for ism in ismlar:
#     print(ism.title())




# # while yordamida lugatni toldirish
# print('ism va yoshni saqlaymiz')
# ismlar = {}
# ishora = True
# while ishora:
#     ism = input('ismini kirit')
#     yosh = input(f'{ism}-ning yoshini kirit')
#     ismlar[ism] = int(yosh)
    
#     savol2 = input('yana ism qoshasizmi ha yoq ')
#     if savol2 == 'yoq':
#         ishora = False

# print('kemagan bollar ')
# for ism, yosh in ismlar.items():
#     print(f" {ism} yoshi {yosh} da ")



# """ Dasturchilarni boholaymiz """
# dasturchilar = ['olim', 'azizbek', 'hasan']
# dasturchilar_boholangan = {}
# while dasturchilar:
#     dasturchi = dasturchilar.pop()
#     baho = input(f' {dasturchi} ning bohosi kirit ')
#     print('boholandi')
#     dasturchilar_boholangan[dasturchi] = int(baho)

# print(dasturchilar)
# print(dasturchilar_boholangan)









print('Istalgan sonning kubini chiqaruvchi dastur')
savol = "Istalgan son kiriting,"
savol += "\n(dasturni to'xtatish uchun esa 'toxta' buyrug'ini yozing )"

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    else:
        print(float(qiymat)**3)

print('\ndastur yakunlandi!')




# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f" {son}-ning kvadrati {son**2}-ga teng! ")


# son = 0
# while son < 10:
#     son += 1
#     if son % 2 != 0:
#         continue
#     else:
#         print(son)






# son = 1           
# while son > 0:   
#     son += 1       
#     if son % 2 != 0:
#         continue
#     else:
#         print('juft sonlar',son)

























