'''
Description:(Double ended queue/stack)
    Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short
    for “double-ended queue”). Deques support thread-safe, memory efficient appends and pops from
    either side of the deque with approximately the same O(1) performance in either direction.
LAST USED:
'''

from collections import deque
if __name__ == "__main__":
    print("CREATING A DEQUE, WE CAN PASS A STRING/LIST/NOTHING")
    d = deque('ghi')  # make a new deque with three items
    for elem in d:  # iterate over the deque's elements
        print(elem.upper(), end=" ")
    print()
    print("APPEND ELEMENTS TO END/START")
    d.append('a')
    d.appendleft('b')
    for elem in d:  # iterate over the deque's elements
        print(elem, end=" ")
    print("REMOVING ELEMENTS")
    print("Remove a element:", d.pop())
    print("Remove a element:", d.popleft())
    print()
    print("CONVERT TO LIST")
    print(list(d))
    print()
    print("ROTATE")
    d.rotate()
    print(d)
    print("ROTATE LEFT")
    d.rotate(-1)
    print(d)
