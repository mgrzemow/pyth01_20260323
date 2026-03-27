"""
Ćwiczenie:

Wygenerować PESEL na podstawie:
- roku, miesiąca i dnia urodzenia,
- numeru kolejnego,
- płci (``True`` dla mężczyzny).
"""


def generuj_pesel_na_piechote(
    rok: int,
    miesiac: int,
    dzien: int,
    nr: int,
    plec_facet: bool,
) -> str:
    """Generuje PESEL krok po kroku.

    Args:
        rok: Rok urodzenia.
        miesiac: Miesiąc urodzenia.
        dzien: Dzień urodzenia.
        nr: Numer kolejny osoby (0-999).
        plec_facet: ``True`` dla mężczyzny, ``False`` dla kobiety.

    Returns:
        Wygenerowany numer PESEL (11 cyfr).
    """
    # Dla roczników >= 2000 zwiększamy miesiąc o 20.
    miesiac_kod = miesiac + 20 if rok >= 2000 else miesiac

    # Budujemy część podstawową PESEL-a bez cyfry kontrolnej.
    rok_s = str(rok)[-2:]
    miesiac_s = f"{miesiac_kod:02d}"
    dzien_s = f"{dzien:02d}"
    nr_s = f"{nr:03d}"
    plec_s = "1" if plec_facet else "0"
    pesel_bez_kontroli = f"{rok_s}{miesiac_s}{dzien_s}{nr_s}{plec_s}"

    # Cyfra kontrolna: ostatnia cyfra sumy wszystkich cyfr.
    suma = 0
    for znak in pesel_bez_kontroli:
        suma += int(znak)
    cyfra_kontrolna = str(suma)[-1]
    return pesel_bez_kontroli + cyfra_kontrolna


def generuj_pesel_skrotowo(
    rok: int,
    miesiac: int,
    dzien: int,
    nr: int,
    plec_facet: bool,
) -> str:
    """Generuje PESEL w wersji skróconej (f-string + sum).

    Args:
        rok: Rok urodzenia.
        miesiac: Miesiąc urodzenia.
        dzien: Dzień urodzenia.
        nr: Numer kolejny osoby (0-999).
        plec_facet: ``True`` dla mężczyzny, ``False`` dla kobiety.

    Returns:
        Wygenerowany numer PESEL (11 cyfr).
    """
    # Złożenie 10 pierwszych cyfr w jednym f-stringu.
    pesel = f"{str(rok)[-2:]}{miesiac + 20 if rok >= 2000 else miesiac:02d}{dzien:02d}{nr:03d}{int(plec_facet)}"

    # Cyfra kontrolna: ostatnia cyfra z sumy cyfr części bazowej.
    return pesel + str(sum(int(znak) for znak in pesel))[-1]


if __name__ == "__main__":
    rok = 2002
    miesiac = 11
    dzien = 3
    nr = 34
    plec_facet = True

    pesel_piechota = generuj_pesel_na_piechote(rok, miesiac, dzien, nr, plec_facet)
    pesel_skrot = generuj_pesel_skrotowo(rok, miesiac, dzien, nr, plec_facet)

    print(pesel_piechota)
    print(pesel_skrot)
