const express = require('express');
const path = require('path');
const server = express();




server.get('/', (req, res) => {
  res
  .status(200)
  .send('NOTHING HERE - BEING UPDATE FOR U')

})

function keepAlive(){
   server.listen(3000, ()=>{console.log("Server đang được chạy ✔️")});
}



module.exports = keepAlive;