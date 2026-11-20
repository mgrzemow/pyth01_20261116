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
import time
import collections


class Stoper:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __enter__(self):
        self.t1 = time.perf_counter()
        # nie zapomnieć zwrócić selfa
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.t2 = time.perf_counter()

    def __repr__(self) -> str:
        return f'{self.nazwa}: {self.t2 - self.t1:.4f} s.'


with Stoper('50 000 insertów') as s:
    x = []
    for i in range(50_000):
        x.insert(0, i)

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

with Stoper('400 000 insertów') as s:
    x = collections.deque()
    for i in range(400_000):
        x.insert(0, i)

print(s)  # 200 000 insertów: 0.002s.
