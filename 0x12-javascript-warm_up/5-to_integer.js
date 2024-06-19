#!/usr/bin/node
(isFinite(Number(process.argv[2]))) ? console.log(`My number: ${process.argv[2]}`) : console.log('Not a number');
