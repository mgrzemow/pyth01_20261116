# uv add requests
import functools

import requests
import concurrent.futures

koszyk_walut = [
                   ('USD', 1234),
                   ('EUR', 1222),
                   ('CHF', 1000),
                   ('NZD', 2200),
                   ('AUD', 3000),
               ] * 10

# * jak można to zoptymalizować?
# ** jak czytać jednocześnie?

def pobierz_kurs(waluta):
    url_szablon = 'https://api.nbp.pl/api/exchangerates/rates/a/{}/?format=json'
    # przygotuj url
    url = url_szablon.format(waluta)
    # wczytaj kurs
    response = requests.get(url)
    response.raise_for_status()
    kurs = response.json()['rates'][0]['mid']
    return kurs

def wycen_walute(para):
    waluta, kwota = para
    kurs = pobierz_kurs(waluta)
    return round(kurs * kwota, 2)


def wycen_koszyk(koszyk_walut: list[tuple[str, float]]) -> float:
    suma = 0
    # with concurrent.futures.ProcessPoolExecutor(10) as executor:
    with concurrent.futures.ProcessPoolExecutor(10) as executor:
        for wynik in executor.map(wycen_walute, koszyk_walut):
            suma = round(suma + wynik, 2)
    return suma


if __name__ == '__main__':
    w = wycen_koszyk(koszyk_walut)
    print(w)
