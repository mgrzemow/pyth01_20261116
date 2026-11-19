# pusty zbiór
s = set()

# wypełniony zbiór
s = {'ala', 'karol', 'ola', 'zosia', 'alabaster'}

print(type(s))
print(s)
for e in s:
    print(e)

print('ola' in s)
s.add('edward')
print(s)
s.remove('edward')
print(s)
s.add('ala')
print(s)
s.add(11)
print(s)
s.add(11.0)
print(s)
print(11 == 11.0)

# do pozbywania się duplikatów
x = ['ala', 'tomek', 'roman', 'ala', 'tomek', 'roman', 'ala', 'tomek', 'roman', 'ala', 'tomek', 'roman', ]
# unikalne wartoścci z x - UWAGA - tracę kolejność
print(set(x))
print(list(set(x)))

# jak wyrzucić duplikaty nie tracąc kolejności - słownikami
d = {}
for e in x:
    d[e] = None
print(list(d.keys()))

