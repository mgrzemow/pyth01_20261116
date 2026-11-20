"""
Ćwiczenie:

Z pliku tekstowego w formacie:
Jan 888999777
Ola 333444555
Paweł 111222333
Ula 333444000

wczytac słownik w postaci:
{'Jan': '888999777',
 ...
}

Następnie napisać pętlę w której użytkownik będzie podawał imiona
a program będzie podawał numery telefonów, lub komunikat, że nie ma takiego numeru
w książce telefonicznej. Warunkiem wyjścia z pętli będzie podanie 'koniec' zamiast imienia.

Rozszerzenia ćwiczenia:
 - jeżeli numeru nie ma w książce, to użytkownik może go dodać

Skrypt czyta (i dopisuje do) `telefony.txt` w bieżącym katalogu.
Klucze słownika są trzymane małymi literami, żeby wyszukiwanie nie zależało
od wielkości liter.
"""

if __name__ == '__main__':
    with open('telefony.txt', 'rt', encoding='utf-8') as f:
        ksiazka_tel = {}
        for linia in f:
            imie, tel = linia.split()
            # dodanie do slownika
            ksiazka_tel[imie.lower()] = tel
    print(ksiazka_tel)
    # walrus (wymaga Pythona >= 3.8): wynik input().lower() trafia do imie
    # i od razu jest porównywany z 'koniec'
    while (imie := input('Podaj imie: ').lower()) != 'koniec':
        # in na słowniku sprawdza klucze
        if imie in ksiazka_tel:
            print(f'Nr telefonu do {imie.capitalize()}: {ksiazka_tel[imie]}')
        else:
            if input(f'Nie mam nr telefonu do {imie.capitalize()}, czy chcesz dodać [t]') == 't':
                tel = input(f'Podaj nr telefonu do {imie.capitalize()}: ')
                ksiazka_tel[imie.lower()] = tel
                # tryb 'a' (append) dopisuje na końcu pliku zamiast go nadpisywać
                with open('telefony.txt', 'at', encoding='utf-8') as f:
                    f.write(f'{imie} {tel}\n')
