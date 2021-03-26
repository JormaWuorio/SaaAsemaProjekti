class SaaAsema:
    def __init__(self, nimi, tyyppi, sijainti, numero):
        self.nimi = nimi
        self.tyyppi = tyyppi
        self.sijainti = sijainti 
        self.numero = numero

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

pvm=input("Anna päivämäärä: ")
sijainti=int(input("Anna sijainti: "))
chica = SaaAsema("chica", "Rannikkoasema", "Chicago", "1")
nyki = SaaAsema("nyki", "Lentokenttä", "New York", "2")
"""
SaaAsemalista =[chica, nyki]
for asema in SaaAsemalista:
    print("Sääasema", asema.sijainti)
"""

eka = SaaHavainto("23.03.", 20, 5, 320, 3/8, 1, 1)
toka = SaaHavainto("24.03", 22, 122, 3000, 1/8, 2, 1)
kolmas = SaaHavainto("25.03.", 21, 90, 240, 4/8, 3, 2)
neljas = SaaHavainto("26.03.", 23, 97, 180, 6/8, 4, 2)
viides = SaaHavainto("27.03.", 24, 88, 150, 2/8, 5, 1)
lista = [eka, toka, kolmas, neljas, viides]
for havainto in lista:
    if havainto.paivamaara == pvm and havainto.numero == sijainti:
      
        print("Päivämäärä:", havainto.paivamaara)
        print("Lämpötila:", havainto.lampotila)
        print("Tuulennopeus:", havainto.tnopeus, "\n")

'''
print("Säähavainto ilmeni", fasfas.paivamaara + ", lämpötila oli", fasfas.lampotila, "\nTuulennopeus oli tuolloin", str(fasfas.tnopeus) + "m/s ja suunta", fasfas.tsuunta, "astetta")
print(str(fasfas.tnopeus) + "m/s kilometreinä on", fasfas.mskmh() + ". Pilvisyys oli", fasfas.pilvisyys, "ja näkyvyys", fasfas.nakyvyys)

print(fasfas.mphkm())
print(fasfas.solmutkm())'''