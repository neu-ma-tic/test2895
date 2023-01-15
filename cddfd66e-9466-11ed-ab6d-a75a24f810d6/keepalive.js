const http = require("http");
const express = require("express");
const app = express();
{
  app.get("/*", (request, response) => {
    response.send("<h2>Online</h2>"); // sends http status "OK"
  });
  app.listen(process.env.PORT);
  setInterval(() => {
    http.get("http://Mountain-Development-DiscordBot.mountaindev.repl.co");
  }, 280000);
}