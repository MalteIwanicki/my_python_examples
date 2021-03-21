# with escape character
print('hello how are you?\nI\'m fine thanks')
# >>>
"""
hello how are you?
I'm fine thanks
"""

# multiline string
print('''this is a multiline string
I can simply break the rule of one line per string 
and don't have to worry much about " and ' 
simply can use the return as well.
End of string.''')
# >>>
"""
this is a multiline string
I can simply break the rule of one line per string 
and don't have to worry much about " and ' 
simply can use the return as well.
End of string.  
"""

# Some methods with strings:

a_string = 'He threw three free throws'
print(a_string[0])
# >>> H
print(a_string[0:4])
# >>> He t
print('free' in a_string)
# >>> True

# .upper() / .lower()
print(a_string.upper())
# >>> HE THREW THREE FREE THROWS
print(a_string.lower())
# >>> he threw three free throws

# .isupper() / .islower()
print('Mixed CaSe'.isupper())
# >>> False
print('UPPER CASE'.isupper())
# >>> True
print('lower case'.islower())
# >>> True
print(''.islower())
# >>> False

# .isalpha(), isalnum(), isdecimal(), isspace(), .istitle()
print('abcdefg'.isalpha())  # only from the alphabet
# >>> True
print('abcdefg12356'.isalnum())  # like alpha but with numbers
# >>> True
print('123456765432'.isdecimal())  # only numbers
# >>> True
print('         '.isspace())  # only spaces
# >>> True
print('The First Letter Is Capitalized'.istitle())
# >>> True
print('i want to be titled'.title())
# >>> I Want To Be Titled


# .startswith(), .endswith()
name = 'Malte Iwanicki'
print(name.startswith('Malte'))
# >>> True
print(name.startswith('M'))
# >>> True
print(name.startswith('te Iwa'))
# >>> False
print(name.endswith('i'))
# >>> True
print(name.endswith('Iwanicki'))
# >>> True

# .join()
# used to join a string with a list of strings:
strings = ['We', 'surely', 'shall', 'see',
           'the', 'sun', 'shine', 'soon']
print('+'.join(strings))
# >>> We+surely+shall+see+the+sun+shine+soon

# .split()
# the opposit of .join, its called upon a string and
# splits it into a list of strings. The split symbol is cut out:
print('Eddie edited it'.split(' '))
# >>> ['Eddie', 'edited', 'it']
print('Eddie edited it'.split('d'))
# >>> ['E', '', 'ie e', 'ite', ' it']

# .ljust(n), .rjust(n), .center()
# adds spaces from left/ right till string reaches the length n
print('left'.ljust(10))
# >>> 'left      '
print('right'.rjust(10))
# >>> '     right'
print('right'.rjust(10,'#'))
# >>> #####right
print('center'.center(10,'*'))
# >>> **center**

# .strip(), .rstrip(), .lstrip()
# without a argument it removes whitespace.
print('***hello***'.strip('*'))
# >>> hello
print('***hello***'.strip('eh*'))
# >>> llo
print('***hello***'.rstrip('*'))
# >>> ***hello
print('***hello***'.lstrip('*'))
# >>> hello***

# .replace()
print('She sells seashells by the seashore'.replace('l','T'))
# >>> She seTTs seasheTTs by the seashore