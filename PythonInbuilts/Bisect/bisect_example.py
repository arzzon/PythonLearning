import bisect
# Bisect is used to know whether the element has to be inserted to keep the list sorted.
# bisect(list,num)->int where list is a sorted list and num is the number that we want
# to insert, return the position where it should be inserted, if the number already exists
# then it returns the position right to it(if we want the left position then use bisect_left()).
# It uses binary search
# bisect and bisect_right() do the same thing
print(bisect.bisect([0, 1, 2, 3, 4, 5, 6, 7], 4))  # 5
print(bisect.bisect_left([0, 1, 2, 3, 4, 5, 6, 7], 4))  # 4
print(bisect.bisect([0, 1, 2, 3, 5, 6, 7], 4))  # 4

# If we want to find as well as insert the number in the correct position in the list then use
# insort(), similarly we have insort_right() and insort_left()
A = [0, 1, 2, 3, 5, 6, 7]
bisect.insort(A,4)
print(A)  # [0, 1, 2, 3, 4, 5, 6, 7]

