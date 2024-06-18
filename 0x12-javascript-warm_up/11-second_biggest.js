#!/usr/bin/node

const arr = process.argv.slice(2);
const len = arr.length;

if (len <= 1) console.log(0);
else {
  arr.map(arg => parseInt(arg));
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
}
