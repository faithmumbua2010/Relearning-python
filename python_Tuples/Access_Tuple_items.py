# You can access tuple items by referring to the index number, inside square brackets

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
print(thistuple[0:2])

# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in this tuple")