"""
Ćwiczenie:

 1. Wczytać z konsoli nr roku
 2. Sprawdzić czy rok jest przestępny.
 3. Wypisać odpowiedni komunikat

 Podpowiedzi:
    Rok jest przestępny jeżeli spełniony jest chociaż jeden z dwóch warunków:
    - dzieli się przez 400
    lub
    - dzieli się przez 4 i nie dzieli się przez 100

 Rozszerzenia ćwiczenia:
  - nie użyć w kodzie ani jednego dwukropka ':'
  - sprawdzić czy użytkownik podał całkowitą liczbę dodatnią > 0
"""
if __name__ == '__main__':

    rok = int(input('Podaj rok: '))
    if rok <= 0:
        # jak spowodowac powstanię błędu
        raise ValueError('Nr roku < 0')
    if rok % 400 == 0 or rok % 4 == 0 and rok % 100 != 0:
        print('przestepny')
    else:
        print('nie przestepny')

    d_400 = rok % 400 == 0
    d_4 = rok % 4 == 0
    d_100 = rok % 100 == 0
    print(f'/4: {d_4}, /100: {d_100}, /400: {d_400}')    
    if d_400 or d_4 and not d_100:
        print('przestepny')
    else:
        print('nie przestepny')

    d_400 = rok % 400 == 0
    d_4 = rok % 4 == 0
    d_100 = rok % 100 == 0

    komunikat = 'przestepny' if d_400 or d_4 and not d_100 else 'nie przestepny'
    print(komunikat)
    
