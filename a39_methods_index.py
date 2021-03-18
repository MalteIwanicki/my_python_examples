# A method is like a function of an object you call it with the object name and then a dot
# and then the method name with the parameters

my_list = ['tree', 'banana', 'pancake']
print(my_list.index('banana'))  # returns the index of the first element called 'banana'.
# => 1

a_list = ['a', 'a', 'a']
print(a_list.index('a'))
# => 0
print(a_list.index('b'))
# raises "ValueError: 'b' is not in list" Exception
