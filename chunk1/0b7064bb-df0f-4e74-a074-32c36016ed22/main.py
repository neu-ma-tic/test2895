import discord,os
from discord.ext import commands

#Global vars
token = os.getenv("MTAwMzI4NDU0MTE4NTcyODU5Mg.GM6ArD.ywN8UReMLmZ5OBpGecRo4T60QGLLxQIAWrwNBg")
bot_name = "BloxFlip Predictor | šø"
cmd_prefix = "."
mod_role = "Mod Role Name"

const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});

await lib.discord.channels['@0.3.0'].messages.create({
  "channel_id": `${context.params.event.channel_id}`,
  "content": `Prediction : `,
  "tts": false,
  "embeds": [
    {
      "type": "rich",
      "title": `zeltales predictor`,
      "description": `Prediction\nāāāāā\n āāāāā\nāāāāā\nāāāāā\nāāāāā`,
      "color": 0x0fd996,
      "fields": [
        {
          "name": `Accuracy`,
          "value": `98%\n`,
          "inline": true
        }
      ],
      "footer": {
        "text": `buy @ zeltales#0001`
      }
    }
  ]
});