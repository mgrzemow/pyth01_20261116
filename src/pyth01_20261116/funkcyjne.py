"""
Elementy programowania funkcyjnego: funkcja jako obiekt (callable), `lambda`,
funkcja-klucz w sortowaniu, memoizacja przez `functools.lru_cache`,
wyrażenia listowe / słownikowe / zbiorowe (comprehensions), wyrażenia
generatorowe oraz `all` / `any`.

Notatki ze szkolenia. Funkcje są na poziomie modułu, kod demonstracyjny
pod `if __name__ == '__main__'`.
"""
import functools


# funkcja jako obiekt
def f1() -> None:
    """Zwykła funkcja - po `def` jest obiektem jak każdy inny."""
    print('f1')


def f2(slowo: str) -> str:
    """Funkcja-klucz: odwrócony napis."""
    return slowo[::-1]


# po nazwiskach, a jak nazwiska są takie same to po imionach

def f3(imie_nazwisko: str) -> list[str]:
    """
    Funkcja-klucz: `['Nazwisko', 'Imię']`.

    Listy porównują się leksykograficznie (najpierw pierwszy element, przy
    remisie drugi), więc sortowanie po takim kluczu daje "po nazwisku,
    potem po imieniu".
    """
    return imie_nazwisko.split()[::-1]


# 1 1 2 3 5 8 13 21
# dekorator lru_cache zapamiętuje wyniki dla już policzonych argumentów
# (memoizacja) - bez niego fibo(990) liczyłoby się dłużej niż istnieje
# wszechświat, bo każde wywołanie rozgałęzia się na dwa kolejne
@functools.lru_cache(maxsize=None)
def fibo(n: int) -> int:
    """
    N-ty wyraz ciągu Fibonacciego, rekurencyjnie z pamięcią podręczną.

    Args:
        n: indeks wyrazu, >= 0

    Returns:
        wyraz ciągu (`fibo(0) == fibo(1) == 1`)
    """
    if n < 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


if __name__ == '__main__':
    # co to jest callable - normalny obiekt
    # wywołanie f1() to tak naprawdę wywołanie metody specjalnej __call__
    f1()
    f1.__call__()

    # takie callable moge stworzyć również jako lambde

    x = ['floraian', 'zad', 'grog']

    x.sort(key=f2)
    print(x)

    # lambda - funkcja anonimowa z jednym wyrażeniem, bez return
    x.sort(key=lambda slowo: slowo[::-1])
    print(x)

    # jak napisać funkcje, która posortuje:
    x = ['Grzegorz Nowak', 'Zenon Adamek', 'Piotr Adamek']

    x.sort(key=f3)
    print(x)

    x.sort(key=lambda imie_nazwisko: imie_nazwisko.split()[::-1])
    print(x)

    print(fibo(990))

    # comprehensions czyli wyrażenia listowe, slownikowe i zbiorowe
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = []
    for n in x:
        if n % 2 == 0:
            y.append(n ** 2)
    print(y)

    # to samo w jednym wyrażeniu: [co_wstawić for element in sekwencja if warunek]
    y = [n ** 2
         for n in x
         if n % 2 == 0]

    print(y)

    # !!! można poczytać co to są generator comprehesions i w ogóle generatory / iteratory / iterable

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # chcę wyprodukować słownik kluicze - liczby z x a wartości - elementy ciagu fobonacciego
    d = {}
    for n in x:
        d[n] = fibo(n)

    print(d)
    # wyrażenie słownikowe: {klucz: wartość for ...}
    d = {n: fibo(n) for n in x}
    print(d)

    # zbiory:
    x = [1, 2, 3, 5, 6, 7, 8, 8, 7, 8, 7, 8, 11, 12, 12, 13]
    # zbiór reszt z dzielenia przez 5:
    # wyrażenie zbiorowe: {element for ...} - duplikaty znikają same
    s = {i % 5 for i in x}
    print(s)

    # fajne zastosowanie comphenesions
    # czy wszystkie / czy którykolwiek

    print(all([True, True, False]))
    print(any([True, True, False]))

    x = ['Ala', 'Tomek', 'Alina']
    # czy wszystkie imiona z x kończą się na 'a'?
    print(all([imie.endswith('a') for imie in x]))
    print(any([imie.endswith('a') for imie in x]))

    # szybciej - lazy evalualtion - liczymy tylko do piierwszego decydującego elementu
    # bez nawiasów [] to wyrażenie generatorowe: elementy są produkowane
    # na żądanie, a all/any przerywają po pierwszym False/True
    print(all(imie.endswith('a') for imie in x))
    print(any(imie.endswith('a') for imie in x))
