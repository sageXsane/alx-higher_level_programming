#!/usr/bin/node

const numArgs = process.argv.length - 1;
let output = '';

if (numArgs <= 1) output = 'No argument';
else if (numArgs === 2) output = 'Argument found';
else output = 'Arguments found';
console.log(output);
