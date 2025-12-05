# class Adam:
#     def __init__(self,ad):
#         self.name=ad #public
#
# a1=Adam("Covdet")
#
# print(a1.name)
#
# a1.name="Siyavuw"
#
# print(a1.name)
# from platform import system_alias

# class Telebe:
#     def __init__(self,ad):
#         self._ad=ad
#
# class Magistr(Telebe):
#      def goster(self):
#           print(f"Magistr ad:{self._ad}")
#
# t1=Magistr("Mugdat")
# t1.goster()
# print(t1._ad)



# class Telebe:
#     def __init__(self,ad):
#         self.__ad=ad
#
#     def goster(self):
#         print(f"Ad:{self.__ad}")
#
# t1=Telebe("murad")
# t1.goster()


# class BankAccount:
#     def __init__(self,balance):
#         self.__balance=balance
#     def get_balance(self):
#         return self.__balance
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#     def withdraw(self,amount):
#         if amount >0 and amount<=self.__balance:
#             self.__balance-=amount
#
# heseb=BankAccount(1000)
# print(heseb.get_balance())
# heseb.deposit(500)
# print(heseb.get_balance())
# heseb.withdraw(1500)
# print(heseb.get_balance())

#
# class BankHesbi:
#     def __init__(self,sahib,balans,pin):
#         self.sahib=sahib
#         self.__balans=balans
#         self.__pin=pin
#     def balans_goster(self):
#         daxil_pin=int(input("pin daxil et:"))
#         if daxil_pin==self.__pin:
#             print(f"Balans:{self.__balans}AZN")
#         else:
#             print("yanlis pin!")
#     def pul_artir(self):
#         daxil_pin = int(input("pini daxil et:"))
#         if daxil_pin==self.__pin:
#             mebleg=int(input("ne qeder elave edeceksiniz?"))
#             if mebleg>0:
#                 self.__balans+=mebleg
#                 print(f"yeni heseb:{self.__balans}")
#             else:
#                 print("mebleg menfi ola bilmez")
#         else:
#             print("pin yanlisidir")
#     def pul_cixar(self):
#         daxil_pin = int(input("pini daxil et:"))
#         if daxil_pin == self.__pin:
#             mebleg = int(input("ne qeder elave edeceksiniz?"))
#             if  0< mebleg<self.__balans:
#                 self.__balans += mebleg
#                 print(f"qalan heseb:{self.__balans}")
#             else:
#                 print("mebleg duzgun deyil kifayet qeder pulunuz yoxdur")
#         else:
#             print("pin yanlisidir")
#
# heseb=BankHesbi("Murad",155,1234)
#
# while True:
#     print("---------bank emeliyyatlari----------")
#     print("1.balans yoxla")
#     print("2.balans artir")
#     print("3.balans pul cixar")
#     print("4.cixis")
#     secim=int(input("emeliyat nomresini daxil et:"))
#     if secim==1:
#         heseb.balans_goster()
#     elif secim==2:
#         heseb.pul_artir()
#     elif secim==3:
#         heseb.pul_cixar()
#     elif secim==4:
#         print("programdan cix")
#         break
#     else:
#         print("secim yanlsidir")














#
#
# class Heyvan:
#     def __init__(self,ad):
#         self.ad=ad
#
#     def ses_cixar(self):
#         print(f"{self.ad} ses cixar")
#
# class It(Heyvan):
#     def __init__(self,ad,cins):
#         Heyvan.__init__(self,ad)
#         self.cins=cins
#
#     def salamla(self):
#         print(f"{self.ad}size salam verir")
# it1=It("Karabas","Alman Cobani")
# it1.ses_cixar()




