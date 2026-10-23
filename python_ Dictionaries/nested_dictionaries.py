myfamily= {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2":{
        "name":"Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

print(myfamily)

#  Access Items in Nested Dictionaries

myfamily= {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2":{
        "name":"Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

print(myfamily["child1"]["name"]) # Emil


# Loop Through Nested Dictionaries- items()

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ' : ', obj[y])