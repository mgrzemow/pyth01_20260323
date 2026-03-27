"""
Ćwiczenie:

1. Wczytać z konsoli nr roku.
2. Sprawdzić czy rok jest przestępny.
3. Wypisać odpowiedni komunikat.

Podpowiedzi:
Rok jest przestępny jeżeli spełniony jest chociaż jeden z dwóch warunków:
- dzieli się przez 400
lub
- dzieli się przez 4 i nie dzieli się przez 100

Rozszerzenia ćwiczenia:
- nie użyć w kodzie ani jednego dwukropka ':'
- sprawdzić czy użytkownik podał całkowitą liczbę dodatnią > 0
"""


def komunikat_przestepny_if(rok: int) -> str:
    """Zwraca komunikat o roku przestępnym z użyciem klasycznego if/else.

    Args:
        rok: Numer roku (wartość dodatnia).

    Returns:
        Napis ``"przestepny"`` albo ``"nie przestepny"``.

    Raises:
        ValueError: Gdy ``rok`` jest mniejszy lub równy 0.
    """
    if rok <= 0:
        raise ValueError("Nr roku < 0")

    d_400 = rok % 400 == 0
    d_4 = rok % 4 == 0
    d_100 = rok % 100 == 0

    if d_400 or (d_4 and not d_100):
        return "przestepny"
    return "nie przestepny"


def komunikat_przestepny_inline_if(rok: int) -> str:
    """Zwraca komunikat o roku przestępnym z użyciem inline if.

    Args:
        rok: Numer roku (wartość dodatnia).

    Returns:
        Napis ``"przestepny"`` albo ``"nie przestepny"``.

    Raises:
        ValueError: Gdy ``rok`` jest mniejszy lub równy 0.
    """
    if rok <= 0:
        raise ValueError("Nr roku < 0")

    d_400 = rok % 400 == 0
    d_4 = rok % 4 == 0
    d_100 = rok % 100 == 0
    return "przestepny" if d_400 or (d_4 and not d_100) else "nie przestepny"


if __name__ == "__main__":
    rok = int(input("Podaj rok: "))


    print(komunikat_przestepny_if(rok))
    print(komunikat_przestepny_inline_if(rok))
