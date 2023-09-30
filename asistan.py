import time
yazi=input(" ")


if "merhaba" in yazi:
        time.sleep(0.5)
        print(" Merhaba yusuf ")
        time.sleep(0.5)
        print(" Nasilsin ?")
        text2=input(" ")

        if text2=="iyi"  :
                time.sleep(0.5)
                print(" Buna sevindim")

        elif text2=="kötü"  :
                time.sleep(0.5)
                print(" Neden kötü hissediyorsun ?")
                text3=input(" ")
                time.sleep(0.5)
                print(" Anliyorum ...")

elif "naber" in yazi or "nasilsin" in yazi :
        time.sleep(0.5)
        print(" İyiyim sen nasilsin ? ")
        his=input(" ") 

        if his=="iyi"   :
                time.sleep(0.5)
                print(" Buna sevindim") 

        elif his=="kötü"    :
                time.sleep(0.5)
                print(" Neden kötü hissediyorsun ?")
                sil=input(" ")
                time.sleep(0.5)
                print(" Anliyorum ...")

elif  "şiir yaz"in yazi :
        time.sleep(0.3)
        print (" Seni bulmaktan önce aramak isterim."'\n'" Seni sevmekten önce anlamak isterim."'\n'" Seni bir yaşam boyu bitirmek değil de,",'\n',"Sana hep, hep yeniden başlamak isterim.")

elif "topla"in yazi or "toplam"in yazi:
        islem=int(input("işlem sayisi giriniz "))
        toplam=0
        while (islem!=0):
         sayi=int(input("Bir sayi giriniz: "))
         toplam=toplam+sayi
         islem=islem-1
        print("Sonuc=",toplam)

elif "çikarma"in yazi or "çikar"in yazi:
        islem=int(input("işlem sayisi giriniz "))
        sonuc=0
        while (islem!=0):
         sayi=int(input("Bir sayi giriniz: "))
         sonuc=sonuc-sayi
         islem=islem-1
        print("Sonuc=",sonuc)

elif "çarpma"in yazi:
        islem=int(input("işlem sayisi giriniz "))
        sonuc=1
        while (islem!=0):
         sayi=int(input("Bir sayi giriniz: "))
         sonuc=sonuc*sayi
         islem=islem-1
        print("Sonuc=",sonuc)
elif yazi=="bölme":
        sonuc=1
        sayi=int(input("Bir sayi giriniz: "))
        sayi=int(input("Bir sayi giriniz: "))
        sonuc=sonuc/sayi
        print("Sonuc=",sonuc)
elif "üs alma"in yazi or "üs al"in yazi or "üs hesapla"in yazi:
        sonuc=1
        sayi=int(input("Bir sayi giriniz: "))
        sonuc=sayi**sayi
        print("Sonuc=",sonuc)
elif "kalani bul" in yazi or "kalani hesapla" in yazi or "kaç kalir"in yazi:
        sonuc=1
        sayi=int(input("Bir sayi giriniz: "))