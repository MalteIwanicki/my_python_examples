# counts the characters of a string
string = 'Black back bat Black back bat Black back bat'

count = {}

for c in string.lower():
    count.setdefault(c,0)
    count[c] += 1

print(count)
# >>> {'b': 9, 'l': 3, 'a': 9, 'c': 6, 'k': 6, ' ': 8, 't': 3}

# pprint is a module that allows you to
# print out messy things much nicer.
# here it sorts it alphabetically.
import pprint
pprint.pprint(count)
# >>> {' ': 8, 'a': 9, 'b': 9, 'c': 6, 'k': 6, 'l': 3, 't': 3}

# .pformat() returns the above as a string
