'''
    Lambda is a anonymous function that can take any number of arguments, these are evaluated
    and a result is returned.
    Syntax:
    lambda arguments: expression
    Rules:
    1) lambda has be written first
    2) No return is written explicitly
    3) lambda statement actually returns the function defined in it.
'''
# We will be using the lambda function to check even/odd.
if __name__ == "__main__":
    # The following lamda function is used to calculate mod 2 of a number and return result.
    check = lambda x: x % 2
    if check(6) == 0:
        print("Even")
    else:
        print("Odd")