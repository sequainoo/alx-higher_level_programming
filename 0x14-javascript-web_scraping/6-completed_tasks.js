#!/usr/bin/node
const request = require('request');
const idMap = {};
const url = process.argv[2];

let todos = [];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    todos = JSON.parse(body);
    for (const todo of todos) {
      if (todo.completed) {
        const id = parseInt(todo.userId);
        if (!idMap[id]) {
          idMap[id] = 1;
        } else {
          idMap[id] += 1;
        }
      }
    }
    console.log(idMap);
  }
});
