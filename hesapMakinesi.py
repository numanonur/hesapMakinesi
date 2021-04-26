while True:
    cal=input("""-------------------------------------------
|      Hesap makinesine hoş geldin       |
| Tooplama İşlemi için-----------------1 |
| Çıkarma İşlemi için------------------2 |
| Çarma İşlemi için--------------------3 |
| Bölme İşlemi için--------------------4 |
| Üslü işlemler için-------------------5 |
| Fakröriyel Bulmak için---------------6 |
| Ortak Kat Bulmak için----------------7 |
| Bölümden Kalı Bulmak için------------8 |
| İki sayının Ortalamasını Bulmak için 9 |
| Yüzde bulmak için-------------------10 | 
| Çıkmak için--------------11'i tuşlayın |
-------------------------------------------
""")
    if cal == "1":
        a=float(input("1. sayıyı giriniz "))
        b=float(input("2. sayıyı giriniz "))
        c= a + b
        print(c)

    elif cal=="2":
        a=float(input("1. sayıyı giriniz "))
        b=float(input("2. sayıyı giriniz "))
        c= a - b
        print(c)

    elif cal=="3":
        a=float(input("1. sayıyı giriniz "))
        b=float(input("2. sayıyı giriniz "))
        c= a * b
        print(c)

    elif cal=="4":
        a=float(input("1. sayıyı giriniz "))
        b=float(input("2. sayıyı giriniz "))
        c= a // b
        print(c)

    elif cal=="5":
        a=float(input("Taban sayısını giriniz "))
        b=float(input("Üs sayısını giriniz "))
        c= a ** b
        print(c)

    elif cal=="6":
        a=int(input("Faktöriyelini bulmak istediğiniz sayıyı giriniz. "))
        faktoriyel = 1
        for a in range(2,a+1):
            faktoriyel *= a
        print("Faktoriyel:",faktoriyel)

    elif cal=="7":
        a=int(input("1.sayısyı girin "))
        b=int(input("2.sayısyı girin "))
        d=int(input("Ortak katın çıkmasını istediğinin en yğksek sayı nedir? "))
        for c in range (1,d):
            if c%a==0 and c%b==0:
                    print(c)

    elif cal=="8":
        a=int(input("Bölüneni girin "))
        b=int(input("Böleni girin "))
        c=a%b
        print("{} sayısının {} sayısına bölümünden kalan {}".format(a,b,c))

    elif cal=="9":
        a = float(input("1. sayı :"))
        b = float(input("2. sayı :"))
        ort=(int(a)+int(b))/2
        print("ort : {0}".format(ort))

    elif cal=="10":
        a=float(input("Yüzdesi alınacak sayıyı giriniz "))
        b=float(input("Yüzdeyi giriniz "))
        c=a*(b/100)
        print("{} sayısınız %{}'i {}".format(a,b,c))
    elif cal=="11":
        break
    else:
        print("Lütfen geçerli bir işlem giriniz...")