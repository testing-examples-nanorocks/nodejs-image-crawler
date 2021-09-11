const express = require("express");
const app = express();
const crawler = require("./crawler");

app.use(express.static("json"));

app.get("/", (req, res) => {
  crawler();
  res.json(require('./json/index.json'))
});

app.get("/search/:word", (req, res) => {
  crawler("/search/" + req.params.word);
  res.json(require("./json/search.json"));
});

app.listen(3000, () => {
  console.log(`listening at http://localhost:3000`);
});