# class BankHesabi:
#     def __init__(self, sahib, hesab):
#         self.sahib=sahib
#         self.__hesab=hesab
#     def Hesab_goster(self):
#         print(f"{self.sahib} hesabi:{self.__hesab}")
#     def Hesabartir(self, mebleg):
#         self.__hesab+=mebleg
#         print(f"{mebleg}AZN elva edildi Yeni hesab:{self.__hesab}")
#     def Hesabazalt(self,mebleg):
#         if mebleg<=self.__hesab:
#             print(f"{mebleg}hesabdan cixildi qalan hesab:{self.__hesab}")
#         else:
#             print("Kasib senin o qeder pulun yoxdu")
#
# class VipHesab(BankHesabi)   :
#     def __init__(self,sahib,hesab,bonus_faiz):
#         BankHesabi.__init__(self,sahib,hesab)
#         self.bonus_faiz=bonus_faiz
#     def bonus_elave_et(self):
#         bonus=self.bonus_faiz*0.01*self._BankHesabi__hesab
#         self._BankHesabi__hesab+=bonus
#         print(f"Bonus{bonus}Elave edildi Yeni Balans:{self._BankHesabi__hesab}")
#
# hesab1=BankHesabi("murad",2849)
# vip1=VipHesab("aqil",35467,365)
#
# hesab1.Hesab_goster()
# hesab1.Hesabartir(500)
#
# vip1.Hesab_goster()
# vip1.bonus_elave_et()




# 
# class Qida:
#     def __init__(self,ad,terkibi):
#         self.ad=ad
#         self.terkibi=terkibi
#     def melumat(self):
#         print(f"{self.ad}-{self.terkibi}")
# 
# 
# class Meyve(Qida):
#     def __init__(self,ad ,terkibi,vitaminc):
#         super().__init__(ad,terkibi)
#         self.vitaminc=vitaminc
# 
#     def vitamin(self):
#         print(f"{self.ad} icinde {self.vitaminc} mg var")
# 
# meyve1=Meyve("alma","a Vitamini",12)
# 
# meyve1.melumat()
# meyve1.vitamin()



# class Heyvan:
#     def __init__(self,ad,cinc):
#         self.ad=ad
#         self.cinc=cinc
#     def melumat(self):
#         print(f"{self.ad}-{self.cinc}")
# class Qus(Heyvan):
#     def __init__(self,ad,cinc,qanaduzunlugu):
#         super().__init__(ad,cinc)
#         self.qanaduzunlugu=qanaduzunlugu
#     def qanadinolcusu(self):
#         print(f"adi-{self.ad}.qanadinin uzunlugu:{self.qanaduzunlugu}")
#
# olcu=Qus("bayqus","disi",15)
# olcu.qanadinolcusu()
# olcu.melumat()




# class Heyavn:
# #     def sescixar(self):
# #         print("Heyvan ses cixar")
# #
# # class It(Heyavn):
# #     def sescixar(self):
# #         print("Hav Hav")
# #
# # class Pisiy(Heyavn):
# #     def sescixar(self):
# #         print("Miyav")
# #
# # h=Heyavn
# # i=It()
# # p=Pisiy()
# # h.sescixar()
# # i.sescixar()
# # p.sescixar()







# class Masin:
#     def suret(self):
#         print(220)
#
# class Mercedes(Masin):
#     def suret(self):
#         print(260)
#
# class BMW(Masin):
#     def suret(self):
#         print(320)
#
# m1=Masin()
# m=Mercedes()
# b=BMW()
# m.suret()
# b.suret()








# class Mehsul:
#     def qiymet(self):
#         return 0
#
# class Kitab(Mehsul):
#     def qiymet(self):
#         return 20
#
# class Tv(Mehsul):
#     def qiymet(self):
#         return 2600
#
#
# m=Mehsul()
# t=Tv()
# k=Kitab()
#
# print(m.qiymet())
# print(t.qiymet())
# print(k.qiymet())
#
# mehsullar=[m,t,k]

# for i in mehsullar:
#     print(i.qiymet())













































#

# class Sirket:
#     def __init__(self,ad,maas):
#         self.ad=ad
#         self.__maas=maas
#     def a(self):
#         print(f"Adi:{self.ad} Mass:{self.__maas}")
# class Manger(Sirket):
#     def __init__(self,ad,maas,komanda_bonus):
#         super().__init__(ad,maas)
#         self.komanda_bonus=komanda_bonus
#     def team_bonus(self):
#         bonus=self.komanda_bonus*0.02*self





















