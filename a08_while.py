count = 0
# RIGHT - better to read, easier to find the loop
while count < 10:
    count += 1
    print(count)

count = 0
# WRONG - single line while loop with one statement is possible, but bad practise
while count < 10: count += 1; print(count)

print ("done")