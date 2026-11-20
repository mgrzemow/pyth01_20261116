"""
Python idzie w kierunku biblioteki pathlib jeśli chodzi o pliki.

Obsługa plików w Pythonie (pathlib) - demo na ok. 15 minut.

ZAŁOŻENIE: Python 3.14 lub nowszy.

Uruchomienie:   python pliki_pathlib_demo.py

Skrypt tworzy w bieżącym katalogu podkatalog tmp__files, wykonuje w nim
wszystkie operacje i na koniec go usuwa. Bieżący katalog zostaje po
uruchomieniu bez zmian. Jeżeli tmp__files już istnieje, skrypt niczego
nie rusza i kończy pracę.

Plan (czas w minutach):
    1. Ścieżki                          3
    2. Czytanie i pisanie               2
    3. Podstawowe operacje na plikach   3
    4. ZIP                              2
    5. glob                             1,5
    6. Chodzenie po katalogach          1,5
    7. Inne użyteczne z os i sys        2
"""

import atexit
import json
import os
import shutil
import sys
import zipfile
from datetime import datetime
from pathlib import Path

# Katalog roboczy: bezwzględna ścieżka do tmp__files w bieżącym katalogu.
TMP = Path.cwd() / "tmp__files"

if TMP.exists():
    # Nie kasujemy cudzych danych: sprzątamy tylko to, co sami utworzyliśmy.
    sys.exit(f"Katalog {TMP} już istnieje - usuń go albo uruchom skrypt gdzie indziej.")

TMP.mkdir()

# Sprzątanie: ta funkcja wykona się przy zakończeniu programu,
# także wtedy, gdy skrypt przerwie się błędem.
atexit.register(shutil.rmtree, TMP)


# ======================================================================
# 1. ŚCIEŻKI (3 min)
# ======================================================================
# Ścieżka to obiekt Path, a nie napis. Buduje się ją operatorem /,
# rozbiera atrybutami. Ten sam kod działa na Windowsie, Linuksie i macOS.
print("\n=== 1. Ścieżki ===")

# --- skąd zacząć ---
print(Path.cwd())                        # bieżący katalog
print(Path.home())                       # katalog domowy użytkownika

# Tak najczęściej!!!
print(Path(__file__).resolve().parent)   # katalog, w którym leży ten skrypt

# Ścieżki względne liczą się od bieżącego katalogu procesu, a nie od
# położenia skryptu - dlatego w skryptach warto zaczynać od Path(__file__).

# --- budowanie ---
p = TMP / "dane" / "raport.tar.gz"
print(p)

# --- rozbieranie ---
print(p.name)        # raport.tar.gz
print(p.stem)        # raport.tar
print(p.suffix)      # .gz
print(p.suffixes)    # ['.tar', '.gz']
print(p.parent)      # .../tmp__files/dane
print(p.parts)       # krotka wszystkich członów ścieżki

# --- warianty tej samej ścieżki ---
# Path jest niemutowalny: with_* i operator / zwracają NOWY obiekt
# i niczego nie zmieniają na dysku.
print(p.with_name("inny.txt"))     # .../dane/inny.txt
print(p.with_suffix(".zip"))       # .../dane/raport.tar.zip
print(p.with_stem("kopia"))        # .../dane/kopia.gz

# --- pytania o ścieżkę ---
# Samo utworzenie Path(...) nie sprawdza, czy plik istnieje.
print(p.exists())                  # False - jeszcze go nie ma
print(TMP.is_dir())                # True
print(TMP.is_file())               # False
print(p.is_absolute())             # True
print(p.relative_to(TMP))          # dane/raport.tar.gz
print(p.is_relative_to(TMP))       # True

# --- normalizacja ---
print(Path("~/notatki.txt").expanduser())    # rozwija ~ do katalogu domowego
print((TMP / "a" / ".." / "b").resolve())    # bezwzględna, bez .. -> .../tmp__files/b
print(p.as_posix())                          # napis z ukośnikami /
print(str(p))                                # napis w stylu systemu - gdy biblioteka chce str


# ======================================================================
# 2. CZYTANIE I PISANIE (2 min)
# ======================================================================
# Mały plik czyta się i zapisuje jedną metodą Path. open() jest potrzebne
# dopiero przy dużych plikach i przy dopisywaniu.
print("\n=== 2. Czytanie i pisanie ===")

notatki = TMP / "notatki.txt"

# --- całość naraz ---
# write_text tworzy plik albo go NADPISUJE, bez pytania.
# Zawsze podawaj encoding="utf-8": w Pythonie 3.14 domyślne jest kodowanie
# systemowe (na polskim Windowsie zwykle cp1250) i polskie znaki się psują.
notatki.write_text("pierwsza linia: zażółć\ndruga linia: gęślą jaźń\n", encoding="utf-8")

