console.log('Der Teufel wird gestartet...')

const { SSL_OP_SSLEAY_080_CLIENT_DH_BUG } = require('constants')
const Discord = require('discord.js')
const fs = require('fs')
const {send} = require('process')
const config = JSON.parse(fs.readFileSync('config.json', 'utf8'))
const client = new Discord.Client({ intents: ["GUILDS", "GUILD_MESSAGES"] })
const {
    prefix,
    token
} = require ('./config.json')
client.setMaxListeners(0)
client.login(config.token)

client.on('ready', () => {
    console.log('Der Teufel wurde erfolgreich gestartet!');
    const activites = [
        "auf UnicornWorld",
        "auf UnicornWorld",
        "auf UnicornWorld",
        "auf UnicornWorld"
    ];

    setInterval(() => {
        const randomIndex = Math.floor(Math.random() * (activites.length -1) +1);
        const newActivity = activites[randomIndex]
        client.user.setActivity(newActivity)
    }, 6500);
});










// Moderation

client.on('message', function(message) {
    if (message.content.startsWith(prefix + "mute")) {
        if (!message.member.permissions.has('MANAGE_ROLES')) return message.channel.send('Du hast hierzu keine Berechtigung! :x:').then(message.react(':x:'))

         let muted = message.guild.roles.cache.get('912836341706928128');
         let member = message.guild.roles.cache.get('895451039120117801');
         let user = message.mentions.members.first();
        if(!user) return message.channel.send("Du musst die Person erwähnen um sie freizuschalten! :x:").then((declineMsg) => { message.react('❌')
        });
    
        user.roles.add(muted);
        user.roles.remove(member);
        message.channel.send("Person gemuted! ✅").then((declineMsg) => {message.react('✅')
    })
    }
})




client.on('message', function(message) {
    if (message.content.startsWith(prefix + "unmute")) {
        if (!message.member.permissions.has('MANAGE_ROLES')) return message.channel.send('Du hast hierzu keine Berechtigung! :x:').then(message.react('❌'))

         let muted = message.guild.roles.cache.get('912836341706928128');
         let member = message.guild.roles.cache.get('895451039120117801');
         let user = message.mentions.members.first();
        if(!user) return message.channel.send("Du musst die Person erwähnen um sie stummzuschalten! :x:").then((declineMsg) => { message.react('❌')
        });
    
        user.roles.remove(muted);
        user.roles.add(member);
        message.channel.send("Person freigeschalten! ✅").then((declineMsg) => {message.react('✅')
    })
    }
})

client.on('message', function(message) {
    if (message.content.startsWith(prefix + "hallo")) {
     message.channel.send('Hallo! :slight_smile:');
    }
});