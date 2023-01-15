const { Client, MessageEmbed } = require('discord.js')
const config = require('./config')
const fs = require("fs")
const data = require('data')

let bot = new Client({
  presence: {
    status: config.status,
    activity: {
      name: config.activity,
      type: config.status_type
    }
  }
})

bot.login(config.bottoken)
require('./server')()

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
function Save(data,filename) {
	fs.writeFile(filename,JSON.stringify(data))
}
function Load(filename) {
	return require(filename)
}

bot.on('ready', () => {
	console.log("Logged in as ".concat(bot.user.tag,'.'))

	guild = bot.guilds.cache.get(config.serverid)
	console.clear()
})