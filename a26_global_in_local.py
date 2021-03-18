def function():
    global animal
    animal = "cat"
    print(animal)

animal = "dog"
function()
print(animal)



def get_a_cat():
    a_cat = "cat"
    print(a_cat)
    return a_cat

animal = "dog"
animal = get_a_cat()
print(animal)

