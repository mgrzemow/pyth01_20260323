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