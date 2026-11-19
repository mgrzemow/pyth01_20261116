class MojMenedzerKontekstu:
    def __init__(self):
        ...

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__', exc_type, exc_val, exc_tb)


with MojMenedzerKontekstu() as alias:
    print(1)
    9/0

print(2)

# napoisać menedżera kontekstu który będzie mierzył cczas wykoanania
# kodu pod with

class Stoper:
    def __init__(self):
        ...

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__', exc_type, exc_val, exc_tb)

    def __repr__(self) -> str:
        return '__repr__'


import time
t1 = time.perf_counter()
# mierzone operacje
t2 = time.perf_counter()
print(t2 - t1)


with Stoper('200 000 insertów') as s:
    x = []
    for i in range(200_000):
        x.insert(0, i)

print(s) # 200 000 insertów: 0.002s.