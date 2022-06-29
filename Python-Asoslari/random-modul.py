# import random

# """ Randint funksiyasi """
# son = random.randint(10,100)
# print('Tasadifiy raqam: ',son)

# """ Choice() funksiyasi: """
# ismlar = ['olim', 'husan', 'asliddin', 'amvar', 'shavkat']
# ism = random.choice(ismlar)
# print(ism)
# print(random.choice(ism))

# """ sonalar ustida choice()"""
# s = list(range(1,10))
# print(s)
# print(random.choice(s))

# """ shuffle alamshtirib tashlash """
# sonlar = list(range(1,11))
# print(sonlar)
# random.shuffle(sonlar)
# print(sonlar)








import random as r

# sonlar = list(range(1,11))
# print("List ichidagi sonlar:", sonlar)

# randint() sonlarni chiqarib berish
# son = r.randint(1,5)
# print("Random qaytargan son:",son)


# # chocie() bilan ishlash:
# ismlar = ["Javohir", "Muzaffar", "Madina", "Ilyos", "Suhrob"]
# print(ismlar) 
# ism = r.choice(ismlar)
# print(ism)
# print(r.choice(ism))

# # sonlar ustida chocie()
# sonlar = list(range(1,11))
# print(sonlar)
# print(r.choice(sonlar))


# shuffle funksiyasi:
sonlar = list(range(1,11))
print(sonlar)
r.shuffle(sonlar)
print(sonlar)














