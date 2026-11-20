"""
Mając plik wejściowy w formacie:

    ola Wrocław
    ala Kraków
    paweł katowice
    zosia Warszawa

Wypisać na ekran powitania:
Cześć Ala, co tam słychać w mieście Kraków?

* dodać do pliku wejściowego puste linie i obsłużyć
** dodać do pliku wejściowego linie zacczynające się od # i też zignorować
*** dodać do pliku wejściowego linie tyl;ko z imieniem i wypisać inne powitanie:
Cześć Ala

Skrypt czyta `imiona_miasta.txt` z bieżącego katalogu.
"""

if __name__ == '__main__':
    with open('imiona_miasta.txt', 'rt', encoding='utf-8') as f:
        # iteracja po pliku daje kolejne linie razem ze znakiem końca linii
        for linia in f:
            linia = linia.strip()
            # pusty napis jest fałszywy - "if linia" odrzuca puste linie
            if linia and not linia.startswith('#'):
                wynik = linia.split()
                if len(wynik) == 2:
                    # unpacking dwuelementowej listy
                    imie, miasto = wynik
                    print(f'Cześć {imie.capitalize()}, co tam słychać w mieście {miasto.capitalize()}?')
                elif len(wynik) == 1:
                    imie = wynik[0]
                    print(f'Cześć {imie.capitalize()}.')
