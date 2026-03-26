class Czlowiek:
    gatunek = 'homo sapiens'

    # self - instancja
    def __init__(self, imie):
        self.imie = imie
        self.atr1 = None


    def przedstaw_sie(self):
        print(f'Cześć, jestem {self.imie}.')

c1 = Czlowiek(imie='Jan')
print(c1.imie)
c1.przedstaw_sie()
print(c1.gatunek)
print(Czlowiek.gatunek)
print(c1.__class__.gatunek)
