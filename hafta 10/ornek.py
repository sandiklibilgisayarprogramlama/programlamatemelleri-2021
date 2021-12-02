for sayac in range(10):
    print(sayac,end=",") # 0,1,2,3,4,5,6,7,8,9
print("\n")
for sayac2 in range(3,8):
    print(sayac2,end=",") # 3,4,5,6,7
print("\n")
for sayac3 in range(1,100,10):
    print(sayac3,end=",") # 1,11,21,31,41,51,61,71,81,91
print("\n")
"""
-
**
---
***
--
*
"""
for i in range(1,6):
    if i%2==1:
        yazilacak = "-"
    else:
        yazilacak="*"
    print(yazilacak*i)

for s in range(5,0,-1):
    if s%2==1:
        yazilacak="*"
    else:
        yazilacak="-"
    print(yazilacak*s)

