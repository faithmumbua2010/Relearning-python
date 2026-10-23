
if (10 == 9)  {
    console.log("It is true")
} else{
    console.log("It is fasle")
}

a = 200;
b = 33;

if (b > a){
    console.log("b is greater than a")
}else{
     console.log("b is not  greater than a")
}

function myFunction(){
    return true}

    if (myFunction()) {
        console.log("YES")
    }else{
        console.log("NO")
    }


myFunction()

// Ternary operator
 age = 19;
let text = (age< 18) ? "Minor" : "Adult";

console.log(text);

let isMember = true;
let discount = isMember ? 0.2 : 0;
console.log(discount)


let number = 3;
if (number > 3){
    console.log("odd")
}else{
    console.log("even")
 }

function myFunction2(){
    let x= 25;
  if(x> 50){
    console.log("You can register")
  }else{
    console.log("You CANNOT register")
  };

}
myFunction2()

// Array length 
// syntax
//  array.length- return the length on an array
//  array.length= number - set the lenth of an array
const fruits = ["apple", "grapes", "mango", "peach"];
console.log(fruits.length)

//  set the length of an array
const people = ["Alvin", "Nancy", "Bradley"];
people.length = 2;
console.log(people)

let i = 3;
for(let i=0; i<5; i++){
 console.log(i);
}

// appending an array to another
//  1) Spread operator

const array1 = [1, 2, 3];
const array2 = [4, 5, 6];

const combined = [...array1, ...array2];
console.log(combined)

//  2) concat()

const array3 = [1, 2, 3];
const array4 = [4, 5, 6];

const combined2 = array1.concat(array2);
console.log(combined2)

//  push() but modifies the original
const friends= ["Alvin", "Nancy", "Victor"];
const people2= ["Faith", "Jean", "janet"];

friends.push(...people2);
console.log(friends);

// sets
// creating a Set - use the new Set() method
const letters = new Set(["a","b","c"]);
console.log(letters);

//  Add values to the set
const numbers = new Set();
numbers.add(1);
numbers.add(2);
numbers.add(3);
numbers.add(1);
numbers.add(1);

console.log(numbers);

//  Objects- variables that can store both values and functions
//  values are stored as key:value pairs called properties
// functions are stored  as key:function() pairs called methods
const user = {
    name: "Alex",
    age: 28,
    isAdmin: true,
  
};
console.log(user.name);

const person ={};
//  Add properties
person.firstName = "John";
person.lastName = "Doe";
person.age = 50;
person.eyeColor = "blue";

console.log(person);

// Object access
//  .Dot notation   - objectName.propertyNmae  
// []Bracket notation- objectName["propertyName"]

const person2 = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  fullName: function(){
    return this.firstName + " " + this.lastName;
  }
}


//  adding a property
person2.country ="Kenya";

console.log(person2.fullName()); // this.  refers to object
console.log(person2);

