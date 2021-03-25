# introducing regex

# this is a long basic way:
def is_date(text: str):
    def is_seperator(text: str):
        seperators = ['.', '/', '-']
        found = False
        for s in seperators:
            if s in text:
                found = True
                break
        return found

    if len(text) < 10:
        return False
    if not ((text[0:2].isdecimal())
            and (is_seperator(text[2]))
            and (text[3:5].isdecimal())
            and (is_seperator(text[5]))
            and (text[6:].isdecimal())):
        return False
    return True


def has_date(text: str):
    for i in range(len(text) + 1):
        chunk = text[i:i + 10]
        if is_date(chunk):
            return True
    return False


message = 'Hello, I need an appointment on the 11.06.2021. ' \
          'Please let me know if that\'s possible. ' \
          'malteiwa@gmail.com ' \
          'Best wishes Malte Iwanicki'

print(has_date(message))  # >>> True
print(has_date('20-12-2021'))  # >>> True
print(has_date('this is not a date'))  # >>> False

# Or use Regex
import re

# a date
# regex strings often have backslashes so we use a raw string
# r'' to avoid using backslash as an exit char.
date_re = re.compile(r"\d\d[./-]\d\d[./-]\d\d\d\d")
mo = date_re.search(message)  # returns a match object
print(mo)  # >>> <re.Match object; span=(36, 46), match='11.06.2021'>
print(mo.group())  # >>> 11.06.2021
print(date_re.findall(message))
# >>> ['11.06.2021']

# Or an email
email_re = re.compile(r'[\w-]+@([\w-]+\.)+[\w-]+')
print(email_re.search(message).group())
# >>> malteiwa@gmail.com

# Lets say we want the day, month and year of a date seperat:
# use brackets () to group your data:
date_splitted = re.compile(r"(\d\d)[./-](\d\d)[./-](\d\d\d\d)")

mo = date_splitted.search(message)  # returns a match object

print(mo.group())  # >>> 11.06.2021
# .group() returns still the same BUT we can give the group an Index now:
print('Day: %s  Month: %s  Year: %s' % (mo.group(1), mo.group(2), mo.group(3)))
# >>> Day: 11  Month: 06  Year: 2021
print(date_splitted.findall(message))
# >>> [('11', '06', '2021')]

# () in the regex string group the data, If we are actually looking for ()
# we need to use escape characters. \( <-would look for literally a bracket.
regex_with_brackets = re.compile(r"\(\d\d\)[./-]\(\d\d\)[./-]\(\d\d\d\d\)")
print(regex_with_brackets.findall('11.06.1993')) # cant find a match.
print(regex_with_brackets.findall('(11).(06).(1993)'))
# >>> ['(11).(06).(1993)']

# use the | pipesymbol to specify a or:
regex_or = re.compile(r'(super|spider|ant|bat|iron)man')
print(regex_or.search('there once was a superhero called antman.').group())
# >>> antman
print(regex_or.search('but superman was much stronger.').group())
# >>> superman
print(regex_or.findall('superman and batman are friends.'))
# >>> ['super', 'bat']