#
# import tkinter as tk
#
# pencere=tk.Tk()
# pencere.title("salam tkinter")
# pencere.geometry("300x300")
# yazi=tk.Label(pencere,text="duymeni basma!")
# yazi.pack()
# yazi.pack()
# yazi.pack()
# def basildi():
#     duyme.config(text="basbada")
# duyme=tk.Button(pencere,text="Bas duymeni",font=("Arial",14),command=basildi)
# duyme.configure()
# duyme.pack(pady=50)
# pencere.mainloop()




#
# import tkinter as tk
# pencere=tk.Tk()
# pencere.geometry("300x200")
# def yeniseyfe():
#     yeni=tk.Tk()
#     yeni.geometry("500x500")

# btn=tk.Button(pencere,text="yeni seyfe",command=yeniseyfe)
# btn.pack(pady=100)
#
# pencere.mainloop()


# import tkinter as tk
#
# pencere = tk.Tk()
# pencere.title("Sadə Pəncərə")
#
# etiket = tk.Label(pencere, text="Salam, Dünya!", font=("Arial", 16))
# etiket.pack(pady=20)
#
# pencere.mainloop()


# import tkinter as tk
#
#
# def etiket_deyis():
#     etiket.config(text="Butona basdın!")
#
#
# pencere = tk.Tk()
# pencere.title("Düymə ilə Etiket Dəyişmək")
#
#
# etiket = tk.Label(pencere, text="Salam, Dünya!", font=("Arial", 16))
# etiket.pack(pady=20)
#
# duyme = tk.Button(pencere, text="Məni bas", command=etiket_deyis, font=("Arial", 14))
# duyme.pack(pady=10)
#
# pencere.mainloop()












#
# import tkinter as tk
# pencere=tk.Tk()
# pencere.geometry("300x200")
# def yeniseyfe():
#     yeni=tk.Tk()
#     yeni.geometry("500x500")
#     def geri():
#         yeni.destroy()
#
#     geriduyme=tk.Button(yeni,text="Geri qayit",command=geri)
#     geriduyme.pack()
#
# btn=tk.Button(pencere,text="Yeni seyfe",command=yeniseyfe)
# btn.pack()
#
# pencere.mainloop()









# import tkinter as tk
# p=tk.Tk()
# p.geometry("300x200")
#
# frame=tk.Frame(p,bg="lightblue")
# frame.pack(fill="both",expand=True)
#
# lb=tk.Label(frame,text="Bu frame icindedir")
# lb.pack()
#
# p.mainloop()














# import tkinter as tk
#
# pencere=tk.Tk()
#
# pencere.geometry("300x300")
#
# frame1=tk.Frame(pencere)
# frame1.pack(fill="both",expand=True)
#
# label1=tk.Label(frame1,text="bura ilk seyfe")
# label1.pack(pady=20)
# def seyfe2_ac():
#     frame1.pack_forget()
#     frame2.pack(fill="both",expand=True)
#
# def geriqayit():
#     frame2.pack_forget()
#     frame1.pack()
#
# btn1=tk.Button(frame1,text="yeni seyfeye kec",command=seyfe2_ac)
# btn1.pack(pady=10)
#
# frame2=tk.Frame(pencere)
#
# label2=tk.Label(frame2,text="Bura ikinci sehife")
# label2.pack(pady=20)
#
# btn2=tk.Button(frame2,text="ilk sehifeye qatit",command=geriqayit)
# btn2.pack(pady=10)
#
# pencere.mainloop()


















#
# import tkinter as tk
# from tkinter import messagebox
#
# pencere=tk.Tk()
# pencere.geometry("300x300")
#
# def goster():
#     messagebox.showinfo("Melumat","bu bir info mesajidir")
#
# btn=tk.Button(pencere,text="Mesaj goster",command=goster)
# btn.pack(pady=20)
#
# pencere.mainloop()


























