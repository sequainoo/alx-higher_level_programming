#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

const charactersPromise = new Promise((resolve, reject) => {
  request(url, (err, response, data) => {
    if (err) {
      reject(err);
    }
    const movie = JSON.parse(data);
    const characters = movie.characters;
    resolve(characters);
  });
});

charactersPromise
  .then(async characters => {
    for (const character of characters) {
      const name = await new Promise((resolve, reject) => {
        request(character, (err, response, data) => {
          if (err) {
            reject(err);
          } else {
            resolve(JSON.parse(data).name);
          }
        });
      });
      console.log(name);
    }
  });
