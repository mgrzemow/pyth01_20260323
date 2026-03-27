import requests


def fibo(n):
    x1 = 1
    x2 = 1
    for _ in range(n - 2):
        x1, x2 = x2, x1 + x2
    return x2


def n_times_fibo(m):
    for _ in range(m):
        x = fibo(10_000)
    return 'wynik'


def dos(n):
    for _ in range(n):
        s = requests.session()
        r = s.get('https://gatling.io')
        if r.status_code != 200:
            print(f'{r.status_code} https://gatling.io\n', end='')

    return 'wynik'

import concurrent.futures as cf
import time

if __name__ == '__main__':

    t1 = time.time()
    with cf.ThreadPoolExecutor(max_workers=16) as executor:
        lista_parametrow = [10] * 32
        for wynik in executor.map(dos, lista_parametrow):
            print(wynik)
    print(time.time() - t1)