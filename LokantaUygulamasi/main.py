masalar=dict()
for i in range(10):
    masalar[i]=0

def hesapEkle():
    masaNo=int(input("Masa No: "))
    gecerli=masalar[masaNo] 
    eklenecek=float(input("Eklenecek Ucret: ")) 
    toplam=gecerli+eklenecek
    masalar[masaNo]=toplam

def hesapSil():
    masaNo=int(input("Masa No: "))
    gecerli=masalar[masaNo]
    eksilecek=float(input("Eklenecek Ucret: "))
    toplam=gecerli-eksilecek
    if toplam < 0:
        print("islemde hata var , kontrol ediniz!!")
    else:
        masalar[masaNo]=toplam    
    

def hesapKontrol(dosya_adi):
    try:
        dosya=open(dosya_adi)
        veriler=dosya.read()
        veriler=veriler.split("\n")
        veriler.pop()
        dosya.close()
        flag=True
    except FileNotFoundError: 
        dosya=open(dosya_adi,"w")
        dosya.close()
        print("İlk kez calistirildi! Kayit dosyasi yaratildi")   
        flag=False

    if flag:
        for i in enumerate(veriler):
            masalar[i[0]]=float(i[1])
    else:
        pass

def kayitGuncelleme():
    dosya=open("kayıt.txt","w")
    for i in range(10):
        ucret=masalar[i]
        ucret=str(ucret)
        dosya.write(ucret+"\n")
    dosya.close()  






def main():
    hesapKontrol("kayıt.txt")
    while True:
        print("""
        [1] Masalari Görüntüle
        [2] Hesap Ekle
        [3] Hesap Sil
        [Q] Cikis
    
        """)

        secim=input("İsleminiz: ")

        if secim=="1":
            for i in range(10):
             print("Masalar {} için hesap: {}".format(i,masalar[i]))
            print("islem tamamlandi! Ana menuye donmek icin 'enter'e bas!")
            input()

        elif secim=="2":
            hesapEkle()
            print("islem tamamlandi! Ana menuye donmek icin 'enter'e bas!")
            input()

        elif secim=="3":
            hesapSil()
            print("islem tamamlandi! Ana menuye donmek icin 'enter'e bas!")
            input()
    
        elif secim=="Q":
            print("Cikiliyor!!")
            quit()    


main()