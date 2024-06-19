#!/usr/bin/node
let counter = +process.argv[2];
if (!counter) {
  console.log('Missing number of occurrences');
} else {
  while (counter > 0) {
    console.log('C is fun');
    --counter;
  }
}
