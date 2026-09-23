# Variable- A container for a value 


#String
first_name= "Faith"  #first_name is our variable which we will assign a string
print(first_name)

last_name= "Mumbua"
food= "pizza"
email= "faithmumbua2010@gmail.com"
print(f"Hello {last_name}") #An f-string -  allows you to embed variables and expressions directly inside strings using curly braces 
print(f"You like {food}")
print(f"Your email is: {email}")

#Integers
age = 25
quantity = 3
num_of_students = 30


print(f"you are {age} years old")
print(f"you are buying {quantity} items")
print(f"Your class has {num_of_students} students")

#float
price= 10.99
gpa = 3.2

print(f"The price is ${price}")
print(f"Your gpa is:{gpa}")


#BOOLEAN
is_student = False


if is_student:
    print("You are a student")
else:
    print("You are NOT a student")