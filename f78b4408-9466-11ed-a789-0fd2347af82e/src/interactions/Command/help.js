const { CommandInteraction, Client } = require('discord.js');
const { SlashCommandBuilder } = require('@discordjs/builders');
const Discord = require('discord.js');
const moment = require("moment");
require("moment-duration-format");

module.exports = {
    data: new SlashCommandBuilder()
        .setName('help')
        .setDescription('Get help with the bot'),

    /** 
     * @param {Client} client
     * @param {CommandInteraction} interaction
     * @param {String[]} args
     */

    run: async (client, interaction, args) => {
        const row = new Discord.MessageActionRow()
            .addComponents(
                new Discord.MessageSelectMenu()
                    .setCustomId('Bot-helppanel')
                    .setPlaceholder('β β Nothing selected')
                    .addOptions([
                        {
                            label: `Commands`,
                            description: `Show the commands of Bot!`,
                            emoji: "π»",
                            value: "commands-Bothelp",
                        },
                        {
                            label: `Invite`,
                            description: `Invite Bot to your server`,
                            emoji: "π¨",
                            value: "invite-Bothelp",
                        },
                        {
                            label: `Support server`,
                            description: `Join the suppport server`,
                            emoji: "β",
                            value: "support-Bothelp",
                        },
                        {
                            label: `Changelogs`,
                            description: `Show the bot changelogs`,
                            emoji: "π",
                            value: "changelogs-Bothelp",
                        },
                    ]),
            );

        return client.embed({
            title: `<:uo_info:1015553303242883112>γ»Help panel`,
            desc: `Welcome to Bot's help panel! We have made a small overview to help you! Make a choice via the menu below`,
            image: "https://cdn.discordapp.com/attachments/843487478881976381/874694194474668052/Bot_banner_invite.jpg",
            fields: [
                {
                    name: `<:uo_BotSupport:1015565238017470514> β Menu doesn't work?`,
                    value: `Try resending the command. If you get no reaction, make sure you report the bug!`
                },
                {
                    name: `<:uo_BotSupport:1015565238017470514>β Found a bug?`,
                    value: `Report this with \`/report bug\``
                },
                {
                    name: `<:to_space:1012038751729491968> β Links`,
                    value: `[Invite](${client.config.discord.botInvite}) | [Vote](https://discord.gg/Ds5CSrGfSW)`
                },
            ],
            components: [row],
            type: 'editreply'
        }, interaction)
    },
};

 