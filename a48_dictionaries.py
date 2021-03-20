# an introduction to dictionaries
# Dictionary hold a pair of values. A key and its value;  key: value
# the values are mutable while the keys are immutable.

# Dictionaries can be created using curly {} braces seperated by commas
a_dict = {'key': 'value', 'different_key': 'value2'}
print(a_dict)
# >>> {'key': 'value', 'different_key': 'value2'}

# access a value like a list one but use it's key instead of an index.
print(a_dict['key'])
# >>> value

# change a value like a list but instead of an index use a key.
a_dict['key'] = 'new value'
print(a_dict)
# >>> {'key': 'new value', 'different_key': 'value2'}

# Example:
person = {'name': 'Malte', 'age': 27}
print('Hello, my name is ' + person['name'] + ". I'm "
      + str(person['age']) + ' years old.')
# >>> Hello, my name is Malte. I'm 27 years old.

# unlike lists dictionaries are unordered
print([1, 2] == [2, 1])
# >>> False

print({1: 1, 2: 2} == {2: 2, 1: 1})
# >>> True

# in operator, not in also works
def start_car(car):
      if 'driver' in car:
            print('bruummm....')
      else:
            print('Waiting for the driver.')

car1 = {'driver': 'Max',
       'passengers': ['Martina', 'Ben', 'Robyn', 'Lilo']}
start_car(car1)
# >>> bruummm....

car2 = {'passengers': ['Arthur']}
start_car(car2)
# >>> Waiting for the driver.

# .keys(), .values() and .items() methods return list-like types
zoo_food = {'tiger': 'meat', 'zebra': 'grass', 'snake': 'mice'}

# .keys()
print(zoo_food.keys())
# >>> dict_keys(['tiger', 'zebra', 'snake'])

# convert it to a list if you want to work with the values
print(list(zoo_food.keys()))
# >>> ['tiger', 'zebra', 'snake']

for k in zoo_food.keys():
      print(k)
      # tiger
      # zebra
      # snake

# .values()
print(list(zoo_food.values()))
# >>> ['meat', 'grass', 'mice']

for v in zoo_food.values():
      print(v)
      # meat
      # grass
      # mice

# .items()
print(list(zoo_food.items()))
# >>> [('tiger', 'meat'), ('zebra', 'grass'), ('snake', 'mice')]
for k, v in zoo_food.items():
      print(k + ' eat ' + v)
      # tiger eat meat
      # zebra eat grass
      # snake eat mice

print(type(zoo_food.items()))
# >>>  <class 'dict_items'>