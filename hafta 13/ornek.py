karakter_dizisi = "Merhaba Dünya"
print(karakter_dizisi)

karakter_dizisi ="Merhaba Dünya"
print("Merhaba","Dünya",sep="\n") # \n newline

karakter_dizisi = "Merhaba\nDünya"
print(karakter_dizisi)

karakter_dizisi="Merhaba\tDünya"
print(karakter_dizisi)

# karakter_dizisi3 = 'İstanbul'dan sabah geldim' - hatalı
karakter_dizisi3 = 'İstanbul\'dan sabah geldim'
karakter_dizisi3 = "İstanbul'dan sabah geldim"
# \ escape kaçış

karakter_dizisi4 ="Ankara'\\nin soğuğu"
print(karakter_dizisi4)

karakter_dizisi = "Merhaba"
"""
m   e   r   h   a   b   a
1   2   3   4   5   6   7
0   1   2   3   4   5   6
"""
print(karakter_dizisi[0])
print(karakter_dizisi[6])
print(karakter_dizisi[2])

# klavyeden girilen bir kelimenin tüm harflerini
# alt alta yazan programı kodlayınız.

print("--------------------------")
girilen = "Merhaba Dünya"
for i in range(0,13):
    print(girilen[i])

girilen=input("bir kelime giriniz: ")
# len(karakter_dizisi) 
# -> içine parametre olarak verilen karakter sayısını geri döndürür
print(len(girilen))

for i in range(0,len(girilen)):
    print(" "*i+girilen[i])

