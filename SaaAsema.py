class SaaAsema:
    def __init__(self, nimi, tyyppi, sijainti, numero):
        self.nimi = nimi
        self.tyyppi = tyyppi
        self.sijainti = sijainti 
        self.numero = numero
    
    @staticmethod
    def tee_saaasema():
        nimi = input("Anna sääaseman nimi: ")
        tyyppi = input("Anna tyyppi: ")
        sijainti = input("Anna sijainti: ")
        numero = input("Anna numero: ")
        uusi = SaaAsema(nimi, tyyppi, sijainti, numero)
        return uusi
        

class SaaHavainto:
    def __init__(self, paivamaara: str, lampotila, tnopeus, tsuunta, pilvisyys, nakyvyys, numero):
        self.paivamaara = paivamaara
        self.lampotila = str(lampotila) + "c"
        self.tnopeus = tnopeus
        self.tsuunta = tsuunta
        self.pilvisyys = pilvisyys
        self.nakyvyys = nakyvyys
        self.numero = numero

    def kmhmph(self):
        mailit = self.tnopeus * 0.62
        return mailit

    def mphkm(self):
        kilometrit = self.tnopeus * 1.60934
        return str(kilometrit) + "km/h"
    
    def solmutkm(self):
        kilometrit = self.tnopeus * 1.852
        return str(kilometrit) + "km/h"

    def mskmh(self):
        kilometrit = self.tnopeus * 3.6
        return str(kilometrit) + "km/h"
    
    @staticmethod
    def tee_saahavainto():
        pvm = input("Anna päivämäärä: ")
        lampo = input("Anna lämpötila: ")
        tnopeus = input("Anna tuulennopeus: ")
        tsuunta = input("Anna tuulensuunta: ")
        pilvisyys = input("Pilvisyys: ")
        nakyvyys = input("Näkyvyys(kilometrejä): ")
        numero = int(input("Anna sijainti(1, 2): "))
        uusi = SaaHavainto(pvm, lampo, tnopeus, tsuunta, pilvisyys, nakyvyys, numero)

        return uusi


def lisaa_listaan():
    while True:
        valinta = input("lisätäänkö sääasema(1) vai havainto(2) vai lopetetaanko(3)?")
        if valinta == "1":
            while True:
                asema = SaaAsema.tee_saaasema()
                saaasemat.append(asema)
                uusi = input("Uusi havainto? (K/E): ")
                if uusi.upper == "E" or uusi == "e":
                    break

        elif valinta == "2":
            while True:
                havainto = SaaHavainto.tee_saahavainto()
                saahavainnot.append(havainto)
                uusi = input("Uusi havainto? (K/E): ")
                if uusi.upper == "E" or uusi == "e":
                    break
        
        elif valinta == "3":
            break

def tulosta():
    for havainto in saahavainnot:
        print("Havainnon päivämäärä:", havainto.paivamaara)
        print("Havainnon lämpötila: ", havainto.lampotila)
        print("Havainnon tuulennopeus: ", havainto.tnopeus)
        print("Havainnon tuulensuunta: ", havainto.tsuunta)
        print("Havainnon pilvisyys: ", havainto.pilvisyys)
        print("Havainnon näkyvyys: ", havainto.nakyvyys)
        print("Havainnon numero: ", havainto.numero, "\n")

    for asema in saaasemat:
        print("Aseman nimi: ", asema.nimi)
        print("Aseman tyyppi: ", asema.tyyppi)
        print("Aseman sijainti: ", asema.sijainti)
        print("Aseman numero: ", asema.numero)

saaasemat = []
saahavainnot = []
lisaa_listaan()
tulosta()