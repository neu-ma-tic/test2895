const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
  data: new SlashCommandBuilder()
    .setName('rate')
    .setDescription('good luck')
    .addStringOption(option =>
        option.setName('thing')
          .setDescription('Let Ben rate a thing!')
          .setRequired(false)),
  async execute(interaction) {
    var rate = Math.floor(Math.random() * 11);
    var str = "";
    switch(rate) {
      case 0:
          str = " you fucking bozo lmao";
          break;
      case 1:
          str = " you walking L";
          break;
      case 2:
          str = " + ratio";
          break;
      case 3:
          str = " :skull: lmao bozo";
          break;
      case 4:
          str = " ho ho ho";
          break;
      case 5:
          str = " :face_with_raised_eyebrow: baen?";
          break;
      case 6:
          str = " yo baen?";
          break;
      case 7:
          str = " BAEN!?";
          break;
      case 8:
          str = " :open_mouth: speed?";
          break;
      case 9:
          str = " :open_mouth: SPEED?!";
          break;
      case 10:
          str = " WALKING W :muscle: :muscle: :muscle: ";
          break;
    }
    await interaction.reply(rate + "/10" + str);
  },
};