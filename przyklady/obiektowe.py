class Czlowiek:
    __slots__ = [
        'imie',
    ]
    gatunek = 'homo sapiens'

    # self - instancja
    def __init__(self, imie):
        self.imie = imie

    def przedstaw_sie(self):
        print(f'Cześć, jestem {self.imie}.')


if __name__ == "__main__":
    pass

c1 = Czlowiek(imie='Jan')
# print(c1.imie)
# c1.przedstaw_sie()
# print(c1.gatunek)
# print(Czlowiek.gatunek)
# print(c1.__class__.gatunek)

c1.imie = 'Ola'
print(c1.imie)
