# sort() sorts the list in numerical or alphabetical order
import random

number_list = []
for i in range(11):
    number_list.append(random.randint(0, 20))
print(number_list)
#[20, 7, 15, 20, 2, 10, 12, 8, 5, 10, 10]
number_list.sort()
print(number_list)
#[2, 5, 7, 8, 10, 10, 10, 12, 15, 20, 20]

string_list = list('C!e,aA37')
print(string_list)
#['C', '!', 'e', ',', 'a', 'A', '3', '7']
string_list.sort(reverse=True)
print(string_list)
#['e', 'a', 'C', 'A', '7', '3', ',', '!']
