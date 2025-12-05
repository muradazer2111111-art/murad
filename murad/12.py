# a=5
# print(a)
# a+=6# ilk isare toplayir ikinci isare menimsedir
# print(a)
#
# b=4
# print(b)
# b-=3
#
#
# c=6
# print(c)
# c*=2
#
#
# d=8
# print(d)
# d/=2
# print(d)


#
# car=input("Masin markasini qeyd et:")
# pulum=120000
#
# deyer=[]
# for carr in car:
#     if carr=='Audi':
#
#         pulum+=5000
#         print(pulum)
#     elif car=='Porshe':
#         pulum+=80000
#     elif car=='RangeRover':
#         pulum+=200000
#     elif car=='BMW':
#         pulum+=120000
#
# for i in carr:
#     if i=="Audi":
#         print("Audi:,"pulum")



# start=int(input("ilk deyer"))
# end=int(input(" son deyer:"))
#
# for i in range(start,end):
#     i+=5
#     print(i)


# for i in range(1,20):
#     if i>10:
#         print(i)

# orrect_login = "Murad25"
# correct_password = ("1234@")
# for a in range(3):
#     login = input("login daxil et:")
#     password = input("Password dail et:")
#     if correct_login == login and correct_password == password:
#         print("Ugurlu emeliyyat sisteme giris")
#         break
#     else:
#         sans = 2 -
#         if sans >= 0:
#             print(f"Sehf giris,Qalan sans:{sans}")
#         if sans == 0:
#             print("3 defe sehv giris hesab bloklandi")

#
#
#
#
# siyahi=["Adem",12,7,8,True]
#
# for x in siyahi:
#     print(x)
#
# yazi="Homosapiyens"
#
# for i in yazi:
#     print(i)














#
# for i in range(1,11):
#     print(i,"->",i**2)

















# 5 deyerin ededi ortasini tapin cap et
# cem=0
# for i in range(5):
#     eded=int(input("Eded daxil et:"))
#     cem+=eded
# print("Ededi orta",cem/5)





# reqemler=[12,15,24,35,1,25,56]
# en_boyuk=reqemler[0]
#
# for i in reqemler:
#     if i>en_boyuk:
#         en_boyuk=i
#         print("En boyuk:",en_boyuk)


#
# for i in range(1,100):
#     if i%3==0  and i%5==0:
#         print(i)


# for i in range (1,6):
#     print("*"*i)

#
#
# h=5
# for i in range(1,h+1):
#     print(" "*(h-i)+"=" *(2*i-1))






#
# for i in range(3):#xaric dovr
#     for j in range(2):
#         print("i:",i,"j:",j)


# for j in range(2):
#     for i in range(3):
#         print("j:",j,"i:",i)


# for i in range(1,4):
#     for j in range (1,4):
#         print(i,"*",j,"=",i*j)
#     print("----------")


# for i in range(3):
#     for j in range(2):
#         if j==1:
#             break
#         print(i,j)




# for i in range(3):
#     for j in range(3):
#         if j==1:
#             continue
#         print(i,j)

#end alta alta yazilmasin komek eden bir kodur eden acar sozdur
# for i in range(5):
#     print(i,end=",")


# for i in range(1,4):
#     for j in range(1, 4):
#         print(i,"+",j,"=",i+j,end="")
#     print()


# for i in range(5):
#     for j in range(4):
#         print("*",end="")
#     print()




# a=0
#
# while a<=5:
#     print(a)
#     a+=1



#
# #bu while dovru deyisenin 10 dan boyuk olmadigini butede isleyecek
# cem=0
# n=1
# while n<=10:
#     cem+=n
#     n+=1
#
# print(cem)



# if 5<7:
#       print("step it")
#
# while 5<7:
#     print("step it")




   # sert duzgun olursa while he cvaxt ixra ola bilmez.
#
# i=36
# while i<35:
#     if i%3==0:
#         print(i)
#     i+=1
# print("Step it")


# #isdifacinin verdiyi eded adinan hem coxdan aza while dovrunu ekrana cap ededn proqramdir.
# num1=int(input("Diapazonun evveli:"))
# num2=int(input("Diapazonun sonu:"))
#
#  while num1<num2+1:
#       print(num1)
#       num1+=1
#
# while num1-1<num2:
#     print(num2)
#     num2-=1



#bu koda mueyen meyveni gorene qeder dovru icra edir eriy meyvesini gorduyde dovru dayanir

