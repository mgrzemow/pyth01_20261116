"""
Obsługa błędów: `try` / `except` / `else` / `finally` i ponowne zgłoszenie
wyjątku gołym `raise`.

W tym demo pierwsza instrukcja w `try` (`open('asdasdasd')`) rzuca
`FileNotFoundError`, więc do dzielenia przez zero i do błędu indeksu nigdy
nie dochodzimy. Łapie go ostatnia klauzula `except Exception`, program
wypisuje informacje o błędzie, wykonuje `finally` i kończy się z tracebackiem
(bo wyjątek jest zgłoszony ponownie).

Kod demonstracyjny jest pod `if __name__ == '__main__'`.
"""

if __name__ == '__main__':
    print(1)
    try:
        open('asdasdasd')
        i = 3
        a = [1, 2, 3, 0]
        x = 9 / a[i]
    # klauzule except są sprawdzane po kolei - najpierw te najbardziej
    # szczegółowe, Exception (klasa bazowa prawie wszystkich błędów) na końcu
    except ZeroDivisionError:
        print('Reakcja na błąd dzielnia przez 0')
        # gołe raise zgłasza ponownie ten sam wyjątek (z oryginalnym tracebackiem)
        raise
    except IndexError:
        print('Reakcja na błąd dostępu do listy')
        raise
    # as e - obiekt wyjątku dostępny pod nazwą e (tylko wewnątrz tej klauzuli)
    except Exception as e:
        print(f'Wystapił błąd typu {e.__class__.__name__}')
        print(f'Wystapił błąd: {e}')
        print(f'Wystapił błąd, dodatkowe parametry: {e.args}')
        raise
    # else wykonuje się tylko wtedy, gdy w try NIE było wyjątku
    else:
        print('Żaden błąd nie wystąpił')
    # finally wykonuje się zawsze - także po raise i po return
    finally:
        print('TO SIĘ WYKONA ZAWSZE !!!')
    # y = x + 9
    # print(2)

    # Wykonuje się tylko jedna klauzula except
    # CHYBA ŻE
    # jest użyte ExceptionGroup - najcześciej w asyncio
    # (ExceptionGroup i składnia except* - wymaga Pythona >= 3.11)
