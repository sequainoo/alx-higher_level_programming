#!/usr/bin/node

let size = process.argv[2];
size = parseInt(size);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  let line = '';
  for (let i = 0; i < size; i++) {
    line += 'X';
  }
  for (let i = 0; i < size; i++) {
    console.log(line);
  }
}
