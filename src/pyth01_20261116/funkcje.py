"""
Funkcje: definiowanie, `return`, brak przeciążania, sposoby przekazywania
parametrów (`*args`, `**kwargs`, parametry tylko-nazwane), zakresy zmiennych
(LEGB), pułapka mutowalnej wartości domyślnej, domknięcia, funkcja jako
argument (`key=`).

Notatki ze szkolenia. Definicje funkcji są na poziomie modułu (można je
importować), zakomentowane wywołania przy każdej funkcji to materiał do
odkomentowania na zajęciach, a kod wykonywany jest pod
`if __name__ == '__main__'`.

Jak się uczyć type hintingu:
[mypy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
"""
from collections.abc import Callable
from typing import Any


# def nazwa_funkcji(parametry):
#     kod funkcji
#     return wartosc_zwracana

def dodaj(x: float, y: float) -> float:
    """
    Dodaje dwie liczby.

    Args:
        x: pierwszy składnik
        y: drugi składnik

    Returns:
        suma `x + y`
    """
    print('Dodaję', x, y)
    return x + y


# co jak nie ma returna

def nie_ma_return() -> None:
    """Funkcja bez `return` - wywołanie i tak zwraca wartość: `None`."""
    print('Nie ma return')


# w = nie_ma_return()
# print(w)

# wydaje mi się że sort będzie zwracaćc posortowaną kopię
# a jednak nie - konwencja: metody modyfikujące obiekt w miejscu zwracają None
# (posortowaną kopię daje funkcja sorted(x)); demo jest pod __main__ na dole

# a co jeżeli zdefiniuję sobie 2 funkcje o
# różnych parametrach
# jedna zastępuje drugą
# NIE MA OVERLOADINGU !!!
# (def to zwykłe przypisanie obiektu funkcji do nazwy - drugi def nadpisuje
# pierwszy, tak jak drugie x = ... nadpisuje pierwsze)
def f1(x: int, y: int) -> None:
    """Pierwsza wersja `f1` - zostanie nadpisana przez następną definicję."""
    print(f'f1({x=}, {y=})')


def f1(x: int) -> None:
    """Druga wersja `f1` - tylko ta istnieje po wczytaniu modułu."""
    print(f'f1({x=})')


# f1(1, 4)

# jak ktoś się bardzo uprze to:
# functools.singledispatch
# google: python multimethod
# ale po co?

# bardzo rozbudowany mechanizm przekazywania parametrów
# do funkcji

# tak najczęściej !!!
# parametry z wartością domyślną można pominąć w wywołaniu
# albo podać pozycyjnie, albo po nazwie
def f2(x: int, y: int, a: int = 11, b: int = 22) -> None:
    """Parametry wymagane (`x`, `y`) i parametry z wartościami domyślnymi (`a`, `b`)."""
    print(f'{x=}, {y=}')
    print(f'{a=}, {b=}')


# f2(1, 2, a=111)
# f2(1, 2, 111)
# f2(1, 2, b=222)

# *args zbiera nadmiarowe argumenty pozycyjne do krotki;
# wszystko po *args da się przekazać już tylko po nazwie
def f3(x: int, y: int, *args: int, a: int = 11, b: int = 22) -> None:
    """Dowolna liczba argumentów pozycyjnych (`*args`) plus parametry nazwane."""
    print(f'{x=}, {y=}')
    print(f'{args=}')
    print(f'{a=}, {b=}')


# f3(1, 2)
# f3(1, 2, 3, 4, 5, 6, 7, 8)
# f3(1, 2, 3, 4, 5, 6, 7, 8, b=222)

# **kwargs zbiera nadmiarowe argumenty nazwane do słownika
def f4(x: int, y: int, *args: int, a: int = 11, b: int = 22, **kwargs: Any) -> None:
    """Pełna sygnatura: pozycyjne, `*args`, nazwane z domyślnymi, `**kwargs`."""
    print(f'{x=}, {y=}')
    print(f'{args=}')
    print(f'{a=}, {b=}')
    print(f'{kwargs=}')


# f4(1, 2, 3, 4, 5, 6, 7, 8, b=222, c=444, e=999)

# nowości
# jak zabronić przekazywania parametrów keyword po kolei bez nazw
# goła * w sygnaturze: wszystko po niej to parametry tylko-nazwane (keyword-only)
# (analogicznie goły / oznacza parametry tylko-pozycyjne - wymaga Pythona >= 3.8)
def f5(x: int, y: int, *, a: int = 11, b: int = 22) -> None:
    """`a` i `b` można podać wyłącznie po nazwie."""
    print(f'{x=}, {y=}')
    print(f'{a=}, {b=}')


