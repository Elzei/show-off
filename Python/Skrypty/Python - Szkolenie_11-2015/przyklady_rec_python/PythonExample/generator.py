def lamYield(x):
    yield x

def dzielniki(liczba):
    dzielnik = []
    dzielnik = filter(lambda x: not liczba % x, range(2,liczba // 2 + 1))
    dzielnik = dzielnik if len(dzielnik) else [0]
    for i in dzielnik:
        yield i


for i in dzielniki(35):
    print i
        
