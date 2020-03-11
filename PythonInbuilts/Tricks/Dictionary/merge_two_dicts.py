# Trick to merge two dictionaries in python 3.5
x = {"a":1,"b":2}
y = {"c":3,"a":4,"d":5}
z = {**x,**y} #y will be merged with x and if x has anything common to y then that will be updated with the value in y.
print("x:",x)
print("y:",y)
print("z:",z)
