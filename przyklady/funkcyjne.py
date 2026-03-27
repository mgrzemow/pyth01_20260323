x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

y = []
for i in x:
    if i % 2 == 0:
        y.append(i ** 2)

y = [i ** 2
     for i in x
     if i % 2 == 0]

print(y)
x = ['Jan', '', 'Ala', 'Jola']
# czy wszystkie niepuste imiona kończą się na a
y = [imie[-1] == 'a' for imie in x if imie]
print(y)
print(all(y))
print(any(y))

# do doczytania - na temat wyrażeń generatorowych
print(all(imie[-1] == 'a' for imie in x if imie))
print(any(imie[-1] == 'a' for imie in x if imie))

# lista długości linii
with open('c19.py', 'rt', encoding='utf-8') as f:
    x = [len(linia) for linia in f]
    print(x)

# można też w ten sposób budować słowniki
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# słownik gdzie kluczami są liczby z x a wartściami ich kwadraty
d = {i: i ** 2 for i in x}
print(d)


# jeżeli potrzebuję użyć parametrów do generowania wartości na bieżąco:
def prosty_generator(n, m):
    while n <= m:
        yield n
        n += 1


for i in prosty_generator(3, 17):
    print(i)

# poza możliwością pisania własnych generatorów, python ma mnóstwo gotowych

# generator liczb w jakimś zakresie
for i in range(10):
    print(i)

{}.items()
{}.keys()
{}.values()

print(zip([1, 2, 3], [11, 22, 33]))
for i in zip([1, 2, 3], [11, 22, 33]):
    print(i)

# warto zajrzeć
import itertools


# funkcja jako first class citizen

def wykonaj_n_razy(f, n, *args, **kwargs):
    for _ in range(n):
        f(*args, **kwargs)

wykonaj_n_razy(print, 7, 'ala', 'ola', 'ula', sep=' - ', end='\n ---- End ----\n')