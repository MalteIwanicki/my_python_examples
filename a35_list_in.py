my_list = [1, 2, 3, 4, 5, [6, 7]]

def function(x):
    if x in my_list:
        print(str(x) + " is in my list")
    else:
        print(str(x) + " is not in my list")

function(3)  # 3 is in my list
function(6)  # 6 is not in my list
