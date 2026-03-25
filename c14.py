"""
Ćwiczenie:

Napisać program, który:

1. Z pliku tekstowego wcztać imiona do listy:
    ['Ala', 'Ela']

2. Dla każdego elementu listy wypisze komunikat:
  - dla imion kończących się na a: 'Cześć Imie, witam panią.'
  - dla imion nie kończących się na a: 'Cześć Imie, witam pana.'

Podpowiedzi:
 - [].append()

Rozszerzenia ćwiczenia:
"""
from pprint import pprint

if __name__ == '__main__':
    lista_imion = []
    with open('imiona.txt', "rt", encoding='utf8') as f:
        for linia in f:
            linia = linia.rstrip().capitalize()
            if linia:
                # print(repr(linia))
                lista_imion.append(linia)
    # pprint(lista_imion)
    for imie in lista_imion:
        suffix = 'panią.' if imie.endswith('a') else 'pana.'
        print(f'Cześć {imie}, witam {suffix}')
