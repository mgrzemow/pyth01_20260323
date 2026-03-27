"""
Ćwiczenie:

Napisać program, który:

1. Wczyta napis z konsoli:
2. Policzy ilość liter i ilość cyfr w napisie.

Podpowiedzi:
 - pętla for dla napisów iteruje po znakach
 - '8'.isdigit() == True
 - 'a'.isalpha() == True
"""
if __name__ == '__main__':
    napis = input('Podaj napis: ')
    ile_liter = 0
    ile_cyfr = 0
    for znak in napis:
        if znak.isdigit():
            ile_cyfr += 1
        if znak.isalpha():
            ile_liter += 1
    print(f'W napisie "{napis}" jest liter: {ile_liter}, cyfr: {ile_cyfr}')
