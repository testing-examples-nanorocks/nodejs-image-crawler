const express = require("express");
const app = express();
const crawler = require("./crawler");
const morgan = require("morgan");

morgan("tiny");

app.use(express.static("json"));

app.get("/", (req, res) => {
  crawler('', res, 'index')
});

app.get("/search/:word", (req, res) => {
  crawler("/search/" + req.params.word, res, req.params.word);
});

app.listen(3000, () => {
  console.log(`listening at http://localhost:3000`);
});
