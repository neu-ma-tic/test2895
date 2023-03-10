const Discord = require('discord.js');

const Functions = require("../../database/models/functions");

module.exports = async (client, guild) => {
    const webhookClient = new Discord.WebhookClient({
        id: client.webhooks.serverLogs.id,
        token: client.webhooks.serverLogs.token,
    });

    if (guild == undefined) return;

    new Functions({
        Guild: guild.id,
        Prefix: client.config.discord.prefix
    }).save();

    try {
      const embed = new Discord.MessageEmbed()
        .setTitle("🟢・Added to a new server!")
        .addField("Total servers:", `${client.guilds.cache.size}`, true)
        .addField("Server name", `${guild.name}`, true)
        .addField("Server ID", `${guild.id}`, true)
        .addField("Server members", `${guild.memberCount}`, true)        
        .addField("Server owner", `<@!${guild.ownerId}> (${guild.ownerId})`, true)
.setThumbnail("https://cdn.discordapp.com/attachments/843487478881976381/852419422392156210/BotPartyEmote.png")
        .setColor(client.config.colors.normal)
                webhookClient.send({
                    username: 'Bot Logs',
                    avatarURL: client.user.avatarURL(),
                    embeds: [embed],
                });

        let defaultChannel = "";
        guild.channels.cache.forEach((channel) => {
            if (channel.type == "GUILD_TEXT" && defaultChannel == "") {
                if (channel.permissionsFor(guild.me).has("SEND_MESSAGES")) {
                    defaultChannel = channel;
                }
            }
        })

        let row = new Discord.MessageActionRow()
            .addComponents(
                new Discord.MessageButton()
                    .setLabel("Invite")
                    .setURL(client.config.discord.botInvite)
                    .setStyle("LINK"),

                new Discord.MessageButton()
                    .setLabel("Support server")
                    .setURL(client.config.discord.serverInvite)
                    .setStyle("LINK"),
            );

        client.embed({
            title: "Thanks for inviting the bot!",
            image: "https://cdn.discordapp.com/attachments/843487478881976381/874694194474668052/Bot_banner_invite.jpg",
            fields: [{
                name: "📢┆Alert!",
                value: 'After more than 1 year we decided to stop Bot on April 15th, for more information go to [this server](https://discord.gg/techpoint)',
                inline: false,
            },
            {
                name: "❓┆How to setup?",
                value: 'The default prefix = \`/\` \nTo run setups with Bot run \`/setup\`',
                inline: false,
            },
            {
                name: "☎️┆I need help what now?",
                value: `You can DM <@313247783748501505> for support or joining the [[Support server]](${client.config.discord.serverInvite})`,
                inline: false,
            },
            {
                name: "💻┆What are the commands?",
                value: 'See that list of commands by doing \`/help\`',
                inline: false,
            },
            {
                name: "📨┆Invite the bot!",
                value: `Invite the bot to click [[HERE]](${client.config.discord.botInvite})`,
                inline: false,
            },
            ],
            components: [row], 
        }, defaultChannel)
    }
    catch (err) {
        throw err;
    }


};