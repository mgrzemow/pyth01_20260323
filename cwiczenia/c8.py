"""
Ćwiczenie:

1. Wczytać z konsoli długości 3 boków trójkąta.
2. Sprawdzić i wypisać na ekran:
- czy trójkąt da się stworzyć
- czy jest prostokątny
- czy jest równoramienny
- czy jest równoboczny
"""

import math


def analizuj_trojkat(a: float, b: float, c: float) -> tuple[bool, bool, bool, bool]:
    """Analizuje własności trójkąta na podstawie długości boków.

    Args:
        a: Długość pierwszego boku.
        b: Długość drugiego boku.
        c: Długość trzeciego boku.

    Returns:
        Krotka czterech flag ``(istnieje, prostokatny, rownoramienny, rownoboczny)``.
        Jeżeli trójkąt nie istnieje, zwraca ``(False, False, False, False)``.
    """
    istnieje = a + b > c and a + c > b and b + c > a
    if not istnieje:
        return False, False, False, False

    rownoboczny = a == b == c
    rownoramienny = a == b or b == c or c == a
    prostokatny = (
        math.isclose(a**2 + b**2, c**2)
        or math.isclose(a**2 + c**2, b**2)
        or math.isclose(b**2 + c**2, a**2)
    )
    return True, prostokatny, rownoramienny, rownoboczny


if __name__ == "__main__":
    a = float(input("Podaj bok: "))
    b = float(input("Podaj bok: "))
    c = float(input("Podaj bok: "))

    istnieje, prostokatny, rownoramienny, rownoboczny = analizuj_trojkat(a, b, c)

    if istnieje:
        print("istnieje")
        if prostokatny:
            print("prostokatny")
        if rownoramienny:
            print("rownoramienny")
        if rownoboczny:
            print("rownoboczny")
    else:
        print("nie istnieje")
