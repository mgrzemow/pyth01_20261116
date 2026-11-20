"""
JSON kontra pickle: zapis i odczyt struktur danych.

- `json` zapisuje tylko podstawowe typy (`str`, `int`, `float`, `bool`,
  `None`, `list`, `dict` z kluczami-napisami), za to plik jest czytelny
  dla człowieka i dla każdego innego języka.
- `pickle` zapisze prawie dowolny obiekt Pythona (tu: skompilowany regex
  i klucz będący liczbą), ale format jest binarny, tylko pythonowy
  i **niebezpieczny** przy odczycie obcych plików.

Dane są na poziomie modułu (można je importować), a zapis/odczyt plików
`dane.json` i `dane.pickle` w bieżącym katalogu jest pod
`if __name__ == '__main__'`.
"""
import json
import pickle
import re
from typing import Any

r = re.compile(r'\d\d')
"""Skompilowany wyrażenie regularne - obiekt, którego JSON nie potrafi zapisać."""

dane_ok_dla_json: dict[str, Any] = {
    'imie': 'Jan',
    'wiek': 23,
    'adresy': [
        {
            'miasto': 'Kraków',
            'ulica': 'Wolności',
            'nr': '15A'
        },
        {
            'miasto': 'Warszawa',
            'ulica': 'Źródlana 11',
            'nr': '22C'
        },
    ]
}
"""Zagnieżdżona struktura z samych typów podstawowych - JSON ją zapisze 1:1."""

# dict[str | int, Any] - klucze mieszane; str | int wymaga Pythona >= 3.10
dane_nie_ok_dla_json: dict[str | int, Any] = {
    'imie': 'Jan',
    'wiek': 23,
    # klucz 12 JSON po cichu zamieniłby na napis "12";
    # wartość r (regex) wywaliłaby json.dump z TypeError
    12: r,
    'adresy': [
        {
            'miasto': 'Kraków',
            'ulica': 'Wolności',
            'nr': '15A'
        },
        {
            'miasto': 'Warszawa',
            'ulica': 'Źródlana 11',
            'nr': '22C'
        },
    ]
}
"""Struktura z regexem i kluczem int - do zapisu nadaje się tylko pickle."""

# jak wyciągnąć nr domu w drugim adresie:
# d['adresy'][1]['nr']

if __name__ == '__main__':
    # dump pisze do pliku (dumps zwraca napis); indent=2 formatuje czytelnie,
    # ensure_ascii=False zostawia polskie znaki zamiast sekwencji ź
    with open('dane.json', 'wt', encoding='utf-8') as f:
        json.dump(dane_ok_dla_json, f, indent=2, ensure_ascii=False)

    with open('dane.json', 'r', encoding='utf-8') as f:
        d1 = json.load(f)

    # po drodze przez plik odtworzyła się identyczna struktura
    print(d1 == dane_ok_dla_json)

    # pickle to format binarny - tryb 'wb' / 'rb', bez encoding
    with open('dane.pickle', 'wb') as f:
        pickle.dump(dane_nie_ok_dla_json, f)

    # uwaga - podczas odczytu z pickle wykonuje się kod
    # nie wolno odpiklowywać nieznanych plików
    with open('dane.pickle', 'rb') as f:
        d2 = pickle.load(f)

    print(d2 == dane_nie_ok_dla_json)
