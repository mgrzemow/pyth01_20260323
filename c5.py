"""
Ćwiczenie:

 1. Wczytać z konsoli długości 3 boków trójkąta
 2. Policzyć pole takiego trójkąta ze wzoru Herona
 3. Wypisać wynik na ekran

 Podpowiedzi:
 - Podniesienie do potęgi 1/2 to to samo co pierwiastkowanie - 4 ** 0.5 == 2
 - zawsze musimy stosować operatory - wyrażenie 3(4+7) jest niepoprawne, musi być 3*(4+7)
 - typ obiektu możemy sprawdzić za pomocą type(), np dla zmiennej x i typu str: if type(x) == str

 Rozszerzenia ćwiczenia:
 - jak stwierdzić, że trójąta o podanych bokach nie da się zbudować?
 - alternatywnie użyć math.sqrt

"""

import math

if __name__ == '__main__':

    a = float(input('Podaj długość boku: '))
    b = float(input('Podaj długość boku: '))
    c = float(input('Podaj długość boku: '))

    if a > b + c or b > a + c or c > a + b:
        print('trójkąt nie istnieje')
    else:
        p = 0.5 * (a + b + c)
        x = p * (p - a) * (p - b) * (p - c)
        print('Pole', x ** .5)
    
    
