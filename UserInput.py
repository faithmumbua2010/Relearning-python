# input() = A function that prompts the user to enter data
# Returns the entered data in a string

name = input("What is your name?:")
age = int(input("How old are you?:"))

age = age+ 1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY!!")
print(f"You are {age} years ols")


length = int(input("Enter the length:")) # The input return value of string so                                    #  you  should typecast to int or float
width = int(input("Enter the width:"))
area = length * width

print(f" The area is {area}cm^2")