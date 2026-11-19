# funkcja jako obiekt
def f1():
    print('f1')


# co to jest callable - normalny obiekt
f1()
f1.__call__()

# takie callable moge stworzyć również jako lambde

x = ['floraian', 'zad', 'grog']


def f2(slowo):
    return slowo[::-1]


x.sort(key=f2)
print(x)

x.sort(key=lambda slowo: slowo[::-1])
print(x)

# jak napisać funkcje, która posortuje:
x = ['Grzegorz Nowak', 'Zenon Adamek', 'Piotr Adamek']


# po nazwiskach, a jak nazwiska są takie same to po imionach

def f3(imie_nazwisko):
    return imie_nazwisko.split()[::-1]


x.sort(key=f3)
print(x)

x.sort(key=lambda imie_nazwisko: imie_nazwisko.split()[::-1])
print(x)

import functools


# 1 1 2 3 5 8 13 21
@functools.lru_cache(maxsize=None)
def fibo(n):
    if n < 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


print(fibo(990))

# comprehensions czyli wyrażenia listowe, slownikowe i zbiorowe
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = []
for n in x:
    if n % 2 == 0:
        y.append(n ** 2)
print(y)

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
d = {n: fibo(n) for n in x}
print(d)

# zbiory:
x = [1, 2, 3, 5, 6, 7, 8, 8, 7, 8, 7, 8, 11, 12, 12, 13]
# zbiór reszt z dzielenia przez 5:
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
print(all(imie.endswith('a') for imie in x))
print(any(imie.endswith('a') for imie in x))
