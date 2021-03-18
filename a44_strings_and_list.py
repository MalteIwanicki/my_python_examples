# some differences between strings and lists

# Similarities:
a_string = 'abcdefg'
print(a_string[3])  # >> d
print(a_string[-4:-1])  # >> def

a_list = list('abcdef')
print(a_list[3])  # >> d
print(a_string[-4:-1])  # >> def

# Differences:

# strings are immutable
# a_string[3] = '3'
# would throw an exception

# lists are mutable:
a_list[3] = '3'
print(a_list[3])  # >> 3

other_string = a_string  # Here a value is assigned to another Variable.
print(other_string)  # >> abcdefg
a_string = "something else"
print(other_string)  # >> abcdefg
# note how the value in other_string stays identical, while the origin changed.

other_list = a_list
print(other_list)  # >> ['a', 'b', 'c', '3', 'e', 'f']
a_list.append('some change')
print(other_list)  # >> ['a', 'b', 'c', '3', 'e', 'f', 'some change']
# note how other_list changed its value even though only a_list was edited
# other_list is only a reference to the existing list not its own unique list.