# meyveler=["alam","ciyelek","erik"]
#
# for meyve in meyveler:
#     if meyve=="erik":
#         break
#     print(meyve, end=" ")

#
# # reqemler siyahisini icinde eger cut edeedler varsa cantinue onlari atlayir ve yanliz tek ededleri cap edir
# reqemler=[1,5,7,10,4,2]
#
# for reqem in reqemler:
#     if reqem%2==0:
#         continue
#     print(reqem)


# while True:
#     secim=int(input("Secim et:"))
#     if secim==1:
#         print("Elave et")
#     elif secim==2:
#         print("Sil")
#     elif secim==3:
#         print("Cix")
#         break




# i=0
# while i<15:
#     i+=1
#     if i==7:
#         continue
#     print(i)



#
# correct_password="12345"
# password=input("Parolu daxil et:")
#
# while password!=correct_password:
#     print("Paral duzdur")
#     password = input("Parolu yeniden daxil et:")
# else:
#     print("Parol duzdur xos geldiniz"


# import random
#
# sirr=random.randint(1,20)
#
# while True:
#     texmin=int(input("Texmin et:"))
#     if texmin==sirr:
#         print("Tebrikler qalibsiniz")
#     else:
#         print("Zeif yanlis texmin yeniden cehd et:")
  


#
#
# try:
#     num=int(input("ededi daxil et"))
#     result=10/num
#     print(result)
# except ZeroDivisionError:
#     print("Sifira bolmek olmur")
#
# except ValueError:
#     print("Xeta dogru olmayan deyer daxil etdiniz")
#
# except Exception as e:
#     print("Xete",e)
#
# finally:
#     print("finally blokunun icrasi")

# a=int(input("Eded daxil et"))
#
# if a!=0:
#     print(10/a)
# else:
#     print("Sifira bolmek olmaz")


# exceptnen sade bir klavyatura yaratmaq
# while True:
#     op=input("Emeliyyat {+,-,*,/} secim {cixmaq ucun exit}:")
#     if op=="exit":
#         break
#     if op not in["+","-","/","*"]:
#         print("yanlis emeliyyar")
#         continue
#     try:
#          a=float(input("ilk eded:"))
#          b=float(input("ikinci eded:"))
#          if op=="+":print(a+b)
#          elif op == "-": print(a - b)
#          elif op == "*": print(a * b)
#          elif op == "/": print(a / b)
#     except Exception as E:
#          print("Xeta",E)



# else bloku try blokunda sef bas vermesinde isleyir
# try:
#     a=int(input("Eded daxil et:"))
#     print(10/a)
#
# except Exception as b:
#     print("Xeta",b)
# else:
#     print("Ela her sey superdi")




# # siyahidaki elementlerin tipini yoxla ve ededleri topla
# element=[1,3,"a","r",6,"asfasf"]
# sum=0
#
# for i in element:
#     try:
#         sum+=i
#     except TypeError:
#         print(f"{i} eded deyil kec")
# print("Cem:",sum)



# print(ord("a"))

# print(chr(65))


# for i in range(65,91):
#     print(i,"=",chr(i))


#
# a=str(input("sozu daxil et:"))
#
# for i in a:
#      print(i,"=",ord(i))





# # encode bir melumati basqa bir melumata cevirmek ucucn isdifade olunur
# text="Salam Dunya"
# print(text)
#
# encoded=text.encode("utf-8")
# print(encoded)
#
# print(encoded.decode("utf-8"))



# text=b"\xc6\x8fd\xc9\x99lat g\xc3\xbcnl\xc9\x99rin bir g\xc3\xbcn\xc3\xbc \xc3\xbcz\xc3\xbcld\xc3\xbc"
#
# e=text.decode("utf-16")
# print(e)


# str1="Hello Wordl"
#
# print(len(str1))
# print(str1[0:10])
#
# print(str1.upper())
# print(str1.lower())
# print(str1.title())
# print(str1.capitalize())




#
# str2="  Salam  "
#
# print(str2.strip())
# print(str2.lstrip())
# print(str2.rstrip())


# meyveler="Banan Alma Armud"
#
# print(meyveler.split())
#
# print("".join(meyveler))
#
# print(meyveler.replace("Alma","Alca"))
#
# print(meyveler.count("a"))




# print("Pythoon".isalpha())
# print("123".isdigit())
# print("123".isnumeric())
# print("Py123".isalnum())





