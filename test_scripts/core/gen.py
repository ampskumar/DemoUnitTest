"""
Python generators are a simple way of creating iterators.
All the work we mentioned above are automatically handled by generators in Python.

Simply speaking, a generator is a function that returns
 an object (iterator) which we can iterate over (one value at a time).

The difference is that while a return statement terminates a function entirely,
 yield statement pauses the function saving all its states and
  later continues from there on successive calls.
"""

import sys


def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
# for value in simpleGeneratorFun():
#     print(value)


def table(n):
    for i in range(1, 3):
        # print("before yield")
        yield n*i
        print("after yield")


for item in table(15):
    print(item)


# print("...............list v/s generator..........")
#
# # List comprehension
# nums_squared_list = [i ** 2 for i in range(1000)]
# print(sys.getsizeof("Memory in Bytes:", nums_squared_list))
# # Generator Expression
# nums_squared_gc = (i ** 2 for i in range(1000))
# print(sys.getsizeof("Memory in Bytes:", nums_squared_gc))
#
# print("3............ Pipelining with Generators......")
# with open('sells.log') as f:
#     # burger_col = (line.split()[3] for line in f.readlines());
#     # for i in burger_col:
#     #     print(i)
#     # print()
#     burger_col = [line.split()[3] for line in f.readlines()];
#     per_hour = (int(x) for x in burger_col if x != 'N/A')
#     print("Total burgers sold = ",sum(per_hour))