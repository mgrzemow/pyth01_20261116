"""
Napisy (`str`): literały, operatory, metody, indeksowanie i wycinanki.

Notatki ze szkolenia. Moduł nie definiuje funkcji ani klas; cały kod
demonstracyjny znajduje się pod `if __name__ == '__main__'`, dzięki czemu
import modułu niczego nie wypisuje.

Przydatne linki:

- [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#formatspec)
"""

if __name__ == '__main__':
    x = 'mama'
    print(type(x))

    # apostrofy i cudzysłowy są równoważne - wybór zależy tylko od tego,
    # jakiego znaku NIE chcemy escape'ować wewnątrz napisu
    x = 'mama'
    y = "mama"
    print(x == y)

    x = '<a href="http://google.com">'
    y = "<a href=\"http://google.com\">"
    print(x == y)

    # potrójne cudzysłowy - napis wieloliniowy, znaki nowej linii
    # trafiają do napisu dosłownie
    x = 'linia1\nlinia2\nlinia3\n'
    y = '''linia1
linia2
linia3
'''
    print(x == y)

    # raw strings - do ścieżek i regexów
    # prefiks r wyłącza interpretację sekwencji \n, \t, \\ itd.
    x = 'c:\\dev\\projects'
    y = r'c:\dev\projects'
    print(x == y)

    # byte strings - TO NIE SĄ NAPISY!!!
    # bytes to ciąg liczb 0-255, str to ciąg znaków Unicode;
    # przejście między nimi to .encode() / .decode() z podanym kodowaniem
    x = b'abc'
    print(type(x))

    x = 'ala'
    # co ja mogę zrobić z napisem?

    # czy jakiś napis jest w napisie
    y = 'ala ma kota'

    # WAŻNE - in zawsze odpowie czy coś jest w czymś
    # (operator in wywołuje pod spodem metodę specjalną __contains__)
    print(x in y)

    # można stringi sklejać +
    print('ala' + ' ma kota')

    # można stringi mnożyć przez int
    print(3 * 'ala')

    # brzydka pułapka:
    # bo wyobraźmy sobie, że mam w x napis zamiast liczby
    # jestem niesłusznie PEWIEN że to jest liczba
    x = '12'
    print(float(3 * x))

    # budowa napisów z kawałków
    imie = 'Jan'
    wiek = 34.2312312
    waga = 78.12312312
    wzrost = 178
    # f stringi
    # https://docs.python.org/3/library/string.html#formatspec

    # sklejanie przez + wymaga ręcznej konwersji str() każdej liczby
    print(imie + ' ma ' + str(wiek) + ' lat, waży ' + str(waga) + ' kg i ma ' + str(wzrost) + ' cm wzrostu.')
    # f-string: wyrażenie w {} jest obliczane, a po dwukropku stoi
    # specyfikacja formatu: ^12 - wyśrodkuj na 12 znakach, .2f - 2 miejsca po kropce
    print(f'{imie:^12} ma {wiek:.0f} lat, waży {waga:.2f} kg i ma {wzrost} cm wzrostu.')

    # f stringi są gadżetem opartym na metodzie .format

    # niemutowalność
    # napisu nie da się zmienić w miejscu - każda metoda zwraca NOWY napis
    x = 'mama'
    # upper zwraca kopię - tu nie przypisuje wiecc nic sie nie zmienia
    x.upper()
    print(x)
    # a tu przypisuje koppie do zmiennej
    x = x.upper()
    print(x)

    # metody informacyjne
    x = 'mama'
    print(x.isdigit())
    print(x.isalpha())
    print(x.islower())
    print(x.isupper())
    print(x.endswith('a'))
    print(x.startswith('ma'))
    # wielkości znaków
    x = 'ala ma kota'
    print(x.upper())
    print(x.lower())
    print(x.title())
    print(x.capitalize())
    # szukanie
    print('ma' in x)
    # z indeksem
    # zwraca -1 jak nie znajdzie
    print(x.find('mk'))
    # wywala się jak nie znajdzie
    # print(x.index('mk'))

    # zamiana
    print(x.replace('ala', 'beata'))

    # czyszczenie
    # z whitespaceów
    x = ' \t\n ala  ma  \t kota\n\t \n'
    print(x)
    # ale jak zobaczyć dokładnie co siedzi w napisie
    # repr() pokazuje napis tak, jak zapisalibyśmy go w kodzie,
    # z widocznymi \n i \t
    print(repr(x))
    print(repr(x.lstrip()))
    print(repr(x.rstrip()))
    print(repr(x.strip()))

    # najczęściej
    x = 'Ala\n'
    print(repr(x))
    print(repr(x.strip()))

    # usuwanie przedrostków i przyrostków
    # removesuffix / removeprefix - wymaga Pythona >= 3.9
    x = 'BEGIN ala ma kota END'
    print(x.removesuffix('END'))
    print(x.removeprefix('BEGIN'))

    # podział napisu na kawałki
    x = 'ala ma kota'
    print(x.split(' '))
    # fajny gadżet
    x = '  ala  ma \t\n kota\n'
    print(x.split(' '))
    # każdy ciąg whitespace to separator
    # split() bez argumentu dodatkowo pomija puste kawałki
    print(x.split())
    # jak złączyć z powrotem

    # join jest metodą SEPARATORA, a argumentem jest dowolna sekwencja napisów
    x = ['ala', 'ma', 'kota']
    print(' <-> '.join(x))

    # w środku wyrażenie listowe (list comprehension) - patrz funkcyjne.py
    x = ['ala\n', 'Ola ', 'karol', 'Ala']
    print(' -- '.join([imie.strip().capitalize() for imie in x]))

    # wybór znaków - indeksowanie
    # UWAGA - tak samo będzie dla list i np dla rekordow w bazie danych
    # czy wierszy/kolumn w macierzacch danych

    x = 'abcdefgh'
    # indeksy dodatnie - od 0
    print(x[0])
    print(x[1])
    print(x[7])
    # indeksy ujemne - od końca - od -1
    print(x[-1])
    print(x[-2])
    print(x[-8])

    # Zakresy, czyli slice, czyli wycinanki
    # x[od_wlacznie:do_wylacznie]
    # wycinanka nigdy nie rzuca IndexError - indeksy poza zakresem są przycinane
    x = 'abcdefgh'
    print(x[1:4])

    # można pomijać jedną z liczb
    # ostatnie 3
    print(x[-3:])
    # pierwsze 2:
    print(x[:2])
    # wszystkie poza pierwszymi 3:
    print(x[3:])
    # wszystkie poza ostatnimi 2:
    print(x[:-2])

    # x[:n] + x[n:] zawsze daje cały napis
    print(x[:2] + x[2:])

    # trzeci parametr: krok
    print(x[1:-1:2])

    # najczęściej - odwrócenie napisu
    # krok -1 czyta od końca
    print(x[::-1])

    # formatowania f-stringów
    x = 'ala'
    print(f'>{x:^10}<')
