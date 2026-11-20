"""
Zbiory (`set`): tworzenie, test przynależności, dodawanie i usuwanie,
usuwanie duplikatów z listy.

Notatki ze szkolenia. Cały kod demonstracyjny jest pod
`if __name__ == '__main__'`.
"""

if __name__ == '__main__':
    # pusty zbiór
    # {} to pusty SŁOWNIK, dlatego pusty zbiór trzeba zrobić przez set()
    s = set()

    # wypełniony zbiór
    s = {'ala', 'karol', 'ola', 'zosia', 'alabaster'}

    print(type(s))
    # zbiór nie ma kolejności - print może pokazać elementy w innym porządku
    print(s)
    for e in s:
        print(e)

    # test przynależności jest szybki (O(1)), bo zbiór jest tablicą haszującą
    print('ola' in s)
    s.add('edward')
    print(s)
    s.remove('edward')
    print(s)
    # dodanie elementu, który już jest, nic nie zmienia
    s.add('ala')
    print(s)
    s.add(11)
    print(s)
    # 11.0 nie zostanie dodane, bo 11 == 11.0 i hash(11) == hash(11.0)
    # - zbiór uznaje je za ten sam element
    s.add(11.0)
    print(s)
    print(11 == 11.0)

    # do pozbywania się duplikatów
    x = ['ala', 'tomek', 'roman', 'ala', 'tomek', 'roman', 'ala', 'tomek', 'roman', 'ala', 'tomek', 'roman', ]
    # unikalne wartoścci z x - UWAGA - tracę kolejność
    print(set(x))
    print(list(set(x)))

    # jak wyrzucić duplikaty nie tracąc kolejności - słownikami
    # słownik zachowuje kolejność wstawiania kluczy (gwarantowane od 3.7),
    # a klucze - tak jak elementy zbioru - nie mogą się powtarzać
    # (krócej: list(dict.fromkeys(x)))
    d = {}
    for e in x:
        d[e] = None
    print(list(d.keys()))
