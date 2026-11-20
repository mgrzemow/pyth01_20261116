"""
Słowniki (`dict`): dostęp przez klucz, sprawdzanie obecności klucza,
iteracja, łączenie słowników (`**`, `update`, `|`).

Notatki ze szkolenia. Cały kod demonstracyjny jest pod
`if __name__ == '__main__'`.
"""

if __name__ == '__main__':
    d = {
        'ola': 'warszawa',
        'paweł': 'kraków',
        'zosia': 'kielce',
        'leon': 'kielce',
    }

    # gdzie mieszka dana osoba
    print(d['ola'])
    # uwaga - dostęp przez nieistniejący klucz daje KeyError
    # print(d['ula'])
    # przypisanie pod nowy klucz dodaje parę do słownika
    d['ula'] = 'lublin'
    print(d['ula'])

    # jak sprawdzić
    imie = 'leon'
    if imie in d:
        print(d[imie])

    # in nie sprawdza wartości
    # (sprawdza tylko klucze; wartości: 'warszawa' in d.values())
    print('warszawa' in d)

    print(d)
    # przypisanie pod istniejący klucz nadpisuje wartość
    d['ula'] = 'warszawa'
    print(d)
    d['kasiaa'] = 'ełk'
    d['kasia'] = 'ełk'
    print(d)
    del(d['kasiaa'])
    print(d)

    # jak nie wiadomo o co chodzi to chodzi o klucz

    # iteracja po słowniku to iteracja po kluczach
    for klucz in d:
        print(klucz, d[klucz])

    # items() zwraca widok par (klucz, wartość) - w pętli rozpakowujemy
    # każdą parę do dwóch zmiennych
    for klucz, wartosc in d.items():
        print(klucz, wartosc)

    # jak stworzyć pusty:
    d = {}

    # trochę bardziej zaawansowanych
    d = {1: 11, 2:22}
    # stary sposób
    # ** rozpakowuje słownik do literału; przy powtórzonym kluczu
    # wygrywa ten, który stoi dalej na prawo
    d1 = {**d, 2: 222, 3:333, 4:444}
    print(d1)
    d1 = {2: 222, 3:333, 4:444, **d}
    print(d1)

    # metoda update
    d1 = {2: 222, 3:333, 4:444}
    # wlej dane z d do d1
    # update modyfikuje d1 w miejscu (zwraca None)
    d1.update(d)
    print(d1)

    # od 3.9: najnowsza składnia |
    # operator | zwraca NOWY słownik - wymaga Pythona >= 3.9
    d1 = {2: 222, 3:333, 4:444} | d
    print(d1)
    d1 = d | {2: 222, 3:333, 4:444}
    print(d1)

    # |= modyfikuje w miejscu, tak jak update - wymaga Pythona >= 3.9
    d1 |= {5:5555, 6:6666}
    print(d1)

    # a co jak kasia mieszka w 2 miastach
    # wartością może być dowolny obiekt, np. lista
    d = {'kasia': ['warszawa', 'kraków']}
