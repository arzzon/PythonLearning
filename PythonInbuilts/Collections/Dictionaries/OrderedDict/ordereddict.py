'''
DESCRIPTION:
    An OrderedDict is a dict that remembers the order that keys were first inserted.
    If a new entry overwrites an existing entry, the original insertion position is
    left unchanged. Deleting an entry and reinserting it will move it to the end.
    NOTE:
        1. By default it follows LIFO principle while deleting the item, for example
           if we call od.popitem() => it will remove the item that was inserted recently
           but we can also ensure that it follows the FIFO while deleting the items by
           providing a last=False parameter(by default last=True LIFO) in the popitem as
           a parameter od.popitem(last=False) => this will ensure that the first item that
           was inserted is removed.
LAST USED:
    LRU Cache
'''
from collections import OrderedDict
if __name__ == "__main__":
    od = OrderedDict()
    od['first'] = 8
    od["second"] = 4
    od["third"] = 7
    od["fourth"] = 14
    od["fifth"] = 3
    for key, value in od.items():
        print(key, ':', value)
    print("# Order is maintained that is guaranteed")
    '''
    first: 8
    second: 4
    third: 7
    fourth: 14
    fifth: 3
    '''
    print("#in simple dictionary order is not maintained")

    print("#Methods available in OrderedDict")
    print("#Adding a key, value to the dict")
    od = OrderedDict()
    od['first'] = 8

    print("#Checking whether a value exists or not")
    key = "first"
    if key in od:
        print("Yes")
    else:
        print("No")

    print("#Remove item LIFO")
    od['first'] = 8
    od["second"] = 4
    od["third"] = 7
    od["fourth"] = 14
    od["fifth"] = 3
    # It will remove ("fifth",3) which is the last one
    od.popitem(last=True) # od.popitem()
    for key, value in od.items():
        print(key, ':', value)

    print("#Remove item FIFO")
    od["fifth"] = 3  # inserted it back
    # It will remove ("first",8) which is the first one
    od.popitem(last=False)
    for key, value in od.items():
        print(key, ':', value)

    print("#Remove a particular (key,value), pop method is used unlike popitem")
    od['first'] = 8
    od["second"] = 4
    od["third"] = 7
    od["fourth"] = 14
    od["fifth"] = 3
    # It will remove ("fifth",3) which is the last one
    print("item removed", od.pop("third"))  # od.popitem()
    for key, value in od.items():
        print(key, ':', value)

    print()
    print("#Deleting an element")
    del od["fourth"]
    for key, value in od.items():
        print(key, ":", value)