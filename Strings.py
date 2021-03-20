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
print(a_string.upper())
# >>> HE THREW THREE FREE THROWS
print(a_string.lower())
# >>> he threw three free throws