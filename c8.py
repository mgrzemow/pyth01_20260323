"""
Ćwiczenie:

 1. Wczytać z konsoli długości 3 boków trójkąta
 2. Sprawdzić i wypisać na ekran:
  - czy trójkąt da się stworzyć
  - czy jest prostokątny
  - czy jest równoramienny
  - czy jest równoboczny

 Podpowiedzi:
  - czy niektóre warunki zależą od siebie i w jaki sposób? Jak to wspłynie na zagnieżdzenie if-ów?

 Rozszerzenia ćwiczenia:
 - czy da się wpisać takie dane, żeby wyszedł trójkąt równoramienny i prostokątny? Dlaczego nie i jak to ominąć?
 - co robi eval()?
"""
import math

if __name__ == '__main__':

    a = float(input('Podaj bok: '))
    b = float(input('Podaj bok: '))
    c = float(input('Podaj bok: '))

    p = (a + b + c) / 2
    istnieje = p * (p - a) * (p - b) * (p - c) > 0

    rownoboczny = a == b == c
    rownoramienny = a == b or b == c or c == a
    prostokatny = math.isclose(a ** 2 + b ** 2, c ** 2) or\
                  math.isclose(a ** 2 + c ** 2, b ** 2) or\
                  math.isclose(b ** 2 + c ** 2, a ** 2)
    
    if istnieje:
        print('istnieje')
        if prostokatny:
            print('prostokatny')
        if rownoramienny:
            print('rownoramienny')
            if rownoboczny:
                print('rownoboczny')
    else:
        print('nie istnieje')

