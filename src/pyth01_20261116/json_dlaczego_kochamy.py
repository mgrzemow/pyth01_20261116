import pickle
import json
import re
r = re.compile(r'\d\d')
dane_ok_dla_json = {
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

dane_nie_ok_dla_json = {
    'imie': 'Jan',
    'wiek': 23,
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
# jak wyciągnąć nr domu w drugim adresie:
# d['adresy'][1]['nr']

with open('dane.json', 'wt', encoding='utf-8') as f:
    json.dump(dane_ok_dla_json, f, indent=2, ensure_ascii=False)


with open('dane.json', 'r', encoding='utf-8') as f:
    d1 = json.load(f)

print(d1 == dane_ok_dla_json)

with open('dane.pickle', 'wb') as f:
    pickle.dump(dane_nie_ok_dla_json, f)

# uwaga - podczas odczytu z pickle wykonuje się kod
# nie wolno odpiklowywać nieznanych plików
with open('dane.pickle', 'rb') as f:
    d2 = pickle.load(f)

print(d2 == dane_nie_ok_dla_json)
