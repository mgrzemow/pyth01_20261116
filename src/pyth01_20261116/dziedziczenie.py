class Pracownik:
    def __init__(self, imie, stawka_norm, stawka_nad):
        self.imie = imie
        self.stawka_norm = stawka_norm
        self.stawka_nad = stawka_nad
        self._konto = 0

    def pracuj(self, ile_h):
        print('Pracuje jako Pracownik')
        if ile_h > 8:
            self._konto += 8 * self.stawka_norm + (ile_h - 8) * self.stawka_nad
        else:
            self._konto += ile_h * self.stawka_norm

    def wyplata(self):
        tmp = self._konto
        self._konto = 0
        return tmp


class Kierownik(Pracownik):
    def __init__(self, imie, stawka_norm, stawka_nad, bonus_kier):
        super().__init__(imie, stawka_norm, stawka_nad)
        self.bonus_kier = bonus_kier

    def pracuj(self, ile_h):
        super().pracuj(ile_h)
        print('Pracuje jako Kierownik')
        if ile_h >= 10:
            self._konto += self.bonus_kier

class Dyrektor(Kierownik):
    # dodatkowy bonus kwotowy bonus_dyr za każde wywołanie metody pracuj
    ...

if __name__ == '__main__':
    p1 = Kierownik('Jan', stawka_norm=20, stawka_nad=40, bonus_kier=300)
    print(p1.wyplata())  # 0
    p1.pracuj(5)  # nalizy mu się 5 * 20 = 100, stan konta 100
    p1.pracuj(10)  # nalizy mu się 8 * 20 + 2 * 40 + 300 = 540, stan konta 340
    print(p1.wyplata())  # 340
    print(p1.wyplata())  # 0
