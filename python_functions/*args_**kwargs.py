  # *args and **kwargs allow functions to accept a unknown number of arguments.

# Arbitrary Arguements- *args

#   if you do not know how many arguments will be passed into your function, add a * before the parameter name.

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function ("Emil", "Tobias", "Linus")

# What is *args?
# The *args parameter allows a function to accept any number of positional arguments.

# Inside the function, args becomes a tuple containing all the passed arguments:

def my_function(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")


# Using *args with Regular Arguments
# Regular parameters must come before *args:
def my_function(greeting, *names):
    for name in names:
        print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")
