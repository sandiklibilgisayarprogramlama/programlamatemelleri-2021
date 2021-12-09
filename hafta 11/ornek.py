
# bir sistemde kullanıcı adı ve şifreyi en fazla 3 kere doğru
# girmesi isteniyor. buna göre kullanıcı adı admin, şifresi
# 123 olan bir kişi için bu bilgileri 3 den fazla yanlış girdiğinde
# ekrana kullanıcınız bloke olmuş yazan programı kodlayınız.

# klavyeden girilen bir sayının asal olup olmadığını 
# hesaplayan programı yazınız.

# klavyeden girilen bir sayıya kadar olan
# asal sayıları ekrana yazdırınız.

# klavyeden girilen bir sayıya kadar olan fibonachi sayılarını
# ekrana yazdırınız.

"""
kadi = "admin"
sifre = 123
blokemi = True
# 0,1,2
for _ in range(3):
    girilen_kadi = input("Kadi giriniz")
    girilen_sifre = int(input("şifre giriniz"))

    if girilen_kadi==kadi and girilen_sifre == sifre:
        print("Tebrikler")
        blokemi = False  
        break
    else:
        print("girilen kadi veya şifre yanlış")

if blokemi:
    print("Bloke oldunuz")


"""


sayi=int(input("Sayı giriniz"))
asalmi = True
if sayi>1:
    for i in range(2,sayi):
        if sayi % i == 0:
            print("asal değildir")
            asalmi = False
            break
else:
    print("Sayı asal değildir")
    asalmi=False
if asalmi:
    print("Sayı Asaldır.")

