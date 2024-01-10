#!/usr/bin/node

const { argv } = require('process');

function factorial (num) {
  if (isNaN(Number(num)) || Number(num) === 1) {
    return 1;
  }
  return Number(num) * factorial(Number(num) - 1);
}
console.log(factorial(argv[2]));
