# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

# 1. Convert the tuple into a list to be able to change it

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x= tuple(y)

print(x)

# Add items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)

# Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

# delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists