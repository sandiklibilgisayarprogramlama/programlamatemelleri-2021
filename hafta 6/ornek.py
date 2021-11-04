# input("ekranda gösterilecek metin") -> str

# str -> int int(str)
# girilen = input("bir sayı giriniz") # str
# girilen = int(girilen) # casting
# print(type(girilen))

# int(input("sayı giriniz")) -> int sayı

#int(input("bir ifade girin")) # 0123456789
# int("er") int fonksiyonu içine 0-9 arasındaki rakamları
# ancak tam sayıya çevirebilir.

# Klavyeden girilen iki sayının toplamını yazan program
"""
s1 = int(input("klavyeden sayı 1 giriniz"))
s2 = int(input("klavyeden sayı 2 giriniz"))

print("{} ile {} sayılarının toplamı {} 'dir.".format(s1,s2,s1+s2))
print(str(s1)+ " ile "+str(s2)+" sayılarının toplamı "+str(s1+s2)+" 'dir")
"""

#klavyen girilen bir sayının 2'ye göre modunu ekrana yazan programı
#kodlayınız. (%) 
"""
sayi = int(input("modu alınacak sayıyı giriniz"))
print("{} sayısının ikiye göre modu {} dır.".format(sayi,sayi%2))
"""
#girilen bir sayının karesini ekrna yazan programı kodlayınız.
"""
sayi = int(input("karesi alınacak sayıyı giriniz"))
print("{} sayısının karesi {} dır.".format(sayi,sayi*sayi)) #sayi**2
print("{} sayısının küpü {} dır.".format(sayi,sayi**3)) # sayi*sayi*sayi
print("{} sayısının dördüncü {} dır.".format(sayi,sayi**4)) # sayi*sayi*sayi*sayi
"""
"""
if kosul:
    koşul sağlanırsa çalışacak kodlar
"""

# girilen bir sayı sıfırdan küçükse ekrana sayı negatif yazan programı 
# kodlayınız
"""
girilen = int(input("sayıyı giriniz"))

if girilen<0:
    print("sayı negatif")
    print("merhaba")

if girilen > 0 :
    print("sayı pozitif")

if girilen == 0: # eşitmi karşılaştırması
    print("sayı 0")
print("program sonlandı")

"""

# klavyeden girilen bir sayı eğer 3 e tam bölünüyorsa 3 e bölünür yazan
# bölünmüyor ise 3 e bölünmez yazan programı kodlayınız.

"""
sayi = int(input("sayı giriniz"))
kalan = sayi%3
if kalan == 0:
    print("sayi 3 e bölünür")
else:
    print("SAYİ 3 E BÖLÜNMEZ")

geçme notu 60 olan bir ders için vize notu ve final notunu
klavyeden girilen bir kişinin dersi geçip geçmediğini 
ekrana yazdıran programı kodlayınız (vize %40 0.4,
 final %60 0.6 ı not ortalaması
hesabında kullanılacak)
"""
"""
vizenot = int(input("vize notunu giriniz"))
finalnot = int(input("final not giriniz"))
ortalama = vizenot*0.4 + finalnot*0.6
print("Ortalama : ",ortalama)
if ortalama>=60: # >= büyük veya eşit <= küçük veya eşittir
    print("geçti")
else:
    print("kaldı")

if sart1:
    kod
elif sart2:
    kod
elif sart3:
    kod
elif sart4:
    kod
elif sart5:
    kod
else:
    kod


klavye girilen bir sayı 3 e bölünüyorsa 3 e tam bölünür,
4 e bölünüyorsa 4 e tam bölünür
5 e bölünüyorsa 5 e tam bölünür yazdırınız.
Not: her ikisine tam bölünenlerde ilk karşılaşına tam bölünür yazılacak.
"""
sayi = int(input("kontrol edilecek sayıyı giriniz:"))
if sayi%3 == 0:
    print("sayı 3 e tam bölünür")
elif sayi%4==0:
    print("sayı 4 e tam bölünür")
elif sayi%5==0:
    print("sayi 5 e tam bölünür")
else:
    print("girdiginiz sayı 3,4,5 e tam bölünmez")