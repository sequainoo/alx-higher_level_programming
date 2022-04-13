#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request(url, (err, response, data) => {
  if (err) {
    return console.log(err);
  }
  const movie = JSON.parse(data);
  const characters = movie.characters;
  let name = '';

  for (const character of characters) {
    request(character, (err, response, data) => {
      if (err) {
        console.log(err);
      } else {
        name = JSON.parse(data).name;
        console.log(name);
      }
    });
  }
});
