##Sayi tahmin oyunu Bilgisayar<=>Kullanici

tahta = [["___", "___", "___"],
         ["___", "___", "___"],
         ["___", "___", "___"]]
print("\n"*3)
for i in tahta:
    print("\t".expandtabs(30), *i, end="\n"*2)
kazanma_ölçütleri = [[[0, 0], [1, 0], [2, 0]],
                     [[0, 1], [1, 1], [2, 1]],
                     [[0, 2], [1, 2], [2, 2]],
                     [[0, 0], [0, 1], [0, 2]],
                     [[1, 0], [1, 1], [1, 2]],
                     [[2, 0], [2, 1], [2, 2]],
                     [[0, 0], [1, 1], [2, 2]],
                     [[0, 2], [1, 1], [2, 0]]]
x_durumu = []
o_durumu = []
sıra = 1
sayac= 1
while True:
    if sıra % 2 == 0:
        işaret = "X".center(3)
    else:
        işaret = "O".center(3)

##random.randint(1,3
    print()
    print("İŞARET: {}\n".format(işaret))
    import random
    sayac+=1
    if sayac %2 == 0:                                      #2 ile bolunebilenler bilgisyar tahmini, bolunemeyenler kullanici yorumu
        x=random.randint(1,3)                              #sayac ile kullanici ve bilgisayar girislerini siraya soktum
        print("yukarıdan aşağıya [1, 2, 3]: ".ljust(30),x) #random ile bilgisyardan 1-3 arasinda tahmin aldim
    if sayac %2 != 0:
        x=input("yukarıdan aşağıya [1, 2, 3]: ".ljust(30)) 
    if x == "q":
        break
    if sayac %2 == 0:
        y=random.randint(1,3)
        print("soldan sağa [1, 2, 3]: ".ljust(30),y)
    if sayac %2 !=0:
        y=input("soldan sağa [1, 2, 3]: ".ljust(30))
    if y == "q":
        break
    x = int(x)-1
    y = int(y)-1
    print("\n"*3)
    if tahta[x][y] == "___":
        tahta[x][y] = işaret
        if işaret == "X".center(3):
            x_durumu += [[x, y]]
        elif işaret == "O".center(3):
            o_durumu += [[x, y]]
        sıra += 1
    else:
        sayac+=1                                        #dolu alana rakam girildiginde tur gecmesi icin konuldu
        print("\nORASI DOLU! TEKRAR DENEYİN\n")
        
        
    for i in tahta:
         print("\t".expandtabs(30), *i, end="\n"*2)
    for i in kazanma_ölçütleri:
        o = [z for z in i if z in o_durumu]
        x = [z for z in i if z in x_durumu]
        if len(o) == len(i):
            print("O KAZANDI!")
            quit()
        if len(x) == len(i):
            print("X KAZANDI!")
            quit()
