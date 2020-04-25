'''
Description:
    My understanding:
        It's like the dict, but it ensures that whenever we access a key if that key is not present,
        then it adds that key to the dictionary with a default value as per the type of the value
        mentioned while creating the default dict.
    Docs definition:
        Returns a new dictionary-like object. defaultdict is a subclass of the built-in dict class.
    It overrides one method and adds one writable instance variable. The remaining functionality
    is the same as for the dict class and is not documented here.
SYNTAX:
    from collections import defaultdict
    dd = defaultdict(<data type of the values that it will contain>)
    example:
    dd = defaultdict(int)
                      |
                      v
        dd["first"] = 1
Last Used:
    On my problems.
'''
from collections import defaultdict
if __name__ == "__main__":
    print("#Initializaton")
    dd = defaultdict(int)
    print("#Difference from regular dictionary")
    print("#When we access a key that doesn't exist in regular dictionary, then it throws error")
    # When uncommented it throws error
    '''d = dict()
    print(d["first"])
    '''
    print(dd["first"]) #Output 0
    print("#But When we access a key that doesn't exist in defaultdict, then it adds that key with a default value")

    print("Usecase:")
    print("#Suppose we just want to get the frequency of numbers in a list")
    nums = [5, 1, 2, 1, 3, 3, 1, 8]
    dd = defaultdict(int)
    for i in nums:
        dd[i] += 1
    for key, value in dd.items():
        print(key, ":", value)
