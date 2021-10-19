ik = ""
while len(ik) != 11 or ik.isdigit()!=True:
    try:
        ik = input("Isikukood: ")
    except ValueError:
        print("Try Again")
print("Isikukoodi analüüs: ".center(50,"-"))
print("Esimene sümbol: ")
ik_list=list(ik)
print(ik_list)
print(ik_list[0])
if int(ik_list[0]) not in [1,2,3,4,5,6]:
    print(ik_list[0]," - ei ole õige!")
else:
    print(ik_list[0]," - õige arv!")
    kuu=ik_list[3]+ik_list[4]
    kuu=int(kuu)
    if kuu>0 and kuu<13:
        print(ik_list[3],ik_list[4],"õiged andmed!")
    else:
        print(ik_list[3],ik_list[4],"ei ole õiged andmed!")
        kuu=ik_list[3]+ik_list[4] #1+0=10
        kuu=int(kuu)
        if kuu>0 and kuu<13:
            print(ik_list[3],ik_list[4],"õiged andmed!")
            paev=int(ik_list[5]+ik_list[6])
            #1,3,5,7,8,10,12, ... - 31 päev
            #2,4,6,9,11     28-29,30-päev
            if int(ik_list[0])==1 or int(ik_list[0])==2:
                aasta=int("18"+ik_list[1]+ik_list[2])
            elif int(ik_list[0])==3 or int(ik_list[0])==4:
                aasta=int("19"+ik_list[1]+ik_list[2])
            elif int(ik_list[0])==5 or int(ik_list[0])==6:
                aasta=int("20"+ik_list[1]+ik_list[2])
            if kuu in [1,3,5,7,8,10,12] and paev>0 and paev<32:
                print(ik_list[5],ik_list[6], "õige päev!")
            elif (kuu in [3,6,9,11] and paev>0 and paev<31 or (kuu == 2 and paev>0 and paev<29)):
                print(ik_list[5],ik_list[6],"õige päev!")
            elif aasta % 4==0 and kuu == 2 and paev>0 and paev>30:
                print(ik_list[5],ik_list[6],"õige päev! 29 vebr.")
            else:
                print(ik_list[5],ik_list[6],"Valed päevad! ")
        else:
            print(ik_list[3],ik_list[4],"Vale kuu!!!")

#Summa = 1×3 + 2×7 + 3×6 + 4×0 + 5×5 + 6×0 + 7×3 + 8×0 + 9×2 + 1×9 = 108.
Summa = 0
for i in range(1,11):
    if i == 10:
        i = 1
    Summa+=i*int(ik_list[i-1])
print("Summa: ",Summa)
jaak=Summa//11
if jaak==10:#II astme kaal: 3 4 5 6 7 8 9 1 2 3
    Summa=0
    for i in range(3,13):
        if i<9:
            Summa+=i*int(ik_list[i-1])
        else:
            Summa+=(i-8)*int(ik_list[i-1])
    jaak=Summa//11
jaak=Summa-jaak*11
print("Kontrollnumber: ",jaak)
if jaak==int(ik_list[10]):
    print("Isikukood on õige!!!!")
else:
    print("Isikukood on vale!!!!")