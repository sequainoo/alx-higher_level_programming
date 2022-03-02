#!/usr/bin/node

let biggest = parseInt(process.argv[2]);
let biggest2 = parseInt(process.argv[3]);
const arr = [];

if (isNaN(biggest) || isNaN(biggest2)) {
  console.log(0);
} else {
  if (biggest < biggest2) {
    let tmp = biggest;
    biggest = biggest2;
    biggest2 = tmp;
  }
  for (let i = 4; i < process.argv.length; i++) {
    arr.push(parseInt(process.argv[i]));
  }
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] >= biggest) {
      biggest2 = biggest;
      biggest = arr[i];
    } else if (arr[i] > biggest2) {
      biggest2 = arr[i];
    }
  }
  console.log(biggest2);
}
