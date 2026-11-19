"""
Ćwiczenie:

 1. Wczytać z konsoli długości 3 boków trójkąta
 2. Policzyć pole takiego trójkąta ze wzoru Herona
 3. Wypisać wynik na ekran

 Podpowiedzi:
 - Podniesienie do potęgi 1/2 to to samo co pierwiastkowanie - 4 ** 0.5 == 2
 - zawsze musimy stosować operatory - wyrażenie 3(4+7) jest niepoprawne, musi być 3*(4+7)
 - typ obiektu możemy sprawdzić za pomocą type(), np dla zmiennej x i typu str: if type(x) == str

 Rozszerzenia ćwiczenia:
 - jak stwierdzić, że trójąta o podanych bokach nie da się zbudować?
 - alternatywnie użyć math.sqrt

"""
import math

if __name__ == '__main__':
    a = float(input('Podaj bok: '))
    b = float(input('Podaj bok: '))
    c = float(input('Podaj bok: '))
    p = (a + b + c) / 2
    x = p * (p - a) * (p - b) * (p - c)
    if x < 0:
        print('Takiego trójkąta nie da się zbudować')
    else:
        s = math.sqrt(x)
        print('Pole trójkąta:', s)
