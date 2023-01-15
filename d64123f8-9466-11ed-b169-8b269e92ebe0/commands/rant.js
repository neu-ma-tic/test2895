const fs = require('node:fs');
const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
  data: new SlashCommandBuilder()
    .setName('rant')
    .setDescription('pray taht')
    .addStringOption(option =>
        option.setName('member')
          .setDescription('either specify a member or leave it blank if it wants to roast you')
          .setRequired(false)),
  async execute(interaction) {
    // Not really great at ranting but hey it was fun making this command xD
    let result = "";
    const start = ["Aight so first off ", "Tbf "];
    const middle = ["you are delusional af, ", "idk what to say but you stink like ass like goddamn, I can smell you across the screen my guy, ", " you are a discrase to your ancestors, "];
    const addition = ["+ ratio ", "+ no bitches ", "+ would punch the hell outta you "];
    const finisher = [". Oh and you can stop using me, I feel dirty even replying to you, bozo.", ". Go get sum bitches instead of arguing with me lmao.", ". Oh and remove that pfp of yours, who even allowed you to post that pfp lmao."];
    var s_index = Math.floor(Math.random() * start.length);
    var m_index1 = Math.floor(Math.random() * middle.length);
    var m_index2 = Math.floor(Math.random() * middle.length);
    var a_index = Math.floor(Math.random() * addition.length);
    var f_index = Math.floor(Math.random() * finisher.length);

    if (m_index1 === m_index2) m_index2 = Math.floor(Math.random() * middle.length);

    result = start[s_index] + middle[m_index1] + middle[m_index2] + addition[a_index] + finisher[f_index];

    await interaction.reply({content: result});
  },
};