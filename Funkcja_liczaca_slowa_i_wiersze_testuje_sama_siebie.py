def countLines(file):
    x = open(file, 'r', encoding='UTF-8')

    return len(x.readlines())


print('Liczba wierszy: ', end='')
print(countLines('app lista komend.txt'))


def countChars(file):
    x = open(file, 'r', encoding='UTF-8')
    total = 0
    for line in x:
        total += (len(line))

    return total


print('Liczba literek: ', end='')
print(countChars('app lista komend.txt'))


def name(file):
    wynik = countLines(file), countChars(file)
    return printer(wynik)


def printer(krotka_wyników):
    return ('Liczba wierszy: {} \nLiczba literek: {}').format(krotka_wyników[0], krotka_wyników[1])


print(name('app lista komend.txt'))


def listing(module, verbose=True):
    if verbose:
        print('-'*60)
        print('nazwa:', module.__name__, 'plik:', module.__file__)
        print('-'*60)

    count = 0
    for attr in module.__dict__:
        print('%02d) %s ' % (count, attr), end=' ')
        if attr.startswith('__'):
            print('<zmienna wbudowana>')
        else:
            print(getattr(module, attr))
        count += 1

    if verbose:
        print(module.__name__, 'ma %d zmiennych' % count)


if __name__ == '__main__':
    import brudnopis
    listing(brudnopis)
