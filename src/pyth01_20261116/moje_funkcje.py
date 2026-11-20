"""
Moduł do importowania przez `modul_importujacy` - pokazuje, co się dzieje
z kodem globalnym modułu przy imporcie, a co przy uruchomieniu bezpośrednim.

Przy imporcie Python wykonuje cały kod modułu (definicje funkcji, przypisania),
ale `__name__` jest wtedy nazwą modułu (`moje_funkcje` lub
`pyth01_20261116.moje_funkcje`), więc blok pod `if __name__ == '__main__'`
się nie wykonuje. Przy uruchomieniu `python moje_funkcje.py` `__name__`
ma wartość `'__main__'`.
"""

NIBY_STALA: int = 123
"""Python nie ma stałych - WIELKIE LITERY to tylko konwencja "nie zmieniaj"."""


def dodaj(x: int, y: int) -> int:
    """
    Dodaje dwie liczby, wypisując po drodze argumenty.

    Args:
        x: pierwszy składnik
        y: drugi składnik

    Returns:
        suma `x + y`
    """
    # f'{x=}' wypisuje "x=<wartość>" - wygodne do debugowania, wymaga Pythona >= 3.8
    print(f'moje_funkcje.dodaj {x=} {y=}')
    return x + y


if __name__ == '__main__':
    print('kod globalny pliku moje_funkcje.py', __name__)
