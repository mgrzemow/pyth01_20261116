"""
Wycena koszyka walut - optymalizacja przez pamięć podręczną (memoizację).

Odpowiedź na pytanie `*` z `c_14`: pobieranie kursu wydzielone do funkcji
`pobierz_kurs`, a dekorator `functools.lru_cache` zapamiętuje jej wynik
dla każdego argumentu. Przy 500 pozycjach i 5 walutach do API idzie
tylko 5 zapytań - reszta trafia w cache.

Wymaga biblioteki `requests` (`uv add requests`).
"""
# uv add requests
import functools

import requests

koszyk_walut: list[tuple[str, float]] = [
    ('USD', 1234),
    ('EUR', 1222),
    ('CHF', 1000),
    ('NZD', 2200),
    ('AUD', 3000),
] * 100
"""Koszyk: lista par (kod waluty, kwota); `* 100` powiela listę 100 razy."""


# * jak można to zoptymalizować?
# ** jak czytać jednocześnie?

# lru_cache zapamiętuje wyniki funkcji w słowniku argumenty -> wynik;
# argumenty muszą być hashowalne (str jest). maxsize=None = bez limitu.
# Od Pythona 3.9 to samo daje krótsze @functools.cache
@functools.lru_cache(maxsize=None)
def pobierz_kurs(waluta: str) -> float:
    """
    Pobiera średni kurs waluty z tabeli A NBP.

    Args:
        waluta: trzyliterowy kod waluty, np. `'USD'`

    Returns:
        kurs średni (`mid`) w PLN
    """
    url_szablon = 'https://api.nbp.pl/api/exchangerates/rates/a/{}/?format=json'
    # przygotuj url
    url = url_szablon.format(waluta)
    # wczytaj kurs
    response = requests.get(url)
    response.raise_for_status()
    kurs = response.json()['rates'][0]['mid']
    return kurs


def wycen_koszyk(koszyk_walut: list[tuple[str, float]]) -> float:
    """
    Sumuje wartość koszyka w PLN; kursy pobierane przez `pobierz_kurs`.

    Args:
        koszyk_walut: lista par `(kod_waluty, kwota)`

    Returns:
        łączna wartość w PLN, zaokrąglona do groszy
    """
    suma = 0
    for waluta, kwota in koszyk_walut:
        kurs = pobierz_kurs(waluta)
        # dolicz do sumy
        suma = round(suma + kurs * kwota, 2)
    return suma


if __name__ == '__main__':
    w = wycen_koszyk(koszyk_walut)
    print(w)
    # statystyki cache: ile trafień, ile faktycznych wywołań
    print(pobierz_kurs.cache_info())
