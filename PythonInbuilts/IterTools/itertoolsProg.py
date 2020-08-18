'''
itertool implements a number of iterator building blocks.
'''
import itertools

# Count
iterator = itertools.count(1, 2)
print("Odd list:", list(next(iterator) for _ in range(5)))

# Permutation
lst = [1, 2, 3]
# permutations(iterable, r) , where r is used to return successive r length permutations of elements in the iterable.
perm = itertools.permutations(lst)  # Returns a permutation object containing all the permutaions(iterable) as tuples
for p in perm:
    print(p)  # (1, 2, 3) (1, 3, 2) (2, 1, 3) (2, 3, 1) (3, 1, 2) (3, 2, 1)

# Combination
txt = "ABCD"
comb = itertools.combinations(txt, 2)  # combinations(iterable, length of subsequence to consider)
for c in comb:
    print(c)  # ('A', 'B') ('A', 'C') ('A', 'D') ('B', 'C') ('B', 'D') ('C', 'D')


