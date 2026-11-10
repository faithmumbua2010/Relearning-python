# A variable is only available from inside the region it is created. This is called scope.
# Local Scope - a variable created inside a function and can only be used inside that function

def myfunc():
    x= 300
    print(x) 

myfunc()
# print(x) - x is not defined


