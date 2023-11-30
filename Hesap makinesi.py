print(""""
********************
HESAP MAKİNESİ
*********************""")


print(""
      "1-Toplama\n"
      "2-Çıkarma\n"
      "3-Çarpma\n"
      "4-Bölme\n")

a=int(input("Birinci sayı: "))
b=int(input("İkinci sayı: "))
işlem=input("işlem seçiniz: ")


if işlem=="1":
    print("{} ile {} toplamı {}'dır.".format(a,b,a+b))
elif işlem=="2":
    print("{} ile {} farkı {}'dır.".format(a,b,a-b))
elif işlem=="3":
    print("{} ile {} çarpımı {}'dır.".format(a,b,a*b))
elif işlem=="4":
    print("{} ile {} bölümü {}'dır.".format(a,b,a/b))

else:
    print("Geçersiz işlem....")
    print("Lütfen geçerli bir işlem giriniz.")