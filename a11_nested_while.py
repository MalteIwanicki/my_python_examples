x = 0
y = 0

while x < 10:
    while x+y < 10:
        if x == 3 and y == 2:
            break
        print(y, end=" ")
        y += 1
    y = 0
    print()
    x += 1
