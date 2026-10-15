
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

