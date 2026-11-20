"""
Wycena koszyka walut - równoległe pobieranie kursów przez
`concurrent.futures.ProcessPoolExecutor`.

Odpowiedź na pytanie `**` z `c_14`: wycena jednej pozycji wydzielona
do funkcji `wycen_walute`, a `executor.map` rozdziela pozycje koszyka między
10 procesów roboczych i zwraca wyniki w kolejności wejścia.

UWAGA (Windows/macOS): procesy robocze startują metodą *spawn*, czyli każdy
z nich od nowa importuje ten moduł. Bez `if __name__ == '__main__'` każdy
proces potomny sam tworzyłby kolejną pulę procesów - stąd ta konstrukcja
jest tu obowiązkowa, nie tylko dobrym zwyczajem.

Dla zadań czekających na sieć (I/O-bound) zwykle lepszy jest
`ThreadPoolExecutor`: wątki są tańsze, a GIL jest zwalniany na czas
operacji sieciowych. Pamięć podręczna z `c_14_cacche` działałaby w wątkach
(wspólna pamięć), a w procesach nie - każdy proces miałby własny cache.

Wymaga biblioteki `requests` (`uv add requests`).
"""
# uv add requests
import concurrent.futures

import requests

koszyk_walut: list[tuple[str, float]] = [
    ('USD', 1234),
    ('EUR', 1222),
    ('CHF', 1000),
    ('NZD', 2200),
    ('AUD', 3000),
] * 10
"""Koszyk: lista par (kod waluty, kwota); `* 10` powiela listę 10 razy."""


# * jak można to zoptymalizować?
# ** jak czytać jednocześnie?

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


# funkcja dla executor.map musi przyjmować JEDEN argument - dlatego para
# (waluta, kwota) jako krotka, rozpakowana w środku
def wycen_walute(para: tuple[str, float]) -> float:
    """
    Wycenia jedną pozycję koszyka.

    Args:
        para: krotka `(kod_waluty, kwota)`

    Returns:
        wartość pozycji w PLN, zaokrąglona do groszy
    """
    waluta, kwota = para
    kurs = pobierz_kurs(waluta)
    return round(kurs * kwota, 2)


def wycen_koszyk(koszyk_walut: list[tuple[str, float]]) -> float:
    """
    Sumuje wartość koszyka w PLN, wyceniając pozycje równolegle w 10 procesach.

    Args:
        koszyk_walut: lista par `(kod_waluty, kwota)`

    Returns:
        łączna wartość w PLN, zaokrąglona do groszy
    """
    suma = 0
    # executor jako menedżer kontekstu: na wyjściu z with czeka na wszystkie
    # zadania i zamyka pulę; map działa jak wbudowane map(), ale wywołania
    # idą do procesów roboczych (argumenty i wyniki są przesyłane przez pickle)
    # alternatywa dla I/O: concurrent.futures.ThreadPoolExecutor(10)
    with concurrent.futures.ProcessPoolExecutor(10) as executor:
        for wynik in executor.map(wycen_walute, koszyk_walut):
            suma = round(suma + wynik, 2)
    return suma


if __name__ == '__main__':
    w = wycen_koszyk(koszyk_walut)
    print(w)
