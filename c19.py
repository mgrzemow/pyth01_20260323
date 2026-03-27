class Pracownik:
    def __init__(self, imie, stawka_norm, stawka_nad):
        self.imie = imie
        self.stawka_norm = stawka_norm
        self.stawka_nad = stawka_nad

    def pracuj(self, ile_h):
        """
        Nalicza zarobki wg zasady że:
        - <= 8h wg stawki normalnej
        - > 8h wg stawki nadgodzinowej

        Args:
            ile_h:

        Returns:

        """
        ...
    def wyplata(self):
        """
        Zwraca zarobioną kwotę i resetuje licznik do 0

        Returns:

        """
        ...

if __name__ == '__main__':
    p1 = Pracownik('Jan', 20, 40)
    print(p1.wyplata()) # 0
    p1.pracuj(5) # naliczy 100, w sumie 100
    p1.pracuj(10) # naliczy 240, w sumie 340
    print(p1.wyplata())  # 340
    print(p1.wyplata())  # 0


