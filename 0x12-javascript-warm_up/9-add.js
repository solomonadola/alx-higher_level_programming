#!/usr/bin/node

const { argv } = require('process');
if (isNaN(Number(argv[2])) || isNaN(Number(argv[3]))) {
  console.log('NaN');
} else {
  console.log(Number(argv[2]) + Number(argv[3]));
}
