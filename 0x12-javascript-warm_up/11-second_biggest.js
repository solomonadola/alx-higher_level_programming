#!/usr/bin/node

const { argv } = require('process');
if (argv.length === 2) {
  console.log(1);
} else if (argv.length === 3) {
  console.log(0);
} else {
  let firstMax = 1;
  let secondMax = 0;
  for (let i = 2; i < argv.length; i++) {
    if (Number(argv[i]) > firstMax) {
      firstMax = Number(argv[i]);
    } else if (Number(argv[i]) > secondMax) {
        secondMax = Number(argv[i]);
    }
  }
  console.log(secondMax);
}
