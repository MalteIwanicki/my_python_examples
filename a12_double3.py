# doubles 3 till its bigger than 123456789 returns the value and its iterations
iteration = 0
number = 3
while number < 123456789:
    number *= 2
    iteration += 1

print('Iterations: ' + str(iteration))
print('Number: ' + str(number))
