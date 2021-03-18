# this shows how to create a real copy of a list

# Copy each value individual into your new variable using a for loop
my_list = [0, 1, 2, 3, 4, 5]
other_list = []
for i in my_list:
    other_list.append(my_list[i])
my_list[3] = 42
print(my_list)  # >> [0, 1, 2, 42, 4, 5]
print(other_list)  # >> [0, 1, 2, 3, 4, 5]

# use the copy module
import copy

my_list = [1, 2, 3, 4, 5]
other_list = copy.deepcopy(my_list)
my_list.append(6)
print(my_list)  # >> [1, 2, 3, 4, 5, 6]
print(other_list)  # >> [1, 2, 3, 4, 5]
