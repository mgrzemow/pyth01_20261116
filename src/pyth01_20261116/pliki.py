# tryby:
# Pierwszy znak:
# r - read
# w - write
# a - append
# Drugi znak:
# t - text
# b - binary


with open('c_stringi.py', 'rt', encoding='utf-8') as f:
    print(f.read())

# można czytać od razu ze ścieżek
# import pathlib
# sciezka = pathlib.Path(__file__).parent / 'napisy.py'
# print(sciezka.read_text(encoding='utf-8'))

# with open('c_stringi.py', 'rt', encoding='utf-8') as f:
#     for linia in f:
#         print(repr(linia))

with open('tmp.txt', 'wt', encoding='utf-8') as f:
    f.write('line 1\n')
    f.write('line 2\n')
    f.write('line 3\n')
    x = 9 / 0
    f.write('line 4\n')
    print(f.closed)
print(f.closed)

