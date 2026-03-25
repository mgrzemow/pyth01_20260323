'''
Ćwiczenie:

Z pliku tekstowego w formacie:
Jan 888999777
Ola 333444555
Paweł 111222333
Ula 333444000

wczytac słownik w postaci:
{'Jan': '888999777',
 ...
}

Następnie napisać pętlę w której użytkownik będzie podawał imiona
a program będzie podawał numery telefonów, lub komunikat, że nie ma takiego numeru
w książce telefonicznej. Warunkiem wyjścia z pętli będzie podanie 'koniec' zamiast imienia.

Podpowiedzi:
 - cheatsheets

Rozszerzenia ćwiczenia:
 - jeżeli numeru nie ma w książce, to użytkownik może go dodać

'''

if __name__ == '__main__':
    ksiazka_tel = {}
    with open('telefony.txt', 'rt', encoding='utf8') as f:
        for linia in f:
            imie, tel = linia.split()
            ksiazka_tel[imie.lower()] = tel
    while (imie := input('Podaj imie: ').lower()) != 'koniec':
        if imie in ksiazka_tel:
            print(f'{imie.capitalize()}: {ksiazka_tel[imie]}.')
        else:
            if input(f'Nie mam nr do {imie.capitalize()}, czy chcesz dodać [t]?').lower() == 't':
                tel = input(f'Podaj nr do {imie.capitalize()}: ')
                ksiazka_tel[imie] = tel
                with open('telefony.txt', 'at', encoding='utf8') as f:
                    f.write(f'{imie.capitalize()} {tel}\n')
