import random
aranan = int(random.uniform(0,100))

hak = 10
while True:
    if hak<=0:
        print("Oyunu Kaybettiniz")
        break

    hak-=1
    girilen = int(input("bir sayı giriniz"))
    if girilen<aranan:
        print(girilen,"' den daha büyük bir sayı girmeyi deneyiniz!")
    elif girilen>aranan:
        print(girilen,"' den daha küçük bir sayı girmeyi deneyiniz!")
    else:
        print("Tebrikler, oyunu Kazandınız!")
        print("Kalan hakkınız: ",hak)
        break


"""
ard arda rastgele bulunan 4 sayıdan hepsinin 4 e bölümünden kalanın 0
olduğunda ekrana bu sayıları yazdıran programı kodlayınız.
"""