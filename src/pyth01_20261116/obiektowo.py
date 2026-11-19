# class NazwaKlasy:
#     atr_klasowy = 12
#
#     def __init__(self, parametr_konstruktora):
#         # jawna instancja klasy
#         # self
#         self.atr_instancji = parametr_konstruktora
#
#     def m1(self, parametr_metody):
#         print('m1', self.atr_instancji, parametr_metody)
#
# instancja = NazwaKlasy('P1')
# instancja.m1('P2')

class Czlowiek:
    gatunek = 'Homo Sapiens'

    def __init__(self, imie, nazwisko, wiek):
        zmienna_lokalna_znika_po_wywolaniu = 12
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.portfel = 0

    def przedstaw_sie(self):
        print(f'Jestem {self.imie} {self.nazwisko}, mam {self.wiek} lat.')

c1 = Czlowiek('Jan', 'Nowak', 42)
c1.przedstaw_sie()
c1.imie = 'Olek'
c1.przedstaw_sie()
