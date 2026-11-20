"""
Ćwiczenie:

Napisać program, który:

- Wczytuje z pliku tekstowego dane:
    - nazwa towaru
    - ilość towaru
    - jednostka miary
    - cena

Plik jest w formacie:
```
Banany 2.4 kg 3.5
Kiwi 3 szt 2.3
Piwo 4 szt 2.4
Kiwi 3 szt 2.3
```

- Po każdym towarze program dodaje dane do słownika zakupów w formacie:
```
{
'chleb': (3, 'szt', 4.6),
'cebula': (1.55, 'kg', 2.5)
}
```

- Jeżeli towar już raz wystąpił i jest w słowniku to zamiast dodawać go
   drugi raz - zwiększamy ilość.

- Używając danych ze słownika stowrzonego w pkt 2 wypisuje na ekran paragon w formie:
```
Pietruszka  2.0 kg x 4.60     9.20
Banany      3.0 kg x  3.5    10.50
----------------------------------
SUMA:                        19.70
```

Kolumny mają mieć szerokości:

- nazwa - 12 znaków,
- ilość - 2 znaki przed przecinkiem i 2 po
- jednostka miary - 4 znaki
- cena - 3 znaki przed przecinkiem i 2 po
- wartość pozycji - 5 znaków przed i 2 po
- SUMA - 7 znaków przed i 2 po

### Podpowiedzi:

 - formatowanie f-stringow

### Rozszerzenia ćwiczenia:

 - co by było gdyby mógł wystąpić towar o różnych jednostkach miary.

### Rozwiązanie

Wersja 3: kod podzielony na dwie funkcje (czytanie danych i generowanie
paragonu), a nazwa pliku z danymi pochodzi z modułu `konfiguracja`.
Rozszerzenie z różnymi jednostkami miary rozwiązano kluczem słownika
w postaci krotki `(towar, jm)`.
"""

# import absolutny przez nazwę pakietu - działa i przy uruchomieniu tego
# pliku jako skryptu, i przy imporcie `pyth01_20261116.c_8_2` z innego miejsca
# (samo `import konfiguracja` działało tylko z katalogu pakietu)
from pyth01_20261116 import konfiguracja


# dict[tuple[str, str], list[float]] - generyki wbudowanych typów w hintach,
# wymaga Pythona >= 3.9
def wczytaj_towary(nazwa_pliku: str = konfiguracja.PLIK_TOWARY) -> dict[tuple[str, str], list[float]]:
    """
    Wczytuje towary z pliku tekstowego i sumuje ilości powtarzających się pozycji.

    Każda linia pliku ma postać `towar ilość jednostka cena`. Pozycje o tej
    samej nazwie **i** tej samej jednostce są łączone (ilości sumowane),
    dzięki czemu `Kiwi 3 szt` i `Kiwi 4.5 kg` zostają osobnymi pozycjami.

    Args:
        nazwa_pliku: ścieżka do pliku z towarami; domyślnie
            `konfiguracja.PLIK_TOWARY` (wartość domyślna jest obliczana
            raz, w momencie definicji funkcji)

    Returns:
        słownik `{(towar, jednostka): [ilość, cena]}`
    """
    with open(nazwa_pliku, 'rt', encoding='utf-8') as f:
        slownik_rekordow = {}
        for linia in f:
            linia = linia.strip()
            towar, ilosc, jm, cena = linia.split()
            # skonwertować
            ilosc = float(ilosc)
            cena = float(cena)
            ilosc_do_tej_pory = 0
            # kluczem słownika może być krotka, bo jest niemutowalna (hashowalna)
            if (towar, jm) in slownik_rekordow:
                ilosc_do_tej_pory = slownik_rekordow[(towar, jm)][0]
            slownik_rekordow[(towar, jm)] = [ilosc + ilosc_do_tej_pory, cena]
    return slownik_rekordow


def generuj_paragon(slownik_rekordow: dict[tuple[str, str], list[float]]) -> str:
    """
    Buduje tekst paragonu ze słownika towarów.

    Args:
        slownik_rekordow: słownik w formacie zwracanym przez `wczytaj_towary`

    Returns:
        wieloliniowy napis: po jednej linii na pozycję, linia z kreskami
        i linia `SUMA:` na końcu
    """
    paragon = ''
    suma = 0
    # zagnieżdżony unpacking: klucz to krotka (towar, jm), wartość to [ilosc, cena]
    for (towar, jm), (ilosc, cena) in slownik_rekordow.items():
        # policzyć wartosc
        wartosc = round(ilosc * cena, 2)
        # zwiększyć sumę
        suma = round(suma + wartosc, 2)
        # wyprodukować linię paragonu
        paragon += f'{towar:12} {ilosc:5.2f} {jm:4} x {cena:6.2f} {wartosc:8.2f}\n'
    # wypisać podsumowanie
    paragon += '-' * 41 + '\n'
    paragon += f'SUMA: {suma:35.2f}\n'
    return paragon


if __name__ == '__main__':
    slownik_rekordow = wczytaj_towary()
    print(generuj_paragon(slownik_rekordow))
