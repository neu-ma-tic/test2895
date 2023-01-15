const Discord = require('discord.js');
const bot = new Discord.Client();

const token = 'NjQxNTIwNzQzNzIwNjgxNDcy.XcJk4g.lu37nf0p4_5JR7seyBu6wpftLIg';

const prefix = '$';

bot.on('ready', () =>{
    console.log('Bot is active!');
    bot.user.setActivity('Over The Palace', { type: 'WATCHING'}).catch(console.error);
})

bot.on('message', msg=>{

    let args = msg.content.substring(prefix.length).split(" ");
    switch(args[0]){
        case 'help':
            msg.channel.sendMessage('Hello there my name is Palace Guard, my prefix is $ and my commands are listed below! \n```$info - this command retrieves server information. \n for example: $info version \n$invite - this command produces an invitation link.```');
            break;
            case 'invite':
            msg.channel.sendMessage('If you want to invite people to our server feel free to use the format listed at "https://pastebin.com/3hru82K4" (https://discord.gg/TS75NrD)');
            break;
            case 'info':
                    var version = 'Beta';
                if(args[1] === 'version'){
                    msg.channel.sendMessage('I am currently in version, '+ version + '.');
                }else{
                    msg.channel.sendMessage('Invalid Argument; try e.g "version"');
                }
                break;
                case 'clear':
                    if(!msg.member.roles.find(r => r.name === "Overseer")) return
                    if(!args[1]) return msg.reply('Invalid Argument!')
                    msg.channel.bulkDelete(args[1]);
                    break;
    }
    // Ignores messages that don't use the prefix.
    if(!msg.content.startsWith(prefix)) { return; }
})

bot.login(token);