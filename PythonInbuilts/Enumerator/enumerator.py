'''
ENUMERATORS:
Iterates and returns  the element and a counter that keeps on increasing with the elements.
By default it starts from 0 but we can specify the start counter.

'''
l1 = ["eat","sleep","repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print(list(enumerate(l1)))

for i in enumerate(l1):
    print(i)

# changing start index to 2 from 0
print(list(enumerate(s1, 2)))

# printing the tuples in object directly
for ele in enumerate(l1):
    print(ele)
# changing index and printing separately
for count, ele in enumerate(l1, 100):
    print(count, ele)

'''
[(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
(0, 'eat')
(1, 'sleep')
(2, 'repeat')
[(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]

'''