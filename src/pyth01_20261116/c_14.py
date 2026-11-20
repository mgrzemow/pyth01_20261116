"""
Wycena koszyka walut kursami z REST API NBP - wersja naiwna.

Dla każdej pozycji koszyka (500 pozycji, bo lista 5 walut jest powielona
100 razy) wykonywane jest osobne zapytanie HTTP, mimo że walut jest tylko 5.
To punkt wyjścia do dwóch pytań z komentarza:

- `*` jak można to zoptymalizować? -> `c_14_cacche` (pamięć podręczna)
- `**` jak czytać jednocześnie? -> `c14_concurrent_futures` (równolegle)

Wymaga biblioteki `requests` (`uv add requests`).
"""
# uv add requests
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

# list[tuple[str, float]] - generyki wbudowanych typów, wymaga Pythona >= 3.9
def wycen_koszyk(koszyk_walut: list[tuple[str, float]]) -> float:
    """
    Sumuje wartość koszyka w PLN, pobierając kurs osobno dla każdej pozycji.

    Args:
        koszyk_walut: lista par `(kod_waluty, kwota)`

    Returns:
        łączna wartość w PLN, zaokrąglona do groszy
    """
    url_szablon = 'https://api.nbp.pl/api/exchangerates/rates/a/{}/?format=json'
    suma = 0
    for waluta, kwota in koszyk_walut:
        # przygotuj url
        # str.format wstawia argument w miejsce {}
        url = url_szablon.format(waluta)
        # wczytaj kurs
        response = requests.get(url)
        # rzuca HTTPError, gdy serwer odpowiedział kodem 4xx/5xx
        response.raise_for_status()
        # .json() parsuje odpowiedź do słowników/list - dalej zwykła nawigacja
        kurs = response.json()['rates'][0]['mid']
        # dolicz do sumy
        suma = round(suma + kurs * kwota, 2)
    return suma


if __name__ == '__main__':
    w = wycen_koszyk(koszyk_walut)
    print(w)
