const Database = require("@replit/database");
const db = new Database();
const botdevs = require("../../config.json").devs;
const discord = require("discord.js");
// Put this file in `commands/type/file.js`
exports.info = {
  name: "command",
  alts: [],
  description: "Command description",
};

exports.run = async function (bot, msg, args, prefix) {

}