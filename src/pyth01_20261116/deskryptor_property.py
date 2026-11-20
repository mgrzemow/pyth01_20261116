"""
Właściwości (`property`): kontrolowany dostęp do atrybutu przez getter
i setter, bez zmiany sposobu użycia (`c1.wiek` zamiast `c1.get_wiek()`).

`property` to deskryptor - obiekt w klasie, który przechwytuje odczyt
i zapis atrybutu instancji o tej nazwie. Pokazane są dwa równoważne zapisy:
jawne `property(fget=..., fset=...)` oraz dekoratory `@property` /
`@wiek.setter` (w komentarzu). Kod demonstracyjny jest pod
`if __name__ == '__main__'`.
"""


class Czlowiek:
    """Człowiek z walidowanym wiekiem."""

    # w __slots__ jest _wiek (prawdziwe miejsce na dane), a nie wiek -
    # wiek jest atrybutem KLASY (property), nie instancji
    __slots__ = [
        'imie',
        '_wiek',
    ]

    def _set_wiek(self, wiek: int) -> None:
        """Setter: zapisuje wiek po sprawdzeniu, że nie jest ujemny."""
        print('_set_wiek', wiek)
        if wiek >= 0:
            self._wiek = wiek
        else:
            raise ValueError('Wiek powinien być >= 0')

    def _get_wiek(self) -> int:
        """Getter: zwraca zapisany wiek."""
        print('_get_wiek')
        return self._wiek

    # property spina getter i setter pod jedną nazwą;
    # c1.wiek wywoła _get_wiek(c1), c1.wiek = 3 wywoła _set_wiek(c1, 3)
    wiek = property(fget=_get_wiek, fset=_set_wiek)

    # @property bez settera = atrybut tylko do odczytu, liczony na żądanie
    @property
    def wiek_miesiace(self) -> int:
        """Wiek w miesiącach (tylko do odczytu, liczony z `wiek`)."""
        return self._wiek * 12

    def __init__(self, imie: str, wiek: int) -> None:
        """
        Args:
            imie: imię
            wiek: wiek w latach, >= 0
        """
        self.imie = imie
        # to przypisanie przechodzi przez setter - walidacja działa
        # już w konstruktorze
        self.wiek = wiek


# class Czlowiek:
#     __slots__ = [
#         'imie',
#         '_wiek',
#     ]

    # @property
    # def wiek(self):
    #     print('_get_wiek')
    #     return self._wiek
    #
    # @wiek.setter
    # def wiek(self, wiek):
    #     print('_set_wiek', wiek)
    #     if wiek >= 0:
    #         self._wiek = wiek
    #     else:
    #         raise ValueError('Wiek powinien być >= 0')
    #
    # def __init__(self, imie, wiek):
    #     self.imie = imie
    #     self.wiek = wiek


if __name__ == '__main__':
    c1 = Czlowiek('Ola', 34)
    print(c1.wiek)
    c1.wiek = 3
    print(c1.wiek)
    print(c1.wiek_miesiace)
