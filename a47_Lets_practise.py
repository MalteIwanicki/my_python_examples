# Some exercises
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1
def sum(list):
    output = 0
    for i in list:
        output += i
    return output
print(sum(my_list))

# 2
def dif(list):
    output = list[0]
    for i in list[1:]:
        output -= i
    return output
print(dif(my_list))

# 3
def max(list):
    output = list[0]
    for i in list:
        if i > output:
            output = i
    return output
print(max(my_list))

# 4
def min(list):
    output = list[0]
    for i in list:
        if i < output:
            output = i
    return output
print(min(my_list))

# 5
my_list = ['abc', 'xyz', 'aba', '1221']
def check_letters(list):
    count = 0
    for i in list:
        if len(i) >= 2 and i[0] == i[-1]:
            count += 1
    return count
print(check_letters(my_list))
