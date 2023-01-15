const keepAlive = require("./server");
const fs = require('node:fs');
const { Client, Collection, Intents } = require('discord.js');
const token = process.env['token'];
  
const client = new Client({intents: [Intents.FLAGS.GUILDS]});

client.commands = new Collection();
const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));

for (const file of commandFiles) {
  const command = require(`./commands/${file}`);
  client.commands.set(command.data.name, command);
}

client.once('ready', () => {
  console.log("BAEN!");
});

client.on('interactionCreate', async interaction => {
  //if (interaction.mentions.has()) // add a feature where it responds back if you ping him hehe
	if (!interaction.isCommand()) return;

	const command = client.commands.get(interaction.commandName);
  if (!command) return;
  
  try {
    await command.execute(interaction);
  } catch (error) {
    console.error(error);
    await interaction.reply({content: "***Puts down phone***", ephemeral: true});
    //await interaction.author.send("There was a problem with Talking Ben! The name of the error is " + error.name + "...here's the full error.\n```" + error + "```");
  }
});
keepAlive();
client.login(token);