# input klavyeden giriş yapmak için kullanılan fonksiyodur.
# girilen her bir ifade str tipinde alınır.
# gerekli tip dönüşümünü siz yapacaksınız.
"""
girilen = input("bişey giriniz : ")
print(girilen)
print(type(girilen))

# str -> int int(çevirilecek)
# str -> float float(çevirilecek)
# float, int -> str str(çevirilecek)
print(int(girilen))
print(type(int(girilen)))
print("-----------------------------")
print(float(girilen))
print(type(float(girilen)))

# klavyeden girilen iki sayıyı çarpıp ekrana
# yazan programı kodlayınız
"""

s1 = int(input("sayı 1 giriniz"))
s2 = int(input("sayı 2 giriniz"))
print("{} ile {} sayılarının çarpımı {}' dir.".format(s1,s2,s1*s2))