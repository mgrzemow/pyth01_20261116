# def nazwa_funkcji(parametry):
#     kod funkcji
#     return wartosc_zwracana

def dodaj(x, y):
    print('Dodaję', x, y)
    return x + y


# co jak nie ma returna

def nie_ma_return():
    print('Nie ma return')


# w = nie_ma_return()
# print(w)

# wydaje mi się że sort będzie zwracaćc posortowaną kopię
x = [1, 2, 6, 3, 8, 7]
y = x.sort()


# a jednak nie
# print(y)

# a co jeżeli zdefiniuję sobie 2 funkcje o
# różnych parametrach
# jedna zastępuje drugą
# NIE MA OVERLOADINGU !!!
def f1(x, y):
    print(f'f1({x=}, {y=})')


def f1(x):
    print(f'f1({x=})')


# f1(1, 4)

# jak ktoś się bardzo uprze to:
# functools.singledispatch
# google: python multimethod
# ale po co?

# bardzo rozbudowany mechanizm przekazywania parametrów
# do funkcji

# tak najczęściej !!!
def f2(x, y, a=11, b=22):
    print(f'{x=}, {y=}')
    print(f'{a=}, {b=}')


# f2(1, 2, a=111)
# f2(1, 2, 111)
# f2(1, 2, b=222)

def f3(x, y, *args, a=11, b=22):
    print(f'{x=}, {y=}')
    print(f'{args=}')
    print(f'{a=}, {b=}')


# f3(1, 2)
# f3(1, 2, 3, 4, 5, 6, 7, 8)
# f3(1, 2, 3, 4, 5, 6, 7, 8, b=222)

def f4(x, y, *args, a=11, b=22, **kwargs):
    print(f'{x=}, {y=}')
    print(f'{args=}')
    print(f'{a=}, {b=}')
    print(f'{kwargs=}')


# f4(1, 2, 3, 4, 5, 6, 7, 8, b=222, c=444, e=999)

# nowości
# jak zabronić przekazywania parametrów keyword po kolei bez nazw
def f5(x, y, *, a=11, b=22):
    print(f'{x=}, {y=}')
    print(f'{a=}, {b=}')


# przez * nie uda się tak:
# f5(1, 2, 3)
# a uda się tak:
# f5(1, 2, a=3)

# required keyword arguments
# czyli parametry wywoływane obowiązkowo po nazwach ale bez
# wartości domyślnych
def f6(x, y, *, a, b):
    print(f'{x=}, {y=}')
    print(f'{a=}, {b=}')


# f6(1, 2, a=3, b=6)

x = 9


def f7():
    x = 99
    return x


# x = f7()


x = []


def f8(p1):
    p1.append(1)
    p1.append(2)
    p1.append(3)


# f8(x)
# print(x)

# Local
# Enclosing
# GLobal
# Built-In

# __name__ = 'global name'
def f9():
    # __name__ = 'enclosing name'
    def f9_1():
        # __name__ = 'local name'
        print(__name__)

    f9_1()


# f9()

# nie należy używać obiektór typów mutowalnych jako
# wartości domyślnych
def f10(i, x=[]):
    x.append(i)
    print(x)


# f10(1)
# f10(2)
# f10(3)

def f10(i, x=None):
    if x is None:
        x = []
    x.append(i)
    print(x)


# f10(1)
# f10(2)
# f10(3)

def f11():
    x = 99

    def f11_1():
        print(x)

    return f11_1


# f = f11()
# f()
# print(f.__closure__[0].cell_contents)

# funkcja która przyjmie dowolne parametry wejściowe
# takiej funkcji fajnie się używa
# np jako zwiadowca
def f12(*args, **kwargs):
    print(f'{args=}')
    print(f'{kwargs=}')


# f12()
# f12(1, 2, 3, 2, 2, 2, 2, 3, aa=11, bb=98, cc=55)

# def f13(*args, **kwargs):
#     print(f'{args=}')
#     print(f'{kwargs=}')
#     return 42

def f13(slowo):
    return slowo[::-1]


x = ['az', 'zebra', 'grog']
x.sort(key=f13)
print(x)

# jak się uczyć type hintingu:
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
