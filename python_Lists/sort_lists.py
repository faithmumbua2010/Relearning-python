# Sort List Alphanumerically
#  sort() - sorts alphanumerrically ascending

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort descending
# reverse = true

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse= True)
print(thislist)

# Customize sort function
def myfunc(n):
    return abs(n- 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


#  sort() is case sensitive
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#  insensitive sort()
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key= str.lower)
print(thislist)

#  reverse()
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)