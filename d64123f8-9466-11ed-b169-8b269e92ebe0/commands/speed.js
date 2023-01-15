const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
  data: new SlashCommandBuilder()
    .setName('speed')
    .setDescription('get a generated image from ben'),
  async execute(interaction) {
    const { MessageAttachment } = require('discord.js');
    const Canvas = require('canvas');
    const canvas = Canvas.createCanvas(862, 484);
    const ctx = canvas.getContext('2d');

    const asset = await Canvas.loadImage('./assets/speed.jpg');
    const avatar = await Canvas.loadImage(interaction.user.displayAvatarURL({format: 'jpg'}));
    ctx.drawImage(asset, 0, 0, canvas.width, canvas.height);
    ctx.drawImage(avatar, 370, 55, 190, 190); // test
    
    const attachment = new MessageAttachment(canvas.toBuffer(), 'lmao-test.png');
    await interaction.reply({files: [attachment]});
  },
};