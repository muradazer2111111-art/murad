#tapsiriq1
# yasi=int(input("Yasi daxil et: "))
# if yasi<18:
#      print("resid deyilsen")
# else:
#      print("residsen")
# curses.ascii import isdigit
#tapsiriq2
# #from platform import system_alias, python_implementation
# from zipfile import
# from functools import reduce

# while True:
#     a=input("qeyd:")
#     if a=="bitdi":
#        break
#     print(a)




# eded=input("Eded daxil et:")
#
# if eded=="0" or eded=="1" or eded=="2":
#     print("daxil etdiyiniz eded:",int(eded))
# else:
#     print("xeta")


# cem=0
# while True:
#     yaz=input("Daxil et:")
#     if yaz=="stop":
#         break
#     eded=int(yaz)
#     if eded>0:
#         cem+=eded
#
#
# while True:
#     soz=(input("daxil et:"))
#     if soz=="exit":
#         break
#     say=soz.count("a")
#     print((f"{soz} sozunde{say} a herfi var"))




# text=input("bir cumle daxil et:")
# saitler=("aioue")
# tapilan=""
# for herf in text:
#     if herf in saitler:
#         tapilan+=herf
# print




# meyveler=['alma','alca','mandarin','limon']
# kurs=list(("C++","Python","C#"))
#
# print(meyveler)
#
# print(kurs)
#
# studentScore=[]
# student=list()
#
# print(studentScore)
# print(student)


#
# reeqmler=(3,5,1,2,7,9,3)
# adlar=['babek','arda','uzun hesen','bilqeyts']
#
# print(len(adlar))
# print(reeqmler.count(3))
#
# print(sorted(adlar))azdan coxa siraliyirdi
# print(sorted(reeqmler,reverse=True))
#
# print(max(reeqmler)) #boyuk
# print(min(reeqmler)) #kicik
# print(sum(reeqmler)) #cem

#
#
# siyahi=[
#     ['alma','banan','gilas'],
#     [1,2],
#     ['qirmizi','yasil','mavi']
# ]
# print(siyahi)
# print(siyahi[0][1])
# print(siyahi[2][0])
# for alt_siyahi in siyahi:
#     print(alt_siyahi)
#
#
#
# for alt_siyahi in siyahi:
#     for element in alt_siyahi:
#         print(element)#alt alta




# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]
# cem=0
#
# for sira in matrix:
#     cem+=sum(sira)
# print(cem)



#
# ededler=[1,2,3,4,5]
#
# cut_eded=[]

# ededler=[1,2,3,4,5]
#
# for i in ededler:
#     print(i)
#
#
# ededler1=[i for i in range(1,6)]
#
# print(ededler1)







# for i in ededler:
#     if i%2==0:
#         cut_eded+=[i*i]
#     print(cut_eded)
#
# ededler1=[j*j for j in ededler if j %2==0]
#
# print(ededler1)








# a=[j*j for j in range(1,21)if j %2!=0]
# print(a)

#
#
# bos_siyahi=[]
# #
# bos_siyahi.append(5)
# print(bos_siyahi)
# #
# bos_siyahi.append(1)
# print(bos_siyahi)
# #
# #
# bos_siyahi.extend([7,3,7])
# print(bos_siyahi)
#
#
#
#
# bos_siyahi.insert(1,9)
# print(bos_siyahi)
#
#
#
# bos_siyahi.remove(7)
# print(bos_siyahi)
#
#
# bos_siyahi.pop()
# print(bos_siyahi)
#
# # bos_siyahi.clear()
# # print(bos_siyahi)
#
#
# l=bos_siyahi.copy()
#
# print(l)

# numbers=[]
#
# n=int(input("listin uzunlugunu daxil edin"))
# for i in range(n):
#     num=int(input(" liste olacaq ededleri daxil et:"))
#     numbers.append(num)
#     print("senin daxil ediyin ededler:",numbers)












#
# numbers=[]
# i=0
# n=int(input("liste nece eded elave etmek isleyirsen:"))
#
# while i<n:
#     num=int(input("liste daxil olacaq ededleri daxil et:"))
#     numbers.append(num)
#     i+=1
#     print(numbers)










#
# reqemler=[20,3,15,8,7,16,1,0,0,544]
# boyuk10=[]
#
# for reqem in reqemler:
#     if reqem>10:
#         boyuk10.append(reqem)
#
# print(sorted(boyuk10))



# reqemler=[1,2,3,4,5,6,7,8,10,15,17]
# cut_list=[]
# tek_list=[]
#
# for reqem in reqemler:
#     if reqem%2==0:
#         cut_list.append(reqem)
#     if reqem%2!=0:
#         tek_list.append(reqem)
# print("cut ededler:",cut_list)
# print("tek ededler:",tek_list)








