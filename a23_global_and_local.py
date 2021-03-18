a_global_variable = "I'm global."

def function():
    print(a_global_variable)
    a_local_variable = "I'm local."
    print(a_local_variable)

function()
print(a_local_variable)
