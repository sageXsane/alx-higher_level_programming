#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (isNaN(num)) { console.log('Missing size'); } else {
  let i, j;
  for (i = 0; i < num; i++) {
    let row = '';
    for (j = 0; j < num; j++) {
      row = row + 'X';
    }
    console.log(row);
  }
}
