"""
Pętla `while`: cztery sposoby zapisania pętli "czytaj aż do słowa koniec"
i operator walrus `:=`.

Notatki ze szkolenia. Kod demonstracyjny jest pod `if __name__ == '__main__'`
i czyta z konsoli.
"""

if __name__ == '__main__':
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
    # := (assignment expression) przypisuje wartość do zmiennej I jednocześnie
    # zwraca ją jako wynik wyrażenia; nawiasy wokół (imie := ...) są konieczne
    # wymaga Pythona >= 3.8
    while (imie := input('Podaj imie: ')) != 'koniec':
        print(f'Cześć {imie}!')

    # walrus działa w dowolnym wyrażeniu - tu po obliczeniu v mamy też
    # pole podstawy w zmiennej s
    r = 10
    h = 5
    v = (s := 3.14 * r * r) * h
