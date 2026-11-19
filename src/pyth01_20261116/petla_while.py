# while warunek:
#     kod

# n = 5
# while n > 0:
#     print(n)
#     n -= 1

# duplikacja kodu - bardzi źle
# imie = input('Podaj imie: ')
# while imie != 'koniec':
#     print(f'Cześć {imie}!')
#     imie = input('Podaj imie: ')

# wartość początkowa
# imie = None
# while imie != 'koniec':
#     if imie is not None:
#         print(f'Cześć {imie}!')
#     imie = input('Podaj imie: ')

# wyjście przez break
# while True:
#     imie = input('Podaj imie: ')
#     if imie == 'koniec':
#         break
#     print(f'Cześć {imie}!')


# od 3.8 operator walrus
while (imie := input('Podaj imie: ')) != 'koniec':
    print(f'Cześć {imie}!')

r = 10
h = 5
v = (s := 3.14 * r * r) * h

