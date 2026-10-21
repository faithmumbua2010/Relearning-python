# Tuples are used to store multiple items in a single variable.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = "apple", "banana", "cherry"
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple length
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(len(thistuple))

# Create Tuple With One Item

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple
thistuple = ("apple",)
print(type(thistuple))


#NOT a tuple
thistuple = ("apple")
print(type(thistuple))  # outputs STRING

# Empty tuple
thistuple = ()
print(type(thistuple))
