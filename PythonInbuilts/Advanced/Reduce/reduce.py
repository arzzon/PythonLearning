'''
    Reduce is used to generate a a single value operations performed on the iterable elements
    using the lambda function logic provided to it. Like, if we want the sum of all the elements
    of a list then reduce will help reduce the list to a value that is the sum.
    IMP: reduce has been removed from the default packages in python 3.6
        To use it we can import it
        from functools import reduce
    Syntax:
    =>  reduce(lambda function, iterable)
    type casting to list:
    =>  list( map(lambda function, iterable) )

'''
from functools import reduce
L = [1, 2, 3, 4, 5, 6]
# Sum of elements in the list.
s = reduce((lambda x, y: x+y), L)
# It's the same as saying sum(L)
#s = sum(L)
print(s)