# # input() = A function that prompts the user to enter data
# # Returns the entered data in a string

# name = input("What is your name?:")
# age = int(input("How old are you?:"))

# age = age+ 1

# print(f"Hello {name}!")
# print("HAPPY BIRTHDAY!!")
# print(f"You are {age} years ols")


# length = int(input("Enter the length:")) # The input return value of string so                                    #  you  should typecast to int or float
# width = int(input("Enter the width:"))
# area = length * width

# print(f" The area is {area}cm^2")



#Exercise 2 - Shopping Cart Program

item = input("What item would you like to buy?:")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")