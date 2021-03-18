# takes three numbers and returns the sum if the
# three numbers are equal return thrice the sum
print('What are your numbers?')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a == b == c:
    print(str((a+b+c)*3))
else:
    print(str(a+b+c))
