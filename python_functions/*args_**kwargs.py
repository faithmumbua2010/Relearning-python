  # *args and **kwargs allow functions to accept a unknown number of arguments.

# Arbitrary Arguements- *args

#   if you do not know how many arguments will be passed into your function, add a * before the parameter name.

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function ("Emil", "Tobias", "Linus")


