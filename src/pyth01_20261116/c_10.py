'''
Ćwiczenie:

Z pliku tekstowego w formacie:
Jan 888999777
Ola 333444555
Paweł 111222333
Ula 333444000

wczytac słownik w postaci:
{'Jan': '888999777',
 ...
}

Następnie napisać pętlę w której użytkownik będzie podawał imiona
a program będzie podawał numery telefonów, lub komunikat, że nie ma takiego numeru
w książce telefonicznej. Warunkiem wyjścia z pętli będzie podanie 'koniec' zamiast imienia.

Rozszerzenia ćwiczenia:
 - jeżeli numeru nie ma w książce, to użytkownik może go dodać

'''

if __name__ == '__main__':
    with open('telefony.txt', 'rt', encoding='utf-8') as f:
        ksiazka_tel = {}
        for linia in f:
            imie, tel = linia.split()
            # dodanie do slownika
            ksiazka_tel[imie.lower()] = tel
    print(ksiazka_tel)
    while (imie := input('Podaj imie: ').lower()) != 'koniec':
        if imie in ksiazka_tel:
            print(f'Nr telefonu do {imie.capitalize()}: {ksiazka_tel[imie]}')
        else:
            if input(f'Nie mam nr telefonu do {imie.capitalize()}, czy chcesz dodać [t]') == 't':
                tel = input(f'Podaj nr telefonu do {imie.capitalize()}: ')
                ksiazka_tel[imie.lower()] = tel
                with open('telefony.txt', 'at', encoding='utf-8') as f:
                    f.write(f'{imie} {tel}\n')

