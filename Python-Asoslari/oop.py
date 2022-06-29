



# son = 25
# print(type(son))

# s = 1.25
# print(type(s))


# def my_func():
#     print("Salom")


# print(type(my_func))







# class Talaba:
#     def __init__(self, ismi, fam, yoshi):
#         self.name = ismi
#         self.fam = fam
#         self.yosh = yoshi

#     def get_name(self):
#         return self.name

# talaba1 = Talaba("Olimjon", fam="Allamov", yoshi=18)  #Obyekt yaratish
# talaba2 = Talaba("Azimjon", "Fazliddinov", 28)  # 2 - qism

# print(talaba1.name)
# print(talaba2.fam)
# print("yoshi",talaba2.yosh)







# class Moshina:
#     def __init__(self, nomi, modeli, rangi, yili):
#         self.nomi = nomi
#         self.model = modeli
#         self.rang = rangi
#         self.yil = yili

#     def get_nomi(self):
#         return self.nomi
    
#     def get_model(self):
#         return self.model

#     def yangi_info(self):
#         print(f" Moshina madeli: {self.model} nomi: {self.nomi} rangi: {self.rang} yili: {self.yil} ")

# moshina1 = Moshina("Malibu", "GM", "Qora", 2022)
# print("Model:",moshina1.get_model())






# class Web_Site:

#     def __init__(self):
#         # Bu yerda saytni footer qismi ishlaydi
#         pass
    
#     def __init__(self):
#         # Bu yerda saytni contact bo'limi ishlaydi
#         pass

#     def __init__(self):
#         # Bu yerda saytni Navbar bo'limi ishlaydi
#         pass








""" Super klass """
# class Moshina:
#     # # Moshinalar haqida ma'lumot
#     def __init__(self,nomi,model,narh,yil):
#         self.nomi = nomi
#         self.model = model
#         self.narh = narh
#         self.yil = yil
    
#     def get_info(self):
#         info = f"Nomi: {self.nomi}, Modeli: {self.model}. "
#         info += f"Narhi: {self.narh}, {self.yil}-yilda ishlab chiqilgan"
#         return info

# moshina1 = Moshina("Malibu", "GM", 35000, 2022)
# print(f" {moshina1.get_info()} ")

        
""" voris klass """ 
# class Yangi_Moshina(Moshina):
#     def __init__(self, nomi, model, narh, yil, karobka):
#         super().__init__(nomi, model, narh, yil)
#         self.karobka = karobka
    
#     # Polimorfizim sifatida yozildi:
#     def get_info(self):
#         info = f"Nomi: {self.nomi}, Modeli: {self.model}. "
#         info += f"Narhi: {self.narh}, {self.yil}-yilda ishlab chiqilgan, Karobkasi: {self.karobka} "
#         return info

# moshina1 = Yangi_Moshina("Captiva", "GM", 25000, 2018, "avtomat")
# print(f" {moshina1.get_info()} ")

        






# class Phone:
#     def __init__(self, nomi, model, rang, narh, yil=0):
#         self.nomi = nomi
#         self.model = model
#         self.rang = rang
#         self.narh = narh
#         self.__yil = yil # yashirin qiymat

#     def __repr__(self):
#         return f"Phone: {self.nomi}, {self.narh} "

#     def __eq__(self, yangi_qiymat):
#         return self.narh == yangi_qiymat.narh

# # class'ning operatoridan foydalanganda:
# tel1 = Phone("IPhone","Apple","Blue", 880, 2021)
# tel2 = Phone("IPhone pro max","Apple","Black", 880, 2020)

# print(tel1.__dict__)



# class Phone:
#     def __init__(self, nomi, madeli, narh, operativka, ch_yili):
#         self.nom = nomi
#         self.model = madeli
#         self.narh = narh
#         self.operativka = operativka
#         self.ch_yili = ch_yili 

#     def get_info(self):
#         info = f"Nomi: {self.nom}, Modeli:{self.model}, Narhi:{self.narh} "
#         info += f"Operatifka: {self.operativka}, Chiqarilgan yili:{self.ch_yili}"
#         return info

# phone1 = Phone("Redmi", "mi", 175, 64, 2020)
# phone2 = Phone("Samsung s10", "Samsung", 500, 128, 2020)
# print(phone1.get_info())
# print(phone2.get_info())

# # voris klass 
# class New_Phone(Phone):
#     def __init__(self, nomi, madeli, narh, operativka, ch_yili, rang):
#         super().__init__(nomi, madeli, narh, operativka, ch_yili)
#         self.rang = rang

#     def get_info(self):
#         info = f"Nomi: {self.nom}, Modeli:{self.model}, Narhi:{self.narh} "
#         info += f"Operatifka: {self.operativka}, Chiqarilgan yili:{self.ch_yili}, Rangi:{self.rang}"
#         return info

# phone3 = New_Phone("IPhone", "Apple", 700, 512, 2022, "Gold")
# print(f"Vorislik javobi | {phone3.get_info()} ")




class Moshina:
    def __init__(self, nomi, modeli, rang, narhi, yili=0):
        self.nomi = nomi
        self.model = modeli
        self.rang = rang
        self.narh = narhi
        self.__yil = yili

    def get_yil(self):
        return self.__yil

    def __eq__(self, new):
        return self.narh == new.narh

    # def __repr__(self):
    #     return f"Phonega tegishli dunder: {self.nomi}, {self.model} "
moshina1 = Moshina("KIA k5", "KIA", "Qora", 45000, 2022)
moshina2 = Moshina("Malibu", "GM", "OQ", 45000, 2022)
print(moshina2 == moshina1)




# son1 = 25
# son2 = 50

# print(son1 == son2)



