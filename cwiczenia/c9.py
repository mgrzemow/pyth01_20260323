"""
Ćwiczenie:

1. Wczytać z konsoli:
- nazwę tagu XML/HTML,
- nazwę atrybutu,
- wartość tagu,
- wartość atrybutu.
2. Skonstruować na tej podstawie kawałek XML/HTML.
"""


def generuj_tag(tag: str, atrybut: str, wartosc_tagu: str, wartosc_atrybutu: str) -> str:
    """Generuje pojedynczy tag HTML/XML z jednym atrybutem.

    Args:
        tag: Nazwa tagu, np. ``"a"``.
        atrybut: Nazwa atrybutu, np. ``"href"``.
        wartosc_tagu: Treść pomiędzy tagiem otwierającym i zamykającym.
        wartosc_atrybutu: Wartość atrybutu.

    Returns:
        Gotowy fragment HTML/XML, np. ``<a href="http://onet.pl">onet</a>``.
    """
    return f'<{tag} {atrybut} = "{wartosc_atrybutu}">{wartosc_tagu}</{tag}>'


if __name__ == "__main__":
    tag = input("Podaj tag: ")
    tag_w = input("Podaj wartość tagu: ")
    atr = input("Podaj atrybut: ")
    atr_w = input("Podaj wartość atrybutu: ")
    wynik = generuj_tag(tag, atr, tag_w, atr_w)
    print(wynik)
