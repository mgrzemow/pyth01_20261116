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
d['ula'] = 'lublin'
print(d['ula'])

# jak sprawdzić
imie = 'leon'
if imie in d:
    print(d[imie])

# in nie sprawdza wartości
print('warszawa' in d)

print(d)
d['ula'] = 'warszawa'
print(d)
d['kasiaa'] = 'ełk'
d['kasia'] = 'ełk'
print(d)
del(d['kasiaa'])
print(d)

# jak nie wiadomo o co chodzi to chodzi o klucz

for klucz in d:
    print(klucz, d[klucz])

for klucz, wartosc in d.items():
    print(klucz, wartosc)

# jak stworzyć pusty:
d = {}

# trochę bardziej zaawansowanych
d = {1: 11, 2:22}
# stary sposób
d1 = {**d, 2: 222, 3:333, 4:444}
print(d1)
d1 = {2: 222, 3:333, 4:444, **d}
print(d1)

# metoda update
d1 = {2: 222, 3:333, 4:444}
# wlej dane z d do d1
d1.update(d)
print(d1)

# od 3.9: najnowsza składnia |
d1 = {2: 222, 3:333, 4:444} | d
print(d1)
d1 = d | {2: 222, 3:333, 4:444}
print(d1)

d1 |= {5:5555, 6:6666}
print(d1)

# a co jak kasia mieszka w 2 miastach
d = {'kasia': ['warszawa', 'kraków']}

