const { Client } = require('discord.js')

const sidebarBotFactory = (opts) => {
  const { token, interval, sidebar } = opts
  const bot = new Client()

  const loop = () => {
    const loopAsync = async () => {
      const { title, activity } = await sidebar()
      await Promise.all([
        bot.user.setActivity(activity),
        bot.guilds.cache.map((guild) => guild.me.setNickname(title)),
      ])
    }
    loopAsync().catch(console.error)
  }

  bot.on('guildCreate', (guild) => {
    console.log(`New server has added the bot! Name: ${guild.name}`)
  })
  bot.on('ready', () => {
    console.log(`Logged in as ${bot.user.tag}!`)
    loop()
    setInterval(loop, interval)
  })

  return () => bot.login(token)
}

module.exports = {
  sidebarBotFactory,
}
