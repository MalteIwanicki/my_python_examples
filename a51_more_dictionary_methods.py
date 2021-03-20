# more methods with dictionaries

zoo = {'tigers': 4, 'elephants': 6, 'camels': 23, 'gorillas': 5}

# .get() avoids a KeyError exception
print(zoo.get('tigers'))
# >>> 4
print(zoo.get('giraffes'))
# >>> None
print(zoo.get('koalas', 0))
# >>> 0

zoo = {'tigers': 4, 'elephants': 6, 'camels': 23, 'gorillas': 5}

if 'lion' not in zoo:
    zoo['lion'] = 0
# or use .setdefault()  - assigns a value to a key if the key doesnt exist yet.
zoo.setdefault('horse',0)

print(zoo)
# >>> {'tigers': 4, 'elephants': 6, 'camels': 23, 'gorillas': 5, 'lion': 0, 'horse': 0}

