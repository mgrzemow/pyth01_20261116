import faker
class Pracownik:
    __slots__ = [
        'imie',
        '_stawka_norm',
        '_stawka_nad',
        '_konto',
    ]

    def __init__(self, *, imie, stawka_norm, stawka_nad):
        self.imie = imie
        self._stawka_norm = stawka_norm
        self._stawka_nad = stawka_nad
        self._konto = 0

    def pracuj(self, ile_h):
        # print('Pracuje jako Pracownik')
        if ile_h > 8:
            self._konto += 8 * self._stawka_norm + (ile_h - 8) * self._stawka_nad
        else:
            self._konto += ile_h * self._stawka_norm

    def wyplata(self):
        tmp = self._konto
        self._konto = 0
        return tmp


class Kierownik(Pracownik):
    __slots__ = [
        '_bonus_kier'
    ]

    def __init__(self, *, bonus_kier, **kwargs):
        super().__init__(**kwargs)
        self._bonus_kier = bonus_kier

    def pracuj(self, ile_h):
        super().pracuj(ile_h)
        # print('Pracuje jako Kierownik')
        if ile_h >= 10:
            self._konto += self._bonus_kier


class Dyrektor(Kierownik):
    __slots__ = [
        '_bonus_dyr'
    ]

    # dodatkowy bonus kwotowy bonus_dyr za każde wywołanie metody pracuj
    def __init__(self, *, bonus_dyr, **kwargs):
        super().__init__(**kwargs)
        self._bonus_dyr = bonus_dyr

    def pracuj(self, ile_h):
        super().pracuj(ile_h)
        # print('Pracuje jako Dyrektor')
        self._konto += self._bonus_dyr

def zatrudnij_zespol(ile_p, ile_k, ile_d):
    """
    Tak naprawdę to jest design pattern factory.

    Args:
        ile_p:
        ile_k:
        ile_d:

    Returns:

    """

    f = faker.Faker('PL_pl')
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
    for p in lp:
        p.pracuj(4)
        p.pracuj(9)
        p.pracuj(12)
    fundusz_plac = sum([p.wyplata() for p in lp])
    print(fundusz_plac)
