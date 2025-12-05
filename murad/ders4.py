# f=open("data,txt","w")
# f.write("Salam necesen\nasfaf\nasfafast")
#
# f.close()
#
# a=open("data,txt","r")
# print(a.read())
# a.close()

# f=open("data.txt","r+")
# print(f.read())
# f.write("\nYeni ")
# f.close()





#
# f=open("data.txt","a")
#
# f.write("setr elave olundu")
# f.close()

# a=open("dat.txt","x")
# a.write("Bura yazildi")
# a.close()

# with open("data.txt","w") as f:
#     f.write("Hello")
#
# with open("data.txt","r") as f:
#     print(f.read())






# with open("data.txt","r+") as cinali:    #hem oxuyub hem yazma qucun isdufa de olunur
#     print(cinali.read())
#     cinali.write("\nSalam")

# with open("data.txt","a") as file:  #en axra elave edir
#     file.write("\nSonuna")
#
# with open("dataa.txt","x",encoding="utf-8") as file: #eyni ad olan  error verir
#     file.write("asfasfafa")

# with open("file1.txt","w") as f1:  #yazi yazmaq ucun
#     f1.write("Ilk fayl")
#
# with open("file1.txt","r") as f1:   #oxumaq ucun
#     content=f1.read()
#
# with open("file2.txt","w") as f2:
#     f2.write(content)











#
# # import tkinter as tk
# from PIL import Image,ImageTk
#
# # pencere=tk.Tk()
#
# # img=tk.PhotoImage(file="purepng.com-mariomariofictional-charactervideo-gamefranchisenintendodesigner-1701528634653vywuz.png")
# # label=tk.Label(pencere,image=img)
# # label.pack()
# # pencere.mainloop




import tkinter as tk
from PIL import Image,ImageTk

pencere=tk.Tk()
image=Image.open("Ordubad_svln_svln4821_me_best_top_photography_resimleri_sekilleri_photos_creative_profil_maraqli_sekil_resim_fotograflari_fotograf_ornek_resimleri_(1).JPG")
img=ImageTk.PhotoImage(image)
label=tk.Label(pencere,image=img)
label.pack()




pencere.mainloop()