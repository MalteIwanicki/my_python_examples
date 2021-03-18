cat = ["big", "black", "butter"]
size = cat[0]
color = cat[1]
favorite_food = cat[2]

size, color, favorite_food = cat

size, color, favorite_food = "small", "orange", "fish"
print("color: " + color)

# Good for swapping:
a = 4
b = "i love cats"

a, b = b, a
print("a: "+ a)
print("b: " + str(b))
