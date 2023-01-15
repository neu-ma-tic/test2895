const Database = require("@replit/database");
const db = new Database();
const botdevs = require("../../config.json").devs;
const discord = require("discord.js");
// Put this file in `commands/type/file.js`
exports.info = {
  name: "rr",
  alts: [],
  description: "Create reaction role",
};

exports.run = async function (bot, msg, args, prefix) {
  let filter = (reaction, user) => {
    return user.id === msg.author.id;
  };
  let embed = new discord.MessageEmbed();
  if (!msg.member.hasPermission("MANAGE_ROLES"))
    return msg.channel.send(
      "You need the `MANAGE_ROLES` permission to do this!"
    );
  if (!args[1])
    return msg.channel.send("Provide a channel to make the reaction role in!");
  if (!args[2])
    return msg.channel.send(
      "Provide a message to make the reaction role with!"
    );
  let role = msg.mentions.roles.first();
  if (!role)
    return msg.channel.send(
      "Please ping a role to create the reaction roles with!"
    );
  embed
    .setTitle("Reaction roles creation")
    .setDescription(
      "React to this message with the emoji you would like me to use! \nThis will time out in 1 minute \n**DO NOT USE NITRO EMOTES. I HAVE NO WAY OF USING THEM**"
    );
  let m = await msg.channel.send(embed);
  m.awaitReactions(filter, { max: 1, time: 60000, errors: ["time"] })
    .then(async (collected) => {
      const reaction = collected.first();
      let emote;
      if (reaction.emoji.id === null) {
        emote = reaction.emoji.name;
      } else {
        emote = reaction.emoji.id;
      }
      try {
        let c = bot.channels.cache.get(args[1]);
        c.messages.fetch(args[2]).then(async (ms) => {
          try {
            ms.react(reaction.emoji);
          } catch (e) {
            return msg.channel.send(
              "An error occured while reacting, I might not have permission to react or you're using a nitro emoji"
            );
          }
        });
        await db
          .get("reactionroleid." + msg.guild.id + "." + args[1])
          .then((value) => {
            if (value === null)
              db.set(
                "reactionroleid." + msg.guild.id + "." + args[1],
                0
              );
          });
        let rr = {
          emoji: emote,
          message: args[2],
          channel: args[1],
          role: role.id,
        };
        db.get("reactionroleid." + msg.guild.id + "." + args[1]).then(
          (value) => {
            db.set("reactionroles." + args[1] + "." + (value + 1), rr);
            db.set(
              "reactionroleid." + msg.guild.id + "." + args[1],
              value + 1
            );
          }
        );
        let id = await db.get(
          "reactionroleid." + msg.guild.id + "." + args[1]
        );
        if (id === null) id = 1;
        msg.channel.send("Created reaction role with id `" + id + "`!");
      } catch (e) {
        console.log(e);
        return msg.channel.send(
          "An error occured! It might be one of these `Missing react permission`, `Invalid channel/message id`, `Invalid emoji`, or `Don't have permission to that channel`"
        );
      }
    })
    .catch(async (collected) => {
      msg.channel.send("No reaction was provided! Stopping setup");
    });
};
