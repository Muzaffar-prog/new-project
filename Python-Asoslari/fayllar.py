

# Tayyor fayldan o'qish:
# fayl = open("myfile.txt")
# mavzu = fayl.read()
# print(mavzu)


# # faqatgina faylda yozilgan 1-qatorda yozilgan kodni oladi
# file1 = open("myfile.txt")
# mavzu = file1.readline()
# print(mavzu)




#Readline orqali barcha ma’lumotlarni o’qib olish
# file1 = open("myfile.txt")
# while True:
#     qator = file1.readline().rstrip('\n')
#     if not qator:
#         break
#     print(qator)
    

# file1= open("myfile.txt", "r")
# for line in file1:
#     print(line)




# f = open("myfile.txt", "w") # file ochildi va ichidagi ma'lumotlar o'chirildi
# f.write("Hamma tekst o'chib ketti! ") # file ga yangi matn qo'shiladi
# f.close()


# f = open("myfile.txt", "r") # yangi qo'shilgan matnni ochish
# print(f.read())




# """ Faylni o'chirish, agar mavjud bo'lsa """
# import os
# if os.path.exists("text.txt"):
#     os.remove("text.txt")
# else:
#     print("Bunday fayl mavjud emas!")




# """ Papkani o'chirish """
# import os
# os.rmdir("myfolder")




# fayl = open("py.txt", "w")
# fayl1 = fayl.read()
# print(fayl1)


""" Faqat bir qatorni o'qib oladi """
# fayl = open("test.txt")
# mavzu = fayl.readline()
# print(mavzu)



# For yordamida:
# file = open("test.txt")
# for n in file:
#     print(n)




# redline orqali barcha ma'lumotlarni o'qish
# file = open("test.txt")
# while True:
#     qatorlar = file.readline()
#     if not qatorlar:
#         break
#     else:
#         print(qatorlar)




# faylga ma'lumot yozish
# fayl = open('test.txt', 'a')
# fayl.write("Bu yangi so'z ")
# fayl.close()

# fayl = open('test.txt', 'r')
# print(fayl.read())




# # faylni ichidagi matnlar o'chib ketadi
# f = open('myfilea.txt', 'w')
# f.write("Bu yerda barcha matnlar o'chib ketdi")
# f.close()

# f = open('myfile.txt', 'r')
# print(f.read())




# # faylni yangi ochish agar ochilgan bo'lsa xato qaytaradi
# f = open('myfilea.txt', 'x')
# f.write("Bu yerda barcha matnlar o'chib ketdi")
# f.close()

# f = open('myfile.txt', 'r')
# print(f.read())












""" Fayllar bilan ishlash """

# fayl = open("myfile.txt")
# f = fayl.read()
# print(f)
# fayl.close()


# Qatorma qator o'qib olish
# fayl = open("myfile.txt")
# f = fayl.readline()
# print(f)


# file = open("myfile.txt")
# while True:
#     f = file.readline().rstrip()
#     if not f:
#         break
#     else:
#         print(f)



""" Yangi file ochib unga ma'lumot qo'shamiz! """
# fayl = open("malumot.txt", "w")
# fayl.write("Assalomu Alaykum bu matn yangi qo'shildi!\nBugun fayl haqida dars o'tyabmiz!")

# fayl = open("malumot.txt", "r")
# print(fayl.read())




# # Yangi file ichida ma'lumot bo'lsa davomidan yozadi
# fayl = open("malumot.txt", "a")
# fayl.write("Assalomu Alaykum bu matn yangi qo'shildi!")
# fayl.close()

# fayl = open("malumot.txt")
# print(fayl.read())






""" Faylni o'chirish! """
import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("Bunday fayl mavjud emas!")


