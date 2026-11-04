# creating a function

def my_function():
    print("Hello from a function")
my_function()
my_function()

# Function names- It's good practice to use descriptive names that explain what the function does.

def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))


# Return values
# When a function reaches a return statement, it stops executing and sends the result back:

def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message)

def get_greeting():
    return "Hello from a function"

print (get_greeting())

# The pass Statement
def my_function():
  pass  # for creating a function placeholder without any code
