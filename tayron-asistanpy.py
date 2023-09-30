import time
from datetime import date
from datetime import datetime
from datetime import timedelta

amesaj=input("")

if amesaj in "merhaba" :
    time.sleep(0.5)
    print(" Merhaba yusuf ")
    time.sleep(0.5)
    print(" Nasılsın ?")
    sil1=input(" ")

    if "iyi"in sil1:
        time.sleep(0.5)
        print(" Buna sevindim ")
    
    elif "kötü"in sil1:
        time.sleep(0.5)
        print(" Neden ?")
        time.sleep(0.5)
        print(" Anladım ..")

elif "nasılsın" in amesaj or "naber" in amesaj :
    time.sleep(0.5)
    print(" İyiyim sen nasılsın ?") 
    sil2=input("")

    if "iyi"in sil2:
        time.sleep(0.5)
        print(" Buna sevindim ")
    
    elif "kötü"in sil2:
        time.sleep(0.5)
        print(" Neden ?")
        time.sleep(0.5)
        print(" Anladım ..")

#giriş bölümü bitti

elif "şiir yaz" in amesaj:
    time.sleep(0.5)
    print (" Seni bulmaktan önce aramak isterim."'\n'" Seni sevmekten önce anlamak isterim."'\n'" Seni bir yaşam boyu bitirmek değil de,",'\n',"Sana hep, hep yeniden başlamak isterim.")

elif "topla" in amesaj or "toplam" in amesaj :
    time.sleep(0.5)
    islem1=int(input("işlem sayısı giriniz "))
    sonuc1=0
    while (islem1!=0):
     time.sleep(0.5)
     sayi1=int(input("Bir sayı giriniz: "))
     sonuc1=sonuc1+sayi1
     islem1=islem1-1
     time.sleep(0.5)
    print("Sonuc=",sonuc1)

elif "çıkarma"in amesaj or "çıkar"in amesaj:
        time.sleep(0.5)
        islem2=int(input("işlem sayısı giriniz "))
        sonuc2=0
        while (islem2!=0):
         time.sleep(0.5)
         sayi2=int(input("Bir sayı giriniz: "))
         sonuc2=sonuc2-sayi2
         islem2=islem2-1
        time.sleep(0.5)
        print("Sonuc=",sonuc2)

elif "çarpma" in amesaj:
        time.sleep(0.5)
        islem3=int(input("işlem sayısı giriniz "))
        sonuc3=1
        while (islem3!=0):
         time.sleep(0.5)
         sayi3=int(input("Bir sayı giriniz: "))
         sonuc3=sonuc3*sayi3
         islem3=islem3-1
        time.sleep(0.5)
        print("Sonuc=",sonuc3)

elif "bölme" in amesaj:
        sonuc4=1
        time.sleep(0.5)
        sayi4=int(input("Bir sayı giriniz: "))
        time.sleep(0.5)
        sayi5=int(input("Bir sayı giriniz: "))
        sonu4c=sonuc4/sayi4
        time.sleep(0.5)
        print("Sonuc=",sonuc4)

elif "üs alma"in amesaj or "üs al"in amesaj or "üs hesapla"in amesaj:
        sonuc5=1
        sayi5=int(input("Bir sayı giriniz: "))
        sonuc5=sayi5**sayi5
        print("Sonuc=",sonuc5)

elif "kalanı bul" in amesaj or "kalanı hesapla" in amesaj or "kaç kalır"in amesaj:
        sonuc6=1
        sayi6=int(input("Bir sayı giriniz: "))
        sayi7=int(input("Bir sayı giriniz: "))
        sonuc6=(sayi6%sayi7)
        print("Sonuc=",sonuc6)  

elif "yusuf kim" in amesaj or "orçun kim"in amesaj or "seni geliştiren kim"in amesaj or "sahibin kim" in amesaj or "yazılımcın kim"in amesaj   :
    time.sleep(0.5)
    print(" Yusuf Orçun Özdemir",'\n'," Öğrenci.\n  adamın dibi")

elif "sevdiğin renk " in amesaj:
    time.sleep(0.5)
    print("Siyaha bayılıyorum ancak siyahın renk olup olmadığı tartışmaları akıp gidiyor ,herneyse sen?")
    sil3=input("")
    print(" Evet o renkte çok güzel")

elif "sevdiğin araba " or "beğendiğin araba"in amesaj :
    time.sleep(0.5)
    print("Porsche  ya senin ?")

elif "sevdiğin yazar" in amesaj:
    time.sleep(0.5)
    print("Koray Yersüren ")