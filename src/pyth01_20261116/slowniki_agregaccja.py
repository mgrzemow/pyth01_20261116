slowa = 'mama mama tata tata mama ja'
# {
#     'mama': 3,
#     'tata': 2,
#     'ja': 1,
# }

d = {}
for slowo in slowa.split():
    # jak pierwszy raz:
    if slowo not in d:
        d[slowo] = 1
    # a jak już było
    else:
        d[slowo] += 1

d = {}
for slowo in slowa.split():
    # get zwraza wartość ze słownika lub wartosc domyślną
    d[slowo] = d.get(slowo, 0) + 1

# collections.defaultdict - potęga - bardzo fajne w
# realnych scenariuszach

import collections

# funkcja wyliczająca wartość domyślną
def f1():
    return 0

d = collections.defaultdict(f1)
for slowo in slowa.split():
    d[slowo] += 1
print(d)

d = collections.defaultdict(lambda: 0)
for slowo in slowa.split():
    d[slowo] += 1
print(d)

d = collections.defaultdict(int)
for slowo in slowa.split():
    d[slowo] += 1
print(d)

x = 'ala alicja alina beata bartek'
{
    'a': ['ala', 'alicja', 'alina'],
   'b': ['beata', 'bartek']
}

d = {}
for slowo in x.split():
    pl = slowo[0]
    # jeżeli nie było do tej pory klucza - zainicjuj pustą listę
    if pl not in d:
        d[pl] = []
    d[pl].append(slowo)
print(d)

d = {}
for slowo in x.split():
    pl = slowo[0]
    lista = d.get(pl, [])
    lista.append(slowo)
    d[pl] = lista
print(d)

# 
d = collections.defaultdict(list)
for slowo in x.split():
    pl = slowo[0]
    d[pl].append(slowo)
print(d)

# .setdefault robi to co get i dodaje od slownika
d = {}
for slowo in x.split():
    pl = slowo[0]
    d.setdefault(pl, []).append(slowo)

