const { MessageEmbed, MessageActionRow, MessageButton } = require("discord.js");
module.exports = {
  name: "ping", // the command name - remember this is a file template for making a new command
  run: async (app, m, args, prefix, id) => {
    m.reply(
      {
        content: "Content - Pong!"
      }
    );
  }
}
