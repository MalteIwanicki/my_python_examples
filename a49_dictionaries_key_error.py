# example for the key error

# trying to access a value with a not existing key throws a KeyError exception.
my_dict = {1: 'value', 2: 'value2'}
print(my_dict['a different key'])
"""
Traceback (most recent call last):
  File "C:/Users/malte/Desktop/VHS/examples/a49_dictionaries_key_error.py", line 4, in <module>
    print(my_dict['a different key'])
KeyError: 'a different key'
"""
