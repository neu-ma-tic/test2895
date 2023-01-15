const Database = require("@replit/database");
const db = new Database();
const botdevs = require("../../config.json").devs;
const discord = require("discord.js");
const options = ["🇦","🇧","🇨","🇩","🇪","🇫","🇬","🇭","🇮","🇯","🇰","🇱","🇲","🇳","🇴","🇵","🇶","🇷","🇸","🇹","🇺","🇻","🇼","🇽","🇾","🇿"]
// Put this file in `commands/type/file.js`
exports.info = {
  name: "poll",
  alts: [],
  description: "Ask a question",
};

exports.run = async function (bot, msg, args, prefix) {
  if (!msg.member.hasPermission("ADMINISTRATOR")) return;

  var poll = msg.content.toString().split(" | ");
  if (!poll[2])
    return msg.channel.send(
      "Please provide a question, description and options"
    );
  let embed = new discord.MessageEmbed();
  let desc = "";
  for (var i = 2; i < poll.length; i++) {
    desc = desc + "\n" + options[i - 2] + " - " + poll[i];
  }
  embed.addField(
    "**Poll:**" + poll[0].substring(args[0].length) + "\n" + poll[1],
    desc
  );
  msg.delete();
  msg.channel
    .send(embed)
    .then((m) => {
      for (var i = 2; i < poll.length; i++) {
        m.react(options[i - 2]);
      }
    });
};
