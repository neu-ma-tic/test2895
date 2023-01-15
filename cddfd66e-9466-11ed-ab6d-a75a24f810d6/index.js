const discord = require("discord.js");
const bot = new discord.Client({
  partials: ["MESSAGE", "REACTION", "CHANNEL"],
});
const ch = require("./cmdhandler.js");
const Database = require("@replit/database");
const db = new Database();
var commands = ch.commands;
require("./keepalive.js");
const config = require("./config.json");
ch.registerCmds(commands);

bot.on("ready", async () => {
  console.log("Starting bot as user " + bot.user.tag + "");
  console.log(commands.size + " commands have been loaded");
  bot.user.setPresence({
    activity: { type: "WATCHING", name: "Mountain Development" },
  });
});

bot.on("message", async (msg) => {
  let prefix = config.prefix;
  if (
    msg.channel.type === "dm" ||
    msg.author.bot
  )
    return;
  let args = msg.content.split(" ");
  if (msg.channel.id === "786231956487536640") {
    if (!msg.content.includes("|")) {
      msg.delete();
      msg.channel
        .send(
          "You need to provide a title and description <@" +
            msg.author.id +
            "> by using `Title | Description`"
        )
        .then((m) => {
          setTimeout(function () {
            m.delete();
          }, 5000);
        });
    } else {
      var suggestion = msg.content.toString().split("|");
      let e = new discord.MessageEmbed();
      e.addField(suggestion[0], suggestion.slice(1).join("|"))
        .setTitle("Suggestion")
        .setAuthor(
          "Suggested by " + msg.author.username + " (" + msg.author.id + ")",
          msg.author.avatarURL()
        )
        .setDescription(
          "Use <:yes:771379453853958204> and <:no:771379408090300427> to vote!"
        )
        .setColor("#89cff0")
        .setFooter(msg.guild.name, msg.guild.iconURL());
      msg.delete();
      msg.channel.send(msg.author.id, e).then(async (m) => {
        await m.react("771379453853958204");
        await m.react("771379408090300427");
      });
    }
  }
  if(!msg.content.toLowerCase().startsWith(prefix.toLowerCase())) return;
  if (!commands.has(args[0].toLowerCase().substring(prefix.length))) return;
  try {
    await require(commands.get(
      args[0].toLowerCase().substring(prefix.length)
    )).run(bot, msg, args, prefix);
  } catch (e) {
    console.log(
      "An error occured while running " + msg.content + "! Log: " + e
    );
  }
});



bot.on("messageReactionAdd", async (reaction, user) => {
  if (user.bot) return;
  let amnt = await db.get(
    "reactionroleid." +
      reaction.message.guild.id +
      "." +
      reaction.message.channel.id
  );
  if (amnt === null) return;
  for (let i = 1; i <= amnt; i++) {
    let data = await db.get(
      "reactionroles." + reaction.message.channel.id + "." + i
    );
    if (data === null) continue;
    if (data.message !== reaction.message.id) continue;
    let emote1;
    if (reaction.emoji.id === null) {
      emote1 = reaction.emoji.name;
    } else {
      emote1 = reaction.emoji.id;
    }
    let member = reaction.message.guild.members.cache.find(
      (member) => member.id == user.id
    );
    if (data.emoji === emote1)
      member.roles.add(
        reaction.message.guild.roles.cache.find((role) => role.id === data.role)
      );
  }
});

bot.on("messageReactionRemove", async (reaction, user) => {
  if (user.bot) return;
  let amnt = await db.get(
    "reactionroleid." +
      reaction.message.guild.id +
      "." +
      reaction.message.channel.id
  );
  if (amnt === null) return;
  for (let i = 1; i <= amnt; i++) {
    let data = await db.get(
      "reactionroles." + reaction.message.channel.id + "." + i
    );
    if (data === null) continue;
    if (data.message !== reaction.message.id) continue;
    let emote1;
    if (reaction.emoji.id === null) {
      emote1 = reaction.emoji.name;
    } else {
      emote1 = reaction.emoji.id;
    }
    let member = reaction.message.guild.members.cache.find(
      (member) => member.id == user.id
    );
    if (data.emoji === emote1)
      member.roles.remove(
        reaction.message.guild.roles.cache.find((role) => role.id === data.role)
      );
  }
});
bot.login(process.env.token);
