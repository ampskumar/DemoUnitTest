# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
    def adder(y):
        return x + y
    return adder


add_15 = create_adder(15)

print(add_15(10))

print("-----------chaining decorators-----------")


def decor2(func):
    def inner():
        x = func()
        return x * x
    return inner


def decor1(func):
    def inner():
        x = func()
        return 2 * x
    return inner


@decor2
@decor1
def num():
    return 10


print(num())
print("-------------parameterized decorator--------------")


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

# def my_wrapper(func):
#     def inner(*args, **kwargs):
#         print("Hi")
#         res = func(*args, **kwargs)#*args, **kwargs
#         print(res)
#     return inner
#
#
# @my_wrapper
# def my_func(first, last):
#     # print("before this")
#     return first+last
#
#
# my_func("amit", "patil")

