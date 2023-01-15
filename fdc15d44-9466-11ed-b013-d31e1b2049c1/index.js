
const discord = require('discord.js')
const client = new discord.Client();
client.login('ODAxODQyMDU2MjUxMDQ3OTk5.YAmjmw.Q3PQzvBC3B3C933yngfMFqcIjiU');
require('./html.js');

client.on('ready', () => {
  console.log('Bot ready!');
});

client.on('message', (msg) => {
  if (msg.content === ('$ping')) {
       msg.channel.send('Pong!');
  };

    client.on('message', (msg) => {
    if (msg.content === ('$pingme')) {
      msg.reply('you asked me to!')
    };
    client.on('message', (msg) => {
      if (msg.content.includes('nigger')) {
        msg.member.kick('Lightning Moderation Auto Kick')
      };

          client.on('message', (msg) => {
    if (msg.content === ('$hackmainframe')) {
      msg.reply('hacking the mainframe upon your demand!')
    };

          client.on('message', (msg) => {
      if (msg.content.includes('nigga')) {
        msg.member.kick('Lightning Moderation Auto Kick')
      }
    })

  client.on('message', (msg) => {
  if (msg.content === ('$help')) {
       msg.channel.send('Commands: help, ping, pingme (Extremely Buggy) - Prefix: $ - More Commands Soon!');
  }
  })
   })
   })
})
})

  