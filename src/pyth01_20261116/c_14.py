# uv add requests
import requests

koszyk_walut = [
    ('USD', 1234),
    ('EUR', 1222),
    ('CHF', 1000),
    ('NZD', 2200),
    ('AUD', 3000),
] * 100

# * jak można to zoptymalizować?
# ** jak czytać jednocześnie?

def wycen_koszyk(koszyk_walut: list[tuple[str, float]]) -> float:
    ...


if __name__ == '__main__':
    w = wycen_koszyk(koszyk_walut)
    print(w)
