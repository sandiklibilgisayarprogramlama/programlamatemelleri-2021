s1 = 0
s2 = 1
girilen =int(input("bir sayı giriniz"))
print(s1,end=" ")
print(s2,end=" ")
for k in range(100):
    onceki = s2
    s2 = s1+s2
    s1=onceki
    if s2>girilen:
        break
    print(s2,end=" ")



