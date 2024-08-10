#!/usr/bin/node

const axios = require('axios');

// Check if a movie ID is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const filmURL = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Fetch film data
axios.get(filmURL)
  .then(response => {
    const characters = response.data.characters;

    // Fetch character data concurrently
    return Promise.all(characters.map(characterURL => axios.get(characterURL)));
  })
  .then(responses => {
    // Print each character name
    responses.forEach(response => console.log(response.data.name));
  })
  .catch(error => {
    console.error('Error:', error.message);
  });
