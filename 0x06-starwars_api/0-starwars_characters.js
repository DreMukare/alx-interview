#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

let charactersArray;

request(url, (err, res, body) => {
  err && console.log(err);

  charactersArray = (JSON.parse(res.body).characters);
  printNames(charactersArray);
});

const printNames = (charactersArray, i = 0) => {
  if (i === charactersArray.length) return;

  request(charactersArray[i], (err, res, body) => {
    err && console.log(err);

    console.log(JSON.parse(body).name);
    printNames(charactersArray, i + 1);
  });
};
