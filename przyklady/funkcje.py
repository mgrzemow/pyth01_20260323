# Ogolny szablon definicji funkcji:
# def nazwa_funkcji(parametry):
#     kod
#     return wynik
if __name__ == "__main__":
    pass


# Prosta funkcja: bierze 2 argumenty i zwraca wynik.
def dodaj(x, y):
    wynik = x + y
    return wynik


# print(dodaj(1, 2))
# print(dodaj("ala", " ma kota"))  # Operator + dziala tez dla napisow.


# Funkcja bez return zwraca domyslnie None.
def tylko_wypisz():
    print("alamakota")


# print(dodaj("ala", 1))  # TypeError: niezgodne typy dla operatora +
# w = tylko_wypisz()
# print(w)  # None


# W Pythonie nie ma klasycznego overloadingu po liczbie argumentow.
# Kolejne definicje o tej samej nazwie nadpisuja poprzednie.
def f1(x, y):
    print("f1", x, y)


def f1(x):
    print("f1", x)


def f1(x, y):
    print(f"{x=}, {y=}")


# f1(1, 2)  # Dziala ostatnia definicja f1.


# Argumenty z wartosciami domyslnymi (a i b).
def f2(x, y, a=11, b=22):
    print(f"{x=}, {y=}")
    print(f"{a=}, {b=}")


# f2(1, 2, b=4)


# *args zbiera dodatkowe argumenty pozycyjne do krotki.
def f3(x, y, *args):
    print(f"{x=}, {y=}")
    print(f"{args=}")


# f3(1, 2, 3, 4, 5, 6, 7, 8, 9)


# Po *args parametry a i b sa keyword-only.
def f4(x, y, *args, a=11, b=22):
    print(f"{x=}, {y=}")
    print(f"{args=}")
    print(f"{a=}, {b=}")


# f4(1, 2, 3, 4, 5, 6, 7, b=999)


# **kwargs zbiera dowolne nazwane argumenty do slownika.
def f5(x, y, *args, a=11, b=22, **kwargs):
    print(f"{x=}, {y=}")
    print(f"{args=}")
    print(f"{a=}, {b=}")
    print(f"{kwargs=}")


# f5(1, 2, 3, 4, 5, 6, 7, b=999, c=111, d=222, e=333, f=444)


d = {"sep": " - ", "end": "\n --- END ---\n"}
# Operator ** rozpakowuje slownik do argumentow nazwanych.
# print(1, 2, 3, 4, **d)


x = (1, 2, 3, 4, 5)
# Operator * rozpakowuje sekwencje do argumentow pozycyjnych.
# print(*x)


# Sam * w sygnaturze rozdziela argumenty pozycyjne i keyword-only.
def f6(x, y, *, a=11, b=22):
    print(f"{x=}, {y=}")
    print(f"{a=}, {b=}")


# f6(1, 2, 3)  # blad: a i b nie moga byc podane pozycyjnie
# f6(1, 2)


# a i b sa tu wymaganymi argumentami keyword-only (bez wartosci domyslnych).
def f7(x, y, *, a, b):
    print(f"{x=}, {y=}")
    print(f"{a=}, {b=}")


# f7(1, 2, a=111, b=222)


# Pulapka: domyslna lista tworzy sie raz, przy definicji funkcji.
def f8(i, x=[]):
    x.append(i)
    print(x)


# f8(1); f8(2); f8(3); f8(4)  # lista narasta miedzy wywolaniami


# Poprawny wzorzec: None jako wartosc domyslna i inicjalizacja w srodku.
def f8(i, x=None):
    if x is None:
        x = []
    x.append(i)
    print(x)


# f8(1); f8(2); f8(3); f8(4)  # kazde wywolanie dostaje nowa liste


x = 99


# Zmienna lokalna o tej samej nazwie nie modyfikuje globalnej.
def f9():
    x = 77
    return x


x = f9()
# print(x)


zmienna = 99


# Odczyt zmiennej globalnej z funkcji.
def f10():
    print(zmienna)


# f10()


# LEGB: Local, Enclosing, Global, Built-in.
def f11():
    def f11_1():
        # __name__ jest tu szukane wedlug LEGB.
        print(__name__)

    f11_1()


# f11()


# Type hinting podpowiada oczekiwane typy (nie wymusza ich w runtime).
# Docstring opisuje przeznaczenie funkcji i sluzy jako dokumentacja.
def f12(p1: float, p2: float, p3: float, x: float) -> float:
    """
    Wylicza wielomian drugiego stopnia.
    """
    print(p1, p2, p3, x)
    return p1 * x**2 + p2 * x + p3


w = f12(1, 2, 3, 4)
print(w)
