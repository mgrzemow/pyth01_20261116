# funkcja jako obiekt
def f1():
    print('f1')
# co to jest callable - normalny obiekt
f1()
f1.__call__()

# takie callable moge stworzyć również jako lambde

x = ['floraian', 'zad', 'grog']

def f2(slowo):
    return slowo[::-1]

x.sort(key=f2)
print(x)

x.sort(key=lambda slowo: slowo[::-1])
print(x)

# jak napisać funkcje, która posortuje:
x = ['Grzegorz Nowak', 'Zenon Adamek', 'Piotr Adamek']
# po nazwiskach, a jak nazwiska są takie same to po imionach
