"""
Własny menedżer kontekstu: klasa `Stoper` mierząca czas wykonania bloku `with`.

Protokół menedżera kontekstu to dwie metody specjalne: `__enter__`
(wywoływana na wejściu do bloku, jej wynik trafia do zmiennej po `as`)
i `__exit__` (wywoływana na wyjściu - także gdy w bloku poleciał wyjątek).

Demo pod `if __name__ == '__main__'` pokazuje przy okazji, że `list.insert(0, x)`
jest O(n) (czas rośnie szybciej niż liczba wstawień), a `collections.deque`
wstawia na początek w czasie stałym.
"""
import collections
import time
from types import TracebackType


# class MojMenedzerKontekstu:
#     def __init__(self):
#         ...
#
#     def __enter__(self):
#         print('__enter__')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('__exit__', exc_type, exc_val, exc_tb)
#
#
# with MojMenedzerKontekstu() as alias:
#     print(1)
#     9/0
#
# print(2)

# napoisać menedżera kontekstu który będzie mierzył czas wykonania
# kodu pod with


class Stoper:
    """
    Menedżer kontekstu mierzący czas wykonania bloku `with`.

    Użycie:

        with Stoper('nazwa') as s:
            ...
        print(s)   # nazwa: 0.1234 s.
    """

    def __init__(self, nazwa: str) -> None:
        """
        Args:
            nazwa: etykieta pomiaru, wypisywana w `repr`
        """
        self.nazwa = nazwa

    def __enter__(self) -> Stoper:
        """Startuje pomiar; wynik tej metody trafia do zmiennej po `as`."""
        # perf_counter - zegar o najwyższej dostępnej rozdzielczości,
        # do mierzenia odstępów czasu (nie do odczytu daty/godziny)
        self.t1 = time.perf_counter()
        # nie zapomnieć zwrócić selfa
        return self

    # Python przekazuje do __exit__ trzy argumenty opisujące wyjątek
    # (albo trzy None, gdy go nie było). Zwrócenie True stłumiłoby wyjątek;
    # None (jak tu) pozwala mu polecieć dalej.
    # type[BaseException] | None - wymaga Pythona >= 3.10
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None,
                 exc_tb: TracebackType | None) -> None:
        """Zatrzymuje pomiar."""
        self.t2 = time.perf_counter()

    def __repr__(self) -> str:
        """Etykieta i zmierzony czas w sekundach."""
        return f'{self.nazwa}: {self.t2 - self.t1:.4f} s.'


if __name__ == '__main__':
    with Stoper('50 000 insertów') as s:
        x = []
        for i in range(50_000):
            x.insert(0, i)

    # zmienna s istnieje także po bloku with - with nie tworzy nowego zakresu
    print(s)  # 200 000 insertów: 0.002s.

    with Stoper('100 000 insertów') as s:
        x = []
        for i in range(100_000):
            x.insert(0, i)

    print(s)  # 200 000 insertów: 0.002s.

    with Stoper('200 000 insertów') as s:
        x = []
        for i in range(200_000):
            x.insert(0, i)

    print(s)  # 200 000 insertów: 0.002s.

    # deque (kolejka dwustronna) ma tani dostęp z obu końców
    with Stoper('400 000 insertów') as s:
        x = collections.deque()
        for i in range(400_000):
            x.insert(0, i)

    print(s)  # 200 000 insertów: 0.002s.
