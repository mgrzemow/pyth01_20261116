'''

Dane: imie = "jan", nazwisko = "KOWALSKI".
Wypisz poprawnie zapisane imię i nazwisko oraz inicjały.

'''
imie = "jan"
nazwisko = "KOWALSKI"

i_n = f'{imie.capitalize()} {nazwisko.capitalize()}'
print(i_n)

inicjaly = f'{imie[0].upper()}.{nazwisko[0].upper()}.'
print(inicjaly)

'''
Dane: zdanie = "Ala ma kota, a kot ma Alę". Wypisz długość napisu, 
ile razy występuje "ma" i ile jest liter „a” bez względu na wielkość.
'''
zdanie = "Ala ma kota, a kot ma Alę"
print(len(zdanie))
print(zdanie.count('ma'))
print(zdanie.lower().count('a'))

'''
Dane: numer = "1234567890123456". Wypisz numer tak, 
żeby widoczne były tylko cztery ostatnie cyfry, a reszta zastąpiona gwiazdkami.'''
numer = "1234567890123456"
ostatnie_4 = numer[-4:]
ilosc_cyfr = len(numer)
wynik = '*' * (ilosc_cyfr - 4) + ostatnie_4
print(wynik)

'''
Dane: email = " Jan.Kowalski@Example.COM ". 
Usuń spacje, zamień na małe litery, wypisz osobno login i domenę.
'''

email = " Jan.Kowalski@Example.COM "

if email is not None and type(email) is str:
    email = email.strip().lower()
    podzielone = email.split('@')
    print(f'Login: {podzielone[0]}, domena: {podzielone[1]}')

'''
Dane: zdanie = "Uczę się Pythona od wczoraj". 
Wypisz liczbę słów oraz pierwsze i ostatnie słowo.
Wynik: 5, Uczę, wczoraj
'''

zdanie = "Uczę się Pythona od wczoraj"

print(len(zdanie.split()))
print(zdanie.split()[0])
print(zdanie.split()[-1])

'''
Dane: data = "2026-11-17". 
Wytnij rok, miesiąc i dzień, a potem wypisz datę w polskim formacie.

Wynik: 17.11.2026'''

data = "2026-11-17"
rok = data[:4]
miesiac = data[5:7]
dzien = data[-2:]
print(f'{dzien}.{miesiac}.{rok}')

rok, miesiac, dzien = data.split('-')
print(f'{dzien}.{miesiac}.{rok}')