# a=[]
# palindromlar=[]
# s=int(input("nece eded daxil etmek isleyirsen:"))
# for i in range(s):
#     deyer=input("daxil edin;")
#     a.append(deyer)
# for deyer in a:
#     if deyer==deyer[::-1]:
#         palindromlar.append(deyer)
#
# print(a)
# print(palindromlar)






#
# def test():
#     x=5
#
# print(test())


# a=[1,2,3]
# a.append("salam")
# print(a)
# a=None
# print(a)

#
#
#
#
# my_tuple=(5,10,15)
# my_list=list(my_tuple)
# my_list.append(25)
# print(my_list)
# print(my_tuple)

#
# set={1,2,3,4,4}
# print(set)
# set.add('gavali')
# print(set)
# set.update("nar","alca")
# print(set)



# fs=frozenset({1,2,3,4})
#
# print(fs)


# telebe={
#     "ad":"ALi" "Babek",
#     "yas":20
#
# }
# print(telebe["ad"])







#
# import math
#
# print(math.pow(2,5))
# print(math.sqrt(25))
# print(math.exp(1))
# print(math.log(10,10))
# print(math.sin(math.pi/4))
#
# print(math.factorial(5))
# print(math.fabs(7))









#
# import random
# print(random.random())
# print(random.randint(1,10))
#
# print(random.uniform(5,10))
#
# colors=["sari","mavi","qirmizi"]
# print(random.choice(colors))
# print(random.choices(colors,k=2))


# import re
# #
# metn="salam dunya menim nomrem 463634646"
#
# netice=re.search(r"\d+",metn)
#
# print(netice.group())
#
# metn1="python 12 , java 9, c++ 11"
#
# reqemler=re.findall(r"\d+",metn1)
# print(reqemler)
#
# print(re.match(r"python",metn1))
#
# yeni=re.sub(r"\d+","**********",metn)
# print(yeni)
#
# print(re.findall(r"\w+",metn))


#
#
#
# import math
#
# ededler=[16,81]
# cut_eded=[]
# tek_eded=[]
# for i in ededler:
#     kok=math.sqrt(i)
#     if kok%2==0:
#         cut_eded.append(kok)
#     if kok%2!=0:
#         tek_eded.append(kok)
# print(cut_eded)
# print(tek_eded)


# import datetime

# while True:
#     try:
#         dogum_il=int(input("ilimizi daxil edin:"))
#         break
#     except ValueError:
#         print("zehmed olmasa reqem daxil et:")
# indiki_il=datetime.datetime.now().year
# yas=indiki_il-dogum_il
# if yas>=18:
#     print("yetkinden")
#
# elif yas<18:
#     print("yetkin deyilsen")




# import random
#
# ededler=[]
# while len(ededler)<5:
#     texmini=random.randint(1,50)
#     if texmini%2==0:
#         ededler.append(texmini)
# print(ededler)


























#
# def salamla(ad):
#     print("Salam xos geldin",ad)
#
#
# def salamla2(ad):
#     return  "Salam Xos geldin",ad
# print(salamla("Murad"))
#
# print(salamla2("Murad"))
#






# def topla(a,b):
#     print(a+b)
#
# print(topla(5,9))
#
#
# def topla2(a,b):
#    return a+b
#
# print(topla2(5,14))










# def Food(a):
#     print("Heelo World",a)
#
#
# Food("Wow are you")















# def Food(ad):
#     return "Hello World",ad
#
# print(Food(5))


























# def topla(a,b):
#     print(a+b)
#
# netice=topla(3,5)
# print(netice*2)
#
# def topla2(a,b):
#     return a+b
#
# netice2=topla2(3,5)
# print(netice2*2)




# def kvadrat(a):
#     return a*a
#
#
# print(kvadrat(5))





# def kub(a):
#     return a*a*a
# print(kub(2))



# def kvadrat(a):
#     return a*a
#
# def hesabla(a):
#     print(kvadrat(a))
#
# hesabla(5)


# def enboyuk(siyahi):
#     en_boyuk=siyahi[0]
#     for i in siyahi:
#         if i>en_boyuk:
#             en_boyuk=i
#     return en_boyuk
# print(enboyuk([1,2,3,4,5]))



# def menseyi(eded):
#     if eded%2==0:
#         print("cut eded")
#     else:
#         print("tek eded")
# a=menseyi(5)




# def tek_cut(a):
#
#     if a%2==0:
#         return "cut"
#     else:
#         return "tek"
# n=int(input("eded daxil et:"))
# print(tek_cut(n))


