const http = require('http');
http.createServer((_, res) => res.end("Server is Ready!")).listen(8080)