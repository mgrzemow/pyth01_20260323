with open('c10.py', mode='rt', encoding='utf-8') as f:
    # tryb odczytu w całości
    tekst = f.read()

print(tekst)

# czytanie linia po linii
with open('c10.py', mode='rt', encoding='utf-8') as f:
    for linia in f:
        print(linia.rstrip())

# zapis - menedżer kontekstu
with open('tmp.txt', 'wt', encoding='utf-8') as f:
    f.write('linia1\n')
    f.write('linia2\n')
    f.write('linia3\n')
    # pomimo wyjątku, dzięki with mamy gwarancję że plik się zamknie
    x = 9 / 0
    f.write('linia4\n')
