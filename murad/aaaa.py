# a=float(input("ilk eded:"))
# b=float(input("ikinci eded:"))
# emeliyyat=input("Emeliyyat qeyd et(+,-,*,/):")
#
# if emeliyyat=="+":
#     print("Netice",a+b)
# elif emeliyyat=="-":
#     print("Netice:",a-b)
# elif emeliyyat=="*":
#     print("Netice:",a*b)
# elif emeliyyat=="/":
#     if b==0:
#         print("Sifira bolmek olmaz")
#     else:
#         print("Netice:",a / b)
# else:
#     print("Yanlis emeliyyat isaresi")






#
# a=int(input("Dogum ilini qeyd et"))
#
# if a>=2013:
#     print("Gen Alpha")
#
# elif a>=1997 and a<=2012:
#     print("Gen Z")
#
# elif a>=1981 and a<=1996:
#     print("Gen Millienal")
#
# elif a>=1965 and a<=1980:
#     print("Gen X")
#
# elif a>=1946 and a<=1965:
#     print("Gen Boomer")
#
# elif a<=1945:
#     print("boomer dovru")











saysistemi=input("secimi daxil et(2/8/10/16)")
eded=int(input("Ededi qeyd et:"))

if saysistemi=="2":
    print("ikilik say sistemi",bin(eded))
elif saysistemi=="8":
    print("sekkizlik say sistemi", oct(eded))
elif saysistemi=="10":
    print("onaltiliq say sistemi",hex(eded))
else:
    print("Bele say sistemi ola bilmez")



