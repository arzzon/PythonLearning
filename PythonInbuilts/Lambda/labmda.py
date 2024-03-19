'''
In Python, lambda is a keyword used to create anonymous functions, also known as lambda functions. 
These functions are small, inline functions that are defined using a single expression. They are 
typically used for short, simple operations where defining a full function using the def keyword 
would be overkill.

The syntax of a lambda function is as follows:

lambda arguments: expression
lambda: Keyword used to indicate the creation of a lambda function.
arguments: The parameters (or arguments) of the function.
expression: The single expression that is evaluated and returned as the result of the function.
Lambda functions can have any number of arguments, but they can only contain a single expression. 
The result of evaluating this expression is automatically returned as the result of the function.

Here's a simple example of a lambda function that adds two numbers:
'''
add = lambda x, y: x + y
print(add(3, 4))  # Output: 7
'''
In this example, lambda x, y: x + y creates a lambda function that takes two arguments (x and y) 
and returns their sum. The function is then assigned to the variable add, which can be called just like a regular function.
'''
# It's handy when using sort functions
# It can help in defining which key to use for sorting
list_of_tuples = [("john", 26),("alexa", 20), ('david', 15)]
# sort based on the ages using lambda and sorted function
print("sorted based on the age:", sorted(list_of_tuples, key=lambda x: x[1])) # sorted return a new list in sorted order
print("reverse sorted based on the age:", sorted(list_of_tuples, key=lambda x: x[1], reverse=True)) # sorted return a new list in reverse sorted order as reverse=True
# sort based on the ages using lambda and sort function
list_of_tuples.sort(key=lambda x: x[1]) # sort updates the list in place where as sorted generates a new list
print("sorted based on the age:", list_of_tuples)
list_of_tuples.sort(key=lambda x: x[1], reverse=True)
print("reverse sorted based on the age:", list_of_tuples)
