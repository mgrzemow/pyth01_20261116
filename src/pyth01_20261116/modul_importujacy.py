"""
Sposoby importowania własnego modułu (`moje_funkcje`) i dlaczego
`from modul import *` jest zły.

Warianty `import moje_funkcje` (bez nazwy pakietu) działają tylko wtedy,
gdy katalog pakietu jest na `sys.path` - czyli w praktyce przy uruchomieniu
skryptu z tego katalogu (Python dodaje katalog skryptu na początek
`sys.path`). Import przez nazwę pakietu działa wszędzie, o ile pakiet jest
zainstalowany (`uv sync` instaluje projekt w trybie editable).
"""

# import modułu - działa nez pakietu

# import moje_funkcje
# print(moje_funkcje.dodaj(1, 2))
# print(moje_funkcje.NIBY_STALA)

# import moje_funkcje as mf
# print(mf.dodaj(1, 2))
# print(mf.NIBY_STALA)

# from moje_funkcje import dodaj
# dodaj(1, 2)

# import przez pakiet
# import pyth01_20261116.moje_funkcje
# pyth01_20261116.moje_funkcje.dodaj(1,2)

# nie wolno:
from math import *
# duże ryzyko nadpisania symboli
# (* wciąga do przestrzeni nazw tego modułu WSZYSTKIE publiczne nazwy z math,
# np. pow, e, gamma - i po cichu nadpisze nasze zmienne o tych nazwach;
# nie widać też, skąd dana nazwa pochodzi)

if __name__ == '__main__':
    # wariant przez pakiet - jedyny, który działa niezależnie od tego,
    # skąd uruchamiamy skrypt
    from pyth01_20261116 import moje_funkcje
    print(moje_funkcje.dodaj(1, 2))
    print(moje_funkcje.NIBY_STALA)
    # __name__ zaimportowanego modułu to jego pełna nazwa, nie '__main__'
    print(moje_funkcje.__name__)
