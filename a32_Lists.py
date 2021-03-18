lol = [["apple","banana","pear"],["elppa","ananab","reap"],[[1,2,3],[4,5,6]]]

print(lol[0][0])  # apple
print(lol[1][-1])  # reap
print(lol[2][0][2])  # 3
print(lol[2][1])  # [4, 5, 6]
print(lol[0][0:2])  # ['apple', 'banana']
print(lol[2][0][1:])  # [2, 3]

print(len(lol))

# you can also assign a list with line breaks
a_list = ['banana',
        'apple',
        'cherry',
        'orange']

# this works also for other types using the \
a_string = 'this is a very very very very very very long ' \
           'string'
