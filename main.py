# class list :
#     def __init__(self,sonlar):
#         self,sonlar=sonlar


#     def add(self):
#         for i in self.sonlar:
#              s+=i
        
# son = list ({1,1,3,4,5,6},)
# son.add()



# class print: 
#   def chiqar(self):
#     print("nexia" , "Tico" , "Damas" , "korganlar qilar havas")
#   def daraja(self):
#     print("Nexia" , "Tico" , "Damas" , "Korganlar, qilar havas")
#   def qoldiq(Self):
#     print14%4)



# m=print()
# m.chiqar()
# m.daraja()
# m.qoldiq()



# class SSS:
#     def __init__ (self,hello):
#         self.hello=hello
#     def salom(self):
#         print('hello world')


# s = SSS("Salom")
# s.salom()




# class world:
#       def __init__(self,James):
#             self.James=James
#       def salom(self):
#             print("James")


# s=world("James")
# s.salom()           






# class WWW:
#       def __init__(self,Jobir):
#             self.Jobir=Jobir
#       def salom (self):
#             print("Jobir")


# s=WWW("Jobir")
# s.salom()




# class Avaz:
#         def __init__(self, name):
#                 self.Odil=Odil
#         def  age (self):
#                 print('Odil')
            

# s=Avaz('Odil')
# s.name()




# class royhat:
#     def __init__(self, davlatlar):
#         self.davlatlar=davlatlar
#     def name(self):
#        print (self.davlat)
#     def tartib(self):
#         o=self.davlat
#     def chipta(self):
#         self.davlat.sort()
#         print(self.davlat)
#     def alifbo(self):
#         self.davlat.sort(revenve= True)
#         print(self.davlat)
#         davlat = royhat 





# class sonlar :
#     def __init__(self,sonlar):
#         self.sonlar=sonlar
#     def qow (self) :
#         s= 0
#         for h in self.sonlar:
#            s+=h
#         print(s)
#     def eng(self):
#         a=self.sonlar
#         b=self.sonlar
#         print(max(a)-min(b))  
#     def soni(self):
#         k=self.sonlar
#         print(len(k))


# sonlar=sonlar(list(range(120,1200,2)))
# sonlar.soni()


















# #meros 
# class Kasb:
#     def __init__(self , name , familiya ,age , year , tillar):
#         self.name=name
#         self.familiya=familiya
#         self.age=age
#         self.self=self
#         self.year=year
#         self.tillar=tillar



# class Dasturchi(Kasb):
#     def __init__(self , name , familiya , age , year , tillar):
#         super(). __init__( self ,  name , familiya ,  age , year)
#         self.til=tillar


# class Uqituvchi(Kasb):
#     def __init__(self , name , familiya , age , year ,tillar, fanlar):
#         super(). __init__(name , familiya , age , year,tillar)
#         self.fanlar=fanlar



# pro =Uqituvchi("Doniyorsher" , "Abduraimov" , 12 , 2011 ,'ss', " SeniorProgrammer")
# print(pro.name)






# class Kasb:
#     def __init__(self , name , familiya , age  , year):
#         self.name=name
#         self.familiya=familiya
#         self.age=age
#         self.year=year









# class Avto:
#     def speed (self):
#         print("Tezlik musir gazni boss!!!!!!!!!")

#     def tormaz (self):
#         print("tuxta qara qizil!!!!!!!!!!!!!!!")

#     def fara (self):
#         print("farangni yoq garang!!!!!!!!!!!!")



# class car(Avto):
#     pass
# class Bus(Avto):
#     pass
# bus=Bus()
# bus.fara()
# bus.tormaz()
# bus.speed()









# class Shaxs:
#     """Shaxslar haqida ma'lumot"""
#     def __init__(self,ism,familiya,passport,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
    
#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info
        
#     def get_age(self,yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil

















# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, passport, tyil):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)









# class Talaba():
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, passport, tyil,idraqam):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
    
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
    
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich
#         super(). ___init__(ism , familiya , passport , tyil)
#         self.fanlar.append
#     def fanga (self,fan):
#         self.fanlar.append[fan]
       
# class Fan :
#     def __init__(self , ismi , murakkabligi):
#         self.ismi=ismi
#         self.murakkabligi=murakkabligi
















# # meros 
# class Kasb:
#      def init(self,name,familya,age,year):
#         self.name = name
#         self.familya = familya
#         self.age = age
#         self.year = year
        
#      def get_name(self):
#         print("Ismi ",self.name)
        
#      def get_familya(self):
#          print("Familyasi ",self.familya)
    


# class Dasturchi(Kasb):
#     def init(self,name,familya,age,year,til):
#         super().init(name,familya,age,year)
#         self.til = til
        
        
# pro = Dasturchi('valijon','shamshidinnov',14,2009,'senior enginner')
# # print(pro.name)
# pro.get_name()
# pro.get_familya()

# class Uqituvchi(Kasb):
#     def init(self,name,familya,age,year,fanlar):
#         super().init(self,name,familya,age,year)
#         self.fan = fanlar
        







# takrorlash
#variable , condirion loop , function , boolen , 

# 'condition'
# a=4
# b=6
# print(a>b)





# sonlar =(list(range(20,30)))
# for son in sonlar:
#     print(son)





# shahar = "samarwand ciyt"
# for i in shahar:
# #     print(i)





# # cars=["Toyota" , "Mazda" , "GM" , "Kia" , "Hyudai"]
# # for car in cars :
# #     if car!="Mazda":
# #         print(car.upper())
# #     elif car != "Kia" :
# #         print(car.title())    
# #     elif car!="toyota":
# #         print(car.title())






# a=input('Birinchi sonni kirit')
# b=input('ikkinchi sonni kirit')
# ism=input('Ismingizni kiriting\n>>>>>>>>')
# if ism=="Admin" :
#     print(' xush kelibsiz Admin. xush kelibsiz royhatni korasizmi')
# if a==b:
#     print("sonlar teng")
# else:
#    print('Sonlar teng emas')



# a=float(input("sonnikiriting>>>>\n"))
# if  a<=0:
#    print("musbat son kirit")
# else : 
#    print(a**(0.5))





# While=True
# a=float(input("Juft sonni kirit:"))
# if a%2:
#     print("Bu juft son emas")
# else:
# #     print("Bu juft son")







# savol=float (input("Yoshingiz kiriting\n>>>>>>>>>>>>>>"))
# if savol <=4:
#     print('Tekin')
# elif savol >=60:
#     print('Tekin')
# elif savol>18:
#     print('1000 som')
# else:
#     savol>=18
#     print('20000')    





# friends = []
# friends.append('John')
# friends.append('Alex')
# friends.append('Danny')
# friends.append('Sobirjon')
# friends.append('Vanya')
# print(friends)
# friends.remove("Vanya")
# friends.remove("John")
# print(friends)
































































































































































































































































































































































































































































































































































