tekst = notatki.read_text(encoding="utf-8")
print(tekst)
print(tekst.splitlines())          # lista linii bez znaków końca linii

# --- dane binarne ---
kopia_bin = TMP / "notatki_kopia.bin"
kopia_bin.write_bytes(notatki.read_bytes())
print(len(kopia_bin.read_bytes()))   # rozmiar w bajtach

# --- dopisywanie na końcu ---
# Tryby: "r" czytanie, "w" zapis od zera, "a" dopisywanie,
# "x" zapis tylko gdy pliku nie ma; z dopiskiem "b" binarnie.
# notatki.open(...) to to samo co open(notatki, ...).
# Blok with sam zamyka plik, także po wyjątku.
with notatki.open("a", encoding="utf-8") as f:
    f.write("trzecia linia: dopisana\n")

# --- duży plik: linia po linii, bez wczytywania całości do pamięci ---
with notatki.open(encoding="utf-8") as f:
    for linia in f:
        print(linia.rstrip())

# --- formaty strukturalne idą tym samym torem ---
dane = {"kurs": "Python", "tematy": ["pathlib", "zip", "glob"], "minut": 15}
plik_json = TMP / "dane.json"
plik_json.write_text(json.dumps(dane, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.loads(plik_json.read_text(encoding="utf-8")))


# ======================================================================
# 3. PODSTAWOWE OPERACJE NA PLIKACH (3 min)
# ======================================================================
# Tworzenie, kopiowanie, przenoszenie, usuwanie i informacje o pliku
# załatwia sam Path. shutil zostaje tylko do usuwania całych drzew.
print("\n=== 3. Podstawowe operacje na plikach ===")

# --- tworzenie katalogów ---
# Wzorzec do zapamiętania: tworzy też katalogi pośrednie i nie zgłasza
# błędu, gdy katalog już istnieje.
kat = TMP / "wyniki" / "2026" / "listopad"
kat.mkdir(parents=True, exist_ok=True)

backup = TMP / "backup"
backup.mkdir()

# --- pusty plik ---
log = kat / "log.txt"
log.touch()                        # tworzy pusty plik albo odświeża datę
log.write_text("start\n", encoding="utf-8")

# --- informacje ---
info = log.stat()
print(info.st_size)                              # rozmiar w bajtach
print(datetime.fromtimestamp(info.st_mtime))     # data modyfikacji

# --- zmiana nazwy ---
# rename zwraca nową ścieżkę. Na Windowsie rzuca błąd, gdy cel istnieje,
# na Linuksie go nadpisuje. replace wszędzie zachowuje się tak samo:
# nadpisuje. Oba działają w obrębie jednego dysku.
log = log.rename(kat / "log_stary.txt")
log = log.replace(kat / "archiwum.txt")
print(log)                         # .../listopad/archiwum.txt

# --- kopiowanie ---
# Działa tak samo dla pliku i dla całego katalogu; zwraca nową ścieżkę.
kopia = log.copy(kat / "kopia.txt")              # kopia pod nową nazwą
log.copy_into(backup)                            # do katalogu, pod tą samą nazwą
(TMP / "wyniki").copy(TMP / "wyniki_kopia")      # cały katalog z podkatalogami

# --- przenoszenie ---
# W odróżnieniu od rename działa też między dyskami.
kopia = kopia.move(backup / "kopia2.txt")        # przeniesienie ze zmianą nazwy
kopia = kopia.move_into(kat)                     # do katalogu, pod tą samą nazwą
print(kopia)                       # .../listopad/kopia2.txt

# --- usuwanie ---
# Usuwanie jest natychmiastowe i omija kosz.
kopia.unlink()                                       # plik
(kat / "nie_ma_mnie.txt").unlink(missing_ok=True)    # bez błędu, gdy pliku nie ma

pusty = TMP / "pusty"
pusty.mkdir()
pusty.rmdir()                      # katalog - tylko pusty

# Path nie ma metody do usuwania niepustego katalogu: zawsze shutil.rmtree.
# Kasuje wszystko pod wskazaną ścieżką, więc ścieżkę warto najpierw
# wypisać i sprawdzić.
shutil.rmtree(TMP / "wyniki_kopia")
print((TMP / "wyniki_kopia").exists())   # False


# ======================================================================
# 4. ZIP: PAKOWANIE I ROZPAKOWANIE KATALOGU (2 min)
# ======================================================================
# Najwygodniej: dwie funkcje z shutil. make_archive pakuje katalog razem
# z podkatalogami, unpack_archive go odtwarza.
print("\n=== 4. ZIP ===")

# przykładowy projekt z podkatalogami (przyda się też w blokach 5 i 6)
projekt = TMP / "projekt"
(projekt / "src" / "pakiet").mkdir(parents=True)
(projekt / "dane").mkdir()
(projekt / "README.md").write_text("# Projekt demo\n", encoding="utf-8")
(projekt / "src" / "main.py").write_text("print('hej')\n", encoding="utf-8")
(projekt / "src" / "main.pyc").write_bytes(b"\x00\x01")
(projekt / "src" / "pakiet" / "__init__.py").write_text("", encoding="utf-8")
(projekt / "src" / "pakiet" / "narzedzia.py").write_text("X = 1\n", encoding="utf-8")
(projekt / "dane" / "wynik_1.csv").write_text("id;wartosc\n1;10\n", encoding="utf-8")
(projekt / "dane" / "wynik_2.csv").write_text("id;wartosc\n2;20\n", encoding="utf-8")
(projekt / "dane" / "wynik_3.csv").write_text("id;wartosc\n3;30\n", encoding="utf-8")

# --- pakowanie ---
# Pierwszy argument to nazwa BEZ rozszerzenia (.zip dopisuje się samo),
# funkcja zwraca pełną ścieżkę archiwum. Archiwum twórz poza pakowanym
# katalogiem, inaczej może zacząć pakować samo siebie.
archiwum = shutil.make_archive(TMP / "backup_projektu", "zip", root_dir=projekt)
print(archiwum)                    # .../tmp__files/backup_projektu.zip

# To samo, ale z katalogiem projekt/ jako folderem głównym w archiwum:
shutil.make_archive(TMP / "backup_z_folderem", "zip", root_dir=TMP, base_dir="projekt")

# Ten sam make_archive robi też "tar", "gztar", "bztar" i "xztar".

# --- rozpakowanie ---
# unpack_archive rozpoznaje format po rozszerzeniu i sam tworzy katalog.
shutil.unpack_archive(archiwum, TMP / "odtworzone")
print((TMP / "odtworzone" / "src" / "main.py").exists())   # True

# --- gdy trzeba wybrać, co trafia do archiwum: moduł zipfile ---
# Bez ZIP_DEFLATED zipfile zapisuje pliki bez kompresji.
with zipfile.ZipFile(TMP / "tylko_zrodla.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for plik in projekt.rglob("*"):
        if plik.is_file() and plik.suffix != ".pyc":
            z.write(plik, plik.relative_to(projekt))    # drugi argument = nazwa w archiwum

# --- zaglądanie do środka bez rozpakowywania ---
with zipfile.ZipFile(TMP / "tylko_zrodla.zip") as z:
    print(z.namelist())                          # lista plików, bez main.pyc
    print(z.read("README.md").decode("utf-8"))   # jeden plik prosto do pamięci
    z.extractall(TMP / "odtworzone_wybrane")     # wszystko na dysk


# ======================================================================
# 5. GLOB: SZUKANIE PLIKÓW WZORCEM (1,5 min)
# ======================================================================
# Path.glob szuka w jednym katalogu, Path.rglob w całym drzewie.
# Oba zwracają gotowe obiekty Path.
#
#   *          dowolny ciąg znaków w obrębie jednej nazwy     *.txt
#   ?          dokładnie jeden znak                           log_?.txt
#   [abc][0-9] jeden znak z podanego zbioru                   dane_[0-9].csv
#   [!abc]     jeden znak spoza zbioru                        [!_]*.py
#   **         dowolnie wiele poziomów katalogów              **/*.json
print("\n=== 5. glob ===")

# Wynik jest generatorem w kolejności systemu plików: żeby go wypisać,
# posortować, policzyć albo użyć ponownie - list(...) / sorted(...).
print(list(projekt.glob("*.md")))                  # pliki .md bezpośrednio w projekt/
print(sorted(projekt.rglob("*.py")))               # pliki .py na każdym poziomie
print(sorted(projekt.glob("**/*.py")))             # to samo co rglob("*.py")
print(sorted(projekt.glob("dane/wynik_?.csv")))    # wzorzec może obejmować katalogi
print(sorted(projekt.glob("dane/wynik_[12].csv"))) # tylko wynik_1 i wynik_2
print(sorted(projekt.glob("*/")))                  # tylko podkatalogi

print(len(list(projekt.rglob("*.py"))))            # 3

# Nie ma składni {a,b} znanej z powłoki: dwa rozszerzenia to dwa
# wywołania albo filtr po suffix.
for plik in sorted(projekt.rglob("*")):
    if plik.suffix in {".md", ".csv"}:
        print(plik.name)

# Wielkość liter zależy od systemu (Windows nie rozróżnia, Linux tak);
# wymusza to argument case_sensitive.
print(list(projekt.glob("*.MD", case_sensitive=False)))   # znajdzie README.md

# Dopasowanie samej nazwy, bez chodzenia po dysku:
print(Path("raport_2026.csv").match("raport_*.csv"))      # True

# Starszy moduł glob (glob.glob("**/*.py", recursive=True)) robi to samo,
# ale zwraca napisy i domyślnie pomija pliki zaczynające się od kropki.


# ======================================================================
# 6. CHODZENIE PO KATALOGACH (1,5 min)
# ======================================================================
# Trzy poziomy: iterdir() dla jednego katalogu, rglob("*") dla całego
# drzewa bez ceregieli, walk() gdy trzeba pracować katalog po katalogu
# albo pomijać gałęzie.
print("\n=== 6. Chodzenie po katalogach ===")

# udajemy repozytorium, żeby było co pomijać
(projekt / ".git").mkdir()
(projekt / ".git" / "config").write_text("[core]\n", encoding="utf-8")

# --- 1. jeden poziom ---
for element in sorted(projekt.iterdir()):
    if element.is_dir():
        print("[D]", element.name)
    else:
        print("   ", element.name)

# --- 2. całe drzewo na płasko ---
# rglob("*") nie umie pomijać gałęzi: przejdzie także przez .git i .venv.
rozmiar = 0
for element in projekt.rglob("*"):
    if element.is_file():
        rozmiar += element.stat().st_size
print(rozmiar)                     # łączny rozmiar plików w bajtach

# --- 3. katalog po katalogu ---
# walk() zwraca trójki: bieżący katalog jako Path, listę NAZW podkatalogów
# i listę NAZW plików. Pełną ścieżkę składa się przez biezacy / nazwa.
for biezacy, katalogi, nazwy_plikow in projekt.walk():
    # Pomijanie gałęzi: usuwamy nazwę z listy W MIEJSCU, wtedy walk()
    # w ogóle nie wchodzi do tego katalogu.
    if ".git" in katalogi:
        katalogi.remove(".git")

    print(biezacy.relative_to(projekt))
    for nazwa in nazwy_plikow:
        plik = biezacy / nazwa
        print("    ", nazwa, plik.stat().st_size)

# walk(top_down=False) odwiedza najpierw najgłębsze katalogi - przydaje
# się przy usuwaniu pustych katalogów od dołu.


# ======================================================================
# 7. INNE UŻYTECZNE Z OS I SYS (2 min)
# ======================================================================
# os odpowiada za rozmowę z systemem operacyjnym, sys za sam interpreter
# i sposób uruchomienia skryptu.
print("\n=== 7. Inne użyteczne z os i sys ===")

# --- sys ---
print(sys.argv)                    # argumenty z wiersza poleceń; [0] to nazwa skryptu
print(sys.platform)                # 'win32', 'linux' albo 'darwin'
print(sys.executable)              # ścieżka do interpretera (widać, czy to venv)
print(sys.version_info)            # wersja Pythona, do porównań: >= (3, 14)
print(sys.path)                    # katalogi, w których Python szuka modułów

# Komunikaty o błędach wypisuj na sys.stderr, żeby nie mieszały się
# z wynikiem przekierowanym do pliku:
print("to jest komunikat na stderr", file=sys.stderr)

# sys.exit(kod) kończy program; kod różny od 0 oznacza błąd.
# Tutaj tylko w komentarzu, żeby demo doszło do końca:
#     if len(sys.argv) < 2:
#         print("Użycie: skrypt.py KATALOG", file=sys.stderr)
#         sys.exit(1)
# Do czegoś więcej niż jeden-dwa argumenty lepiej użyć modułu argparse.

# --- os ---
# Zmienne środowiskowe jako słownik; .get(nazwa, domyślna) nie rzuca błędu.
print(os.environ.get("BACKUP_DIR", "brak zmiennej BACKUP_DIR"))
print(os.cpu_count())              # liczba rdzeni
print(os.getpid())                 # identyfikator bieżącego procesu
print(repr(os.sep))                # separator katalogów: '\\' albo '/'
print(repr(os.pathsep))            # separator wpisów w PATH: ';' albo ':'
print(repr(os.linesep))            # koniec linii: '\r\n' albo '\n'
print(os.access(TMP, os.W_OK))     # czy mamy prawo zapisu (R_OK odczyt, X_OK wykonanie)
print(os.getcwd())                 # bieżący katalog jako napis - to samo co Path.cwd()

# os.chdir(p) zmienia bieżący katalog dla CAŁEGO procesu, a więc znaczenie
# wszystkich ścieżek względnych. Bezpieczniej budować ścieżki bezwzględne
# - ten skrypt nie woła chdir ani razu.

# os.startfile(p) otwiera plik lub katalog w domyślnym programie
# (tylko Windows). W demo niewywoływane:
#     if sys.platform == "win32":
#         os.startfile(TMP)

# Funkcje z os.path (join, basename, splitext, exists) to starszy
# odpowiednik rzeczy z bloku 1; w nowym kodzie zastępuje je Path.


# Polecenie systemowe
os.system('dir')

print("\nKoniec - katalog tmp__files zostanie teraz usunięty.")

