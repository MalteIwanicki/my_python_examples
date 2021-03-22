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
date_re = re.compile(r"\d\d[./-]\d\d[./-]\d\d\d\d")
mo = date_re.search(message)  # returns a match object
print(mo) # >>> <re.Match object; span=(36, 46), match='11.06.2021'>
print(mo.group()) # >>> 11.06.2021
print(date_re.findall(message))
# >>> ['11.06.2021']

# Or an email
email_re = re.compile(r'[\w-]+@([\w-]+\.)+[\w-]+')
print(email_re.search(message).group())
# >>> malteiwa@gmail.com

