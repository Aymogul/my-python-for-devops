def square(number):
    """Calculate the square of number."""
    return number ** 2

square(7)

square(2.5)

# Returning a Result to a Function’s Caller
print('The square of 7 is', square(7))

print('The square of 2.5 is', square(2.5))

# the function definition is def
# the function name is square
# the function parameter or variable is number
# the return is the answer to the execution of the function 

def square(number: float) -> float:
    """Calculate the square of a number."""
    return number ** 2
square(5)
square(4)

print('The square of 5 is', square(5))

print('The square of 4 is', square(4))
