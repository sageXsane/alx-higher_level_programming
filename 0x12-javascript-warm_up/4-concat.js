#!/usr/bin/node

const arg2 = process.argv[2];
const arg3 = process.argv[3];
let output = '';

if (!arg2) output = 'undefined';
else output = arg2;
output = output + ' is ';
if (!arg3) output = output + 'undefined';
else output = output + arg3;
console.log(output);
