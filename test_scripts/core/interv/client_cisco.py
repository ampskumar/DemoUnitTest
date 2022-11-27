def check_even(func):
    def inner(a, b):
        res = func(a, b)
        if res % 2 == 0:
            print("result is even")
        else:
            print("result is odd")
    return inner


@check_even
def add(a, b):
    return a+b


add(2, 4)

mydict = {'a': [1, 2, 3, {'aa': [20, 30, 40]}]}
print(mydict['a'][-1]['aa'][1])
a = 10


def add(a, b):
    a = 20
    c = a + b
    print(c)
    return c


a = 30

add(80, 20)