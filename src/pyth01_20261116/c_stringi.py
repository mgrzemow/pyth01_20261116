"""
Ćwiczenia z napisów: imię i nazwisko, zliczanie, maskowanie numeru karty,
rozbiór adresu e-mail, słowa w zdaniu, formatowanie daty.

Każde zadanie poprzedza jego treść w napisie wieloliniowym, a rozwiązanie
jest bezpośrednio pod nim. Cały kod jest pod `if __name__ == '__main__'`.
"""

if __name__ == '__main__':
    '''
    Dane: imie = "jan", nazwisko = "KOWALSKI".
    Wypisz poprawnie zapisane imię i nazwisko oraz inicjały.
    '''
    imie = "jan"
    nazwisko = "KOWALSKI"

    # capitalize() - pierwsza litera duża, reszta małe
    i_n = f'{imie.capitalize()} {nazwisko.capitalize()}'
    print(i_n)

    # [0] - pierwszy znak napisu
    inicjaly = f'{imie[0].upper()}.{nazwisko[0].upper()}.'
    print(inicjaly)

    '''
    Dane: zdanie = "Ala ma kota, a kot ma Alę". Wypisz długość napisu,
    ile razy występuje "ma" i ile jest liter „a” bez względu na wielkość.
    '''
    zdanie = "Ala ma kota, a kot ma Alę"
    print(len(zdanie))
    print(zdanie.count('ma'))
    # "bez względu na wielkość" - najpierw sprowadzamy wszystko do małych liter
    print(zdanie.lower().count('a'))

    '''
    Dane: numer = "1234567890123456". Wypisz numer tak,
    żeby widoczne były tylko cztery ostatnie cyfry, a reszta zastąpiona gwiazdkami.
    '''
    numer = "1234567890123456"
    # wycinanka od -4 do końca
    ostatnie_4 = numer[-4:]
    ilosc_cyfr = len(numer)
    # mnożenie napisu przez int powiela go
    wynik = '*' * (ilosc_cyfr - 4) + ostatnie_4
    print(wynik)

    '''
    Dane: email = " Jan.Kowalski@Example.COM ".
    Usuń spacje, zamień na małe litery, wypisz osobno login i domenę.
    '''
    email = " Jan.Kowalski@Example.COM "

    # defensywne sprawdzenie typu: `is not None` i porównanie typów przez `is`
    # (type(x) is str jest ściślejsze niż isinstance - nie uwzględnia podklas)
    if email is not None and type(email) is str:
        # metody można łączyć w łańcuch, bo każda zwraca nowy napis
        email = email.strip().lower()
        podzielone = email.split('@')
        print(f'Login: {podzielone[0]}, domena: {podzielone[1]}')

    '''
    Dane: zdanie = "Uczę się Pythona od wczoraj".
    Wypisz liczbę słów oraz pierwsze i ostatnie słowo.
    Wynik: 5, Uczę, wczoraj
    '''
    zdanie = "Uczę się Pythona od wczoraj"

    # split() bez argumentu dzieli po dowolnych białych znakach
    print(len(zdanie.split()))
    print(zdanie.split()[0])
    print(zdanie.split()[-1])

    '''
    Dane: data = "2026-11-17".
    Wytnij rok, miesiąc i dzień, a potem wypisz datę w polskim formacie.

    Wynik: 17.11.2026
    '''
    data = "2026-11-17"
    # sposób 1: wycinanki o stałych pozycjach
    rok = data[:4]
    miesiac = data[5:7]
    dzien = data[-2:]
    print(f'{dzien}.{miesiac}.{rok}')

    # sposób 2: split + rozpakowanie (unpacking) listy do trzech zmiennych
    rok, miesiac, dzien = data.split('-')
    print(f'{dzien}.{miesiac}.{rok}')
