# pętla while
# while warunek:
#     kod

# i = 5
# while i > 0:
#     print(i)
#     i -= 1

# duplikacja kodu
# imie = input('Podaj imię: ')
# while imie !='koniec':
#     print(f'Cześć {imie}.')
#     imie = input('Podaj swoje imię: ')

# w początkowa - uwaga czasem trudno wymyśleć bezpieczną w poczatkowa
# imie = None
# while imie !='koniec':
#     if imie is not None:
#         print(f'Cześć {imie}.')
#     imie = input('Podaj swoje imię: ')

# wyjście przez break - proste i czytelne
# while True:
#     imie = input('Podaj swoje imię: ')
#     if imie == 'koniec':
#         print('Do widzenia.')
#         break
#     if imie == 'exit':
#         print('Bye bye')
#         break
#     print(f'Cześć {imie}.')

# od 3.8 operator walrus :=
while (imie := input('Podaj swoje imię: ')) != 'koniec':
    print(f'Cześć {imie}.')

r = 10
h = 10
v = (s := 3.14 * r * r) * h
print(s, v)
