//4. Create an object "person" with properties firstname and lastname. Display these
//properties using 2 different ways of accessing.
const person = {
  firstName: "rahul",
  lastName: "koppula",
};
// firstWay
console.log(person.firstName);
console.log(person.lastName);

//secondWay
console.log(person["firstName"]);
console.log(person["lastName"]);