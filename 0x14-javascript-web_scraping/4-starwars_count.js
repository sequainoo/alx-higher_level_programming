#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const userApiEnd = '/people/18/';

let all = [];
let userMovies = [];

request(url, (err, respose, body) => {
  if (err) {
    console.log(err);
  } else {
    all = JSON.parse(body).results;
    userMovies = all.filter((movie) => {
      const characters = movie.characters;
      for (const character of characters) {
        if (character.endsWith(userApiEnd)) {
          return true;
        }
      }
      return false;
    });
    console.log(userMovies.length);
  }
});
