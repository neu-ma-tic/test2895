const { Client, Intents, MessageAttachment, MessageEmbed } = require('discord.js');

const client = new Client({ 
    intents: [
        Intents.FLAGS.GUILDS, 
        Intents.FLAGS.GUILD_MESSAGES
    ] 
});

client.on('ready', () => {
    console.log(`my bot is ready!!!!`);
});

client.on('messageCreate', (message) => {
    if (message.content === 'hi') {
        message.reply({
            content: "hello",
        })
    }
});

const img = new MessageAttachment('chestnut.jpg');

const msg_embed = new MessageEmbed()
.setTitle('This is a picture!')
.setImage('attachment://chestnut.jpg'); 

client.on('messageCreate', (message) => {
    if (message.content === 'hi chestnut') {
        message.reply({
            embeds: [msg_embed], 
            files: [img],
        })
    } 
}); 

client.login("token here");