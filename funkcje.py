# def nazwa_funkcji(parametry):
#     kod
#     return wynik

def dodaj(x, y):
    wynik = x + y
    return wynik


# print(dodaj(1, 2))
# print(dodaj('ala', ' ma kota'))

# funkcja bez return zwraca None
def tylko_wypisz():
    print('alamakota')


# print(dodaj('ala', 1))
# w = tylko_wypisz()
# print(w)

# ciekawostka
def f1(x, y):
    print('f1', x, y)


# nie ma przeciążania (overloading), druga definicja nadpisała pierwszą
def f1(x):
    print('f1', x)


# f1(2, 3)

def f1(x, y):
    print(f'{x=}, {y=}')


# f1(1, 2)

def f2(x, y, a=11, b=22):
    print(f'{x=}, {y=}')
    print(f'{a=}, {b=}')


# f2(1, 2, b=4)

def f3(x, y, *args):
    print(f'{x=}, {y=}')
    print(f'{args=}')


# f3(1, 2, 3, 4, 5, 6, 7, 8, 9)

def f4(x, y, *args, a=11, b=22):
    print(f'{x=}, {y=}')
    print(f'{args=}')
    print(f'{a=}, {b=}')


# f4(1, 2, 3, 4, 5, 6, 7, b=999)

def f5(x, y, *args, a=11, b=22, **kwargs):
    print(f'{x=}, {y=}')
    print(f'{args=}')
    print(f'{a=}, {b=}')
    print(f'{kwargs=}')


# f5(1, 2, 3, 4, 5, 6, 7, b=999, c=111, d=222, e=333, f=444)

d = {
    'sep': ' - ',
    'end': '\n --- END ---\n'
}
# print(1, 2, 3, 4, **d)

x = (1, 2, 3, 4, 5)


# print(x)

# print(1,2,3,4,5)
# print(*x)

# jak zabronić przekazywania keyword parameters za pomocą kolejności
def f6(x, y, *, a=11, b=22):
    print(f'{x=}, {y=}')
    print(f'{a=}, {b=}')


# f6(1, 2, 3)
# f6(1, 2)

# required keyword only parameters
# parametry a i b są obowiązkowe i muszą być podane po nazwie
def f7(x, y, *, a, b):
    print(f'{x=}, {y=}')
    print(f'{a=}, {b=}')


# f7(1, 2, a=111, b=222)


# uwaga - wartośc domyślna inicjuje się w momencioe definiowania funkcji!!!!
def f8(i, x=[]):
    x.append(i)
    print(x)


# f8(1)
# f8(2)
# f8(3)
# f8(4)

# uwaga - należy używać innej wartości i inicjować w kodzie
def f8(i, x=None):
    if x is None:
        x = []
    x.append(i)
    print(x)


# f8(1)
# f8(2)
# f8(3)
# f8(4)

x = 99


def f9():
    x = 77
    return x


x = f9()
# print(x)


zmienna = 99


def f10():
    print(zmienna)


# f10()

# Local
# Enclosing
# Global
# Built-In

# __name__ = 'global name'


def f11():
    # __name__ = 'enclosing name'

    def f11_1():
        # __name__ = 'local name'
        print(__name__)

    f11_1()


# f11()

# Type hinting - czyli podpowiadanie typów
# fajny opis tu:
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
# Docstrings - czyli dokumentacja w kodzie
def f12(p1: float, p2: float, p3: float, x: float) -> float:
    """
    Wylicza wielomian drugiego stopnia

    Dalszy opis, lorem ipsum...
    """
    print(p1, p2, p3, x)
    return p1 * x ** 2 + p2 * x + p3

w = f12(1, 2, 3, 4)
print(w)
