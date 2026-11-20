class Czlowiek:
    __slots__ = [
        'imie',
        '_wiek',
    ]

    def _set_wiek(self, wiek):
        print('_set_wiek', wiek)
        if wiek >= 0:
            self._wiek = wiek
        else:
            raise ValueError('Wiek powinien być >= 0')

    def _get_wiek(self):
        print('_get_wiek')
        return self._wiek

    wiek = property(fget=_get_wiek, fset=_set_wiek)

    @property
    def wiek_miesiace(self):
        return self._wiek * 12

    def __init__(self, imie, wiek):
        self.imie = imie
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
