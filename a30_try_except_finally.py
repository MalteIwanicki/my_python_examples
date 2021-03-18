try:
    k = 5 // 0  # raises divide by zero exception.

# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")

#would be executed if you could divide by zero
else:
    print(k)

finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')
