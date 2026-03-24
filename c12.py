"""
Ćwiczenie:

Napisać program, który:

1. Będzie sprawdzał w pętli while czy istnieje plik 'lock.txt'
2. Tak długo jak plik istnieje będzie:
 - wypisywał komunikat: 'Plik lock.txt istnieje, usuń go aby kontynuować. Masz N s'
 - zmniejszał ilość pozostałych sekund o 1 (zaczynamy odliczanie od powiedzmy 15.
3. Po usunięciu pliku 'lock.txt' w wyznaczonym czasie wypisze 'No, nareszcie! Musiałem cię poganiać {n} razy'
4. Jeżeli pozostały czas dobiegnie końca, wypisze 'Za późno, żegnam'

Podpowiedzi:
 - import os.path
   os.path.isfile()
 - import time
   time.sleep()
"""
import os.path
import time

if __name__ == '__main__':

    # n = 15
    # i = n
    # while True:
    #     if not os.path.isfile('lock.txt'):
    #         print(f'No, nareszcie! Musiałem cię poganiać {n - i} razy')
    #         break
    #     if i <= 0:
    #         print('Za późno, żegnam.')
    #         break
    #     print(f'Plik lock.txt istnieje, usuń go aby kontynuować. Masz {i} s')
    #     time.sleep(1)
    #     i -= 1

    # dziwactwo pythonowe - można dopisać else do pętli

    n = 15
    i = n
    while i > 0:
        if not os.path.isfile('lock.txt'):
            print(f'No, nareszcie! Musiałem cię poganiać {n - i} razy')
            break
        print(f'Plik lock.txt istnieje, usuń go aby kontynuować. Masz {i} s')
        time.sleep(1)
        i -= 1
    # else do pętli wykonuje się jeżeli NIE wyszedłem z pętli przez break
    else:
        print('Za późno, żegnam.')
