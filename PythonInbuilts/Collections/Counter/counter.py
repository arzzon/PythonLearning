'''
Counter function in collection is used to count the number of occurrences of different
letters and stores them in a dictionary with key as the letter and it's values as the
count.
For example:
s = "abac"
c = collections.Counter(s)
print(c)
Counter({'d': 3, 'a': 2, 'b': 1, 'c': 1})
Note: Order is as per the string not alphabetically
'''
import collections
if __name__ == "__main__":
    s = 'bacaddd'
    c = collections.Counter(s)
    print(c['k'])
    print(sorted(c.keys()))

    print(c.__len__())