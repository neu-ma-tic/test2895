const fs = require('node:fs');
const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
  data: new SlashCommandBuilder()
    .setName('heyben')
    .setDescription('pray lmao')
    .addStringOption(option =>
        option.setName('question')
          .setDescription('Ask a question and get a response!')
          .setRequired(true)),
  async execute(interaction) {
    const response = ["Yes?", "No.", "Eugh", "Ho ho ho!"];
    var index = Math.floor(Math.random() * 5);
    await interaction.reply(response[index]);
  },
};