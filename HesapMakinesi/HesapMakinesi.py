print("""

[1] Toplama İşlemi
[2] Çikarma İşlemi
[3] Çarpma İşlemi
[4] Bölme İşlemi
[5] Üs Alma
[Q] Çikiş

""")
  

giris=input("Seciminiz: ")
if giris =="1":
    x=input("İlk Sayi: ")
    x=float(x)
    y=input("İkinci Sayi: ")
    y=float(y)

    print("İşlem Sonucu: ",x+y)

elif giris=="2":
    x=input("İlk Sayi: ")
    x=float(x)
    y=input("İkinci Sayi: ")
    y=float(y)

    print("İşlem Sonucu: ",x-y)

elif giris=="3":
    x=input("İlk Sayi: ")
    x=float(x)
    y=input("İkinci Sayi: ")
    y=float(y)

    print("İşlem Sonucu: ",x*y)

elif giris=="4":
    x=input("İlk Sayi: ")
    x=float(x)
    y=input("İkinci Sayi: ")
    y=float(y)

    print("İşlem Sonucu: ",x/y)

elif giris=="5":
    x=input("Taban: ")
    x=float(x)
    y=input("Kuvvet: ")
    y=int(y)
    print("İşlem Sonucu: ",x**y)

elif giris=="q" or giris=="Q":
    print("Cikiliyor...")    
    quit()

else:
    print("Hatali Girildi")
    quit()


