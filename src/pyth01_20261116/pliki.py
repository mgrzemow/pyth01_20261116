"""
Pliki: `open()`, tryby otwarcia, menedżer kontekstu `with`.

Notatki ze szkolenia. Kod demonstracyjny jest pod `if __name__ == '__main__'`;
czyta plik `c_stringi.py` i zapisuje `tmp.txt` w bieżącym katalogu, więc
skrypt trzeba uruchamiać z katalogu pakietu.

Pełniejsze omówienie plików i ścieżek (`pathlib`) jest w module
`system_plikow_i_os`.
"""

if __name__ == '__main__':
    # tryby:
    # Pierwszy znak:
    # r - read
    # w - write
    # a - append
    # Drugi znak:
    # t - text
    # b - binary

    # with = menedżer kontekstu: na wejściu otwiera plik, na wyjściu z bloku
    # ZAWSZE go zamyka (także gdy w środku poleci wyjątek) - patrz c_13.py
    # encoding podajemy jawnie, bo domyślne kodowanie zależy od systemu
    # (na polskim Windowsie cp1250) i polskie znaki by się posypały
    with open('c_stringi.py', 'rt', encoding='utf-8') as f:
        print(f.read())

    # można czytać od razu ze ścieżek
    # import pathlib
    # sciezka = pathlib.Path(__file__).parent / 'napisy.py'
    # print(sciezka.read_text(encoding='utf-8'))

    # plik jest iterowalny - for daje kolejne linie razem ze znakiem '\n'
    # with open('c_stringi.py', 'rt', encoding='utf-8') as f:
    #     for linia in f:
    #         print(repr(linia))

    # demonstracja: wyjątek wewnątrz with nie zostawia otwartego pliku
    # - w tmp.txt zostaną 3 linie, a f.closed po wyjściu z bloku będzie True
    try:
        with open('tmp.txt', 'wt', encoding='utf-8') as f:
            f.write('line 1\n')
            f.write('line 2\n')
            f.write('line 3\n')
            x = 9 / 0
            # tu już nie dojdziemy
            f.write('line 4\n')
            print(f.closed)
    except ZeroDivisionError:
        print('Wyjątek w bloku with - plik i tak został zamknięty.')
    # with nie tworzy nowego zakresu zmiennych - f jest nadal dostępne
    print(f.closed)
