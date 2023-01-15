const http = require("express");
const run = http();
const port = 3000;
(async () => {
  try {
    run.get("/", async (req, res) => {
      res.send("keep_alive")
    });
    const ch = require("chalk");
    run.listen(port, async () => {
      console.log(ch.cyan(".. || Successfully Executed Keep_alive file || .."))
    });
  } catch (error) {
    if (error) return;
  }
})();
