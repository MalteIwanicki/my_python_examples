# remove() removes the first element
# with the given value.

a_list = ['a', 'a', 'b', 'a']
a_list.remove('b')
print(a_list)
# => ['a', 'a', 'a']
a_list.remove('a')
print(a_list)
# => ['a', 'a']

# pop() removes and returns the last item
a_list = [0, 1, 2, 3, 4, 5]
print(a_list.pop())  # >> 5
print(a_list)  # >> [0, 1, 2, 3, 4]
#pop(i) removes and returns the item at given index
print(a_list.pop(1))  # >> 1
print(a_list)  # [0, 2, 3, 4]
