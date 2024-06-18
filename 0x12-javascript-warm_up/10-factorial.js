#!/usr/bin/node

function factorial (a) {
  let ans = 1;
  if (isNaN(a)) return (1);

  let i;
  for (i = 1; i <= a; i++) {
    ans *= i;
  }
  return (ans);
}

const output = factorial(parseInt(process.argv[2]));
console.log(output);
