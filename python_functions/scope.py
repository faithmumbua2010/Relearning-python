# A variable is only available from inside the region it is created. This is called scope.
# Local Scope - a variable created inside a function and can only be used inside that function

def myfunc():
    x= 300
    print(x) 

myfunc()
# print(x) - x is not defined


# Function Inside Function
# he variable x is not available outside the function, but it is available for any function inside the function:

def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()