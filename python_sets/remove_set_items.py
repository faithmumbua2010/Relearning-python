# To remove an item in a set, use the remove(), or the discard() method.

thisset = {"apple", "banana", "cherry"}
thisset.remove("apple")
print(thisset)


# Note: If the item to remove does not exist, discard() will NOT raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.discard("pie")
print(thisset)

# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


#  del deletes the set completely
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset) # it will throw an error
