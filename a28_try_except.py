def divide_10_by(divisor):
    try:
        return 10 / divisor
    except ZeroDivisionError:
        print("Error: you tried to divide by zero")


for i in range(10, -11, -5):
    print(divide_10_by(i))

