"""
Odczyt z REST API (kursy walut NBP) biblioteką `requests` i obsługa błędu HTTP.

Kod waluty jest celowo błędny (`usdasdasd`), więc serwer odpowiada 404,
a `raise_for_status()` zgłasza `requests.HTTPError` - skrypt kończy się
tracebackiem. To demonstracja, że błąd HTTP nie jest wyjątkiem sam z siebie:
`requests.get` zwraca odpowiedź z kodem 404 jak każdą inną i dopiero my
decydujemy, czy to błąd (zakomentowany wariant z `status_code`) czy wyjątek.

Kod demonstracyjny jest pod `if __name__ == '__main__'`.
"""
from pprint import pprint

import requests

# jeżeli kiedyś ktoś będzie myślał o asyncio
# to lepiej użyć httpx

if __name__ == '__main__':
    url_szablon = 'https://api.nbp.pl/api/exchangerates/rates/{}/{}/?format=json'
    tabela = 'a'
    waluta = 'usdasdasd'
    url = url_szablon.format(tabela, waluta)
    r = requests.get(url)
    # if r.status_code == 200:
    #     pprint(j := r.json())
    #     print(j['rates'][0]['mid'])
    # else:
    #     print('Błąd HTTP', r.status_code)
    r.raise_for_status()
    # walrus: zapis sparsowanej odpowiedzi do j i od razu przekazanie
    # jej do pprint - wymaga Pythona >= 3.8
    pprint(j := r.json())
    print(j['rates'][0]['mid'])
