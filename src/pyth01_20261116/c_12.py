"""
Napisać klasę Spychacz

Spychacz będzie miał następujące dane:
 - nr_rej
 - x
 - y
 - kierunek

Spychacz będzie potrafił:
 - się stworzyć w (0, 0) skierowany w góre
 - jechać przed siebie o ustaloną odległość
 - skręcić w prawo o 90 stopni
 - wypisać swoje dane: nr_rej i pozycję
"""

class Spychacz:
    ...

if __name__ == '__main__':
    s1 = Spychacz('rk12345')
    s1.wypisz_sie() # Spychacz rk12345 w (0, 0)

    s1.jedz(12)
    s1.skrec_w_prawo()
    s1.wypisz_sie() # Spychacz rk12345 w (0, 12)

    s1.jedz(12)
    s1.skrec_w_prawo()
    s1.wypisz_sie() # Spychacz rk12345 w (12, 12)

    s1.jedz(12)
    s1.skrec_w_prawo()
    s1.wypisz_sie() # Spychacz rk12345 w (12, 0)

    s1.jedz(12)
    s1.skrec_w_prawo()
    s1.wypisz_sie() # Spychacz rk12345 w (0, 0)
