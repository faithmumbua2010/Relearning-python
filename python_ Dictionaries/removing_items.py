# 1) pop()- removes the item with the specified key name

thisdict = {
    "brand" : "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.pop("model")
print(thisdict)

#  2) popitem() - removes the last inserted item 


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# 3) del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# 4) clear() - empties the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)