#
# import tkinter as tk
# from tkinter import messagebox
#
# window=tk.Tk()
# window.geometry("300x300")
#
# login=tk.Entry(window)
# login.pack(pady=10)
#
# password=tk.Entry(window,show='*')
# password.pack(pady=20)
# def yoxla():
#     if login.get()=="" or password.get()=="":
#         messagebox.showerror("Xeta","Login password bos ola bilmez")
#
#     else:
#         messagebox.showinfo("ugurlu","Qeydiyyat tamamlandi")
# btn=tk.Button(window,text="Qeydiyyat tamamla",command=yoxla)
# btn.pack(pady=25)
# window.mainloop()














#
# #
# import tkinter as tk
# from tkinter import messagebox
#
# window=tk.Tk()
# window.geometry("300x300")
#
# login=tk.Entry(window)
# login.pack(pady=10)
#
# password=tk.Entry(window,show='*')
# password.pack(pady=20)
# def yoxla():
#     if login.get()=="" or password.get()=="":
#         messagebox.showerror("Xeta","Login password bos ola bilmez")
#
#     else:
#         yeni=tk.Tk()
#         yeni.geometry("505x505")
#
#
# btn=tk.Button(window,text="Qeydiyyat tamamla",command=yoxla)
# btn.pack(pady=25)
#
# window.mainloop()















# import tkinter as tk
# from tkinter import messagebox

# pencer=tk.Tk()
# pencer.title("Qeydiyyat")
# pencer.geometry("500x500")
# 
# login_frame=tk.Frame(pencer,bg="grey")
# login_frame.pack(fill="both",expand=True)
#
# login_entry=tk.Entry(login_frame)
# login_entry.pack(pady=10)
#
# pass_entry=tk.Entry(login_frame,show="*")
# pass_entry.pack(pady=20)

