"""
Ćwiczenie:
Napisać program, który:
 1. Wczytuje imię z konsoli
 2. Wypisuje na konsolę: Cześć {imię} witaj na kursie pythona!

 Podpowiedzi:
 - input('napis') - wypisuje napis w konsoli i wczytuje napis
   wpisany przez użytkownika
 - print() - wypisuje w konsoli podane obiekty (np napisy)
"""

if __name__ == '__main__':
    imie = input('Podaj swoje imię: ')
    # print z kilkoma argumentami rozdziela je spacją (parametr sep=' ')
    print('Cześć', imie, 'witaj na kursie.')
