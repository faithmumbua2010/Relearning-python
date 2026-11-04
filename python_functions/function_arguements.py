# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the actual value that is sent to the function when it is called.

def my_function(fname): #fname- parameter
    print(fname + " Refsnes")

my_function("Emil")  # Emil- arguement
my_function("Tobias")
my_function('Linus')
# When the function is called, we pass along a first name, which is used inside the function to print the full name:


# Default Parameters Values
# You can assign default values to parameters. If the function is called without an argument, it uses the default value:

def my_function(name = "friend"):
    print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function() # returns Hello friend

