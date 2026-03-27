# try:
#     x = 9 / 0
# except ZeroDivisionError:
#     print('dzielenie przez 0')
#     raise


try:
    {}
except ZeroDivisionError:
    print('reakcja na /0')
    raise
except IndexError:
    print('reakcja na zły indeks')
    raise
except FileNotFoundError as e:
    print('reakcja na brak pliku', e, e.args)
    raise
except Exception as e:
    print('reakcja na inny błąd', e, type(e).__name__, e.args)
    raise
finally:
    print('TO SIĘ WYKONAN ZAWSZE !!!')