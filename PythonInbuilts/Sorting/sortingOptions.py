'''
Sorting options available in python3
'''
if __name__ == "__main__":
    a = [3, 2, 4, 1, 8, 0]
    # sorted(iterable, key=functionName, reverse=True/False)
    # By default key=None and reverse=False
    # Returns a sorted list, but doesn't sort the provided list
    b = sorted(a)
    print(a)
    print(b)
    # Sort in reverse order
    c = sorted(a, reverse=True)
    print(c)
    # Sort on the basis of a key
    d = [(1,5),(2,2),(3,1)]
    # Returns the second element of the tuple, which will be used as the key to sort
    getKey = lambda t: t[1]
    '''
    # Equivalent function
    def getKey(t):
        return t[1]
    '''
    # This getKey function can be customized to process each element and return a key.
    e = sorted(d, key=getKey)
    print(e)  # [(3, 1), (2, 2), (1, 5)]

    # sort function
    # iterable.sort(key=functionName, reverse=True/False)
    # It sorts the list itself.
    a.sort()
    print(a)