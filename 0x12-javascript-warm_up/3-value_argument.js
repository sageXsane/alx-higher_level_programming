#!/usr/bin/node

const arg = process.argv[2];
let output = '';

if (!arg) output = 'No argument';
else output = arg;
console.log(output);
