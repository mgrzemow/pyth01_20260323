"""
Ćwiczenie:

Napisać program, który:

1. Wczytuje z pliku tekstowego dane:
 - nazwa towaru
 - ilość towaru
 - jednostka miary
 - cena

Plik jest w formacie:
Banany 2.4 kg 3.5
Kiwi 3 szt 2.3
Piwo 4 szt 2.4
Kiwi 3 szt 2.3
Kiwi 4.5 kg 11.5

2. Po każdej wczytanej linii wypisuje na ekran linię paragonu w formie:
Pietruszka  2.0 kg x 4.60     9.20

3. Na koniec wypisuje podsumowanie:
----------------------------------
SUMA:                        19.70

Kolumny mają mieć szerokości:
nazwa - 12 znaków,
ilość - 2 znaki przed kropką i 2 po
jednostka miary - 4 znaki
cena - 3 znaki przed kropką i 2 po
wartość pozycji - 5 znaków przed kropką i 2 po
SUMA - 7 znaków przed kropką i 2 po

Podpowiedzi:
 - formatowanie f-stringow
 - czytanie z pliku - patrz ściąga

Rozszerzenie ćwiczenia:
 - zebrać paragon w wieloliniowym stringu i wypidać na sam koniec
"""
if __name__ == '__main__':
    with open('towary.txt', 'rt', encoding='utf-8') as f:
        suma = 0
        for linia in f:
            # podzielić linię na kawałki
            podzielona_linia = linia.split()
            # przypisać do zmiennych
            # skonwertować
            towar, ilosc, jm, cena = podzielona_linia
            ilosc = float(ilosc)
            cena = float(cena)
            # wyliczyć wartość pozycji
            wartosc = round(ilosc * cena, 2)
            # zwiększyć sumę
            suma = round(suma + wartosc, 2)
            # wypisac linię paragonu
            print(f'{towar:12} {ilosc:5.2f} {jm:4} x {cena:6.2f} {wartosc:8.2f}')
        print('-' * 41)
        print(f'SUMA: {suma:35.2f}')
