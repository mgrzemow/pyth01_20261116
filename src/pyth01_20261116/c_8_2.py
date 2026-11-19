"""
Ćwiczenie:

Napisać program, który:

1. Wczytuje z pliku tekstowego dane:
 - nazwa towaru
 - ilość towaru
 - jednostka miary
 - cena

Plik jest w formacie:
Banany 2.4 kg 3.5
Kiwi 3 szt 2.3
Piwo 4 szt 2.4
Kiwi 3 szt 2.3


2. Po każdym towarze program dodaje dane do słownika zakupów w formacie:
{
'chleb': (3, 'szt', 4.6),
'cebula': (1.55, 'kg', 2.5)
}

3. Jeżeli towar już raz wystąpił i jest w słowniku to zamiast dodawać go
   drugi raz - zwiększamy ilość.

3. Używając danych ze słownika stowrzonego w pkt 2 wypisuje na ekran paragon w formie:
Pietruszka  2.0 kg x 4.60     9.20
Banany      3.0 kg x  3.5    10.50
----------------------------------
SUMA:                        19.70

Kolumny mają mieć szerokości:
nazwa - 12 znaków,
ilość - 2 znaki przed przecinkiem i 2 po
jednostka miary - 4 znaki
cena - 3 znaki przed przecinkiem i 2 po
wartość pozycji - 5 znaków przed i 2 po
SUMA - 7 znaków przed i 2 po

Podpowiedzi:
 - formatowanie f-stringow

 Rozszerzenia ćwiczenia:
 - co by było gdyby mógł wystąpić towar o różnych jednostkach miary.

"""

# w jaki sposób zediniować poszczególne parametry wejściowe

from pprint import pprint

if __name__ == '__main__':
    with open('towary.txt', 'rt', encoding='utf-8') as f:
        suma = 0
        paragon = ''
        #
        slownik_rekordow = {}
        for linia in f:
            linia = linia.strip()
            # podzielić linię na kawałki .split
            # przypisać do 4 zmiennych
            towar, ilosc, jm, cena = linia.split()

            # skonwertować
            ilosc = float(ilosc)
            cena = float(cena)

            #
            ilosc_do_tej_pory = 0
            if (towar, jm) in slownik_rekordow:
                ilosc_do_tej_pory = slownik_rekordow[(towar, jm)][0]
            rekord = [ilosc + ilosc_do_tej_pory, cena]
            slownik_rekordow[(towar, jm)] = rekord

    #
    for (towar,jm), (ilosc, cena) in slownik_rekordow.items():
        # policzyć wartosc
        wartosc = round(ilosc * cena, 2)
        # zwiększyć sumę
        suma = round(suma + wartosc, 2)
        # wyprodukować linię paragonu
        paragon += f'{towar:12} {ilosc:5.2f} {jm:4} x {cena:6.2f} {wartosc:8.2f}\n'
    # wypisać podsumowanie
    paragon += '-' * 41 + '\n'
    paragon += f'SUMA: {suma:35.2f}\n'
    print(paragon)


































