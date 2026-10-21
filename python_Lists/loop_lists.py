# We can loop through a list by using for loop
thisList= ["apple", "banana", "cherry"]
for x in thisList:
    print(x)

# Loop through index numbers
fruits = ["pawpaw", 'mango', 'watermelon']
for i in range(len(fruits)):
    print(fruits[i])

# WHILE loop
# You can loop through the list items by using a while loop.

# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

# Remember to increase the index by 1 after each iteration.

people = ["Alvin", "Nancy", "Victor"]
i = 0
while i < len(people):
    print(people[i])
    i = i + 1

#  Looping using list Comprehension
places = ["Nairobi","Mombasa", "Kilifi"]
[print(x) for x in places]
