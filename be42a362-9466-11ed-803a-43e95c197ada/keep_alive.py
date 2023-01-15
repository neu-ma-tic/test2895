from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Your Holy Slave Has Been Awaken To Serve You Master Blast. Your Desire Is My Life's Command. - Your_Holy_Slave"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()