#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const endpoint = `https://swapi-api.hbtn.io/api/films/${id}`;

request(endpoint, (err, response, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(data).title);
  }
});
