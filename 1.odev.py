##-Kullanicidan aklindan 0-100 araliginda bir sayi tutmasini isteyin.

import random
print("Aklinizdan 0-100 araliginda bir sayi tutunuz")
bilgisayar=random.randint(0,100)
bilgisayar1=0
bilgisayar2=0
print(bilgisayar)


while True:
    kul=input(" ")
    sayac=0
    sira=0
    if kul=="-":
        sayac-=10
        bilgisayar1=random.randint(sayac,bilgisayar)
        print(bilgisayar1)
        
    if kul=="+":
        sira+=10
        bilgisayar2=random.randint(sira,bilgisayar)
        print(bilgisayar2)
        
        continue
            

            

