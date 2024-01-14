#!/usr/bin/node
const { argv } = require('process');
if (!isNaN(Number(argv[2]))) {
  console.log('My number: ' + argv[2]);
} else {
  console.log('Not a number');
}