# def davam_et():
# #     l=login_entry.get()
# #     p=pass_entry.get()
# #
# #     if l=="" or p=="":
# #         messagebox.showerror("Xeta","Bos buraqmax olmaz")
# #     else:
# #         login_frame.pack_forget()
# #         yeni_frame.pack(fill="both",expand=True)
#
# # btn1=tk.Button(login_frame,text="Davam et",bg="brown",command=davam_et)
# # btn1.pack(pady=25)
# #
# # yeni_frame=tk.Frame(pencer)
# #
# # def geriqatit():
# #     yeni_frame.pack_forget()
# #     login_frame.pack(fill="both",expand=True)
# #
# # btn2=tk.Button(yeni_frame,text="Geriqayit",command=geriqatit)
# # btn2.pack()
# # pencer.mainloop()


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# import tkinter as tk
#
# pencere=tk.Tk()
# listbox=tk.Listbox(pencere)
# listbox.pack(pady=20)
# pencere.geometry("400x400")
# listbox.insert(tk.END,"Murad")
# listbox.insert(tk.END,"Huseyn")
# listbox.insert(1,"Aqil")
#
# pencere.mainloop()
#
#
#
#
#
# import tkinter as tk
#
# root=tk.Tk()
# root.geometry("500x500")
# listbox1=tk.Listbox(root)
# listbox1.pack()
#
# my_list=["Adem","Murad","Ferid","Nihad","Ziyeddin"]
#
# for item in my_list:
#     listbox1.insert(tk.END,item)
#
# def show_selected():
#     selected=listbox1.curselection()
#     for i in selected:
#         print(listbox1.get(i))
#
# btn=tk.Button(root,text="sec",command=show_selected)
# btn.pack(pady=20)
# root.mainloop()
#
#
#
#
# import tkinter as tk
#
# pencere=tk.Tk()
# pencere.geometry("300x300")
#
# listbox1=tk.Listbox(pencere)
# listbox1.pack()
#
# my_list=["HR departman","Adem","Murad","proqramlasdirma","Ferid","Nihad","Ziyeddin"]
#
# for item in my_list:
#     listbox1.insert(tk.END,item)
#
# def show_selected():
#     selected=listbox1.curselection()
#     for i in selected:
#         print(listbox1.get(i))
#
# pencere.mainloop()
#
#
#
#
#
#
#
#
#
#
#
# import tkinter as tk
#
# pencere=tk.Tk()
# pencere.geometry("500x500")
# listbox=tk.Listbox(pencere)
# listbox.pack()
#
# my_list=["AA","PM","AS","QJ"]
# for item in my_list:
#     listbox.insert(tk.END,item)
# def delete():
#     selected=listbox.curselection()
#     for i in selected:
#         listbox.delete(i)
#
# def deleteall():
#     listbox.delete(0,tk.END)
#
# btn =tk.Button(pencere, text="Sil",command=delete)
# btn.pack()
# btn1 =tk.Button(pencere, text="hamisini sil",command=deleteall)
# btn1.pack()
#
# pencere.mainloop()
#
#
#
#
#
#
# import tkinter as tk
# from operator import index
# from tkinter import messagebox
#
# pencere=tk.Tk()
# pencere.geometry("500x500")
#
# listbox=tk.Listbox(pencere)
# listbox.pack()
#
#
# entry=tk.Entry(pencere,width=30)
# entry.pack(pady=5)
#
# def elava_et():
#     elave=entry.get()
#     if elave:
#         listbox.insert(tk.END,elave)
#         entry.delete(0,tk.END)
#     else:
#         messagebox.showerror("XEta","Bos ola bilmez")
# def delete():
#     secim=listbox.curselection()
#     if secim:
#         index=secim[0]
#         listbox.delete(index)
#     else:
#         messagebox.showerror("Xeta","Secim edin")
#
# def update():
#     secim = listbox.curselection()
#     if secim:
#         index = secim[0]
#         yenideyer=entry.get()
#         if yenideyer:
#             listbox.delete(index)
#             listbox.insert(index,yenideyer)
#         else:
#             messagebox.showwarning("Xeta","Bos ola bilmez")
#     else:
#         messagebox.showerror("Xeta","Ilk once secim edin")
# btn=tk.Button(pencere,text="Elave et",width=15,command=elava_et,bg="yellow")
# btn.pack(pady=10)
#
# btn2=tk.Button(pencere,text="Sil",width=15,command=delete,bg="pink")
# btn2.pack(pady=15)
#
# btn3=tk.Button(pencere,text="Update",width=15,command=update,bg="grey")
# btn3.pack(pady=15)
# pencere.mainloop()









