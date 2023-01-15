const Database = require("@replit/database");
const db = new Database();
const botdevs = require("../../config.json").devs;
const discord = require("discord.js");
// Put this file in `commands/type/file.js`
exports.info = {
  name: "report",
  alts: [],
  description: "Report a user for breaking the rules",
};

exports.run = async function (bot, msg, args, prefix) {
  let otherFilters = (response) => {
    return response.author.id === msg.author.id;
  };
  msg.delete();
  msg.channel
    .send(
      "Please **view your DMs** to continue. Make sure you have DMS enabled"
    )
    .then((m) => {
      setTimeout(function () {
        m.delete();
      }, 5000);
    });
  let channel = await msg.author
    .send(
      new discord.MessageEmbed()
        .setTitle("Report")
        .setDescription(
          "Please provide the username and id of who you want to report \n*This will time out in 30 seconds*"
        )
    );
    channel.channel.awaitMessages(otherFilters, { max: 1, time: 30000, errors: ["time"] })
    .then(async (collect) => {
      msg.author
        .send(
          new discord.MessageEmbed()
            .setTitle("Report")
            .setDescription("Please provide a reason for creating the report! \n*This will time out in 30 seconds*")
        );
        channel.channel.awaitMessages(otherFilters, { max: 1, time: 30000, errors: ["time"] })
        .then(async (collected) => {
          msg.author.send(
            "Thanks for taking the time to report this user! I have forwarded this to staff."
          );
          bot.channels.cache
            .get("786247960174395482")
            .send(
              new discord.MessageEmbed()
                .setTitle(
                  "User report by " +
                    msg.author.username +
                    " (" +
                    msg.author.id +
                    ")"
                )
                .setDescription(
                  "Reporting: " +
                    collect.first().content.toString() +
                    "\nFor: " +
                    collected.first().content.toString()
                )
            );
        })
        .catch(() => {
          return msg.author.send("**Report timed out!** Canceled.");
        });
    })
    .catch(() => {
      return msg.author.send("**Report timed out!** Canceled.");
    });
};
