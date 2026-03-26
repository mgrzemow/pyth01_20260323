"""
Napisać klasę Spychacz

Spychacz będzie pamiętał następujące dane:
 - nr rejestracyjny
 - pozycję w układzie x, y
 - kierunek góra / dół / lewo / prawo

Spychacz rodzi się w (0, 0) skierowany w górę.

Sspycha umie / ma metody:
- jechać przed siebie o n kroków - jedz(7)
- skrecać w prawo o 90 stopni - skret_w_prawo
- wypisać swoją pozycję 'Sychacz kr12345 w (13, 7)' - wypisz
"""


class Spychacz:
    __slots__ = [
        '_kierunek',
        'nr_rej',
        '_x',
        '_y',
    ]
    kierunki = 'NESW'

    def __init__(self, nr_rej):
        self.nr_rej = nr_rej
        self._kierunek = 0
        self._x = 0
        self._y = 0

    def skret_w_prawo(self):
        self._kierunek = (self._kierunek + 1) % 4

    def wypisz(self):
        print(f'{self.__class__.__name__}("{self.nr_rej}") w ({self._x}, {self._y})')

    def __str__(self):
        return f'{self.__class__.__name__}("{self.nr_rej}") w ({self._x}, {self._y}) skierowany na {Spychacz.kierunki[self._kierunek]}'

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.nr_rej}")'

    def __int__(self):
        return 66

    # NIE UŻYWAĆ!!!
    # def __bool__(self):
    #     return False

    # operatory - fajne ale musi mieć sens!
    def __eq__(self, other):
        return self.nr_rej == other.nr_rej



    def jedz(self, n):
        if Spychacz.kierunki[self._kierunek] == 'N':
            self._y += n
        elif Spychacz.kierunki[self._kierunek] == 'E':
            self._x += n
        elif Spychacz.kierunki[self._kierunek] == 'S':
            self._y -= n
        elif Spychacz.kierunki[self._kierunek] == 'W':
            self._x -= n


if __name__ == "__main__":
    s1 = Spychacz('kr12345')
    print(s1)  # (0,0)
    s1.jedz(7)
    s1.skret_w_prawo()
    print(s1)  # # (0,7)
    s1.jedz(7)
    s1.skret_w_prawo()
    print(s1)  # (7,7)
    s1.jedz(7)
    s1.skret_w_prawo()
    print(s1)  # (7,0)
    s1.jedz(7)
    s1.skret_w_prawo()
    print(s1)  # (0,0)

    s2 = Spychacz('wa44455')
    s2.jedz(27)
    print([s1, s2])
    print(int(s2))
    s3 = Spychacz(nr_rej='kr12345')
    print(s1 == s3)

    import pathlib
    p1 = pathlib.Path(__file__).parent / 'html'
    print(p1)
