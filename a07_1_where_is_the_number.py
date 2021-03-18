# Checks if a number is between 100 and 1000 or 1001 and 2000
number = int(input('your number:'))
print(str(number),end=' ')
if 100<= number <= 1000:
    print('is between 100 and 1000.')
elif 1001 <= number <= 2000:
    print('is between 1001 and 2000.')
else:
    print('is not between 100 and 2000.')

