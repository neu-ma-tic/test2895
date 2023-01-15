const { Client, Collection } = require("discord.js")
const ch = require("chalk")
const fs = require("fs")

const app = new Client({ intents: 32767 });
function login() { // login the bot
  app.login(process.env["token"]) // create .env name it "token" and paste there your bot token.
};

(async () => { // sync bot function
  app.on("ready", async (r) => {
    console.log(ch.greenBright(`.. || login as ${ch.bold(app.user.tag)} || ..`));
    try {
      app.user.setActivity(
        {
          name: "DiscordJS", // your bot status name.
          type: "WATCHING", // the status type [LISTENING, WATCHING, STREAMING, COMPETING, PLAYING]
          status: "idle" // your bot status type this must be same as the status setup
        }
      );
      app.user.setStatus("idle");
    } catch (error) {
      if (error) return;
    }
  });
})();
// keep_alive handler
function keep_alive() {
  require("./keep_alive.js");
}
// creating a ( prefix ) command handler
app.commands = new Collection();
app.aliases = new Collection();
["handler"].forEach((i) => {
  require(`./src/${i}`)(app) // connect the file
});
app.on("messageCreate", async (m) => {
  if (m.author.bot) return;
  if (!m.guild) return;
  
  const { prefix, id } = require("./src/config.json");
  
  if (!m.content.startsWith(prefix)) return;
  if (!m.member) m.member = await m.guild.fetchMember(m);
  
  let args = m.content.slice(prefix.length).split(/ +/g);
  let cmd = args.shift().toLowerCase();
  let command = app.commands.get(cmd);
  
  if (!command) command = app.commands.get(app.aliases.get(cmd));

  if (command) {
    command.run(app, m, args, prefix, id);
  }
});
keep_alive(); // HTTP
login(); // runner
