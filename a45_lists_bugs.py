# Some bugs with lists

def change(some_list):  # we expect the change of some_list to only effect
    some_list.append('something new')  # itself, not the global variable my_list


my_list = ['something old']
change(my_list)
print(my_list)  # >> ['something old', 'something new']
# but my_list changes because it only is a reference to the list in the memory
