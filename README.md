# Python - kurs 5-dniowy

Materiały z pięciodniowego szkolenia z języka Python, prowadzonego przez
**Michała Grzemowskiego** dla AltKom.
([LinkedIn](https://www.linkedin.com/in/michal-grzemowski-trainer/)).

Repozytorium zawiera notatki pisane na żywo w trakcie zajęć oraz rozwiązania
ćwiczeń. Każdy plik w `src/pyth01_20261116/` to osobna notatka lub ćwiczenie:
treść zadania i omówienie są w docstringu modułu, definicje funkcji i klas na
poziomie modułu, a kod demonstracyjny pod `if __name__ == '__main__':`, dzięki
czemu moduły można zarówno uruchamiać jako skrypty, jak i importować.

## Uruchamianie

Projekt zarządzany jest przez [uv](https://docs.astral.sh/uv/), wymaga
Pythona 3.14 lub nowszego.

```
uv sync
cd src\pyth01_20261116
uv run python napisy.py
```

Skrypty, które czytają pliki z danymi (`towary.txt`, `telefony.txt`,
`emails.txt`, `imiona_miasta.txt`), trzeba uruchamiać z katalogu
`src\pyth01_20261116`, bo ścieżki są względne.

## Dokumentacja

Dokumentacja HTML generowana z docstringów przez
[pdoc3](https://pdoc3.github.io/pdoc/) jest w katalogu `docs/html/`;
punkt wejścia: `docs/html/pyth01_20261116/index.html`.
Żeby ją odświeżyć po zmianach w kodzie:

```
generuj_dokumentacje.bat
generuj_dokumentacje.bat otworz    # dodatkowo otwiera index.html w przeglądarce
```

## Co jest gdzie

### Podstawy języka

| Plik | Temat |
|---|---|
| `napisy.py` | napisy: literały, raw strings, bytes, metody, f-stringi, indeksowanie i wycinanki |
| `c_stringi.py` | ćwiczenia z napisów (inicjały, maskowanie numeru karty, rozbiór e-maila, data) |
| `listy_krotki.py` | listy, krotki, `namedtuple`, rozpakowywanie (unpacking) |
| `zbiory.py` | zbiory, usuwanie duplikatów |
| `slowniki.py` | słowniki: dostęp, iteracja, łączenie (`**`, `update`, `\|`) |
| `slowniki_agregaccja.py` | zliczanie i grupowanie: `get`, `setdefault`, `defaultdict` |
| `petla_for.py` | pętla `for`, `enumerate` |
| `petla_while.py` | pętla `while`, operator walrus `:=` |
| `bledy.py` | wyjątki: `try` / `except` / `else` / `finally`, `raise` |
| `funkcje.py` | funkcje: parametry, `*args` / `**kwargs`, zakresy (LEGB), domknięcia, pułapki |
| `funkcyjne.py` | funkcja jako obiekt, `lambda`, `lru_cache`, comprehensions, `all` / `any` |

### Moduły i importy

| Plik | Temat |
|---|---|
| `moje_funkcje.py` | moduł do importowania, zachowanie `__name__` |
| `modul_importujacy.py` | sposoby importu, dlaczego nie `from x import *` |
| `konfiguracja.py` | "stałe" we wspólnym module |

### Pliki i system

| Plik | Temat |
|---|---|
| `pliki.py` | `open`, tryby, `with` |
| `system_plikow_i_os.py` | `pathlib` od A do Z: ścieżki, czytanie i pisanie, kopiowanie, ZIP, `glob`, `walk`, `os` i `sys` |
| `json_dlaczego_kochamy.py` | JSON kontra pickle |

### Programowanie obiektowe

| Plik | Temat |
|---|---|
| `obiektowo.py` | klasa, `__init__`, `self`, atrybuty klasy i instancji |
| `dziedziczenie.py` | dziedziczenie, `super()`, `__slots__`, fabryka obiektów |
| `deskryptor_property.py` | `property`: getter i setter |
| `c_12.py` | ćwiczenie Spychacz: metody specjalne (`__repr__`, `__eq__`, `__lt__`, `__getitem__`, `__call__`...) |
| `c_13.py` | własny menedżer kontekstu (`Stoper`), `list.insert` kontra `deque` |
| `c_sharp_operator.py` | emulacja operatorów `?.` i `??` z C# |

### Sieć i współbieżność

| Plik | Temat |
|---|---|
| `odczyt_z_rest_api.py` | REST API NBP przez `requests`, obsługa błędu HTTP |
| `c_14.py` | wycena koszyka walut: wersja naiwna (500 zapytań) |
| `c_14_cacche.py` | ... z pamięcią podręczną `lru_cache` (5 zapytań) |
| `c14_concurrent_futures.py` | ... równolegle przez `ProcessPoolExecutor` |

### Ćwiczenia

Treść każdego zadania jest w docstringu pliku.

| Plik | Zadanie |
|---|---|
| `c_1.py` | powitanie z konsoli |
| `c_2.py` | netto i VAT z kwoty brutto |
| `c_3.py` | sekundy na h:m:s, funkcja zwracająca krotkę |
| `c_4.py` | pole trójkąta ze wzoru Herona |
| `c_5.py` | rok przestępny |
| `c_6.py` | czy trójkąt jest prostokątny (`math.isclose`) |
| `c_7.py` | powitania z pliku `imiona_miasta.txt` |
| `c_8.py`, `c_8_1.py`, `c_8_2.py` | paragon z pliku `towary.txt` w trzech wersjach: jednoprzebiegowa, lista rekordów, funkcje i słownik |
| `c_9.py` | lista imion z konsoli, powitanie zależne od końcówki |
| `c_10.py` | książka telefoniczna z pliku `telefony.txt` |
| `c_11.py` | grupowanie adresów z `emails.txt` po domenach i zapis do plików |

### Pliki z danymi

`towary.txt`, `telefony.txt`, `emails.txt`, `imiona_miasta.txt` - dane
wejściowe do ćwiczeń; `gmail.com.txt`, `o2.pl.txt`, `onet.pl.txt` - wynik
działania `c_11.py`.

## Licencja

Materiały są udostępnione na licencji
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl)
(Uznanie autorstwa - Użycie niekomercyjne - Na tych samych warunkach).
Możesz z nich korzystać i je modyfikować, podając autora i nie używając ich
komercyjnie; przeróbki udostępniaj na tej samej licencji. Pełny tekst: plik `LICENSE`.
