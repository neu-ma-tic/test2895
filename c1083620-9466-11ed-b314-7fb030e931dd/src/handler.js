const { readdirSync } = require('fs')
const ch = require("chalk")
const ascii = require('ascii-table');

const table = new ascii('Status');
table.setHeading('Name', 'Result');

module.exports = (app) => {
  
  readdirSync('./cmds').forEach(dir => {
    
    const commands = readdirSync(`./cmds/${dir}/`).filter(file => file.endsWith('.js'));
    
    for (let file of commands) {
      let pull = require(`../cmds/${dir}/${file}`);
      
      if (pull.name) {
        app.commands.set(pull.name, pull)
        table.addRow(file, ch.greenBright("1"));
      } else {
        table.addRow(file, ch.redBright("0"));
        continue;
      }
      
      if (pull.aliases && Array.isArray(pull.alises)) pull.aliases.forEach(alias => {
        app.aliases.set(alias, pull.name);
      })
    }
  });
  console.log(ch.blue(table.toString()));
  
}
