#!/usr/bin/node

const request = require('request');

const filmNum = process.argv[2] + '/';
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

request(filmURL + filmNum, async function (err, res, body) {
  if (err) {
    console.error('Error fetching film:', err);
    return;
  }

  const charURLList = JSON.parse(body).characters;

  for (const charURL of charURLList) {
    await new Promise(function (resolve, reject) {
      request(charURL, function (err, res, body) {
        if (err) {
          console.error('Error fetching character:', err);
          reject(err); // If error occurs, reject the promise
        } else {
          console.log(JSON.parse(body).name);
          resolve(); // Resolve the promise once the character name is logged
        }
      });
    });
  }
});
