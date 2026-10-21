#  Copying lists
#  1) copy()

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# 2) list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# 3) Slice operator :
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)