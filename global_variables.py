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
    t = "smart" # this is a local variable
    print(f"Faith is {t}")

myfunc()

print(f"Our class is {x}")

    #  GLOBAL VARIABLES INSIDE FUNCTIONS
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.

def myfuntion():
    global p 
    p = "fantastic"

myfuntion()

print(f"Bawlinf is {p}")

# CHANGING THE VALUE OF GLOBAL VALUE INSIDE A FUNCTION
x = "awesome"

def myPythonFunc():
    global x
    x= "fantastic"

myPythonFunc()

print(f"Mary is {x}")

