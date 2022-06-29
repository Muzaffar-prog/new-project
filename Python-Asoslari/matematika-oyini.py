
""" Matematika o'yini """

import random
import os
def menu():

    birinchimi = True
    while True:
        if birinchimi:
            print("\n\n✋Assalomu Alaykum bu  == MATEMATIKA ==  o'yini dasturi\nbu dastur orqali siz o'z bilimgizni sinab ko'rishingiz mumkun."
                  "\ndasturni ishga tushirish uchun quyidagi menu'dan kerakli darajani tanlab o'yinni boshlang!")
            tanlov = input("""\n\t\t- + / * kerakli bo'limni tanlang * / + -
                 1. OSON,
                 2. O'RTA,
                 3. QIYIN,
                 4, ortga...
        1 va 4 oralig'idagi son kiriting.
        Kiriting>>> """)
            birinchimi = False
        else:
            tanlov = input("Xato, 1 va 4 oralig'idagi son kiriting. ")

        if tanlov.isdigit() and int(tanlov) in range(1, 5):
            return int(tanlov)



def play(daraja):
    takror = 5
    user_bal = 0
    for j in range(takror):
        amallar = random.choice(["+", "-", "*", "/"])
        masala = None
        javob = None
        for son in range(daraja + 1):
            a = random.randint(1, 10)
            if son == 0:
                masala = str(a)
                javob = a
            else:
                masala += f" {amallar} {a} "
                if amallar == "+":
                    javob += a
                elif amallar == "-":
                    javob -= a
                elif amallar == "*":
                    javob *= a
                if amallar == "/":
                    javob = round(javob / a, 2)
        natija = input(f"Misolni javobini yozing: {masala} =  ")
        if float(natija) == javob:
            print("Javob to'g'ri!")
            user_bal += 1
        else:
            print(f"Xato, to'g'ri javob: {javob}\n")
    print(f"Siz {takror} savoldan {user_bal}-ta to'g'ri javob topdingiz")




while True:
    os.system('cls')
    tanlov = menu()
    if tanlov == 1:
        print("\nHurmatli o'yinchi siz menu'dan <<OSON>> bo'limini tanladingiz:")
        play(daraja=1)

    elif tanlov == 2:
        print("\nHurmatli o'yinchi siz menu'dan <<O'RTA>> bo'limini tanladingiz:")
        play(daraja=2)

    elif tanlov == 3:
        print("\nHurmatli o'yinchi siz menu'dan <<QIYIN>> bo'limini tanladingiz:")
        play(daraja=3)

    elif tanlov == 4:
        print("Siz dasturdan chiqdingiz!")
        break

    savol = input("Yana o'yin o'ynaysizmi? | ha/yoq: ")
    if savol == "ha":
        continue
    else:
        print("O'yin tugadi!")
        break
