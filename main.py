def main():
    ogrenci_adi = str(input("Ogrenci Adı :"))
    ogrenci_soyadi = str(input("Ogrenci Soyadi :"))
    ogrenci_no = int(input("Ogrenci No :"))
    dogru_sayisi = int(input("Doğru Sayisi :"))
    yanlis_sayisi = int(input("Yanlıs Sayisi :"))

    if(dogru_sayisi + yanlis_sayisi<50):
        ogrenci_obje = Student(ogrenci_adi, ogrenci_soyadi, ogrenci_no)
        soru_objesi = Soru()
        net = soru_objesi.NetSayisi(dogru_sayisi,yanlis_sayisi)
        hesap = soru_objesi.Hesapla(net)
        ogrenci_obje.studentInformation()
        print("Puan :", hesap)
    else:
        print("Girilen soru sayısı 50'den fazla.")


if __name__ == '__main__':
    main()

class Student():

    def studentInformation(self):
        print("Ögrenci Adı :" + self.ogrenci_adi)
        print("Ögrenci Soyadı :" + self.ogrenci_soyadi)
        print("Ögrenci No :" + str(self.ogrenci_no))

    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciNo):
        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciNo = ogrenciNo

class Soru():
    def NetSayisi(self, dogru_sayisi, yanlis_sayisi):
        temp = float(yanlis_sayisi / 4)
        netSayisi = dogru_sayisi - temp
        return netSayisi

    def Hesapla(self, netSayisi):
        hesap = netSayisi * 2
        return hesap







