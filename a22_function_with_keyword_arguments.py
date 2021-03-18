print("hello", end=".")

def my_function(turn_on=False):
    if turn_on:
        print("turned on")
    else:
        print(("turned of"))

my_function()
my_function(turn_on=True)

