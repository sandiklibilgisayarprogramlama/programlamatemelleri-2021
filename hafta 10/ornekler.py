"""
***
**
*
*
**
***

ooooo
*   *
ooooo
*   *
ooooo
"""

for i in range(3,0,-1):
    print("*"*i)
for i in range(1,4):
    print("*"*i)

for k in range(1,6):
    if k%2==1:
        print("o"*5)
    else:
        print("*"+" "*3+"*")
"""
Klavyeden girilen bir metin ifadesini yine klavyeden girilen
bir sayı kadar ekrana alt alta yazan programı kodlayınız.

1 ile klavyeden girilen bir sayı arasıdaki çift 
sayıları toplayıp toplama sonucunu ekrana yazan 
programı kodlayınız.

Kullanıcının girdiği iki sayı arasından 5 e 
bölünenlerin listesini ekrana yazan programı kodlayınız.

# debug
kelime=input("tekrar yazılmasını istediğiniz kelimeyi giriniz")
tekrar_sayisi=int(input("tekrar sayısını giriniz"))

for k in range(tekrar_sayisi):
    print(kelime)

toplam=0
sayi=int(input("sayı giriniz"))
for k in range(sayi):
    if k % 2 ==0:
        toplam = toplam + k

print(toplam)



bas = int(input("başlangıç giriniz : "))
bitis = int(input("bitiş giriniz : "))

for i in range(bas,bitis+1):
    if i % 5 == 0:
        print(i)


klavyeden girilen 10 sayı için eğer bu sayılardan 
herhangi biri sıfırdan küçükse programı sonlandıran
kodu yazınız.
"""
for k in range(10): # 0,1,2, ..9
    say = float(input("klavyeden bir sayı giriniz"))
    if say<0:
        print(say)
        break

# break komutu herhangi bir şart saglandığında döngüden
# çıkmak için kullanılan komuttur.

"""

"""