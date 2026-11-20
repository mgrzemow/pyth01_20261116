"""
Dziedziczenie: hierarchia `Pracownik` -> `Kierownik` -> `Dyrektor`,
rozszerzanie metod przez `super()`, przekazywanie argumentów konstruktora
w górę przez `**kwargs`, `__slots__` w łańcuchu dziedziczenia oraz
prosta fabryka obiektów.

Idea: każda klasa pochodna dokłada do metody `pracuj` swój bonus, ale sam
mechanizm naliczania stawek jest tylko w klasie bazowej - zmiana w jednym
miejscu działa dla wszystkich. Kod demonstracyjny jest pod
`if __name__ == '__main__'`.
"""
import faker


class Pracownik:
    """
    Pracownik rozliczany godzinowo: stawka normalna do 8 h, nadgodziny powyżej.

    `__slots__` zamyka listę dozwolonych atrybutów instancji (nie da się
    przez literówkę utworzyć nowego) i oszczędza pamięć, bo instancja
    nie ma słownika `__dict__`.
    """

    __slots__ = [
        'imie',
        '_stawka_norm',
        '_stawka_nad',
        '_konto',
    ]

    # goła * - wszystkie parametry konstruktora tylko po nazwie;
    # przy tylu liczbach tego samego typu chroni przed pomyleniem kolejności
    def __init__(self, *, imie: str, stawka_norm: float, stawka_nad: float) -> None:
        """
        Args:
            imie: imię i nazwisko
            stawka_norm: stawka za godzinę w ramach 8 h
            stawka_nad: stawka za każdą godzinę powyżej 8 h
        """
        self.imie = imie
        self._stawka_norm = stawka_norm
        self._stawka_nad = stawka_nad
        self._konto = 0

    def pracuj(self, ile_h: float) -> None:
        """
        Dopisuje do konta wynagrodzenie za `ile_h` godzin pracy.

        Args:
            ile_h: liczba przepracowanych godzin w jednym dniu
        """
        # print('Pracuje jako Pracownik')
        if ile_h > 8:
            self._konto += 8 * self._stawka_norm + (ile_h - 8) * self._stawka_nad
        else:
            self._konto += ile_h * self._stawka_norm

    def wyplata(self) -> float:
        """
        Wypłaca (zeruje) konto.

        Returns:
            kwota zgromadzona od ostatniej wypłaty
        """
        tmp = self._konto
        self._konto = 0
        return tmp


class Kierownik(Pracownik):
    """Pracownik z bonusem kwotowym za dzień, w którym przepracował >= 10 h."""

    # w klasie pochodnej __slots__ wymienia TYLKO nowe atrybuty;
    # sloty klasy bazowej są dziedziczone
    __slots__ = [
        '_bonus_kier'
    ]

    # **kwargs zbiera parametry, których Kierownik sam nie zna, i przekazuje
    # je w całości do konstruktora klasy bazowej - dzięki temu dodanie
    # parametru w Pracowniku nie wymaga zmian tutaj
    def __init__(self, *, bonus_kier: float, **kwargs: object) -> None:
        """
        Args:
            bonus_kier: bonus za dzień z >= 10 h pracy
            **kwargs: parametry przekazywane do `Pracownik.__init__`
        """
        # super() zwraca "widok" na klasę bazową - wywołujemy jej __init__,
        # żeby zainicjowała swoje atrybuty, i dopiero dokładamy własne
        super().__init__(**kwargs)
        self._bonus_kier = bonus_kier

    def pracuj(self, ile_h: float) -> None:
        """Jak w `Pracownik`, plus bonus kierowniczy przy >= 10 h."""
        # nadpisana metoda najpierw wywołuje wersję bazową (rozszerzanie,
        # nie zastępowanie zachowania)
        super().pracuj(ile_h)
        # print('Pracuje jako Kierownik')
        if ile_h >= 10:
            self._konto += self._bonus_kier


class Dyrektor(Kierownik):
    """Kierownik z dodatkowym bonusem kwotowym za każdy dzień pracy."""

    __slots__ = [
        '_bonus_dyr'
    ]

    # dodatkowy bonus kwotowy bonus_dyr za każde wywołanie metody pracuj
    def __init__(self, *, bonus_dyr: float, **kwargs: object) -> None:
        """
        Args:
            bonus_dyr: bonus za każdy dzień pracy
            **kwargs: parametry przekazywane do `Kierownik.__init__`
        """
        super().__init__(**kwargs)
        self._bonus_dyr = bonus_dyr

    def pracuj(self, ile_h: float) -> None:
        """Jak w `Kierownik`, plus bonus dyrektorski za każdy dzień."""
        # łańcuch: Dyrektor.pracuj -> Kierownik.pracuj -> Pracownik.pracuj
        super().pracuj(ile_h)
        # print('Pracuje jako Dyrektor')
        self._konto += self._bonus_dyr


def zatrudnij_zespol(ile_p: int, ile_k: int, ile_d: int) -> list[Pracownik]:
    """
    Tworzy zespół pracowników z losowymi nazwiskami.

    Tak naprawdę to jest design pattern factory: jedno miejsce, które wie,
    jak budować obiekty różnych klas, a wywołujący dostaje gotową listę.

    Args:
        ile_p: liczba zwykłych pracowników
        ile_k: liczba kierowników
        ile_d: liczba dyrektorów

    Returns:
        lista obiektów; `list[Pracownik]`, bo Kierownik i Dyrektor
        też są Pracownikami (dziedziczenie = relacja "jest")
    """

    f = faker.Faker('pl_PL')
    lista_p = []
    for _ in range(ile_p):
        lista_p.append(Pracownik(imie=f.name(), stawka_norm=20, stawka_nad=40))
    for _ in range(ile_k):
        lista_p.append(Kierownik(imie=f.name(), stawka_norm=20, stawka_nad=40, bonus_kier=100))
    for _ in range(ile_d):
        lista_p.append(Dyrektor(imie=f.name(), stawka_norm=20, stawka_nad=40, bonus_kier=100, bonus_dyr=500))
    return lista_p


if __name__ == '__main__':
    lp = zatrudnij_zespol(10, 3, 1)
    # polimorfizm: wołamy p.pracuj() nie wiedząc, która to klasa -
    # Python sam wybiera właściwą wersję metody
    for p in lp:
        p.pracuj(4)
        p.pracuj(9)
        p.pracuj(12)
    fundusz_plac = sum([p.wyplata() for p in lp])
    print(fundusz_plac)
