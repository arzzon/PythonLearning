'''
    Map is used to generate another iterable from the iterable provided to it along with
    the lambda function, where each element of the generated iterable is mapped/modified
    to some value based on the lambda function logic provided to it.
    It returns a map object which contains all those filtered elements. We can type cast
    these objects to iterables like list/set etc.
    Syntax:
    =>  map(lambda function, iterable)
    type casting to list:
    =>  list( map(lambda function, iterable) )

'''
L = [1, 2, 3, 4, 5, 6]
# Each element in the list is squared.
squaredList = list(map((lambda x: x**2), L))
print(squaredList)