# pusty słownik
if __name__ == "__main__":
    pass

import pprint

d = dict()
d = {}
# ywpełniony słownik
d = {'ala': 45,
     'tomek': 33,
     'zosia': 45,
     'karol': 35,
     }
# wyciąganie wartości po kluczu:
print(d['ala'])
print(d['tomek'])
# sprawdzanie - po kluczu
print(45 in d)
print('ala' in d)
# iterowanie:
for klucz in d:
    print(klucz, d[klucz])
# dodawanie do slownika -  uwaga od wersji 3.4 słowniki gwarantują zachowanie kolejności
# przed 3.4: collections.OrderedDict

d['oskar'] = 66
print(d)
# nadpisywanie
d['oskar'] = 56

d['włodekk'] = 34
print(d)
d['włodek'] = 34
print(d)
del (d['włodekk'])
print(d)

{
    'ala': [11, 22, 33]
}

{
    (1, 2): 'aa'
}

x = 'mama mama tata mama tata ja'
{
    'mama': 3,
    'tata': 2,
    'ja': 1,
}

d = {}
for slowo in x.split():
    # jak pierwszy raz
    if slowo not in d:
        d[slowo] = 1
    # kolejne razy
    else:
        d[slowo] = d[slowo] + 1
print(d)

d = {}
for slowo in x.split():
    d[slowo] = d.get(slowo, 0) + 1

print(d)

# defaultdict - potęga !!!
import collections


def zwroc_zero():
    return 0


d = collections.defaultdict(zwroc_zero)
for slowo in x.split():
    d[slowo] += 1
print(d)

d = collections.defaultdict(int)
for slowo in x.split():
    d[slowo] += 1

print(d)

# dla typów niemutowalnych - kolekcji
x = 'ala alicja alina beata bartek'
{
    'a': ['ala', 'alicja', 'alina'],
    'b': ['beata', 'bartek'],
}

d = {}
for slowo in x.split():
    pl = slowo[0]
    if pl not in d:
        d[pl] = []
    d[pl].append(slowo)

# get - niezbyt ładne
d = {}
for slowo in x.split():
    pl = slowo[0]
    lista = d.get(pl, [])
    lista.append(slowo)
    d[pl] = lista

# defaultdict
d = collections.defaultdict(list)
for slowo in x.split():
    pl = slowo[0]
    d[pl].append(slowo)

# skrótowe iterowanie po słowniku:
d = {'ala': 45,
     'tomek': 33,
     'zosia': 45,
     'karol': 35,
     }
for klucz, w in d.items():
     print(klucz, w)