# przez * nie uda się tak:
# f5(1, 2, 3)
# a uda się tak:
# f5(1, 2, a=3)

# required keyword arguments
# czyli parametry wywoływane obowiązkowo po nazwach ale bez
# wartości domyślnych
def f6(x: int, y: int, *, a: int, b: int) -> None:
    """`a` i `b` są wymagane i można je podać wyłącznie po nazwie."""
    print(f'{x=}, {y=}')
    print(f'{a=}, {b=}')


# f6(1, 2, a=3, b=6)

x = 9


def f7() -> int:
    """
    Przypisanie wewnątrz funkcji tworzy zmienną LOKALNĄ.

    Globalne `x = 9` nie zmienia się po wywołaniu - `x = 99` w środku to inna
    zmienna, widoczna tylko w tej funkcji.
    """
    x = 99
    return x


# x = f7()


x = []


def f8(p1: list[int]) -> None:
    """
    Argument jest przekazywany przez referencję do obiektu.

    Funkcja nie przypisuje nic do `p1`, tylko modyfikuje obiekt, na który
    `p1` wskazuje - dlatego zmiana jest widoczna u wywołującego.
    """
    p1.append(1)
    p1.append(2)
    p1.append(3)


# f8(x)
# print(x)

# Local
# Enclosing
# GLobal
# Built-In
# - w tej kolejności Python szuka nazwy (reguła LEGB)

# __name__ = 'global name'
def f9() -> None:
    """Zagnieżdżona funkcja widzi nazwy z funkcji zewnętrznej (E) i modułu (G)."""
    # __name__ = 'enclosing name'
    def f9_1() -> None:
        # __name__ = 'local name'
        print(__name__)

    f9_1()


# f9()

# nie należy używać obiektór typów mutowalnych jako
# wartości domyślnych
# wartość domyślna jest obliczana RAZ, przy definicji funkcji - ta sama lista
# jest współdzielona przez wszystkie wywołania
def f10(i: int, x: list[int] = []) -> None:
    """Pułapka: mutowalna wartość domyślna (zostanie nadpisana poprawną wersją)."""
    x.append(i)
    print(x)


# f10(1)
# f10(2)
# f10(3)

# poprawny idiom: domyślnie None, nowa lista tworzona przy każdym wywołaniu
# list[int] | None - wymaga Pythona >= 3.10
def f10(i: int, x: list[int] | None = None) -> None:
    """Poprawna wersja: `None` jako wartownik, lista tworzona w środku."""
    if x is None:
        x = []
    x.append(i)
    print(x)


# f10(1)
# f10(2)
# f10(3)

# Callable[[], None] - typ "funkcja bez argumentów zwracająca None";
# collections.abc.Callable jako generyk - wymaga Pythona >= 3.9
def f11() -> Callable[[], None]:
    """
    Domknięcie (closure): zwrócona funkcja pamięta `x` z zakresu `f11`,
    mimo że `f11` już się zakończyła.
    """
    x = 99

    def f11_1() -> None:
        print(x)

    return f11_1


# f = f11()
# f()
# print(f.__closure__[0].cell_contents)

# funkcja która przyjmie dowolne parametry wejściowe
# takiej funkcji fajnie się używa
# np jako zwiadowca
def f12(*args: Any, **kwargs: Any) -> None:
    """Przyjmuje cokolwiek i wypisuje, co dostała - "zwiadowca"."""
    print(f'{args=}')
    print(f'{kwargs=}')


# f12()
# f12(1, 2, 3, 2, 2, 2, 2, 3, aa=11, bb=98, cc=55)

# def f13(*args, **kwargs):
#     print(f'{args=}')
#     print(f'{kwargs=}')
#     return 42

def f13(slowo: str) -> str:
    """Funkcja-klucz do sortowania: odwrócony napis."""
    return slowo[::-1]


if __name__ == '__main__':
    # f-stringi z = (np. f'{x=}') użyte w funkcjach wyżej - wymaga Pythona >= 3.8

    # sort modyfikuje listę w miejscu i zwraca None
    x = [1, 2, 6, 3, 8, 7]
    y = x.sort()
    print(y)
    print(x)

    # funkcja jako argument: sort wywoła f13 dla każdego elementu
    # i posortuje po tym, co f13 zwróci (tu: po odwróconych napisach)
    x = ['az', 'zebra', 'grog']
    x.sort(key=f13)
    print(x)
