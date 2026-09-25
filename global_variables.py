# Variables that are created outside of a function and can be used both inside and outside functions

# GLOBAL VARIABLES
x = "awesome"

def myfun():
    print("Python is" + x)
    print(f"Python is {x}") # they all do the same thing

myfun()  # we are calling the function , if we DON'T call it, nothing gets dispalyed

# LOCAL VARIABLES
x= "full" # This is a global variable
def myfunc():
    x= "smart" # this is a local variable
    print(f"Faith is {x}")

myfunc()

print(f"Our class is {x}")
