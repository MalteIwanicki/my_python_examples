# a lambda example

# lambda is a short, anonymous function.
# can take any number of arguments but have only one expression

lambda_function = lambda parameter1, parameter2 : parameter1 * parameter2

print(lambda_function(3,4))
# >>> 12

# this is shorter than using a normal function:
def my_function(parameter1, parameter2):
    return parameter1 * parameter2

print(my_function(4,3))
# >>> 12

# Use lambda functions when an anonymous function is required for a short period of time.
