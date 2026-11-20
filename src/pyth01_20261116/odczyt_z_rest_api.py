from pprint import pprint

import requests

# jeżeli kiedyś ktoś będzie myślał o asyncio
# to lepiej użyć httpx

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
pprint(j := r.json())
print(j['rates'][0]['mid'])
