const app = require('express')();

app.all('/', (req, res)=>{
    res.send('Your bot is alive!')
})

function keepAlive(){
    app.listen(3000, ()=>{console.log("Server is Ready!")});
}

module.exports = keepAlive;
