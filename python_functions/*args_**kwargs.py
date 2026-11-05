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



# Practical Example with *args
# A function that calculates the sum of any number of values:

def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_numbers(1, 2, 3))
print(sum_numbers(3, 8, 3))
print(sum_numbers(7, 9, 9))


# Finding the maximum value:
def my_function(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(my_function(3, 7, 2, 9, 1))


# Arbitrary Keyword Arguments - **kwargs
# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
# Inside the function, kwargs becomes a dictionary containing all the keyword arguments:



def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname= "Tobias", lname= "Refsnes"  )

# Accessing values from **kwargs
def my_function(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)

my_function(name = "Tobias", age= 30, city= "Bergen")


# Using **kwargs with Regular Arguments
# Regular parameters must come before **kwargs:

def my_function(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print("", key + ":", value)

my_function("emil123", age= 25, city= "Oslo", hobby = "coding")


# Combining *args and **kwargs
# The order must be:
   # regular parameters
   # *args
  # **kwargs

def my_function(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguements:", args)
    print("Keyword arguements:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")


# Unpacking Arguments
# The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.


# Unpacking Lists with * into arguements
def my_function(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # # Same as: my_function(1, 2, 3)
print(result)


