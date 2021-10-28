"""
print fonksiyonu ekranda çıktı göstermek amaçlı kullanılır.
"""
print("merhaba")
print("dünya")

print("Afyon","Kocatepe","Üni","Sandıklı","MYO")

# \t ascii kodu 4 karakter boşluk bırakmak için kullanılabilir.
# \n ascii kodu imleci bir alt satıra göndermek için kullanılabilir.

print("afyon\t","karahisar") # konsolda 4 karakter boşluk görünür.
print("afyon\n","karahisar") # konsolda karahisar aşağı satırda görünür

# sep parametresi virgüller ayrılmış ifadeleri yazdırırken aradaki ayırıcı
# yı tanımlar.

print("Afyon","Kocatepe","Üni","Sandıklı","MYO",sep="-")

# end parametresi satır sonunda neyin yer alacağını belirtir.

print("merhaba dünya","zalim dünya",end="!")
print("zalimsin dünya")

# print içinde tek tırnak kullanılarakta metin ifadeleri yazılabilir.

print('tık tırnaklı yazdım')
print("İstanbul'u çok seviyorum")

# escape karakteri (\) ile string ifadelerin içinde tek tırnağın 
# kesme olarak kullanıldığı gösterilebilir.

print('istanbul\'u çok seviyorum')

print('istanbul"u çok seviyorum')
print("istanbul\"u çok seviyorum")

# string' leri birleştirmek için + (artı) işareti de kullanılabilir.
print("ahmet"+" "+"süleyman "+"cumhur")

print("toplam : "+"12")
print("toplam : "+str(12))

s1 = 12
s2 = 15
print(str(s1)+" ile "+str(s2)+" sayılarının toplamı "+str(s1+s2)+"' dir.")
print(str(s1)+" ile "+str(s2)+" sayılarının fark "+str(s1-s2)+"' dir.")
print(str(s1)+" ile "+str(s2)+" sayılarının çarpım "+str(s1*s2)+"' dir.")
print(str(s1)+" ile "+str(s2)+" sayılarının bölme "+str(s1/s2)+"' dir.")


print("{} ile {} sayılarının toplamı {}'  dir.".format(s1,s2,s1+s2))
print("{} ile {} sayılarının fark {}'  dir.".format(s1,s2,s1-s2))
print("{} ile {} sayılarının çarpım {}'  dir.".format(s1,s2,s1*s2))
print("{} ile {} sayılarının bölüm {}'  dir.".format(s1,s2,s1/s2))


