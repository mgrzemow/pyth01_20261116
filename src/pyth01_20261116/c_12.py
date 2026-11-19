"""
Napisać klasę Spychacz

Spychacz będzie miał następujące dane:
 - nr_rej
 - x
 - y
 - kierunek

Spychacz będzie potrafił:
 - się stworzyć w (0, 0) skierowany w góre
 - jechać przed siebie o ustaloną odległość
 - skręcić w prawo o 90 stopni
 - wypisać swoje dane: nr_rej i pozycję
"""


class Spychacz:
    # dozwolone atrybuty instancji klasy
    __slots__ = [
        'nr_rej',
        '_x',
        '_y',
        '_kierunek',
        '_dlugosc',
    ]

    _kierunki = 'NESW'

    def __init__(self, nr_rej):
        self.nr_rej = nr_rej
        self._x = 0
        self._y = 0
        self._kierunek = 0
        self._dlugosc = 567

    # str nie zastępuje repr
    # def __str__(self):
    #     return f'S Spychacz {self.nr_rej} w ({self._x}, {self._y})'

    # jeżeli chcę mieć jedną konwersję do stringa to lepiej __repr__
    # bo repr zastepuje str
    def __repr__(self):
        return f'R Spychacz {self.nr_rej} w ({self._x}, {self._y})'

    # metody delegowane z wywołań funkcji globalnych
    def __len__(self):
        return self._dlugosc

    # konwersje - zazwyczaj __str__, inne można ale po co?

    def __float__(self):
        return 44.3546345432

    # Zdecydowanie unikać:
    # def __bool__(self):
    #     return False

    # operatory
    def __eq__(self, other):
        return self.nr_rej == other.nr_rej

    # do sortowania
    def __lt__(self, other):
        return self.nr_rej < other.nr_rej

    # i wiele innych operatorów - tylko po co?

    # z ciekawszych
    # operator indeksowania i slicingu
    # s1[1]
    # s1['klucz']
    # s1[1:4:9]
    def __getitem__(self, item):
        print('__getitem__', item)

    # inne - często mocno zaawansowane ale też bardzo poteżne

    # jak ze spycchacza zrobić funkcje
    def __call__(self, *args, **kwargs):
        print('__call__', args, kwargs)


    def jedz(self, odleglosc):
        if self.__class__._kierunki[self._kierunek] == 'N':
            self._y += odleglosc
        elif self.__class__._kierunki[self._kierunek] == 'E':
            self._x += odleglosc
        elif self.__class__._kierunki[self._kierunek] == 'S':
            self._y -= odleglosc
        elif self.__class__._kierunki[self._kierunek] == 'W':
            self._x -= odleglosc

    def skrec_w_prawo(self):
        self._kierunek = (self._kierunek + 1) % 4


if __name__ == '__main__':
    s1 = Spychacz('rk12345')
    print(s1)  # Spychacz rk12345 w (0, 0)
    s1.jedz(12)
    s1.skrec_w_prawo()
    print(s1)  # Spychacz rk12345 w (0, 12)

    s1.jedz(12)
    s1.skrec_w_prawo()
    print(s1)  # Spychacz rk12345 w (12, 12)

    s1.jedz(12)
    s1.skrec_w_prawo()
    print(s1)  # Spychacz rk12345 w (12, 0)

    s1.jedz(12)
    s1.skrec_w_prawo()
    print(s1)  # Spychacz rk12345 w (0, 0)
    print([s1, s1])

    # to wyszukuje w całym łańcuchu dziedziczenia
    print(hasattr(s1, '__repr__'))
    print(hasattr(s1, '__str__'))

    # a to nie
    print('__str__' in vars(s1.__class__))

    # można dodawać atrybuty do instancji po stworzeniu z klasy
    # to jest straszne - robię literówkę i się o tym nie dowiem
    # na sczęście da się to wyłączyć dodajac __slots__

    # Atrybuty prywatne są po prostu tłumaczona na inną nazwę:
    # Dodatkowo jest to niewygodne jeżeli chcemy mieć dostęp do takiego
    # atrybutu z klasy pochodnej
    # s1._Spychacz__kierunek = 7
    # z tego powodu lepiej chyba używać słabej/deklaratywnej prywatności:
    # _kierunek

    print(len(s1))
    print(float(s1))
    # dlaczego nie przeciążać konwersji do bool?
    # if s1:
    #     print('s1 nie jest None')
    # else:
    #     print('s1 jest None')
    s1 = Spychacz('kr12345')
    s2 = Spychacz('kr12345')
    print(s1 == s2)

    s1 = Spychacz('kr12345')
    s2 = Spychacz('ar12345')
    x = [s1, s2]
    x.sort()
    print(x)
    s1[0]
    s1['asdas']
    s1[0:77:2]
    s1(1, 2, 3, a=22, b=99)
