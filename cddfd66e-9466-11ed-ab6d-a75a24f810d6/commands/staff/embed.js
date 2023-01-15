const Database = require("@replit/database");
const db = new Database();
const botdevs = require("../../config.json").devs;
const discord = require("discord.js");
// Put this file in `commands/type/file.js`
exports.info = {
  name: "embed",
  alts: [],
  description: "Send message in a nice embed",
};

exports.run = async function (bot, msg, args, prefix) {
  if (!msg.member.hasPermission("ADMINISTRATOR")) return;
  let embed = msg.content.toString().split(" | ");
  let title = embed[0].substring(args[0].length + 1);
  embed = embed.slice(1).join(" | ");
  msg.delete();
  msg.channel.send(
    new discord.MessageEmbed()
      .setTitle(title)
      .setDescription(embed ? embed : "")
  );
};
