"""
Agregacja danych w słowniku: zliczanie wystąpień i grupowanie elementów.

Ten sam problem rozwiązany na kilka sposobów, od najbardziej "ręcznego"
do idiomatycznego:

1. `if klucz not in d` - jawna inicjalizacja,
2. `dict.get(klucz, domyslna)`,
3. `collections.defaultdict`,
4. `dict.setdefault`.

Kod demonstracyjny jest pod `if __name__ == '__main__'`.
"""
import collections


def f1() -> int:
    """
    Funkcja wyliczająca wartość domyślną dla `defaultdict`.

    `defaultdict` wywołuje ją bez argumentów, gdy ktoś odwoła się
    do nieistniejącego klucza.

    Returns:
        zawsze 0 - punkt startowy licznika
    """
    return 0


if __name__ == '__main__':
    slowa = 'mama mama tata tata mama ja'
    # {
    #     'mama': 3,
    #     'tata': 2,
    #     'ja': 1,
    # }

    d = {}
    for slowo in slowa.split():
        # jak pierwszy raz:
        if slowo not in d:
            d[slowo] = 1
        # a jak już było
        else:
            d[slowo] += 1

    d = {}
    for slowo in slowa.split():
        # get zwraza wartość ze słownika lub wartosc domyślną
        d[slowo] = d.get(slowo, 0) + 1

    # collections.defaultdict - potęga - bardzo fajne w
    # realnych scenariuszach

    # defaultdict to podklasa dict; przy odwołaniu do brakującego klucza
    # (metoda specjalna __missing__) wywołuje podaną fabrykę, wstawia jej
    # wynik pod ten klucz i go zwraca - dlatego d[slowo] += 1 nie rzuca KeyError
    d = collections.defaultdict(f1)
    for slowo in slowa.split():
        d[slowo] += 1
    print(d)

    # to samo z funkcją anonimową (lambda)
    d = collections.defaultdict(lambda: 0)
    for slowo in slowa.split():
        d[slowo] += 1
    print(d)

    # najkrócej: int() wywołane bez argumentu zwraca 0
    d = collections.defaultdict(int)
    for slowo in slowa.split():
        d[slowo] += 1
    print(d)

    x = 'ala alicja alina beata bartek'
    # cel:
    # {
    #     'a': ['ala', 'alicja', 'alina'],
    #     'b': ['beata', 'bartek']
    # }

    d = {}
    for slowo in x.split():
        pl = slowo[0]
        # jeżeli nie było do tej pory klucza - zainicjuj pustą listę
        if pl not in d:
            d[pl] = []
        d[pl].append(slowo)
    print(d)

    d = {}
    for slowo in x.split():
        pl = slowo[0]
        lista = d.get(pl, [])
        lista.append(slowo)
        d[pl] = lista
    print(d)

    # list() bez argumentu zwraca pustą listę
    d = collections.defaultdict(list)
    for slowo in x.split():
        pl = slowo[0]
        d[pl].append(slowo)
    print(d)

    # .setdefault robi to co get i dodaje od slownika
    # (zwraca wartość spod klucza, a jeśli klucza nie ma - najpierw wstawia
    # wartość domyślną; dzięki temu append działa na liście ze słownika)
    d = {}
    for slowo in x.split():
        pl = slowo[0]
        d.setdefault(pl, []).append(slowo)
    print(d)
