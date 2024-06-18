#!/usr/bin/node

const num = parseInt(process.argv[2]);
let output = '';

if (isNaN(num)) output = 'Not a number';
else output = 'My number: ' + num;
console.log(output);
