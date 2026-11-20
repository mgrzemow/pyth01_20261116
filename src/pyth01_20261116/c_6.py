"""
Ćwiczenie:

 1. Boki trójkąta mają długości:
  - b1 = 1
  - b2 = 2 ** 0.5 - to będzie nasza ew przeciwprostokątna
  - b3 = wartość podaną w konsoli przez użytkownika
 2. Sprawdzić czy trójkąt jest prostokątny i wypisać odpowiedni komunikat

 Podpowiedzi:
  - sprawdzić w konsoli ile jest 0.1 + 0.1 + 0.1
  - aby używać biblioteki math należy wykonać polecenie: import math
  - co to takiego math.isclose()?
  - mając kursor klawiatury na interesującej nas funkcji nacisnąć ctr-q
"""
import math

if __name__ == '__main__':
    b1 = 1
    b2 = 2 ** .5
    b3 = float(input('podaj bok: '))

    # liczby zmiennoprzecinkowe są przybliżeniami (0.1 + 0.1 + 0.1 != 0.3),
    # dlatego zamiast == porównujemy je przez math.isclose
    # \ na końcu linii kontynuuje instrukcję w następnej linii
    if math.isclose(b2 ** 2, b1 ** 2 + b3 ** 2) or \
            math.isclose(b3 ** 2, b1 ** 2 + b2 ** 2):
        print('prostokatny')
    else:
        print('nie prostokatny')
