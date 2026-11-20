"""
Pętla `for`: wykonaj operację dla każdego elementu obiektu iterowalnego,
a gdy naprawdę potrzebny jest indeks - `enumerate()`.

Notatki ze szkolenia. Kod demonstracyjny jest pod `if __name__ == '__main__'`.
"""

if __name__ == '__main__':
    napis = 'abcd'

    # wykonaj operacje dla wszystkichce elementów jakiegoś obiektu
    # for działa z każdym obiektem iterowalnym (iterable): napis, lista,
    # krotka, słownik, zbiór, plik, range()... - nie ma tu licznika ani indeksu
    for znak in napis:
        print(znak)

    lista = [1, 2, 3, 4]
    for elem in lista:
        print(elem)

    # Najczęściej NIE potrzebujemy indeksów, żeby wykonać operację dla
    # wszystkich elementów struktury danych - for daje nam od razu element.
    # Pętla "po indeksach" w stylu innych języków to w Pythonie zły nawyk:
    # for i in range(len(lista)):
    #     print(lista[i])

    # Jeżeli indeks jest naprawdę potrzebny (np. numeracja na wydruku),
    # używamy enumerate() - zwraca pary (indeks, element), które rozpakowujemy
    # w nagłówku pętli
    imiona = ['Ola', 'Ala', 'Karol']
    for i, imie in enumerate(imiona):
        print(i, imie)

    # start= ustawia, od czego zacząć liczyć (domyślnie 0)
    for nr, imie in enumerate(imiona, start=1):
        print(f'{nr}. {imie}')
