if __name__ == '__main__':
    print(1)
    try:
        open('asdasdasd')
        i = 3
        a = [1, 2, 3, 0]
        x = 9 / a[i]
    except ZeroDivisionError:
        print('Reakcja na błąd dzielnia przez 0')
        raise
    except IndexError:
        print('Reakcja na błąd dostępu do listy')
        raise
    except Exception as e:
        print(f'Wystapił błąd typu {e.__class__.__name__}')
        print(f'Wystapił błąd: {e}')
        print(f'Wystapił błąd, dodatkowe parametry: {e.args}')
        raise
    else:
        print('Żaden błąd nie wystąpił')
    finally:
        print('TO SIĘ WYKONA ZAWSZE !!!')
    # y = x + 9
    # print(2)

    # Wykonuje się tylko jedna klauzula except
    # CHYBA ŻE
    # jest użyte ExceptionGroup - najcześciej w asyncio
