#!/usr/bin/node
const fs = require('fs');
const filename = process.argv[2];

fs.readFile(filename, 'utf8', (err, text) => {
  if (err) {
    console.log(err);
  }
  else {
    console.log(text);
  }
});
