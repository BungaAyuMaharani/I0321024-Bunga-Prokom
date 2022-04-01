totalBelanja =int(input("Total Belanja="))
KartuMember =str(input("Member? (Y/T)"))
if KartuMember=="Y":
    if totalBelanja >= 500000:
        diskon= "0.25"
        totalBayar = totalBelanja - (totalBelanja*0.25)
    elif totalBelanja >= 100000:
        diskon= "0.2"
        totalBayar = totalBelanja - (totalBelanja*0.2)
    elif totalBelanja <= 100000:
        diskon= "0.1"
        totalBayar = totalBelanja - (totalBelanja*0.1)
elif KartuMember=="T":
    if totalBelanja >= 100000:
        diskon= "0.1"
        totalBayar = totalBelanja -(totalBelanja*0.1)
    else:
        diskon= "0"
        totalBayar = totalBelanja -(totalBelanja*0)
print("Total Belanja Anda Sebesar =",totalBelanja)
print("Selamat Anda Mendapatkan Diskon Sebesar =",diskon)
print("Total Belanja Yang Harus Anda Bayar Adalah =",totalBayar)

