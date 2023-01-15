const Database = require("@replit/database");
const db = new Database();
const botdevs = require("../../config.json").devs;
const discord = require("discord.js");
// Put this file in `commands/type/file.js`
exports.info = {
  name: "deny",
  alts: [],
  description: "Deny a suggestion",
};

exports.run = async function (bot, msg, args, prefix) {
  if (!msg.member.hasPermission("ADMINISTRATOR")) return;
  if (!args[1] || isNaN(args[1]))
    return msg.channel.send("That looks like an invalid id!");
  let suggestion2;
  try {
    suggestion2 = await msg.guild.channels.cache
      .get("786231956487536640")
      .messages.fetch(args[1]);
    suggestion2.embeds[0];
  } catch (e) {
    msg.channel.send("It looks like that id is invalid!");
  }
  let reason2 = "No reason provided";
  if (args[2])
    reason2 = msg.content.substring(args[0].length + args[1].length + 2);
  let suggestionembed = new discord.MessageEmbed(suggestion2.embeds[0])
    .setTitle("Denied Suggestion")
    .setColor("#FF0000")
    .setDescription(
      "**Denied by:** " + msg.author.username + " \n**For:** " + reason2 + ""
    );
  suggestion2.delete();
  msg.channel.send("Suggestion has been denied!");
  bot.channels.cache.get("786277252009951281").send(suggestionembed);
};
