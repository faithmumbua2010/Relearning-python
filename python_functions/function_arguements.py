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


def my_function(country = "Norway"):
    print("I am from", country)

my_function("Sweden")
my_function()


# Keyword Arguments
# You can send arguments with the key = value syntax.
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is ", name)

my_function(animal="dog", name="Buddy") # the order does not matter, you can even start with name


# Positional Arguments

# When you call a function with arguments without using keywords, they are called positional arguments.
# Positional arguments must be in the correct order:
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function("Buddy", "dog")


# Mixing Positional and Keyword Arguments
# positional arguments must come before keyword arguments:

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

# Passing Different Data Types
def my_function(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)


# passing dictionary
def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)