#
# import tkinter as tk
# from tkinter import messagebox
# user_data={}
#
# def register_page():
#     reg=tk.Toplevel(root)
#     reg.title("Qeydiyyat")
#     reg.geometry("300x350")
#
#     tk.Label(reg,text="Isdifadeci ad").pack(pady=5)
#     ent_user=tk.Entry(reg)
#     ent_user.pack()
#
#     tk.Label(reg,text="Isdifadeci password").pack(pady=5)
#     ent_pass=tk.Entry(reg,show="*")
#     ent_pass.pack()
#
#
#     tk.Label(reg,text="NickName").pack(pady=5)
#     ent_nickname=tk.Entry(reg)
#     ent_nickname.pack()
#
#     tk.Label(reg,text="Age").pack(pady=5)
#     ent_age=tk.Entry(reg)
#     ent_age.pack()
#
#
#     tk.Label(reg,text="Cins").pack(pady=5)
#     ent_gender = tk.Entry(reg)
#     ent_gender.pack()
#
#     def register():
#         username=ent_user.get()
#         password=ent_pass.get()
#         ad=ent_nickname.get()
#         yas=ent_age.get()
#         cins=ent_gender.get()
#
#         if not username or not password:
#             messagebox.showerror("Xeta","Isdifadeci adi ve ya sifre bos ola bilmez")
#             return
#
#         if username in user_data:
#             messagebox.showerror("Xeta","Bu isdifadeci adi isdifade olunur")
#             return
#
#         user_data[username]={
#             "password":password,
#             "ad":ad,
#             "yas":yas,
#             "cins":cins
#         }
#         messagebox.showinfo("Ok","Qeydiyyat tamamlanir")
#         reg.destroy()
#     tk.Button(reg,text="Qeyad ol",bg="#4caf50",fg="white",command=register).pack(pady=20)
#
# def change_password_window(username):
#     win=tk.Toplevel(root)
#     win.title("Sifre deyis")
#     win.geometry("300x230")
#
#     tk.Label(win,text="Kohne password").pack(pady=5)
#     old_pass=tk.Entry(win,show="*")
#     old_pass.pack()
#
#     tk.Label(win,text="Yeni password").pack(pady=5)
#     new_pass = tk.Entry(win,show="*")
#     new_pass.pack()
#
#     tk.Label(win,text="Yeni password(tekrar").pack(pady=5)
#     new2_pass = tk.Entry(win,show="*")
#     new2_pass.pack()
#
#     def chanege_pass():
#         if old_pass.get()!=user_data[username]["password"]:
#             messagebox.showerror("Xeta","Parol sehfdir")
#             return
#         if new_pass.get()!=new2_pass.get():
#             messagebox.showerror("Xeta","Yeni password uygun gelmir")
#             return
#
#         user_data[username]["password"]=new_pass.get()
#         messagebox.showinfo("ok","Ugurlu tamamlandi")
#
#         win.destroy()
#
#     tk.Button(win,text="Tesdiqle",bg="#4acf50",fg="white",command=chanege_pass).pack(pady=15)
#
# def open_profile(username):
#     prof=tk.Toplevel(root)
#     prof.title("Profil")
#     prof.geometry("300x380")
#
#     user=user_data[username]
#
#     tk.Label(prof,text=f"Profil:{username}",font=("Arial",14,"bold")).pack(pady=10)
#
#     tk.Label(prof,text="Ad").pack()
#
#     ent_name=tk.Entry(prof)
#     ent_name.insert(0,user["ad"])
#     ent_name.pack()
#
#     tk.Label(prof, text="yas").pack()
#
#     ent_age=tk.Entry(prof)
#     ent_age.insert(0,user["yas"])
#     ent_age.pack()
#
#     tk.Label(prof, text="Cins").pack()
#
#     ent_gender=tk.Entry(prof)
#     ent_gender.insert(0,user["cins"])
#     ent_gender.pack()
#
#     def update_info():
#         user["ad"]=ent_name.get()
#         user["yas"]=ent_age.get()
#         user["cins"]=ent_gender
#         messagebox.showinfo("ok","Melumat yenilendi")
#
#
#
#     def delete_account():
#         if messagebox.askyesno("Tesdiq","Hesabi silmeknisleyirsiniz?"):
#            del user_data[username]
#            messagebox.showinfo("OK","Hesab silindi")
#            prof.destroy()
#
#     tk.Button(prof,text="Yenile",bg="grey",fg="pink",command=update_info).pack(pady=10)
#
#     tk.Button(prof,text="Hesabi sil",bg="blue",fg="black",command=delete_account).pack(pady=10)
#
#     tk.Button(prof,text="sifre deyis",bg="green",fg="white",command=lambda:change_password_window(username)).pack(pady=10)
#
#
#
# def open_admin_panel():
#     admin_win=tk.Toplevel(root)
#     admin_win.title("Admin Panel")
#     admin_win.geometry("300x600")
#     tk.Label(admin_win,text="Admin Paneli").pack(pady=10)
#
#     listbox=tk.Listbox(admin_win,width=30)
#     listbox.pack(pady=10)
#
#     for username in user_data:
#         listbox.insert(tk.END,username)
#
#     tk.Label(admin_win, text="Yeni sifre").pack(pady=5)
#     ent_new_password = tk.Entry(admin_win,show="*")
#     ent_new_password.pack()
#
#     tk.Label(admin_win, text="Yas").pack(pady=5)
#     ent_age = tk.Entry(admin_win)
#     ent_age.pack()
#
#     tk.Label(admin_win, text="Cins").pack(pady=5)
#     ent_gender = tk.Entry(admin_win)
#     ent_gender.pack()
#
#     tk.Label(admin_win, text="Ad").pack(pady=5)
#     ent_name = tk.Entry(admin_win)
#     ent_name.pack()
#
#     def select_user(event):
#         selected=listbox.curselection()
#         if selected:
#             username=listbox.get(selected[0])
#
#             user=user_data[username]
#             ent_name.delete(0,tk.END)
#             ent_name.insert(0,user["ad"])
#
#             ent_age.delete(0, tk.END)
#             ent_age.insert(0, user["yas"])
#
#             ent_gender.delete(0, tk.END)
#             ent_gender.insert(0, user["cins"])
#     listbox.bind("<<ListboxSelect>>",select_user)
#
#     def update_user():
#         selected = listbox.curselection()
#         if selected:
#             username = listbox.get(selected[0])
#
#             user = user_data[username]
#             user["ad"]=ent_name.get()
#             user["yas"] = ent_age.get()
#             user["cins"] = ent_gender.get()
#             messagebox.showinfo("Ok",f"{username} Mellumat yenilendi")
#
#     def change_user_pass():
#         selected = listbox.curselection()
#         if selected:
#             username = listbox.get(selected[0])
#             new_pass=ent_new_password.get()
#
#             if len(new_pass)<3:
#                 messagebox.showinfo("Xeta","Sifre 3den az ola bilmez!")
#                 return
#
#             user_data[username]["password"]=new_pass
#             messagebox.showerror("Ok", f"{username}Sifre yenilendi!")
#     def delete():
#         selected = listbox.curselection()
#         if selected:
#             username = listbox.get(selected[0])
#             if messagebox.askyesno("Tesdiq", "Hesabi silmeknisleyirsiniz?"):
#                 del user_data[username]
#                 listbox.delete(selected[0])
#
#                 ent_name.delete(0,tk.END)
#                 ent_age.delete(0,tk.END)
#                 ent_gender.delete(0,tk.END)
#                 messagebox.showinfo("OK",f"{username}hesabi silindi")
#
#     tk.Button(admin_win, text="Yenile", bg="grey", fg="pink", command=update_user).pack(pady=10)
#
#     tk.Button(admin_win, text="Hesabi sil", bg="blue", fg="black", command=delete).pack(pady=10)
#
#     tk.Button(admin_win, text="sifre deyis", bg="green", fg="white", command= change_user_pass).pack(pady=10)
#
#
#
#
# def login():
#     username=ent_user.get()
#     password=ent_pass.get()
#
#     if username=="admin" and password=="admin":
#         open_admin_panel()
#
#     elif username in user_data and user_data[username]["password"]==password:
#         open_profile(username)
#     else:
#         messagebox.showerror("Xeta","Login ve ya sifre sefdir")
#
#
#
# root=tk.Tk()
# root.title("Login Sistemi")
# root.geometry("500x500")
#
# tk.Label(root,text="Isdifadeci adi").pack(pady=5)
#
# ent_user=tk.Entry(root)
# ent_user.pack()
#
# tk.Label(root,text="Isdifadeci password").pack(pady=5)
# ent_pass=tk.Entry(root,show="*")
# ent_pass.pack()
#
# tk.Button(root,text="Daxil ol",bg="pink",fg="white",command=login).pack(pady=10)
#
# tk.Button(root,text="Qeydiyyat ol",bg="#2169f3",fg="white",command=register_page).pack(pady=10)
#
#
#
#
#
#
# root.mainloop()






#
# import tkinter as tk
# from tkinter import ttk
#
# root=tk.Tk()
#
# root.geometry("500x500")
#
# adlar=["kamal","murad","nihad","qulam"]
#
# comba=ttk.Combobox(root,values=adlar,state="readonly")
# comba.pack(pady=20)
# def secildi(event):
#     secilen_ad=comba.get()
#     secilen_label.config(text=f"secdiyiniz ad:{secilen_ad}")
# comba.bind("<<ComboboxSelected>>",secildi)
#
# secilen_label=tk.Label(root,text="Hele secim etmediniz")
# secilen_label.pack(pady=10)
#
#
# root.mainloop()









#






