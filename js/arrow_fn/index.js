const dollars = ["$ 32.00", "$ 15.00", "$ 12.00", "$ 17.00", "$ 20.00"];

// ARRAY MAP
// boomer
let prices = [];
for (let i = 0; i < dollars.length; i++) {
    prices[i] = Number(dollars[i].slice(1, dollars[i].length));
}
console.log(prices);

// zoomer
prices = [];
for (const dollar of dollars) {
    prices.push(Number(dollar.slice(1, dollar.length)));
}
console.log(prices);

// map
prices = [];
prices = dollars.map((dollar) => Number(dollar.slice(1, dollar.length)));
console.log(prices);

// filter
// manual
let expensive = [];

for (const price of prices) {
    if (price >= 20) {
        expensive.push(price);
    }
}
console.log(expensive);
// cool
expensive = [];
expensive = prices.filter((price) => price >= 20);
console.log(expensive);

// REDUCE
//  old ways
let sum = 0;

for (const price of expensive) {
    sum += price;
}
console.log(sum);
// nice way
sum = expensive.reduce((acum, price) => acum + price);
console.log(sum);

// ALL AT ONCE

sum = dollars
    .map((dollar) => Number(dollar.slice(1, dollar.length)))
    .filter((price) => price >= 20)
    .reduce((acum, price) => acum + price);

console.log(sum);
