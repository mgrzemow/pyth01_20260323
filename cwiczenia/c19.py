import abc


class PracownikAbstract(metaclass=abc.ABCMeta):
    __slots__ = ['_zarobki'
                 ]

    def wyplata(self):
        """
        Zwraca zarobioną kwotę i resetuje licznik do 0

        Returns:

        """
        tmp = self._zarobki
        self._zarobki = 0
        return tmp

    @abc.abstractmethod
    def pracuj(self, ile_h):
        ...

    @abc.abstractmethod
    def __init__(self):
        ...


class Pracownik(PracownikAbstract):
    __slots__ = [
        'imie',
        '_stawka_norm',
        '_stawka_nad',
    ]

    def __init__(self, *, imie, stawka_norm, stawka_nad):
        self.imie = imie
        self._stawka_norm = stawka_norm
        self._stawka_nad = stawka_nad
        self._zarobki = 0

    def pracuj(self, ile_h):
        """
        Nalicza zarobki wg zasady że:
        - <= 8h wg stawki normalnej
        - > 8h wg stawki nadgodzinowej

        Args:
            ile_h:

        Returns:

        """
        if ile_h <= 8:
            self._zarobki += self._stawka_norm * ile_h
        else:
            self._zarobki += self._stawka_nad * (ile_h - 8) + self._stawka_norm * 8


class Kierownik(Pracownik):
    __slots__ = [
        '_bonus_kier'
    ]

    def __init__(self, *, bonus_kier, **kwargs):
        super().__init__(**kwargs)
        self._bonus_kier = bonus_kier

    def pracuj(self, ile_h):
        """
        Nalicza kwotowo bonus kierownika jeżeli ile_h >= 10
        Args:
            ile_h:

        Returns:

        """
        super().pracuj(ile_h)
        if ile_h >= 10:
            self._zarobki += self._bonus_kier


class Dyrektor(Kierownik):
    """
    Dyrektor zarabia tak jak Kierownik, a dodatkowo
    ma bonus dyrektorski za każde wywołanie metody pracuj.
    """
    __slots__ = [
        '_bonus_dyr'
    ]

    def __init__(self, *, bonus_dyr, **kwargs):
        super().__init__(**kwargs)
        self._bonus_dyr = bonus_dyr

    def pracuj(self, ile_h):
        """
        Nalicza kwotowo bonus dyrektora
        Args:
            ile_h:

        Returns:

        """
        super().pracuj(ile_h)
        self._zarobki += self._bonus_dyr


def rekrutuj_zespol(ile_p: int, ile_k: int, ile_d: int) -> list[Pracownik]:
    lista_p = []
    for _ in range(ile_p):
        lista_p.append(Pracownik(imie='Jan', stawka_norm=20, stawka_nad=40))
    for _ in range(ile_k):
        lista_p.append(Kierownik(imie='Ola', stawka_norm=20, stawka_nad=40, bonus_kier=100))
    for _ in range(ile_d):
        lista_p.append(Dyrektor(imie='Zofia', stawka_norm=20, stawka_nad=40, bonus_kier=100, bonus_dyr=200))
    return lista_p


if __name__ == '__main__':
    # p1 = Pracownik('Jan', 20, 40)
    # print(p1.wyplata())  # 0
    # p1.pracuj(5)  # naliczy 100, w sumie 100
    # p1.pracuj(10)  # naliczy 240, w sumie 340
    # print(p1.wyplata())  # 340
    # print(p1.wyplata())  # 0
    # p1 = Kierownik('Jan', 20, 40, 100)
    # print(p1.wyplata())  # 0
    # p1.pracuj(5)  # naliczy 100, w sumie 100
    # p1.pracuj(10)  # naliczy 340, w sumie 440
    # print(p1.wyplata())  # 440
    # print(p1.wyplata())  # 0

    # p1 = Dyrektor(imie='Jan',
    #               stawka_norm=20,
    #               stawka_nad=40,
    #               bonus_kier=100,
    #               bonus_dyr=500)
    # print(p1.wyplata())  # 0
    # p1.pracuj(5)  # naliczy 600, w sumie 100
    # p1.pracuj(10)  # naliczy 840, w sumie 440
    # print(p1.wyplata())  # 1440
    # print(p1.wyplata())  # 0

    lista_p = rekrutuj_zespol(10, 2, 1)
    for p in lista_p:
        p.pracuj(10)
        p.pracuj(12)
        p.pracuj(6)
        p.pracuj(0)
    suma = 0
    for p in lista_p:
        suma += p.wyplata()
    print(suma)
