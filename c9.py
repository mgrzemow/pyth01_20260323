"""
Ćwiczenie:

 1. Wczytać z konsoli:
  - nazwę tagu XML/HTML,
  - nazwę atrybutu,
  - wartość tagu
  - wartość atrybutu
 2. Skonstruować na tej podstawie kawałek XMLa/HTMLa.

 Np. dla danych a, href, onet, http://onet.pl
 Wypisać: <a href = "http://onet.pl">onet</a>

 Podpowiedzi:
  - f-strings
"""

if __name__ == '__main__':
    tag = input('Podaj tag: ')
    wynik = f'<a href = "http://onet.pl">onet</a>'