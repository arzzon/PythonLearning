# Random library usage
import random
# Generate pseudo-random integer N between x and y, i.e., x <= N <= y
print(random.randint(1, 9))
# Generate pseudo-random number(float) N between 0.0 and 1.0, i.e., 0.0 <= N <= 1.0
print(random.random())
# Shuffle a sequence in place
A = [1,2,3,4]
random.shuffle(A)
print(A)
