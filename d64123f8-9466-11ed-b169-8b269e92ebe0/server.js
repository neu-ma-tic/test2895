// ik, you shouldn't host bots on replit, but this is gonna be on prolly 2 - 3 servers so

const express = require('express');

const server = express();

server.all("/", (req, res) => {
    res.send("Talking Ben is currently running! ^^");
})

function keepAlive() {
  server.listen(3000, () => {
    console.log("Server is ready!");
  })
}

module.exports = keepAlive;