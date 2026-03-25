x = [11, 22, 'mama', 12.7, True, None]
x = []
a = 11
b = 22
c = 33
x = [a, b, c]
a = 'mama'
print(x)
x = [11,
     22,
     33,
     ]
print(x[1])
print(x[1:])
print(x + [44, 55])
print(x)
x.append(44)
print(x)
x.append([55, 66])
print(x)
del (x[-1])
print(x)
x.extend([55, 66])
print(x)
x += [77, 88]
print(x)
x[0] = 5
print(x)
x.insert(0, -11)
print(x)

print(33 in x)
for element in x:
    print(element)

# lista jest wolna podczas wstawiania/usuwania na początek lub w środek
# w praktyce to się zdarzy, jeżeli potraktuuję listę jako kolejkę FIFO

# import time
# for n in [50_000, 100_000, 200_000]:
#      t1 = time.perf_counter()
#      x = []
#      for i in range(n):
#           x.insert(0, i)
#      print(f'{n}: {time.perf_counter() - t1:.2f} s.')
#
# # co zamiast listy - collections.deque
# # bardziej zaawansowane kolejki są w multiprocessing
# import collections
# for n in [50_000, 100_000, 200_000]:
#      t1 = time.perf_counter()
#      x = collections.deque()
#      for i in range(n):
#           x.insert(0, i)
#      print(f'{n}: {time.perf_counter() - t1:.2f} s.')


# krotki - tuple - niemutowalne

x = (1, 2, 3)
# del(x[0])
# x.append(4)
# x[0] = 22

# 1 elementowa krotka
x = (9,)
print(x, type(x))

# krotka jest niemutowalna ale może zzawierać mutowalne obiekty - to zazwyczaj zły pomysł
x = ([], [])
x[0].append(1)
x[0].append(2)
x[0].append(3)
print(x)

# lista/krotka jako rekord danych
x = ['Jan', 44, 189, 78, 'Otwock', True]
imie = x[0]

# lista rekordow
x = [
    ['Jan', 44, 189, 78, 'Otwock', True],
    ['Jan', 44, 189, 78, 'Otwock', True],
]

for r in x:
    imie = r[0]
    wiek = r[1]
    ...

# unpacking
r = ['Jan', 44, 189, 78, 'Otwock', True]
imie, wiek, wzrost, waga, miasto, czy_aktywne = r
print(imie, miasto)

#  unpacking działa pomiędzy listami a krotkami
r = ('Jan', 45)
imie, wiek = r

r = ('Jan', 45)
(imie, wiek) = r

r = ['Jan', 45]
imie, wiek = r

[imie, wiek] = r

# w miejscach gdzie to jest jednoznaczne składniowo - można pominąć nawiasy krotki
x = (1, 2)
x = 1, 2
print(x)

# unpacking pozwala na fajne sztuczki
x = 'Ala'
y = 'Karol'

# jak zamienić wartości
x, y = y, x

print(x, y)
# unpacking ma więcej funkcjonalności - do doczytania gorąco polecam!!!
