'''
DESCRIPTION:
    MY DESCRIPTION:
        Counter function in collection is used to count the number of occurrences of different
    letters and stores them in a dictionary with key as the letter and it's values as the
    count.
    DOCUMENTATION:
        A Counter is a dict subclass for counting hashable objects. It is an unordered collection
    where elements are stored as dictionary keys and their counts are stored as dictionary values.
    Counts are allowed to be any integer value including zero or negative counts. The Counter class
    is similar to bags or multisets in other languages.
For example:
s = "abac"
c = collections.Counter(s)
print(c)
Counter({'d': 3, 'a': 2, 'b': 1, 'c': 1})
Note: Order is as per the string not alphabetically
'''

from collections import Counter
if __name__ == "__main__":
    print("#Passing string as argument to count the characters")
    s = 'cabaddd'
    c = Counter(s)
    print("string:", s)
    for key, value in c.items():
        print(key, ":", value)
    print("#To get a list based on the counts")
    print(sorted(c.keys(), key = (lambda x: c[x])))
    print("#To get a list based on the counts and if the counts are equal then sort alphabetically")
    print("For this we need to return a tuple in the lambda expression where the 1st value in the tuple\
decides the first value to be considered for sorting and the 2nd value is the 2nd value that will be\
used in case first values are similar in two or more cases.")
    print(sorted(c.keys(), key = (lambda x: (c[x], x)) ) )
    print("#Length of the counter dictionary")
    print(c.__len__())
    print()
    print("#Passing list as argument to count the list items")
    l = ["hi", "bye", "hi"]
    c = Counter(l)
    print("List:", l)
    for key, value in c.items():
        print(key, ":", value)

    print()
    print("#Deleting an element")
    l = ["hi", "bye", "hi"]
    print("List:", l)
    c = Counter(l)
    del c["hi"]
    for key, value in c.items():
        print(key, ":", value)

    print("#elements()")
    print("returns all the elements repeated as the frequency in which they are present in the counter dict")
    c = Counter(a=4, b=2, c=0, d=-2)
    print(list(c.elements()))  # ['a', 'a', 'a', 'a', 'b', 'b']

    print("#most_common([n])")
    print("Returns n most frequent elements with their frequency.")
    print(Counter('abracadabra').most_common(3))  # [('a', 5), ('b', 2), ('r', 2)]

    print("#subtract([iterable-or-mapping])")
    print("If we have another counter and we want to subtract the second counter from the first counter\
, which means subtracting their frequencies we use subtract function")
    c = Counter(a=4, b=2, c=0, d=-2)
    d = Counter(a=1, b=2, c=3, d=4)
    c.subtract(d)
    print(c)  # Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

    print("update([iterable-or-mapping])")
    print("If we want to update the counter with another counter.")
    print("Counter before update:", c)
    print("New counter to update:", d)
    c.update(d)
    print("Counter after update:", c)

