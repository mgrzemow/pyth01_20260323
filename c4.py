"""
Ćwiczenie:

Napisać program, który:
 1. Wczyta z konsoli kwotę brutto i stawkę VAT
 2. Wypisze kwotę netto i kwotę VAT wg podanej stawki

 Podpowiedzi:
 - input() zwraca zawsze obiekt str (napis) - konieczna jest konwersja do typów liczbowych

 Rozszerzenia ćwiczenia:
 - wczytać z konsoli i zamienić na liczbę w jednej linii
"""

def wylicz_netto(brutto, stawka):
    netto = round(brutto / (1 + stawka / 100), 2)
    vat = round(brutto - netto, 2)
    return netto, vat

if __name__ == '__main__':
    brutto = input('Podaj kwotę brutto: ')
    stawka = input('Podaj stawkę VAT: ')
    brutto = float(brutto)
    stawka = float(stawka)

    netto, vat = wylicz_netto(brutto, stawka)

    print('Brutto: ', brutto)
    print('Netto: ', netto)
    print('VAT: ', vat)
