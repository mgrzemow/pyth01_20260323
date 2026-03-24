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

