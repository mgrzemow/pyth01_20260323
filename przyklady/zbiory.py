# zbiory piszemy w {}
if __name__ == "__main__":
    pass

s = {'Ala', "Ola", 'Karol', 'Monika', 'Adam', 'Ola'}
print(s)
print(type(s))
# zbiory nie gwarantują żadnej kolejności elementów
s.add('Piotr')
print(s)
# dodanie do zbioru elementu ktory już tam jest nic nie zmienia
s.add('Ola')
print(s)
# jak sprawdzić czy coś jest w zbiorze:
print('Ola' in s)
# podobnie jak liosty zbiory są heterogenicznie
s.add(12)
print(s)
# jak przeiterować - pamiętamy że kolejność jest nieustalona
for e in s:
    print(e)

# co to znaczy taki ssam element
s.add(12.0)
print(s)
# 12.0 nie dodało się do zbioru
# ponieważ 12 == 12.0 - decyduje równość ==

# w praktyce:
x = [1, 2, 3, 2, 3, 2, 3, 4, 3, 2, 3, 4, 6, 7, 6, 7, 6, 7, 8, 7, 8, 9, 8, 9]
# jak dostać unikalne elementy z listy:
print(set(x))

# uwaga - kolejność jest nieznana
lista_bez_duplikatow = list(set(x))

# jeżeli chcę zachować kolejność - czary mary:
lista_bez_duplikatow_z_kolejnoscia = list({i: None for i in x}.keys())
print(lista_bez_duplikatow_z_kolejnoscia)

# jak stworzyć pusty zbiór:
s = set()

# fajne operacje na zbiorach
abcdef = set('abcdef')
defghi = set('defghi')
print(abcdef)
print(defghi)
print(abcdef & defghi)
print(abcdef | defghi)
print(abcdef ^ defghi)
print(abcdef - defghi)
