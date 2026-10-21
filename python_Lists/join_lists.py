#   Join two lists
#  1) + operator

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Append()- Adds an element at the end of the list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for y in list2:
    list1.append(y)

print(list1)


# extend()
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)