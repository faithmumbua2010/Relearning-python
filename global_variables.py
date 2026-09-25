# Variables that are created outside of a function and can be used both inside and outside functions

x = "awesome"

def myfun():
    print("Python is" + x)
    print(f"Python is {x}") # they all do the same thing

myfun()  # we are calling the function 