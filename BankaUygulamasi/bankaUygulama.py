from os import system as komut

class Musteri():
    def __init__(self,ID,PAROLA,ISIM):
        self.isim=ISIM
        self.id=ID
        self.parola=PAROLA
        self.bakiye=0

class Banka():
    def __init__(self):
       self.musteriler=list()

    def musteri_ol(self,ID:str,PAROLA:str,ISIM:str):
       self.musteriler.append(Musteri(ID,PAROLA,ISIM))
       print("Bankamiza kayit yaptirdiginiz icin tesekkurler!!") 


def main():
    banka=Banka()
    while True:
        komut("clear")
        print("""
        [1] Banka Musterisiyim
        [2] Banka Musterisi Olmak isyiyorum    
        """)

        secim = input("Seciminiz: ")

        if secim=="1":
            ids=[i.id for i in banka.musteriler]
            ID=input("ID: ")
            if ID in ids:
               for musteri in banka.musteriler:
                if ID == musteri.id:
                    print("hosgeldiniz {}".format(musteri.isim))
                    parola=input("Parolaniz: ")
                    if parola==musteri.parola:
                        print("Giris basarili!!")
                        while True:
                            komut("clear")
                            print("""
                            [1] Bakiye Sargula
                            [2] Para Yatir (Kendi Hesabima)
                            [3] Para Yatir (Baskasinin Hesabina)
                            [4] Para Cek
                            [Q] Cikis
                            """)

                            secim2=input("İsleminiz: ")

                            if secim2=="1":
                                print("Bakiyeniz: {}".format(musteri.bakiye))
                                input("Ana menuye donmek icin 'enter'e basin!!")
                            elif secim2=="2":
                                miktar=int(input("Miktar: "))
                                onay=input("Kendi hesabiniza {} TL para yatirma islemini onayliyor musunuz?: E/H\n".format(miktar))
                                if onay=="E" or onay =="e":
                                    musteri.bakiye+=miktar
                                    print("Paraniz Yatirildi!!")
                                    input("Ana menuye donmek icin 'enter'e basin!!")

                                elif onay =="h" or onay=="H":
                                    print("Islem iptal edildi")
                                    input("Ana menuye donmek icin 'enter'e basin!!")

                                else:
                                    print("Hatali girildi, islem iptal!!")
                                    input("Ana menuye donmek icin 'enter'e basin!!")        

                            elif secim2=="3":
                                arananID=input("Musteri ID: ")
                                if arananID in ids:
                                    for digerMusteri in banka.musteriler:
                                        if arananID== digerMusteri.id:
                                            miktar=int(input("Miktar: "))
                                            if miktar <= musteri.bakiye:
                                                onay=input("{} adli musterimize {} TL para yatirma islemini onayliyor musunuz?: E/H\n".format(digerMusteri.isim,miktar))
                                                if onay == "e" or onay=="E":
                                                    digerMusteri.bakiye+=miktar
                                                    musteri.bakiye-=miktar
                                                    print("Para aktarildi!!")
                                                    input("Ana Menuye donmek icin 'enter'e basin!!")
                                                elif onay=="h" or onay=="H":
                                                    print("Islem iptal edildi!!")
                                                    input("Ana Menuye donmek icin 'enter'e basin!!")
                                                else:
                                                    print("Hatali Giris, Islem iptal")
                                                    input("Ana Menuye donmek icin 'enter'e basin!!")
                                            else:
                                                print("Bakiyeniz bu islem icin yetersiz!!")        
                                else:
                                  print("Musteri bulunamadi!!")
                                  input("Ana Menuye donmek icin 'enter'e basin!!")

                            elif secim2=="4":
                                miktar=int(input("Miktar: "))
                                if miktar<=musteri.bakiye:
                                    musteri.bakiye-=miktar
                                    print("Islem tamamlandi, paranizi aliniz!!")
                                    input("Ana Menuye donmek icin 'enter'e basin!!")
                                else:
                                    print("Bakiyeniz bu islem icin yetersiz")
                                    input("Ana Menuye donmek icin 'enter'e basin!!")  

                            elif secim2=="q" or secim2=="Q":
                                break    

        elif secim=="2":
            ID=input("ID: ")
            ISIM=input("ISIM: ")
            PAROLA=input("PAROLA: ")
            banka.musteri_ol(ID, PAROLA, ISIM)




if __name__=="__main__":
    main()