"""
Ćwiczenie:

1. Wczytujemy adresy email z podanego pliku tekstowego emails.txt
2. Pogrupować adresy email po domenach, jedncześnie pozbywając się duplikatów. Proponuję format:
{
'gmail.com': {'ala@gmail.com', 'ela@gmail.com'}
...
}
3. Zapisujemy adresy email do plików o nazwie pochodzącej od nazwy domeny,
   wg schematu:
   np wszystkie adresy @gmail.com mają zostać zapisane w pliku gmail.com.txt

Podpowiedzi:
 - nazwę domeny można wyciąć z adresu znajdując znak @
"""
from pprint import pprint

{
    'gmail.com': {'ala@gmail.com', 'ela@gmail.com'},
    'o2.pl': {'tomek@o2.pl'}
}

if __name__ == '__main__':
    slownik_maili = {}
    with open('emails.txt', 'r', encoding='utf8') as f:
        for linia in f:
            # wyczyścić adres
            linia = linia.strip()
            # sprawdzić czy poprawny
            if '@' in linia:
                # dodać do zbioru
                domena = linia.split('@')[1]
                if domena not in slownik_maili:
                    slownik_maili[domena] = set()
                slownik_maili[domena].add(linia.lower())

    pprint(slownik_maili)
    # dla każdego adresu ze zbioru:
    for domena, zbior_maili in slownik_maili.items():
        with open(domena + '.txt', 'wt', encoding='utf8') as f:
            # dopisać adres
            for email in zbior_maili:
                f.write(email + '\n')

