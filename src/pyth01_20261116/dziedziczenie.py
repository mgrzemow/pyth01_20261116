class Pracownik:
    def __init__(self, imie, stawka_norm, stawka_nad):
        ...

    def pracuj(self, ile_h):
        ...

    def wyplata(self):
        ...


if __name__ == '__main__':
    p1 = Pracownik('Jan', stawka_pod=20, stawka_nad=40)
    print(p1.wyplata())  # 0
    p1.pracuj(5)  # nalizy mu się 5 * 20 = 100, stan konta 100
    p1.pracuj(10)  # nalizy mu się 8 * 20 + 2 * 40 = 240, stan konta 340
    print(p1.wyplata())  # 340
    print(p1.wyplata())  # 0
