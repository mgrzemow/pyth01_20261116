"""
Ćwiczenie:

 1. Wczytać z konsoli nr roku
 2. Sprawdzić czy rok jest przestępny.
 3. Wypisać odpowiedni komunikat

 Podpowiedzi:
    Rok jest przestępny jeżeli spełniony jest chociaż jeden z dwóch warunków:
    - dzieli się przez 400
    lub
    - dzieli się przez 4 i nie dzieli się przez 100

 Rozszerzenia ćwiczenia:
  - nie użyć w kodzie ani jednego dwukropka ':'
  - sprawdzić czy użytkownik podał całkowitą liczbę dodatnią > 0
"""

if __name__ == '__main__':
    rok = int(input('Podaj rok: '))
    d400 = rok % 400 == 0
    d4 = rok % 4 == 0
    d100 = rok % 100 == 0

    if d400 or d4 and not d100:
        print('przestępny')
    else:
        print('Nie przestępny')
