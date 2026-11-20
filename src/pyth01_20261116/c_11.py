"""
Ćwiczenie:

1. Wczytujemy adresy email z podanego pliku tekstowego emails.txt
2. Pogrupować adresy email po domenach, jedncześnie pozbywając się duplikatów. Proponuję format:
{
'gmail.com': {'ala@gmail.com', 'ela@gmail.com'}
...
}
3. Zapisujemy adresy email do plików o nazwie pochodzącej od nazwy domeny,
   wg schematu:
   np wszystkie adresy @gmail.com mają zostać zapisane w pliku gmail.com.txt

Podpowiedzi:
 - nazwę domeny można wyciąć z adresu znajdując znak @

Idea: słownik grupuje (klucz = domena), a zbiór jako wartość sam usuwa
duplikaty. To ten sam wzorzec "grupowania" co w `slowniki_agregaccja.py`.
Skrypt czyta `emails.txt` i tworzy pliki `<domena>.txt` w bieżącym katalogu.
"""
from pprint import pprint

if __name__ == '__main__':
    with open('emails.txt', 'rt', encoding='utf-8') as f:
        slownik_maili = {}
        for linia in f:
            # łańcuch metod: każda zwraca nowy napis, który przetwarza następna
            # removesuffix - wymaga Pythona >= 3.9
            linia = linia.strip().removesuffix(',').lower()
            if '@' in linia:
                print(linia)
                # wydłubać domenę
                # unpacking do dwóch zmiennych; _ = "login mnie nie interesuje"
                _, domena = linia.split('@')
                # sprawdzić czy jest w słowniku
                if domena not in slownik_maili:
                    slownik_maili[domena] = set()
                # dodac
                # (add na zbiorze ignoruje duplikaty - stąd brak sprawdzania)
                slownik_maili[domena].add(linia)
    pprint(slownik_maili)
    # dla wszystkich domen
    for domena, zbior_maili in slownik_maili.items():
        # otworczyć plik
        with open(f'{domena}.txt', 'wt', encoding='utf-8') as f:
            # dla wszyskich adresów
            for email in zbior_maili:
                # dopisac plik
                f.write(email + '\n')
