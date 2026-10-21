# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)

# print(newlist)

#  Now let us use list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

# THE SYNTAX 
#  newlist = [expression for item in iterable if condition == True]

newlist = [x for x in range(10) if x < 5]
print(newlist)
