#!/usr/bin/node

const { argv } = require('process');
if (argv.length <= 3) {
  console.log(1);
} else {
  const numbers = argv.slice(2, argv.length)
    .map((num) => Number(num)).sort((x, y) => x - y);
  console.log(numbers[numbers.length - 2]);
}
