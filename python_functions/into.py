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
