"""
Ćwiczenie:

1. Wczytać napis z konsoli
2. W podanym napisie zamienić wszystkie wystąpienia
   pierwszej litery na '%' poza pierwszą literą


   Np:
   Dla napisu 'ALABASTER'
   Wypisać:
   'AL%B%STER'

 Podpowiedzi:
  - slicing
  - .replace()
"""

if __name__ == '__main__':

    napis = input('Podaj napis:')
    pl = napis[0]
    reszta = napis[1:]
    reszta = reszta.replace(pl, '%')
    wynik = pl + reszta
    print(wynik)