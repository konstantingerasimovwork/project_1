'use strict';

// Dolphins score 44, 23 and 71.
// Koalas score 65, 54 and 49
// Dolphins score 85, 54 and 41.
// Koalas score 23, 34 and 27

// $(document).ready(function () {
//     $('#calendar').eCalendar();
// });

// const calcAverage = (scoreOne, scoreTwo, scoreThree) => (scoreOne + scoreTwo + scoreThree) / 3;

// // const calcAverageDolphins = calcAverage(44, 23, 71);
// // const calcAverageKoalas = calcAverage(65, 54, 49);

// const calcAverageDolphins = calcAverage(85, 54, 41);
// const calcAverageKoalas = calcAverage(23, 34, 27);

// const checkWinner = function (avgDolhins, avgKoalas) {
//     if (calcAverageDolphins >= (calcAverageKoalas * 2)) {
//         console.log(`The Dolphins win (${calcAverageDolphins} vs ${calcAverageKoalas})`);
//     } else if (calcAverageKoalas >= (calcAverageDolphins * 2)) {
//         console.log(`The Koalas win (${calcAverageKoalas} vs ${calcAverageDolphins})`);
//     } else (console.log("Nobody win!"))
//     return;
// };

// checkWinner(calcAverageDolphins, calcAverageKoalas);

// const calcAverage = (scoreOne, scoreTwo, scoreThree) => (scoreOne + scoreTwo + scoreThree) / 3;

// // const calcAverageDolphins = calcAverage(44, 23, 71);
// // const calcAverageKoalas = calcAverage(65, 54, 49);

// let calcAverageDolphins = calcAverage(85, 54, 41);
// let calcAverageKoalas = calcAverage(23, 34, 27);

// const checkWinner = (avgDolhins, avgKoalas) =>
//     (calcAverageDolphins >= (calcAverageKoalas * 2)) ? console.log(`The Dolphins win (${calcAverageDolphins} vs ${calcAverageKoalas})`) : (calcAverageKoalas >= (calcAverageDolphins * 2)) ? console.log(`The Koalas win (${calcAverageKoalas} vs ${calcAverageDolphins})`) : console.log("Nobody win!");

// checkWinner(calcAverageDolphins, calcAverageKoalas);

// calcAverageDolphins = calcAverage(44, 23, 71);
// calcAverageKoalas = calcAverage(65, 54, 49);

// checkWinner(calcAverageDolphins, calcAverageKoalas);

// function pow(x, n) {
//     let result = 1;

//     for (let i = 0; i < n; i++) {
//         result *= x;
//     }

//     return result;
// }

// let x = prompt("x?", '');
// let n = prompt("n?", '');

// if (n <= 0) {
//     alert(`Степень ${n} не поддерживается,
//     введите целую степень, большую 0`);
// } else {
//     alert(pow(x, n));
// }

// const friends = ['Peter', 'Ben', 'John', 'Steve'];
// console.log(friends);
// console.log(friends.length);
// console.log(friends[0]);
// friends[2] = 'Bob';
// console.log(friends);

// const me = ['Konstantin', 'Gerasimov', 34, 'male', friends];
// console.log(me.length);
// console.log(me);
// const stillMe = me.push('married');
// console.log(me);
// me.unshift(stillMe);
// console.log(me);
// console.log(me.at(-2));

// The bill was 275, the tip was 41.25,
// and the total value 316.25

// const bill = 40;

// const fullBill = bill >= 50 && bill <= 300 ? `The bill was ${bill}, the tip was ${bill * 0.15},
// and the total value ${bill + (bill * 0.15)}` : `The bill was ${bill}, the tip was ${bill * 0.2},
// and the total value ${bill + (bill * 0.2)}`;

// console.log(fullBill);

// let calcTip = function (bill) {
//     let tip = bill >= 50 && bill <= 300 ? bill * 0.15 : bill * 0.2;
//     console.log(`The bill was ${bill}, the tip was ${tip}, and
//     the total value ${bill + tip}`);
//     return tip;
// };

// calcTip(100);

// let bills = [125, 555, 44];

// let tips = [calcTip(bills[0]), calcTip(bills[1]), calcTip(bills[2])];
// console.log(bills, tips);

// let total = [bills[0] + tips[0], bills[1] + tips[1], bills[2] + tips[2]];
// console.log(total);

// const user = {};
// const user = {
//     name: "John",
//     surname: "Smith",
// };

// user.name = "Pete";
// delete user.name;

// function isEmpty(obj) {
//     if (obj === undefined) {
//         return console.log(true);
//     } else (console.log(false));
// };

// isEmpty(1);

// function isEmpty(obj) {
//     for (let key in obj) {
//         return console.log(false);
//     }
//     return console.log(true);
// }

// isEmpty();

// const jonas = {
//   'first Name': 'Jonas',
//   lastName: 'Shmedtmann',
//   age: 2037 - 1991,
//   friends: ['Micael', 'John', 'Peter'],
// };
// console.log(jonas);
// jonas.country = 'America';
// delete jonas.country;
// console.log(jonas['first Name'], jonas.friends[2]);
// // Jonas has 3 frinds, and his best friend is Micael.

// console.log(
//   `${jonas['first Name']} has ${jonas.friends.length} friends, and his best friend is ${jonas.friends[0]}.`
// );

// for (let key in jonas) {
//   console.log(key);
//   console.log(jonas[key]);
// }




// let salaries = {
//   John: 100,
//   Ann: 160,
//   Pete: 130
// }

// let sum = Number(salaries.John + salaries.Ann + salaries.Pete);
// console.log(sum)

// let user = {};
// user[7] = 'Go';

// const jonas = [
//     'Jonas',
//     'Schmedmann',
//     2037 - 1991,
//     'teacher',
//     ['Michael', 'Peter', 'Steven']
// ];

// for(let  i = 0; i < 5; i++){
//     console.log(jonas[i]);
// }

// for (let i = 0; i < 3; i++) {
//     alert( `number ${i}!` );
//   }

// let count = prompt('Введите число больше 100?', 0);
// count = Number(count);
// let i = 0;
// do{
//     alert(prompt('Введите число больше 100?', 0));
// } while (count < 101){
//     alert(prompt('Введите число больше 100?', 0));
//     i++;
// }

// let num;

// do {
//   num = prompt("Введите число больше 100?", 0);
// } while (num <= 100 && num);

async function testTaxiResult() {

}

testTaxiResult();
