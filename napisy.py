x = 'mama'
y = "mama"
print(x == y)

x = "<a href=\"http://onet.pl\">onet.pl</a>"
y = '<a href="http://onet.pl">onet.pl</a>'
print(x == y)

x = 'Tom\'s sick'
y = "Tom's sick"
print(x == y)

x = '\nlinia1\nlinia2\nlinia3\n'
y = '''
linia1
linia2
linia3
'''
print(x == y)

x = '\\d\\d'
y = r'\d\d'
print(x == y)

# uwaga na byte sstringi - to nie są napisy
# to jest ciąg bajtów
x = b'abc\xAA'
print(type(x))

# proste indeksowanie
x = 'mama'
print(x[1])

# sklejanie
print('ala' + ' ma' + ' kota')

# uwaga - można stringi mnożyć
print('abc' * 4)

# uwaga pułapka
# mam liczbę, ale zapisaną jako napis
x = '12'
print(float(x * 4) / 5)

# konstrukcja stringów
imie = 'Jan'
wiek = 44
waga = 88
wzrost = 178
# takie sklejanie jest niewydajne, i bardzo męczące
x = imie + ' ma ' + str(wiek) + ' lat, wazy ' + str(waga) + ' kg i ma ' + str(wzrost) + 'cm wzrostu.'
# a można prościej
y = f'{imie} ma {wiek} lat, wazy {waga} kg i ma {wzrost}cm wzrostu.'
print(y)

# stringi są niemutowalne
x = 'mama'
print(id(x))
x = x.upper()
print(id(x))
print(x)

# formatowanie pól w fstrings
# konstrukcja stringów
imie = 'Jan\n'
wiek = 44.23143234
waga = 88.123123
wzrost = 178.213123312
y = f'{imie.strip():^12} ma {wiek:8.0f} lat, wazy {waga:.1f} kg i ma {wzrost:.2f}cm wzrostu.'
print(y)

# napis jako wzorzec
szablon = '{:^12} ma {:8.0f} lat, wazy {:.1f} kg i ma {:.2f}cm wzrostu.'
# wypełnienie szablonu danymi
wynik = szablon.format(imie.strip(), wiek, waga, wzrost)
print(wynik)
# import requests
# szablon_url = 'https://api.nbp.pl/api/exchangerates/rates/a/{}/?format=json'
# waluta = 'usd'
# url = szablon_url.format(waluta)
# r = requests.get(url)
# print(r.json()['rates'][0]['mid'])

# zakresy, slicing, wycinanki
x = 'abcdefgh'

print(x[0])
print(x[7])
print(x[-1])
print(x[-8])

print(x[1:4])
print(x[1:-1])
# pierwsze 2:
print(x[:2])
# ostatnie 3:
print(x[-3:])
# wszystkie poza pierwszymi 3:
print(x[3:])
# wszystkie poza ostatnimi 2:
print(x[:-2])
# print(x[:do])
# print(x[od:])

# 3 parametr to krok
print(x[1:-1:2])

# odwrócenie kolejności
print(x[::-1])

x = 'mama'
x.upper()

# metody informacyjne
x = 'mama'
# metody .is_costam
print(x.islower())
print(x.isupper())
print(x.startswith('ma'))
print(x.endswith('ma'))
print(x.count('ma'))
print(x.find('ma'))
# Jak sprawdzić czy coś jest w czymś w pythonie - in
# BARDZO WARTO ZAPAMIĘTAĆ
print('ma' in x)

# zarządzanie wielkością zanaków
x = 'ala ma kota'
print(x.upper())
print(x.lower())
print(x.title())
print(x.capitalize())

print(x.zfill(13))

#czyszczenie
x = 'Jan\n'
print(x.strip())
x = '\t  \n ala  ma \t kota  \n\t'
print(x.strip())
print(x.lstrip())
print(x.rstrip())

x = '10 33 55END'
print(x.removesuffix('END'))
x = '10 33 55'
print(x.removesuffix('END'))

# podział i łączenie
x = 'ala ma kota'
print(x.split(' '))
x = 'ala:ma:kota'
print(x.split(':'))

x = 'ala  ma\tkota'
print(x.split(' '))
print(x.split())

x = '\t \t ala \t ma\t\nkota   \n'
print(x.split(' '))
print(x.split())

x = '\t \t ala, \t ma\t\nkota   \n'
print(x.replace(',', ' ').split())

x = ['ala', 'ma', 'kota']
print(':'.join(x))
