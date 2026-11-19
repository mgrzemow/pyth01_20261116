# listy
from os import name

x = [1, 2, 3]
print(type(x))

# pusta lista
x = []

x.append(1)
x.append(2)
x.append(3)

print(x)

x.insert(0, 'poczatek')
print(x)

del (x[-1])
print(x)

print(x[0])
print(x[-1])
print(x[:2])

x[1] = 1.5
print(x)

for e in x:
    print(e)

print(1.5 in x)

print(x)
x1 = [11, 22, 33]
x.append(x1)
print(x)
x.pop()

x.extend(x1)
print(x)
x += [44, 55, 66]
print(x)

del (x[-2:])

# typowe zastosowania list

# lista podobnych elementów
lista_imion = ['Ola', 'Ala', 'Karol']

# lista - rekord
rekord_danych = ['Ola', 34, 'Warszawa', 166, True]

# połączenie - lista rekordów
lista_rekordow = [
    ['Ola', 34, 'Warszawa', 166, True],
    ['Ala', 24, 'Kraków', 186, True],
    ['Tomek', 44, 'Kielce', 176, False],
]

# krotki
k = (1, 2, 3, 'Ala')
print(k)
print(type(k))
# nie da się krotki zmienić
# k[0] = 11
# del(k[-1])

# podczas doklejania += powstaje nowa krotka
print(id(k))
k += (1, 2)
print(k)
print(id(k))

# uwaga 1 - krotka jest niemutowalna ale jej zawartość nniekoniecznie
# to jest zły styl - zamiast tego lepiej listę list
k = ([], [])
k[0].append('Ola')
k[0].append('Ala')
k[0].append('Ula')
print(k)

# uwaga 2 - krotki są tylko trochę szybksze i lżejsze od list
# nie nie jestem pewien - może być lista

# uwaga 3
# jednoelementowa krotka

k = (9)
print(type(k))

k = (9,)
print(type(k))

# named tuple
# dataclass

import collections

A = collections.namedtuple('NazwaTupla', ['x', 'y', 'z'])
a = A(x=1, y=2, z=3)
print(a)
print(a.x)
print(a.y)
print(a.z)
print(a[0])

# unpacking - działa dla list i krotek:
# z lewejs trony krotka zmiennych
x, y, z = [1, 2, 3]
(x, y, z) = [1, 2, 3]

# w miejscach gdzie nie jest to niezbędne można pominąć (),
# a i tak powstanie krotka

[x, y, z] = (1, 2, 3)

# a co jeżeli nie potrzebuję wszystkich elementów
r = ['Ala', 34, 66, 176, 'Warszawa']
imie, _, _, _, miasto = r

# a co jeżeli liczba elementów jest zmienna
lista_r = [
    ['Ala', 34, 66, 176, 'Warszawa'],
    ['Ala', 34, 66, 176, 'Warszawa', 'Polska'],
    ['Ala', 34, 66, 176, 'Warszawa', 'Polska', 'UE'],
]

# zmienna z * dostaje nadmiarowe elementy
for imie, wiek, waga, wzrost, miasto, *reszta in lista_r:
    print(imie, wiek, reszta)

# wszystko razem
for imie, wiek, _, _, miasto, *reszta in lista_r:
    print(imie, wiek, miasto, reszta)

# zagnieżdzony unpacking
a, b, (c, d, e) = [1, 2, [3, 4, 5]]
