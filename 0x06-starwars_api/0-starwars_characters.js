#!/usr/bin/node

const request = require('request');

// Base URL for the Star Wars API
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

// Function to make HTTP GET requests and return a promise
function fetchData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to load ${url}, status code: ${response.statusCode}`));
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

// Function to fetch and display character names for a given film
async function displayCharacters (movieId) {
  try {
    // Validate movieId
    if (isNaN(movieId)) {
      console.error('Movie ID must be a number.');
      return;
    }

    // Fetch movie data
    const filmData = await fetchData(`${filmURL}${movieId}/`);
    const characterURLs = filmData.characters;

    // Fetch all characters concurrently but display in order
    const characterPromises = characterURLs.map(url => fetchData(url));
    const characterData = await Promise.all(characterPromises);

    // Print each character's name in the order received
    characterData.forEach(character => {
      console.log(character.name);
    });
  } catch (error) {
    console.error('Error:', error.message);
  }
}

// Main function to parse input and invoke character display
function main () {
  const movieId = process.argv[2];
  if (!movieId) {
    console.error('Usage: ./0-starwars_characters.js <movie_id>');
    return;
  }
  displayCharacters(movieId);
}

// Start the script
main();
