const Discord = require("discord.js")
const client = new Discord.Client()

client.on("ready", () => {
  console.log(`Logged in as ${client.user.tag}!`)
})

client.on("message", msg => {
  if (msg.content === "ping") {
    msg.reply("pong");
  }
})

  if (msg.content === "$inspire") {
    getQuote().then(quote => msg.channel.send(quote))
  }

client.on("message", msg => {
  if (msg.content === "$inspire") {
    getQuote().then(quote => msg.channel.send(quote))
  }

  if (sadWords.some(word => msg.content.includes(word))) {
    const encouragement = encouragements[Math.floor(Math.random() * encouragements.length)]
    msg.reply(encouragement)
  }

})

client.login(process.env.TOKEN)
const mySecret = process.env['token']