# def enboyuktap(siyahi):
#     en_boyuk=siyahi[0]
#     for i in siyahi:
#         if i>en_boyuk:
#             en_boyuk=i
#     return en_boyuk
# n=int(input("nece eded daxil edeceksen:"))
# ededler=[]
# for i in range(n):
#     eded=int(input(f"{i+1}-ci eded"))
#     ededler.append(eded)
# deyisen=enboyuktap(ededler)
# print(deyisen)
#
# print(ededler)
# print(enboyuktap(ededler))
























# def kvadrat():
#     while True:
#         try:
#          n=int(input("eded daxil et:"))
#          return n*n
#         except ValueError:
#            print("xeta zehmed eded daxil edin:")
# print(kvadrat())











#
# def a():
#     print("Hello World")
#
# def b(mesaj):
#     print(mesaj)
# b(5)
#
# def c():
#     return "Hello"
#
# d=c()
# print(c())

















#
# def qebulet_qaytar(num1,num2):
#     return num1+num2
#
# a=qebulet_qaytar(5,9)
# print(a)

















































































#prasudr


#
# def topla (a,b):
#     return a+b
#
# print(topla(5,9))


# def vur (a,b):
#     return a*b
#
# a=int(input("eded daxil et:"))
# b=int(input("eded daxil et:"))
# print(vur(a,b))








#
# def topla(a,b,c):
#     return a+b+c/3
# a=int(input("ededi daxil et:"))
# b=int(input("ededi daxil et:"))
# c=int(input("ededi daxil et:"))
# print(topla(a,b,c))



# ededler=[1,2,3,4,5]
#
# def cem(siyahi):
#     return sum (siyahi)/len(siyahi)
#
# print(cem(ededler))




# ededler=[1,2,3,4,5]
#
# def enboyuk(siyahi):
#     return max(ededler)
# print(enboyuk(ededler))




#
# def a(*args):
#     print(args)
# a("Salam","Necesen",2025,29)
#
# def cem(*reqemler):
#     toplam=0
#     for i in reqemler:
#         toplam+=i
#     return toplam
# print(cem(1,2,3))




#
# def sozler(*alma):
#     for i in alma:
#         print(i.upper())
# sozler("alma","aye")

# def melumat_goster(**bilgi):
#     for acar, deyer in bilgi.items():
#         print(acar,"=",deyer)
# melumat_goster(ad="Murad",yas=27,seher="Baki")
#
# def yas_tap(**melumat):
#     if "yas" in melumat:
#         print("Yas:",melumat["yas"])
#     else:
#         print("yas daxil edilmeyib")
#
# yas_tap(ad="Murad",yas=27,seher="Baki")
# yas_tap(ad="Murad",seher="Ulanbator")


# def salamla(ad="qonaq"):
#     print("Salam",ad)
#
# salamla()
# salamla("Murad")

# def hesabla(a=20,b):
#     print(a+b)
# hesabla()





#
# def funksiya(ad="Murad",dil="az"):
#     if dil=="az":
#         print("salam",ad)
#     elif dil=="en":
#         print("Hello",ad)
#     else:
#         print("Bonjur",ad)
# funksiya("Aysel","en")
#
# ad=input("Ad daxil et:")
# dil=input("dil daxil et:")
# funksiya(ad,dil)


















# yasin=int(input("yas daxil et"))
# def a(yas):
#      if yas==18:
#         print("18 tamam")
#      elif yas>18:
#         print("yetisgin")
#      elif yas<18:
#          print("balacasaan")
# a(yasin)






# def faktorial(n):
#     if n==1:
#         return 1
#     else:
#         return n* faktorial(n-1)
#
# print(faktorial(5))

















#
# def ters_yaz(s):
#     if len(s)==0:
#         return ""
#     else:
#         return s[-1]+ters_yaz(s[:-1])
# print(ters_yaz("nicat"))
























# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# a=int(input("eded daxil et:"))
# for i in range(a):
#     print(fib(i),end=" ")



#
# def loop():
#     print("Hello")
#     return loop()
# loop()






# def kvadrat(x):
#     return x*x
# print(kvadrat(5))
# print((lambda a:a*a)(4))
# print((lambda a,b:a+b)(10,15))
#
#
# sozler=["Alma","Armud","Alca"]
# print(list(map(str.upper,sozler)))






# ededler=[1,2,3,4,5]
# def vur(x):
#     return x*2
#
# netice=list(map(vur,ededler))
# print(netice)
#
# print(list(map(lambda x:x/4,ededler)))


# ededler=[1,2,3,4,5]
# def vur(x):
#     return x+20
# c=list(map(vur,ededler))
# print(c)
# print(list(map(lambda a:a+20,ededler)))




# bos=[]
# n=int(input("uzunluq daxil et:"))
# for i in range(n):
#     a=int(input("ededler daxil et:"))
#     bos.append(a)
# print(bos)
# print(list(map(lambda x:x/4,bos)))

