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

{
    'gmail.com': {'ala@gmail.com', 'ela@gmail.com'},
    'o2.pl': {'tomek@o2.pl'}
}

if __name__ == '__main__':
    zbior_maili = set()
    with open('emails.txt', 'r', encoding='utf8') as f:
        for linia in f:
            # wyczyścić adres
            linia = linia.strip()
            # sprawdzić czy poprawny
            if '@' in linia:
                # dodać do zbioru
                zbior_maili.add(linia.lower())

    print(zbior_maili)
    # dla każdego adresu ze zbioru:
    for email in zbior_maili:
        # otowrzyć plik domena.txt w trybie at
        domena = email.split('@')[1]

        with open(domena + '.txt', 'at', encoding='utf8') as f:
            # dopisać adres
            f.write(email + '\n')

