"""
Ćwiczenie:

1. Wczytujemy adresy email z podanego pliku tekstowego emails.txt
2. Zapisujemy adresy email BEZ POWTÓRZEŃ do plików o nazwie pochodzącej od nazwy domeny,
   wg schematu:
   wszystkie adresy @gmail.com mają zostać zapisane w pliku gmail.com.txt
   dla dowolnej domeny występującej w adresach w pliku wejściowym

Podpowiedzi:
 - tryb append zapisu do pliku 'at'
 - nazwę domeny można wyciąć z adresu znajdując znak @
 - dla zapewnienia unikalności - użyjemy zbioru do wczytanych adresów
"""
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

