"""
Podstawy programowania obiektowego: klasa, konstruktor `__init__`, `self`,
atrybuty klasy i instancji, metody.

Notatki ze szkolenia. Kod demonstracyjny jest pod `if __name__ == '__main__'`.
"""


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
    """
    Człowiek z imieniem, nazwiskiem, wiekiem i portfelem.

    `gatunek` to atrybut klasy - wspólny dla wszystkich instancji,
    przypisany raz, w ciele klasy. Atrybuty instancji (`imie`, `nazwisko`,
    `wiek`, `portfel`) powstają dopiero w `__init__`, osobno dla każdego
    obiektu.
    """

    gatunek: str = 'Homo Sapiens'
    """Atrybut klasy - ten sam dla wszystkich instancji."""

    # __init__ to inicjalizator wywoływany automatycznie po utworzeniu obiektu;
    # self to jawna referencja do tworzonej instancji (Python przekazuje ją sam)
    def __init__(self, imie: str, nazwisko: str, wiek: int) -> None:
        """
        Args:
            imie: imię
            nazwisko: nazwisko
            wiek: wiek w latach
        """
        # zwykła zmienna lokalna metody - znika po zakończeniu __init__
        zmienna_lokalna_znika_po_wywolaniu = 12
        # przypisanie do self.<nazwa> tworzy atrybut instancji
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.portfel = 0

    def przedstaw_sie(self) -> None:
        """Wypisuje imię, nazwisko i wiek."""
        print(f'Jestem {self.imie} {self.nazwisko}, mam {self.wiek} lat.')


if __name__ == '__main__':
    # wywołanie klasy tworzy instancję; argumenty trafiają do __init__
    c1 = Czlowiek('Jan', 'Nowak', 42)
    # c1.przedstaw_sie() to skrót od Czlowiek.przedstaw_sie(c1)
    c1.przedstaw_sie()
    # atrybuty instancji można czytać i zmieniać z zewnątrz
    c1.imie = 'Olek'
    c1.przedstaw_sie()
