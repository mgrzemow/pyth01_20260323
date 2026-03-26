import konfiguracja


def wczytaj_towary(nazwa_pliku: str = konfiguracja.PLIK_TOWARY) -> dict[str, tuple[float, str, float]]:
    """
    Wczytuje towary z pliku tekstowego.

    Dalszy opis...

    Args:
        nazwa_pliku: plik wejściowy w formacie....

    Returns:
        Opis struktury zwracanej...

    """
    slownik_rekordow = {}
    with open(nazwa_pliku, 'rt', encoding='utf-8') as f:
        for linia in f:
            towar, ilosc, jm, cena = linia.split()
            ilosc, cena = float(ilosc), float(cena)
            # jeżeli już było to sumuję ilości
            if towar in slownik_rekordow:
                slownik_rekordow[towar][0] += ilosc
            # a jak nie było to po prostu dodaję
            else:
                slownik_rekordow[towar] = [ilosc, jm, cena]
    return slownik_rekordow


def generuj_paragon(slownik_rekordow: dict[str, tuple[float, str, float]]) -> str:
    """
    Generuje paragon ze słownika wejściowego...

    Lorem ipsum...

    Args:
        slownik_rekordow:

    Returns:

    """
    suma = 0
    paragon = ''
    for towar, (ilosc, jm, cena) in slownik_rekordow.items():
        # wyliczyć wartość pozycji
        wartosc = round(ilosc * cena, 2)
        # zwiększyć sumę
        suma = round(suma + wartosc, 2)
        # wypisac linię paragonu
        paragon += f'{towar:12} {ilosc:5.2f} {jm:4} x {cena:6.2f} {wartosc:8.2f}\n'
    paragon += '-' * 41 + '\n'
    paragon += f'SUMA: {suma:35.2f}\n'
    return paragon
