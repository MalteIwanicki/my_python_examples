# A sting formatting example

name = 'Malte'
age = '27'
home = 'Berlin'

print(name + ' is ' + age + ' years old and lives in ' + home + '.')
# >>> Malte is 27 years old and lives in Berlin.

# Or you use string formatting, this makes your code much more readable.
print('%s is %s years old and lives in %s.' % (name, age, home))
# >>> Malte is 27 years old and lives in Berlin.

