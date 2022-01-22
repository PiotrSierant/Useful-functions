def adder(*args, default=None):  # funkcja do dodawania sekwencji, list, czy liczb
    '''self-adding function'''
    from operator import add
    from functools import reduce
    try:
        return reduce(add, args)
    except TypeError as e:
        return default


def adder_dict(dictionary, *args):  # funkcja do łączenia słowników
    '''a function for adding two or more dictionaries '''
    for _ in args:
        for i in args:
            dictionary.update(i)

    return dictionary


def copyDict(dictionary):  # funkcja do kopiowania kluczy słowników
    '''a function that copies the keys of dictionaries'''
    listArgument = []
    x = dictionary.keys()
    for i in x:
        listArgument.append(i)

    return listArgument


print(copyDict(p))


x = {'x': 1, 2: 1, 3: 1}
y = {1: 2, 2: 2, 3: 2}
z = {'b': 7, 'g': 8, 'n': 9}
p = {'hhh': 7, 'p[': 8, 'ppp': 9}
#print(adder(5, 5, 6, 7))
#print(adder('hehe', 'hehe', 'hehe'))
# adder_dict(x, y, z, p))
