from flask import Flask
from threading import Thread

app = Flask("Pogchamp")

@app.route("/")
def home():
  return "This message is very pog"
def run():
  app.run(host="0.0.0.0",port=8080)

def keep_alive():
  server = Thread(target=run)
  server.start()