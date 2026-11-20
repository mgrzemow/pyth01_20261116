@echo off
rem Generuje dokumentacje HTML pakietu pyth01_20261116 za pomoca pdoc3.
rem
rem Uzycie:
rem     generuj_dokumentacje.bat          - generuje do katalogu docs\html
rem     generuj_dokumentacje.bat otworz   - jak wyzej i otwiera index.html w przegladarce
rem
rem Wymaga: uv (srodowisko z pdoc3 jest w pyproject.toml, uv run je dociagnie).

setlocal

rem przejscie do katalogu, w ktorym lezy ten skrypt (katalog projektu)
cd /d "%~dp0"

rem polskie znaki w komunikatach pdoc i w docstringach
set PYTHONUTF8=1
chcp 65001 >nul

set WYJSCIE=docs\html

echo Generuje dokumentacje do %WYJSCIE% ...
uv run pdoc --html --force --output-dir "%WYJSCIE%" pyth01_20261116
if errorlevel 1 (
    echo BLAD: pdoc zakonczyl sie bledem.
    exit /b 1
)

echo Gotowe: %CD%\%WYJSCIE%\pyth01_20261116\index.html

if /i "%~1"=="otworz" (
    start "" "%WYJSCIE%\pyth01_20261116\index.html"
)

endlocal