#
#
# ededler=[1,2,3,4,5]
# def cut(a):
#     return a%2==0
# print(list(filter(cut,ededler)))
# print(list(filter(lambda x:x%2==0,ededler)))





# from functools import reduce
#
# def cem(x,y):
#     return x+y
# ededler=[1,2,3,4,5]
#
# print(reduce(cem,ededler))
# print(reduce(lambda x,y:x+y,ededler))
# print(reduce(lambda x,y:x if x>y else y,ededler))



# from functools import reduce
#
#
# ededler=[1,2,3,4,5]
# step=list(map(lambda x:x*4,ededler))
# print(list(step))
# step2=list(filter(lambda x:x%3==0,step))
# print(step2)
# print(reduce(lambda a,b:a+b,step2))



# ooe-obyekt yonumlu proqramladirma










# class Telebe:
#     pass
#
#
#
# telebe1=Telebe()
# telebe1.name="murad"
#
# telebe1.surname="Quluzade"
#
# print(telebe1.name,telebe1.surname)


#
#
# class Masin:
#     pass
#
#
#
# masin1=Masin()
# masin1.name1="mercedes",2015,"36500"
# masin1.name2="BMW",2020,"46700"
# masin1.name3="RangeRover",2016,"35000$"
# print(masin1.name1)
# print(masin1.name2)
# print(masin1.name3)












# class Telebe:
#     def __init__(self,name,surname,age):
#         self.name=name
#         self.surname=surname
#         self.age=age
#     def goster(self):
#         print(f"{self.name},{self.surname},{self.age}")
# telebe1=Telebe("murad","Quluzade",13)
# telebe2=Telebe("Azer","Quluyev",214)
# telebe3=Telebe("Ferit","Eliyev",243)
#
# telebeler=(telebe1,telebe2,telebe3)
# maxi=0
# for t in telebeler:
#     if t.age>maxi:
#         maxi=t.age
# print(maxi)
#
# max_yas=max(t.age for t in telebeler)
# print(max_yas)





# class Kitap:
#     def __init__(self,adi,sehife,janr):
#      self.adi=adi
#         self.sehife=sehife
#         self.janr=janr
#     def goster(self):
#         print(f"{self.adi} {self.sehife} {self.janr}")
# kitap1=Kitap("nil uzerinde olum",400,"qorxulu")
# kitap1.goster()








# class Topla:
#     def __init__(self,a,b):
#         self.topla1=a
#         self.topla2=b
#     def hesabla(self):
#         return self.topla1+self.topla2
# a=int(input("eded daxil et:"))



























# import tkinter as tk
#
# root=tk.Tk()
# root.geometry("500x500")
# img=tk.PhotoImage(file="purepng.com-mariomariofictional-charactervideo-gamefranchisenintendodesigner-1701528634653vywuz.png")
# lb=tk.Label(root,image=img)
# lb.pack()
# root.mainloop()



# import tkinter as tk
# from logging import currentframe
# from tkinter import *
# from PIL import Image,ImageTk



# root=tk.Tk()
# root.geometry("500x500")
#
# image1=Image.open("purepng.com-mariomariofictional-charactervideo-gamefranchisenintendodesigner-1701528634653vywuz.png")
#
# photo1=ImageTk.PhotoImage(image1)
# label1=tk.Label(root,image=photo1)
# label1.place(x=0,y=0)
#
#
# image2=Image.open("purepng.com-mariomariofictional-charactervideo-gamefranchisenintendodesigner-1701528634653vywuz.png")
#
# photo2=ImageTk.PhotoImage(image2)
# label2=tk.Label(root,image=photo2)
# label2.place(x=750,y=0)
#
#
#
#
#
#
# image3=Image.open("download.jpg")
# photo3=ImageTk.PhotoImage(image3)
# label3=tk.Label(root,image=photo3)
# label3.place(x=750,y=0)


# import tkinter as tk
#
# from PIL import Image,ImageTk
#
#
#
# image_path=["logo2.png","download.jpg"]
#
# root=tk.Tk()
#
# root.geometry("700x700")
#
# def change_image():
#     global current_image
#     current_image=(current_image+1)%len(image_path)
#     image=Image.open(image_path[current_image])
#     tk_image=ImageTk.PhotoImage(image)
#     label.configure(image=tk_image)
#     label.image=tk_image
#     root.after(2000,current_image)
#
# current_image=0
# image = Image.open(image_path[current_image])
# tk_image = ImageTk.PhotoImage(image)
# label=tk.Label(root,image=tk_image)
# label.pack()
# root.after(2000, current_image)
#
# label.pack()


# root.mainloop()




























# f=open("data.txt","w")
# f.write("Salam necesen")
#
# f.close()
#
# a=open("data.txt","r")
# print(a.read())
# a.close()