const Database = require("@replit/database");
const db = new Database();
const botdevs = require("../../config.json").devs;
const discord = require("discord.js");
// Put this file in `commands/type/file.js`
exports.info = {
  name: "say",
  alts: ["echo"],
  description: "Say message",
};

exports.run = async function (bot, msg, args, prefix) {
  if (!msg.member.hasPermission("ADMINISTRATOR")) return;
  msg.delete();
  msg.channel.send(
    msg.substring(args[0].length + 1)
  );
};
