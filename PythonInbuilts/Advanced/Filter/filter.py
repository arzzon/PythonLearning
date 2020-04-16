'''
    Filter is used to filter out specific elements from an iterable(like list) provided to it,
    along with the logic to filter which is provided as a lambda function. It returns a filter
    object which contains all those filtered elements. We can type cast these objects to iterables
    like list/set etc.
    Syntax:
    =>  filter(lambda function, iterable)
    type casting to list:
    =>  list( filter(lambda function, iterable) )

'''
L = [1, 2, 3, 4, 5, 6]
# List with only even elements
evensList = list(filter((lambda x: x % 2 == 0), L))
print(evensList)