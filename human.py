class Human():
    def __init__(self):
        self.ad = "Alican"
        self.soyad = "Olkun"
        self.yas = 28
        self.ulke = "Turkiye"
        self.sehir = "istanbul"
        self.yetenekler = []

    def kisiBilgileri(self):
        return self.ad, self.soyad, self.yas, self.ulke, self.sehir, self.yetenekler

    def yetenek_ekle(self, yetenekEkle):
        self.yetenekler.append(yetenekEkle)


def main():
    insan1 = Human()
    insan1.yetenek_ekle("Programming")
    insan1.yetenek_ekle("GUitar")
    print(insan1.kisiBilgileri())


if __name__ == '__main__':
    main()