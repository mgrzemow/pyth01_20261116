"""
Ćwiczenie:

Napisać program, który:

1. W pętli while będzie prosił użytkownika o podanie imienia i
   dla każdego imienia będzie dodawał je do listy.
   Warunek wyjścia z pętli - użytkownik podaje 'koniec'.

2. Dla każdego elementu listy wypisze komunikat:
  - dla imion kończących się na a: 'Cześć Imie, witam panią.'
  - dla imion nie kończących się na a: 'Cześć Imie, witam pana.'

Podpowiedzi:
 - [].append()

Rozszerzenia ćwiczenia:
"""
if __name__ == '__main__':

    lista_imion = []
    # operator walrus := przypisuje i zwraca wartość w jednym wyrażeniu
    # (patrz petla_while.py) - wymaga Pythona >= 3.8
    while (imie := input('Podaj imie: ')) != 'koniec':
        lista_imion.append(imie)

    for imie in lista_imion:
        if imie.endswith('a'):
            print(f'Cześć {imie}, witam panią.')
        else:
            print(f'Cześć {imie}, witam pana.')
