const { Client, Discord, Intents } = require("discord.js");
const chalk = require("chalk");
const client = new Client({
    intents: [
        Intents.FLAGS.GUILDS,
        Intents.FLAGS.GUILD_MESSAGES,
        Intents.FLAGS.GUILD_BANS,
        Intents.FLAGS.GUILD_MEMBERS,
        Intents.FLAGS.DIRECT_MESSAGE_TYPING,
        Intents.FLAGS.DIRECT_MESSAGES,
        Intents.FLAGS.GUILD_INVITES,
        Intents.FLAGS.GUILD_MESSAGE_REACTIONS,
        Intents.FLAGS.GUILD_EMOJIS_AND_STICKERS,
        Intents.FLAGS.GUILD_INTEGRATIONS,
        Intents.FLAGS.GUILD_VOICE_STATES
    ],
});
const { token } = require("./config.json")

client.on("ready", () => {
    (console.log(
        chalk.cyan("[Information] ") + chalk.blue(`Đã kết nối tới ${client.user.username}`)))
    client.user.setActivity("NQN BOT");
})

client.on("messageCreate", async(messageCreate) => {

    if (messageCreate.author.bot) return;
    let msg = messageCreate.content;

    let emojis = msg.match(/(?<=:)([^:\s]+)(?=:)/g)
    if (!emojis) return;
    emojis.forEach(m => {
        let emoji = client.emojis.cache.find(x => x.name === m)
        if (!emoji) return;
        let temp = emoji.toString()
        if (new RegExp(temp, "g").test(msg)) msg = msg.replace(new RegExp(temp, "g"), emoji.toString())
        else msg = msg.replace(new RegExp(":" + m + ":", "g"), emoji.toString());
    })

    if (msg === messageCreate.content) return;

    let webhook = await messageCreate.channel.fetchWebhooks();
    let number = randomNumber(1, 2);
    webhook = webhook.find(x => x.name === "NQN" + number);

    if (!webhook) {
        webhook = await messageCreate.channel.createWebhook(`NQN` + number, {
            avatar: client.user.displayAvatarURL({ dynamic: true })
        });
    }

    await webhook.edit({
        name: messageCreate.member.nickname ? messageCreate.member.nickname : messageCreate.author.username,
        avatar: messageCreate.author.displayAvatarURL({ dynamic: true })
    })

    messageCreate.delete().catch(err => {})
    webhook.send(msg).catch(err => {})

    await webhook.edit({
        name: `NQN` + number,
        avatar: client.user.displayAvatarURL({ dynamic: true })
    })


})



client.login(token);
//--------------------------------------------------- F U N C T I O N S --------------------------------------

function randomNumber(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}