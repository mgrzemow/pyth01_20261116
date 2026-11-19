"""
Dane:
sekundy = 98765.
Zamień na godziny, minuty i sekundy.
Przypomnienie - operatory // i %
"""

if __name__ == '__main__':
    sekundy = 98765
    godziny = sekundy // (60 * 60)
    reszta = sekundy % (60 * 60)
    minuty = reszta // 60
    sekundy = reszta % 60
    print('H:', godziny, 'M:', minuty, 'S:', sekundy)
