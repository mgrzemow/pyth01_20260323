class Pracownik:
    __slots__ = [
        'imie',
        '_stawka_norm',
        '_stawka_nad',
        '_zarobki'
    ]

    def __init__(self, imie, stawka_norm, stawka_nad):
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

    def wyplata(self):
        """
        Zwraca zarobioną kwotę i resetuje licznik do 0

        Returns:

        """
        tmp = self._zarobki
        self._zarobki = 0
        return tmp


class Kierownik(Pracownik):
    __slots__ = [
        '_bonus_kier'
    ]

    def __init__(self, imie, stawka_norm, stawka_nad, bonus_kier):
        super().__init__(imie, stawka_norm, stawka_nad)
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

    class Dyrektor:
        """
        Dyrektor zarabia tak jak Kierownik, a dodatkowo
        ma bonus dyrektorski za każde wywołanie metody pracuj.
        """

if __name__ == '__main__':
    # p1 = Pracownik('Jan', 20, 40)
    # print(p1.wyplata())  # 0
    # p1.pracuj(5)  # naliczy 100, w sumie 100
    # p1.pracuj(10)  # naliczy 240, w sumie 340
    # print(p1.wyplata())  # 340
    # print(p1.wyplata())  # 0
    p1 = Kierownik('Jan', 20, 40, 100)
    print(p1.wyplata())  # 0
    p1.pracuj(5)  # naliczy 100, w sumie 100
    p1.pracuj(10)  # naliczy 340, w sumie 440
    print(p1.wyplata())  # 440
    print(p1.wyplata())  # 0
