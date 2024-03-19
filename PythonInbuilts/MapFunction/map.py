'''
In Python, map() is a built-in function used to apply a given function to each item of an iterable 
(such as a list, tuple, or string) and return a new iterable with the results. It's a functional 
programming concept that allows you to process data in a concise and efficient manner.

The general syntax of the map() function is: 
 map(function, iterable)

function: The function to apply to each item of the iterable. This function will be called with one 
argument for each item in the iterable.
iterable: The iterable (e.g., list, tuple, string) whose items will be passed to the function.

The map() function returns an iterator, which can be converted to other iterable types (such as a 
list or tuple) using the list() or tuple() functions if needed.

Here's a simple example demonstrating the use of map():
'''

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Define a function to square a number
def square(x):
    return x ** 2

# Use map() to apply the square function to each number in the list
squared_numbers = map(square, numbers)

# Convert the iterator to a list
squared_numbers_list = list(squared_numbers)

# Print the squared numbers
print(squared_numbers_list)  # Output: [1, 4, 9, 16, 25]

# Same using lambda
print(list(map(lambda x: x**2, numbers)))
'''
In this example, the square() function is applied to each item in the numbers list using map(), 
resulting in a new list containing the squared numbers.
'''