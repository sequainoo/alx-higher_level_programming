#!/usr/bin/node
const request = require('request');
const id_map = {};
const url = process.argv[2];

let todos = []

request(url, (err, response, body) => {
  if (err) {
    console.log(error);
  } else {
    todos = JSON.parse(body);
    for (let todo of todos) {
      if (todo.completed) {
        let id = parseInt(todo.userId)
        if (!id_map[id]) {
	  id_map[id] = 1;
	} else {
	  id_map[id] += 1;
	}
      }
    }
    console.log(id_map);
  }
});
