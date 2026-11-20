"""
Dane:
sekundy = 98765.
Zamień na godziny, minuty i sekundy.
Przypomnienie - operatory // i %

Ćwiczenie pokazuje też funkcję zwracającą kilka wartości naraz (krotkę)
i rozpakowanie jej po stronie wywołania.
"""


# zbuduj funkcję zrwacającą krotkę

# tuple[int, int, int] jako hint typu - wymaga Pythona >= 3.9
# (wcześniej: from typing import Tuple; Tuple[int, int, int])
def zamien_s_na_hms(sekundy: int) -> tuple[int, int, int]:
    """
    Zamienia sekundy na godziny, minuty i sekundy.

    Args:
        sekundy: liczba sekund do rozłożenia, >= 0

    Returns:
        krotka `(godziny, minuty, sekundy)`
    """
    # // - dzielenie całkowite, % - reszta z dzielenia
    godziny = sekundy // (60 * 60)
    reszta = sekundy % (60 * 60)
    minuty = reszta // 60
    sekundy = reszta % 60
    # return z kilkoma wartościami po przecinku pakuje je w krotkę
    return godziny, minuty, sekundy


if __name__ == '__main__':
    sekundy = 98765
    # unpacking zwróconej krotki do trzech zmiennych
    godziny, minuty, sekundy = zamien_s_na_hms(sekundy)
    print('H:', godziny, 'M:', minuty, 'S:', sekundy)
