const Database = require("@replit/database");
const db = new Database();
const botdevs = require("../../config.json").devs;
const discord = require("discord.js");
// Put this file in `commands/type/file.js`
exports.info = {
  name: "editembed",
  alts: [],
  description: "Send message in a nice embed",
};

exports.run = async function (bot, msg, args, prefix) {
  if (!msg.member.hasPermission("ADMINISTRATOR")) return;
  let embed = msg.content.toString().split(" | ");
  let title = embed[0].substring(args[0].length + args[1].length + args[2].length + 3);
  embed = embed.slice(1).join(" | ");
  let m = await bot.channels.cache.get(args[1]).messages.fetch(args[2]);
  m.edit(
    new discord.MessageEmbed()
      .setTitle(title)
      .setDescription(embed ? embed : "")
  );
  msg.channel.send(
    new discord.MessageEmbed()
    .setTitle("Edited embed")
    .setDescription("Successfully edited the embed!")
  )
};
