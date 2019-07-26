##-Kullanicidan aklindan 0-100 araliginda bir sayi tutmasini isteyin.

import random
print("""Aklinizdan 0-100 araliginda bir sayi tutunuz, tuttugunuz sayi
      tahminimden kuccukse (-) ye, buyukse (+)  ya basiniz, sayiyi bildimse
      (bildin) yaziniz.""")

tahmin1=0
tahmin2=101
tahminler=[]

while True:
    
    bilgisayar=random.randint(tahmin1,tahmin2)
    print("Tahminim",bilgisayar)
    kullanici=input("kullanici degerlendirmesi :")
    kullanici=kullanici.lower()   
    tahminler.append(bilgisayar)
    print(tahminler)
    if kullanici=="-":
        tahmin2=bilgisayar    
    elif kullanici=="+":
        tahmin1=bilgisayar
    elif kullanici=="bildin": 
        print("Oyun icin tesekkurler")
        break
        continue
            

            

