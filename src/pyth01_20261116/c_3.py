"""
Dane:
sekundy = 98765.
Zamień na godziny, minuty i sekundy.
Przypomnienie - operatory // i %
"""


# zbuduj funkcję zrwacającą krotkę

def zamien_s_na_hms(sekundy):
    godziny = sekundy // (60 * 60)
    reszta = sekundy % (60 * 60)
    minuty = reszta // 60
    sekundy = reszta % 60
    return godziny, minuty, sekundy


if __name__ == '__main__':
    sekundy = 98765
    godziny, minuty, sekundy = zamien_s_na_hms(sekundy)
    print('H:', godziny, 'M:', minuty, 'S:', sekundy)
