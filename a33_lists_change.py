my_list = [0,1,2,3,4,5,6,7,8,9]
print(my_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list[4] = "hello"
print(my_list)  # [0, 1, 2, 3, 'hello', 5, 6, 7, 8, 9]
my_list[2:4] = [0,0,0]
print(my_list)  # [0, 1, 0, 0, 0, 'hello', 5, 6, 7, 8, 9]
other_list = [10,11,12]
my_list = my_list + other_list
print(my_list)  # [0, 1, 0, 0, 0, 'hello', 5, 6, 7, 8, 9, 10, 11, 12]
my_list = [1,2,3]*2
print(my_list)  # [1, 2, 3, 1, 2, 3]

