"""
Napisać klasę Spychacz

Spychacz będzie pamiętał następujące dane:
 - nr rejestracyjny
 - pozycję w układzie x, y
 - kierunek góra / dół / lewo / prawo

Spychacz rodzi się w (0, 0) skierowany w górę.

Sspycha umie / ma metody:
- jechać przed sisebie o n kroków - jedz(7)
- skrecać w prawo o 90 stopni - skret_w_prawo
- wypisać swoją pozycję 'Sychacz kr12345 w (13, 7)' - wypisz
"""
class Spychacz:
    ...

if __name__ == "__main__":
    s1 = Spychacz('kr12345')
    s1.wypisz() # (0,0)
    s1.jedz(7)
    s1.skret_w_prawo()
    s1.wypisz() # # (0,7)
    s1.jedz(7)
    s1.skret_w_prawo()
    s1.wypisz() # (7,7)
    s1.jedz(7)
    s1.skret_w_prawo()
    s1.wypisz() # (7,0)
    s1.jedz(7)
    s1.skret_w_prawo()
    s1.wypisz() # (0,0)
