const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.type('text/plain');
  const databaseFile = process.argv[2];

  if (!databaseFile) {
    res.status(400).send('Please provide the database file path as an argument.');
    return; // Important : arrête l'exécution ici
  }

  countStudents(databaseFile)
    .then((output) => {
      res.send(`This is the list of our students\n${output}`);
    })
    .catch((error) => {
      res.status(500).send(error.message);
    });
});

app.listen(1245);

module.exports = app;
