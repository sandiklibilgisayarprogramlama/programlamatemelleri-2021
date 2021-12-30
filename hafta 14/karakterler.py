# len(karakter) -> parametre olarak verilen string ifadenin
# karakter sayısını getirir.

kelime = "merhaba dünya" # text-transform -> uppercase,lowercase,capitalize
print(len(kelime))

print(kelime.capitalize()) # sadece ilk harf büyük
print(kelime.title()) # başlığa çevirme
print(kelime.upper()) # hepsi büyük
print(kelime.lower()) # hepsi küçük
print("ismailçşüö".upper()) # tr karakterlerde i de sıkıntı var.

isim = "Fatma"
    #   01234
isim_ilk_harf = isim[0] # F

for indis in range(len(isim)):
    print(isim[indis])

# strip karakterlerin varsa başında veya sonundaki boşlukları
# temizler

ornek = "     merhaba dünya "
print(ornek)
print(ornek.strip())

# replace -> belirli bir bölümü değiştirmek için kullanılır.

ornek = " selam Sınıf"

print(ornek)
print(ornek.replace("selam","merhaba"))

# klavyeden girilen bir cümleyi büyük harfe çeviren kodu yazınız.
# (Not: i ler büyük İ olarak görünmelidir.)

#girdi = input("bir kelime giriniz: ") #ismet
#girdi = girdi.replace("i","İ").upper() #İsmet
#girdi = girdi.upper() # İSMET
#print(girdi)

# find arama amaçlı kullanılır. Eğer varsa bulunan
# kelimenin indisini döndürür. eğer yoksa -1 döndürür.
print("merhaba dünya".find("qweqweqe"))

#klavyeden girilen bir ifadenin email olup olmadığının kontrolü
#nü yapan program

"""
sart=True
girilen = input("bir eposta giriniz")
at_inx=girilen.find("@") 
dot_inx = girilen.find(".")
#at ve nokta şartı
if not dot_inx-at_inx>0:
    sart=False

if at_inx==0:
    sart=False

for inx in range(len(girilen)):
    if girilen[inx]!= "@" and girilen[inx]!="." and \
         girilen[inx]!="_":
        if not girilen[inx].isalnum():
            sart=False

if dot_inx==len(girilen)-1:
    sart=False

if sart==False:
    print("girilen email değil")
else:
    print("girilen email")
"""

print(ord("Ş")) # parametre olarak verilen karakterin
# ascii kodunu döndürür
print(chr(90)) # ascii tablosundaki numaraya göre
# karakter döndürür
# Alfabedeki harfleri ekrana yazdıran kodu yazınız.
for k in range(65,91):
    print(chr(k))
"""
# girilen bir ifadeyi ascii ile ifade ediniz.
girilen = input("şifrelenecek mesajı giriniz: ")
for k in range(len(girilen)):
    print(str(ord(girilen[k])),end="")
"""

# karakter ayırma
ornek = "ıtfybın.şlölmjvfxszs dünya"
print(ornek[len(ornek)-1])
print(ornek[-1])
print(ornek[-2])

# ilk 3 karakter
print(ornek[0:3])
# son üç karakter
print(ornek[len(ornek)-3:len(ornek)])
bosluk_inx=ornek.find(" ")
print(ornek[0:bosluk_inx])

# Soru
"""
Lorem Ipsum is simply dummy text of the printing and typesetting industry.Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.

Yukarıda verilen metinden yola çıkarak aşağıdaki soruları
bulan kodu yazınız.

A) kelime sayısını yazdıran program
b) harf sayısını yazdıran program (bosluklar sayılmayacak)
c) büyük harfle başlayan kelime sayısı
d) noktalama işareti sayısı
e) rakam sayısı
f) cümle sayısı


"""

