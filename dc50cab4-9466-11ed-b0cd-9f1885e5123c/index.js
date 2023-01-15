const fs = require('fs');

const Discord = require('discord.js');

const client = new Discord.Client({
	disableEveryone: true
});

const { CanvasSenpai } = require('canvas-senpai');

const { NekoBot } = require('nekobot-api');

const api = new NekoBot();

const canva = new CanvasSenpai();

const bottoken = process.env.token;

const db = require('quick.db');

const ms = require('ms');

const fetch = require('node-fetch');

const querystring = require('querystring');

const ytdl = require('ytdl-core');

const YoutubeAPI = require('simple-youtube-api');

const youtube = new YoutubeAPI(process.env.ytkey);

const { play } = require('./handlers/music');

const Dlang = require('discordbot-script');

const trim = (str, max) => (str.length > max ? `${str.slice(0, max - 3)}...` : str);

const discordScript = require('discordbot-script');

const bot = new discordScript({
	token: bottoken,
	prefix: ['$getServerVar[prefix]']
});

const http = require('http');

const server = http.createServer((req, res) => {
	res.writeHead(200);
	res.end('ok');
});
server.listen(3000);

client.queue = new Map();
client.vote = new Map();

bot.Variables({
	prefix: 's?',
	color: 'NA',
	snipe: '',
	author: '',
  currency: '',
  icon: '$',
  name: 'coins'
});

bot.MessageEvent();

bot.MessageDeleteCommand({
	name: '$channelID[]',

	code: `$setChannelVar[snipe;$message[];$channelID[]]
$setChannelVar[author;$authorID;$channelID[]]
`
});

bot.onMessageDelete();

bot.AwaitedCommand({
  name: "work",
  code: "$setVar[currency;$sum[$getVar[currency;$authorID];$random[750;1250]];$authorID] Nice work $username[], you got $getVar[icon]$random[750;1250]"
})

bot.ExecutableCommand({
name: "gbeg",
code: `
$title[$username[] went begging]
$description[**$randomText[Donald Trump;Hilliary Clinton;Dick hertz;Skinny Penis;Charles Dickens;Bananamaster2006;Random dumbass;You;Your dick;Yo mama;Yuu;Donkey;Horse;Random furry;Nerd]**: $randomText[Sure;Here;Kk;I like you;Ok here;Ehhh take sum;ok;Lol ok, take some;Yes please.;Here you go;Kkk]

You got $getVar[icon]$random[250;500]]
$color[RANDOM]
$addTimestamp
$footer[Requested by $username[];$userAvatar[$authorID]]
$setVar[currency;$sum[$getVar[currency;$authorID];$random[250;500]];$authorID]
`
})

bot.ExecutableCommand({
  name: "bbeg",
  code: `
 $title[$username[] went begging]
 $color[RANDOM]
 $addTimestamp
 $footer[Requested by $username[];$userAvatar[$authorID]]
 $description[**$randomText[Donald Trump;Hilliary Clinton;Dick hertz;Skinny Penis;Charles Dickens;Bananamaster2006;Random dumbass;You;Your dick;Yo mama;Yuu;Donkey;Horse;Random furry;Nerd]**: $randomText[No u;I share my money with noone;Gay;Yeah, no.;Omg go away;poor kid XD;Ur mom;Later..]
 
 You got nothing.]
  `
})

bot.AwaitedCommand({
name: "search",
code: "Place searched: **$toUppercase[$message[]]**, you got $getVar[icon]$random[500;1500] $setVar[currency;$sum[$getVar[currency;$authorID];$random[500;1500]];$authorID]"
})


const folders = fs.readdirSync('./commands/');

for (const files of folders) {
	const folder = fs
		.readdirSync(`./commands/${files}/`)
		.filter(file => file.endsWith('.js'));

	for (const commands of folder) {
		const command = require(`./commands/${files}/${commands}`);
		bot.Command({
			name: command.name,
			aliases: command.aliases,
      code: command.code
		});
	}
}

function clean(text) {
	if (typeof text === 'string')
		return text
			.replace(/`/g, '`' + String.fromCharCode(8203))
			.replace(/@/g, '@' + String.fromCharCode(8203));
	else return text;
}

client.on('ready', () => {
	console.log(`${client.user.tag} (discord.js) is ready!`);
});

client.on('message', async message => {
	if (message.author.bot || !message.guild) return;

	let prefix = db.get(`prefix_${message.guild.id}`);
	if (prefix === null) prefix = 's?';

	if (!message.content.startsWith(prefix)) return;

	if (!message.member)
		message.member = await message.guild.fetchMember(message);

	const args = message.content
		.slice(prefix.length)
		.trim()
		.split(/ +/g);

	const cmd = args.shift().toLowerCase();
	if (cmd.length === 0) return;

	const cmdx = db.get(`cmd_${message.guild.id}`);
	if (cmdx) {
		let cmdy = cmdx.find(x => x.name === cmd);
		if (cmdy) message.channel.send(cmdy.responce);
	}
	
	
	function findUser(stuff) {
let u;
if (message.mentions.members.first() != undefined) {
return message.mentions.members.first().id
} else if (isNaN(stuff) == false && stuff.length == 18){
   return stuff
} else {
 let users = message.guild.members.cache.array().filter(m => m.displayName.toLowerCase().includes(stuff.toLowerCase())).slice(0,1);
return users.map(u => "" + u.id).shift()
}
}
	
	
	

	if (cmd === 'eval') {
		if (
			message.author.id == '635319965335158796' ||
			message.author.id == '743767109817073664'
		) {
			try {
				const code = args.join(' ');

				let evaled = eval(code);

				if (typeof evaled !== 'string')
					evaled = require('util').inspect(evaled);

				message.channel.send(clean(evaled), { code: 'xl' });
			} catch (err) {
				message.channel.send(`\`ERROR\` \`\`\`xl\n${clean(err)}\n\`\`\``);
			}
		}
	} else
	if (cmd === 'play' || cmd === 'p') {
		let embed = new Discord.MessageEmbed().setColor('BLUE');
		
		if (!args.length) {
			embed.setAuthor("❌  Wrong Syntax: Type `prefix play <URL> or video name`.");
			return message.channel.send(embed);
		}
		
		const { channel } = message.member.voice;
		
		if (!channel) {
			embed.setAuthor('⛔ You need to be in a voice channel!');
			return message.channel.send(embed);
		}
		
		const targetsong = args.join(' ');
		const videoPattern = /^(https?:\/\/)?(www\.)?(youtube\.com|youtu\.?be)\/.+$/gi;
		const playlistPattern =/^.*(youtu.be\/|list=)([^#\&\?]*).*/gi;
		const urlcheck = videoPattern.test(args[0]);
		
		if (!videoPattern.test(args[0]) && playlistPattern.test(args[0])) {
			embed.setAuthor('⛔ Playlists are not supported!');
			return message.channel.send(embed);
		}
		
		const serverQueue = message.client.queue.get(message.guild.id);
		
		const queueConstruct = {
			textChannel: message.channel,
			channel,
			connection: null,
			songs: [],
			loop: false,
			volume: 100,
			playing: true
		};
		
		const voteConstruct = {
			vote: 0,
			voters: []
		}
		
		let songData = null;
		let song = null;
		
		if (urlcheck) {
			try {
				songData = await ytdl.getInfo(args[0]);
				
				song = {
					title: songData.videoDetails.title,
					url: songData.videoDetails.video_url,
					duration: songData.videoDetails.lengthSeconds,
					thumbnail: songData.videoDetails.thumbnail.thumbnails[3].url
				};
			} catch (error) {
				if (message.include === 'copyright') {
					return message
					  .reply('⚠️ There is copyrighted content in that video!')
					  .catch(console.error);
				} else {
					console.error(error);
				}
			}
		} else {
			try {
				const result = await youtube.searchVideos(targetsong, 1);
				songData = await ytdl.getInfo(result[0].url);
				
				song = {
					title: songData.videoDetails.title,
					url: songData.videoDetails.video_url,
					duration: songData.videoDetails.lengthSeconds,
					thumbnail: songData.videoDetails.thumbnail.thumbnails[3].url,
				};
				
				
			} catch (error) {
				console.log(error);
				if (error.errors[0].domain === 'usageLimits') {
					return message.channel.send('🚫 The bot\'s youtube api key has reached its limit. Please wait for another 24 hours for the limits to be removed.');
				}
			}
		}
		
		if (serverQueue) {
			if (serverQueue.songs.length > Math.floor(0 - 1) && 0 !== 0) {
				return message.channel.send('❗ You can\'t add more songs than 0 in the queue!');
			}
			
			serverQueue.songs.push(song);
			embed.setAuthor('🎼 Added a new song to the queue', client.user.displayAvatarURL({ dynamic: true }));
			embed.setDescription(`**[${song.title}](${song.url})**`);
			embed.setThumbnail(song.thumbnail)
			  .setFooter('Likes - ' + songData.videoDetails.likes + ', Dislikes - ' + songData.videoDetails.dislikes);
			  
			 return serverQueue.textChannel
			   .send(embed)
			   .catch(console.error);
			   
			   
		} else {
			queueConstruct.songs.push(song);
		}
		
		if (!serverQueue)
		  message.client.queue.set(message.guild.id, queueConstruct);
		  message.client.vote.set(message.guild.id, voteConstruct);
		
		if (!serverQueue) {
			try {
				queueConstruct.connection = await channel.join();
				
				play(queueConstruct.songs[0], message).then(message.guild.me.voice.setSelfDeaf(true));
			} catch (error) {
				console.error(`Could not join voice channel: ${error}`);
				message.client.queue.delete(message.guild.id);
				await channel.leave();
				return message.channel
				  .send({
				  	embed: {
				  		description: `😕 Could not join voice channel: ${error}`,
				  		color: 'ff2050'
				  	}
				  })
				  .catch(console.error)
			}
		}
	} else
	if (cmd === 'stop') {
		let embed = new Discord.MessageEmbed().setColor("BLUE")
		
		const { channel } = message.member.voice;
		
		if (!channel) {
			embed.setAuthor('⛔ You need to be in a voice channel to execute this command!');
			return message.channel.send(embed);
		}
		
		const serverQueue = message.client.queue.get(message.guild.id);
		
		if (!serverQueue) {
			embed.setAuthor('❌ There is currently nothing playing.');
			return message.channel.send(embed);
		}
		
		serverQueue.songs = [];
		serverQueue.connection.dispatcher.end();
	} else
	if (cmd === 'skip') {
		let embed = new Discord.MessageEmbed().setColor("BLUE");
		
		const { channel } = message.member.voice;
		
		if (!channel) {
			embed.setAuthor("⛔ You need to be in a voice channel to execute this command!");
			return message.channel.send(embed)
		}
		
		const serverQueue = message.client.queue.get(message.guild.id);
		const vote = message.client.vote.get(message.guild.id);
		if (!serverQueue) {
			embed.setAuthor("❌ There is currently nothing playing.");
			return message.channel.send(embed)
		}
		
		const vcvote = Math.floor(message.guild.me.voice.channel.members.size / 2);
		const okie = Math.floor(message.guild.me.voice.channel.members.size / 2 - 1);
		console.log(message.guild.me.voice.channel.members.size);
		
		if (!message.member.hasPermission("ADMINISTRATOR")) {
			if (vote.vote > okie) {
				serverQueue.connection.dispatcher.end();
				embed.setDescription('VoteSkip || Skipping the song!');
				embed.setThumbnail(client.user.displayAvatarURL());
				return message.channel.send(embed);
			}
			
			if (vote.voters.includes(message.author.id)) {
				return message.channel.send('❗ You already voted to skip the song!');
			}
			
			if (vcvote === 2) {
				serverQueue.connection.dispatcher.end();
				embed.setDescription('✔ | Skipping the song!');
				embed.setThumbnail(client.user.displayAvatarURL());
				return message.channel.send(embed);
			}
			
			vote.vote++
			vote.voters.push(message.author.id);
			return message.channel.send(`ℹ You voted for the song to skip, we need ${Math.floor(vcvote - vote.vote)} votes more!`)
		}
		
		serverQueue.connection.dispatcher.end();
		embed.setDescription('✔ | Skipping the song!');
		embed.setThumbnail(client.user.displayAvatarURL());
		message.channel.send(embed);
		} else
		if (cmd === 'queue' || cmd === 'q') {
			let embed = new Discord.MessageEmbed().setColor("BLUE");
			
			const { channel } = message.member.voice;
			
			if (!channel) {
				embed.setAuthor('⛔ You need to be in a voice channel to execute this command!');
				return message.channel.send(embed);
			}
			
			const serverQueue = message.client.queue.get(message.guild.id);
			
			if (!serverQueue) {
				embed.setAuthor('⛔ There is currently nothing playing.');
				return message.channel.send(embed);
			}
			
			embed.setDescription(
				`${serverQueue.songs
				.map((song, index) => index + 1 + '. ' + song.title)
				.join('\n\n')}`,
				{ split: true }
			);
			
			embed.setThumbnail(client.user.displayAvatarURL());
			message.channel.send(embed);
		} else
		if (cmd === 'np' || cmd === 'nowplaying') {
			let embed = new Discord.MessageEmbed().setColor("BLUE");
			
			const { channel } = message.member.voice;
			if (!channel) {
				embed.setAuthor('⛔ You need to be in a voice channel to execute this command!');
				return message.channel.send(embed);
			}
			
			const serverQueue = message.client.queue.get(message.guild.id);
			
			if (!serverQueue) {
				embed.setAuthor('🚫 There is currently nothing playing.');
				return message.channel.send(embed)
			}
			
			embed.setDescription(`**Now Playing** - ${serverQueue.songs[0].title} 🎶`)
			  .setThumbnail(serverQueue.songs[0].thumbnail);
			  
			message.channel.send(embed)
		} else if (cmd == "chat") {
  
  const cleverbot = require("cleverbot-free");
  cleverbot(args).then(response => 
      message.channel.send(`**${message.author.tag}**: ` + response).catch(err => {
          return message.channel.send("An error occured");
      }));
} else if (cmd == "urban") {

if (args[0] === 'urban') return;

	if (!args.length) {
		return message.channel.send('You need to supply a search term!');
	}
	
	const query = querystring.stringify({ term: args.join(' ')});
	
	const { list } = await fetch(`https://api.urbandictionary.com/v0/define?${query}`).then(response => response.json());

  if (!list.length) {
  	return message.channel.send(`No results found for **${args.join(' ')}**.`);
  }
  
  const [answer] = list;

  const embed = new Discord.MessageEmbed()
    .setColor('WHITE')
    .setTitle(answer.word)
    .setURL(answer.permalink)
    .addFields(
    	{ name: 'Definition', value: trim(answer.definition, 1024) },
    	{ name: 'Example', value: trim(answer.example, 1024) },
    	{ name: 'Rating', value: `${answer.thumbs_up} 👍 ${answer.thumbs_down} 👎` },
    ); 
  





    message.channel.send(embed)
  
} else if (cmd == "translate") {
  const translate = require('@vitalets/google-translate-api');
  const input = args.join(" ");
 
translate(input, {to: 'en'}).then(res => {

  let embed = new Discord.MessageEmbed()
  .setTitle("Translation")
  .setColor(`RANDOM`)
  .addField("Text",input,true)
  .addField("Translation",res.text,true)
  .setFooter("Translated from " + res.from.language.iso.toUpperCase())
    message.channel.send(embed)
}).catch(err => {
    message.channel.send(err);
});
	
  } else if (cmd === '8ball') {
        if (!args.slice(0).join(" ")) {
        const ErrorEmbed = new Discord.MessageEmbed()
        .setTitle('Youch! I bumped into an error!')
        .setColor(0xff0000)
        .addField('Error', `\`\`Provide a question for the 8-ball.\`\``)
        .setTimestamp()

        return message.channel.send(ErrorEmbed);
      }

      const RatingArray = ['🟢', '🟡', '🔴']
      
      const Choices = [
      	 {Rating: 0, Message : "It is certain."},
         {Rating: 0, Message : "It is decidedly so."},
         {Rating: 0, Message : "Without a doubt."},
         {Rating: 0, Message : "Yes - definitely."},
         {Rating: 0, Message : "You may rely on it."},
         {Rating: 0, Message : "As I see it, yes."},
         {Rating: 0, Message :"Most likely."},
         {Rating: 0, Message : "Outlook good."},
         {Rating: 0, Message : "Yes."},
         {Rating: 0, Message : "Signs point to: Yes."},
      	
         {Rating: 1, Message : "Cannot predict now."},
         {Rating: 1, Message : "Concentrate and ask again."},

         // Bad Fate
         {Rating: 2, Message : "Don't count on it."},
         {Rating: 2, Message : "My sources say no."},
         {Rating: 2, Message : "My reply is no."},
         {Rating: 2, Message : "Outlook not so good."},
         {Rating: 2, Message : "Very doubtful."},
      ]

      const Choice = Choices[Math.floor(Math.random() * Choices.length)]

      const Embed = new Discord.MessageEmbed()
      .setTitle('The 8-Ball has spoken!')
      .setColor(0xa6e1ff)
      .setDescription(`\`\`${args.slice(0).join(" ")}\`\``)
      .addField('Answer', `\`\`${Choice.Message}\`\``)
      .addField('Rating', RatingArray[Choice.Rating])
      .setFooter(`Requested by ${message.member.user.tag}`, message.member.user.displayAvatarURL({ dynamic: true }))

      return message.channel.send(Embed)

  } else if (cmd == "rps") {
const input = args
let choices;

if (input == "rock") {
choices = ["**rock**, we tied.","**scissors**, you won.","**paper**, i won."]

} else if (input == "paper") {
choices = ["**rock**, you won.","**scissors**, i won.","**paper**, we tied."]

} else if (input == "scissors") {
choices = ["**rock**, i won.","**scissors**, we tied.","**paper**, you won."]

} else {
return message.channel.send("Please choose rock, paper or scissors")

} 
const rps = choices[Math.floor(Math.random() * choices.length)]
let embed = new Discord.MessageEmbed()
.setTitle("Rock, paper, scissors!")
.setDescription("You chose **" + input + "**, I chose " + rps)
.setColor(rps.replace("**rock**, you won.","0x00FF00").replace("**paper**, you won.","0x00FF00").replace("**scissors**, you won.","0x00FF00").replace("**rock**, i won.","0xff0000").replace("**paper**, i won.","0xff0000").replace("**scissors**, i won.","0xff0000").replace("**rock**, i won.","0xff0000").replace("**rock**, we tied.","0xffff00").replace("**paper**, we tied.","0xffff00").replace("**scissors**, we tied.","0xffff00"))

message.channel.send(embed)

	
} else if (cmd == "meme") {
	 const got = require("got")
   const subreddits = ["dankmemes","me_irl","memes","MemeEconomy"]
   const subreddit = subreddits[Math.floor(Math.random() * subreddits.length)]

got(`https://www.reddit.com/r/${subreddit}/random.json`).then(response => {
  let content = JSON.parse(response.body);
  var title = content[0].data.children[0].data.title;
  var link = content[0].data.children[0].data.url;
  var upvotes = content[0].data.children[0].data.ups;
  var downvotes = content[0].data.children[0].data.downs;
  let embed = new Discord.MessageEmbed()
  .setDescription(`**` + title + `**`) 
  .setImage(link) 
  .setColor(`RANDOM`)
  .setURL(link)
   message.channel.send(embed) }).catch(console.error);
	  
  } else if (cmd === 'volume' || cmd === 'vol') {
  	let embed = new Discord.MessageEmbed().setColor("BLUE");
  	
  	const { channel } = message.member.voice;
  	
  	if (!channel) {
  		embed.setAuthor('⛔ You need to be in a voice channel to execute this command!');
  		return message.channel.send(embed);
  	}
  	
  	const serverQueue = message.client.queue.get(message.guild.id);
  	
  	if (!serverQueue) {
  		embed.setAuthor('❌ Nothing is currently playing in the queue');
  		return message.channel.send(embed);
  	}
  	
  	if (!args[0]) {
  		embed.setAuthor(`🎹 The current volume is ${serverQueue.volume}.`);
  		return message.channel.send(embed);
  	}
  	
  	if (isNaN(args[0])) {
  		embed.setAuthor('🔢 Please only use numerical values as the volume!');
  		return message.channel.send(embed);
  	}
  	
  	if (args[0] > 200) {
  		embed.setAuthor('❌ The maximum volume is only until 200.');
  		return message.channel.send(embed);
  	}
  	
  	serverQueue.volume = args[0];
  	serverQueue.connection.dispatcher.setVolumeLogarithmic(args[0] / 200);
  	embed.setDescription(`✅ Successfully set the volume to ${args[0]}!`);
  	embed.setThumbnail(client.user.displayAvatarURL());
  	message.channel.send(embed);
  } else if (cmd === 'loop') {
  	let embed = new Discord.MessageEmbed().setColor("BLUE");
  	
  	const { channel } = message.member.voice;
  	if (!channel) {
  		embed.setAuthor('⛔ You need to be in a voice channel to execute this command!');
  		return message.channel.send(embed);
  	}
  	
  	const serverQueue = message.client.queue.get(message.guild.id);
  	if (!serverQueue) {
  		embed.setAuthor('🚫 There is currently nothing playing in the queue.');
  		return message.channel.send(embed);
  	}
  	
  	serverQueue.loop = !serverQueue.loop;
  	
  	embed.setDescription(`🔁 Loop is now **${serverQueue.loop ? "Enabled" : "Disabled"}**!`);
  	embed.setThumbnail(client.user.displayAvatarURL());
  	message.channel.send(embed);
  } else if (cmd === 'pause') {
  	let embed = new Discord.MessageEmbed().setColor("BLUE");
  	const { channel } = message.member.voice;
  	
  	if (!channel) {
  		embed.setAuthor('⛔ You need to be in a voice channel to execute this command!');
  		return message.channel.send(embed);
  	}
  	
  	const serverQueue = message.client.queue.get(message.guild.id);
  	
  	if (!serverQueue) {
  		embed.setAuthor('🚫 There is currently nothing playing in the queue.');
  		return message.channel.send(embed);
  	}
  	
  	if (serverQueue && serverQueue.playing) {
  		serverQueue.playing = false;
  		serverQueue.connection.dispatcher.pause(true);
  		
  		embed.setDescription('⏸ Paused the currently playing song!');
  		embed.setThumbnail(client.user.displayAvatarURL());
  		return message.channel.send(embed);
  	}
  } else if (cmd === 'resume') {
  	let embed = new Discord.MessageEmbed().setColor("BLUE");
  	const { channel } = message.member.voice;
  	
  	if (!channel) {
  		embed.setAuthor('⛔ You need to be in a voice channel to execute this command!');
  		return message.channel.send(embed);
  	}
  	
  	const serverQueue = message.client.queue.get(message.guild.id);
  	
  	if (!serverQueue) {
  		embed.setAuthor('🚫 There is currently nothing playing in the queue.');
  		return message.channel.send(embed);
  	}
  	
  	if (serverQueue && !serverQueue.playing) {
  		serverQueue.playing = true;
  		serverQueue.connection.dispatcher.resume();
  		
  		embed.setDescription('🎆 Resumed the currently paused song!');
  		embed.setThumbnail(client.user.displayAvatarURL());
  		return message.channel.send(embed);
    }
    embed.setDescription('❌ There is nothing paused that I can resume!');
    message.channel.send(embed);
  
  } else if (cmd === 'jump') {
  	let embed = new Discord.MessageEmbed().setColor("BLUE"); 
  	const { channel } = message.member.voice;
  	if (!channel) { 
  		embed.setAuthor("YOU NEED TO BE IN VOICE CHANNEL :/") 
  		return message.channel.send(embed); 
  		
  	} 
  	const serverQueue = message.client.queue.get(message.guild.id); 
  	if (!serverQueue) { 
  		embed.setAuthor("There is nothing playing.")
  		return message.channel.send(embed); 
  		
  	} 
  	if(!args[0]) {
  		embed.setAuthor(`Please Give The Song Number`)
  		return message.channel.send(embed) 
  		
  	} 
  	if(isNaN(args[0])) {
  		embed.setAuthor("Please Use Numerical Values Only")
  		return message.channel.send(embed) 
  		
  	} 
  	if(serverQueue.songs.length < args[0]) { 
  		embed.setAuthor("Unable To Find This Song in Queue")
  		return message.channel.send(embed) 
  		
  	} 
  	serverQueue.songs.splice(0, Math.floor(args[0] - 1))
  	serverQueue.connection.dispatcher.end() 
  	embed.setDescription(`JUMPED TO THE SONG NUMBER - ${args[0]}`)
  	message.channel.send(embed)
  } else if (cmd === 'setwelcome') {
  	if (!message.member.hasPermission('MANAGE_MESSAGES')) return;
  	
  	let channel = message.mentions.channels.first();
  	
  	if (!channel) return message.channel.send('Please mention a channel!');
  	
  	db.set(`welchannel_${message.guild.id}`, channel.id);
  	message.channel.send(`The welcome channel is successfully set to **${channel}**!`)
  } else if (cmd == "joke") {
	const { attachments } = await fetch(`https://icanhazdadjoke.com/slack`).then(response => response.json())
  const [joke] = attachments;

let embed = new Discord.MessageEmbed()
.setTitle(`Here's your joke ${message.author.username}`)
.setDescription(`**${joke.fallback}**`)
.setColor(`RANDOM`)
.setFooter(`Requested by ${message.author.username}`,message.author.displayAvatarURL())
.setTimestamp()
  message.channel.send(embed)
   
} else if (cmd == "weather"){
  const weather = require("weather-js")
if (!args) {
  return message.channel.send("And the name of the place?")
}
  weather.find({search: args, degreeType: 'C'}, function(err, result) {
    try {
     
    let embed = new Discord.MessageEmbed()
    .setTitle(`Weather in ${result[0].location.name}`)
    .setColor(`RANDOM`)

    .addField("Temperature", `${result[0].current.temperature} celcius`, true)
    .addField("Sky Text", result[0].current.skytext, true)
    .addField("Humidity", result[0].current.humidity, true)
    .addField("Wind Speed", result[0].current.windspeed, true)//What about image
    .addField("Observation Time", result[0].current.observationtime, true)
    .addField("Wind Display", result[0].current.winddisplay, true)
    .setThumbnail(result[0].current.imageUrl);
       message.channel.send(embed)
    } catch(err) {
      return message.channel.send(`Could'nt get the weather for requested place`)
    }
    });   
} else if (cmd == "translate") {

  if (!args.join(" ")) {
    return message.channel.send("What do you want me to translate?")
  }
   const translate = require('@vitalets/google-translate-api');
  const input = args.join(" ")
 
translate(input.join(" "), {to: 'en'}).then(res => {

  let embed = new Discord.MessageEmbed()
  embed.setTitle("Translation")
  embed.setColor(`RANDOM`)
  embed.addField("Text",input.join(" "),true)
  embed.addField("Translation",res.text,true)
 embed.setFooter("Translated from " + res.from.language.iso.toUpperCase())
    message.channel.send(embed)
}).catch(err => {
    console.log(err);
});
} else if (cmd == "covid") {
  const track = require("novelcovid");

if (args == "") {


      let corona = await track.all() 
      
      let embed = new Discord.MessageEmbed()
      .setTitle("Global covid-19 cases")
      .setColor(`RANDOM`)
      .addField("Total Cases", corona.cases, true)
      .addField("Total Deaths", corona.deaths, true)
      .addField("Total Recovered", corona.recovered, true)
      .addField("Today Cases", corona.todayCases, true)
      .addField("Today Deaths", corona.todayDeaths, true)
      .addField("Active Cases", corona.active, true);
      
      message.channel.send(embed)
} else {
let corona = await track.countries({country:args}) 

if (corona.cases == undefined) {
  return message.channel.send("Couldnt get covid stats for requested country")
}
      
      let embed = new Discord.MessageEmbed()
      .setTitle(`Covid-19 cases for ${corona.country}`)
      .setColor(`RANDOM`)
      
      .addField("Total Cases", corona.cases, true)
      .addField("Total Deaths", corona.deaths, true)
      .addField("Total Recovered", corona.recovered, true)
      .addField("Today Cases", corona.todayCases, true)
      .addField("Today Deaths", corona.todayDeaths, true)
      .addField("Active Cases", corona.active, true);
      
     message.channel.send(embed)
}
} else if (cmd == "google") {
const  googleIt = require('google-it')
googleIt({'query': args.join(" ")}).then(results => {;
let res = results[0]; 
let title = res.title;
let description = res.snippet;
let url = res.link;
let embed = new Discord.MessageEmbed();
embed.setTitle(title)
embed.setDescription(description)
embed.setURL(url)
embed.setColor(`RANDOM`)
embed.setFooter(`Requested by ${message.author.username}`,message.author.displayAvatarURL())
embed.setTimestamp()
embed.setAuthor("Google search results for " + args.join(" "));
message.channel.send(embed)
}).catch(e => {
 return message.channel.send("No results for the query")
})

} else if (cmd == "wiki" || cmd == "wikipedia") {
const wiki = require("wikijs").default();
const query = args.join(" ");
const search = await wiki.search(query, 1);
if (search.results[0] == undefined) {
  return message.channel.send("Couldnt find wiki for given query")
}
const result = await wiki.page(search.results[0]);
if (query == "") {
  return message.channel.send("What do you want me to search on wikipedia")
}
else if (!search.results.length) {
  return message.channel.send("Couldnt find requested query on wikipedia")
}

let description = await result.summary();
if (description.length < 150) {
  description = description
} else {
  description = `${description.substring(0, 1950)}...\nClick [**here**](${result.raw.fullurl}) to read more!`
}

let embed = new Discord.MessageEmbed()
embed.setDescription(description)
embed.setAuthor(`Wiki for ${query}`)
embed.setTitle(result.raw.fullurl.replace("https://en.wikipedia.org/wiki/","").replace(/_/gi," "))
embed.setURL(result.raw.fullurl)
embed.setFooter(`Requested by ${message.author.username}`,message.author.displayAvatarURL())
embed.setTimestamp()
embed.setColor(`RANDOM`)

message.channel.send(embed)


} else if (cmd == "calculate" || cmd == "calc") {
  
  let embed = new Discord.MessageEmbed()
  if (args == "") {
    return message.channel.send("Provide a calculation")
  }
  function replace(text,thing,stuff) {
return text.split(thing).join(stuff)
}
  const query = replace(args.toString(),"+","%2B")
  const answer = await fetch(`http://api.mathjs.org/v4/?expr=${query}`).then(response => response.text());

  if (answer.length == 0) {
    return message.channel.send("Please give a proper calculation")
  } else if (answer.includes("Error") == true) {
    return message.channel.send("Provide a proper calculation, make sure you dont separate items by a space\n\nThe operators are:\nAddition = +\nSubstraction = -\nMultiplication = *\nDivision = /\nDecimal = .")
  }
  embed.setTitle("Calculation")
  embed.addField("Question",args,true)
  embed.addField("Answer",answer,true)
  embed.setColor(`RANDOM`)
  embed.setFooter(`Requested by ${message.author.username}`,message.author.displayAvatarURL())
  embed.setTimestamp()
  message.channel.send(embed).catch(err => {
    return message.channel.send("I was unable to calculate the given calculation")
  })
} else if (cmd == "define" || cmd == "dictionary") {

  try {
    const query = args.join(" ")
    const  [ body ] = await fetch("https://api.dictionaryapi.dev/api/v2/entries/en/" + query).then(response => response.json())
    message.channel.send(body.meanings.shift().definitions.shift().definition)
} catch (error) {
   message.channel.send("Couldnt find requested term on the dictionary");
}

} else if (cmd == "country") {
  if (args == "") {
    return message.channel.send("Provide a country name")
  }
  try {
  const [ list ] = await fetch(`https://restcountries.eu/rest/v2/name/${args}?fullText=true`).then(response => response.json())

  

  let name = list.name;
  let status = list.status;
  let domain = list.topLevelDomain.shift();
  let code = list.alpha2Code;
  let callingcode = list.callingCodes.join(", ")
  let capital = list.capital;
  let region = list.region;
  let subregion = list.subregion;
  let population = list.population;
  let demonym = list.demonym;
  let embed = new Discord.MessageEmbed()
  if (status == 404) {
    return message.channel.send("kid")
  }
  embed.setAuthor(`${args} the country`)
  embed.setTitle(name)
  embed.addField("Domain",domain,true)
  embed.addField("Code",code,true)
  embed.addField("Calling code",callingcode,true)
  embed.addField("Capital",capital,true)
  embed.addField("Region",region,true)
  embed.addField("Subregion",subregion,true)
  embed.addField("Population",population,true)
  embed.addField("Demonym",demonym,true)
  embed.setColor(`RANDOM`)
  message.channel.send(embed)
  } catch (error) {
    message.channel.send("Country not found")
  }
} else if (cmd == "time") {
  const moment = require("moment-timezone")
  const q = args.join(" ")
  if (q == "") {
    return message.channel.send("Please provide a timezone")
  } else {
    const zone = moment.tz.zone(q);
    if (!zone) {
      return message.channel.send("Timezone not found")
    } else {
      const embed = new Discord.MessageEmbed()
      embed.setAuthor(`Time in ${q}`)
      embed.setTitle(q.toUpperCase())
      embed.setDescription(`It is **${moment().tz(q).format("HH:mm")}** in **${q}**`)
      embed.setColor(`RANDOM`)
      embed.setFooter(`Requested by ${message.author.username}`,message.author.displayAvatarURL())
      embed.setTimestamp()
      

      message.channel.send(embed)
    }
  }
  
} else if (cmd == "gif") {
  const giphykey = process.env.giphy_key;
    const { data } = await fetch(`https://api.giphy.com/v1/gifs/search?api_key=${giphykey}&q=${args.join(" ")}&limit=1`).then(response => response.json())
    const [gif] = data;
    if (gif == undefined) {
      return message.channel.send("No gif results for requested query")
    }
    const lin = gif.url;
    const id = gif.id;
    const image = `https://media3.giphy.com/media/${id}/giphy.gif`;
    const name = gif.slug.replace(/-/gi," ").replace(id,"")
    const embed = new Discord.MessageEmbed();
    embed.setAuthor(`Gif for ${args.join(" ")}`)
    embed.setTitle(name)
    embed.setURL(lin)
    embed.setImage(image)
    embed.setColor(`RANDOM`)
    embed.setTimestamp()
    embed.setFooter(`Requested by ${message.author.username}`,message.author.displayAvatarURL())
   message.channel.send(embed)

} else if (cmd == "lyrics" || cmd == "ly") {
  const q = args.join(" ")
  try {
  const info = await fetch(`https://some-random-api.ml/lyrics?title=${q}`).then(response => response.json())
  let embed = new Discord.MessageEmbed()
  let lyrics;
  if (info.lyrics.length < 1950) {
    lyrics = info.lyrics
  } else {
    lyrics = `${info.lyrics.substring(0, 1950)}....
    [Show more](${info.links.genius})!`
  }
  embed.setDescription(lyrics)
  embed.setTitle(`${info.title} by ${info.author}`)
  embed.setAuthor(`Lyrics for ${q}`)
  embed.setTimestamp()
  embed.setColor(`RANDOM`)
  embed.setFooter(`Requested by ${message.author.username}`,message.author.displayAvatarURL())
  embed.setThumbnail(info.thumbnail.genius)
  
  message.channel.send(embed)
  } catch (error) {
    message.channel.send("a")
  }
} else if (cmd == "reddit") {
  const got = require("got")
   const subreddits = ["dankmemes","me_irl","memes","MemeEconomy"]
   const subreddit = args.join(" ")
try {
  const [ content ] = await fetch(`https://www.reddit.com/r/${subreddit}/random.json`).then(response => response.json())
  var title = content.data.children[0].data.title;
  var link = content.data.children[0].data.url;
  let embed = new Discord.MessageEmbed()
  embed.setTitle(`**` + title + `**`) 
  embed.setImage(link) 
  embed.setColor(`RANDOM`)
  embed.setURL(link)
   message.channel.send(embed) 
}
 catch (error) {
message.channel.send("Subreddit not found")
}
} else if (cmd == "avatar") {
  let u = findUser(args.join(" "))
  if (u == undefined) {
    u = message.author.id
  
} 
let embed = new Discord.MessageEmbed()
embed.setAuthor("Avatar of " + client.users.cache.get(u).tag)
embed.setColor(`RANDOM`)
embed.setURL(client.users.cache.get(u).displayAvatarURL({dynamic: true}))
embed.setImage(client.users.cache.get(u).displayAvatarURL({dynamic: true}))
message.channel.send(embed)

} else if (cmd == "ping") {
  let embed = new Discord.MessageEmbed()
  embed.setTitle(`Bot ping`)
  embed.setDescription(`${message.author.username}, the bot ping is **${client.ws.ping}** ms`)
  embed.setFooter(`Requested by ${message.author.username}`,message.author.displayAvatarURL())
  embed.setTimestamp()
  embed.setColor(`RANDOM`)
  message.channel.send(embed)
}
})



client.on('guildMemberAdd', async member => {
	let chx = db.get(`welchannel_${member.guild.id}`);
	
	if (chx === null) {
		return;
	}
	
	let data = await canva.welcome(member, { link: "https://cdn.discordapp.com/attachments/739837131144429720/758887254361243659/images_1.jpeg" });
	
	const attachment = new Discord.MessageAttachment(data, "welcome-image.png");
	
	client.channels.cache.get(chx).send(`Welcome to **${member.guild.name}**, ${member.user.tag}!`, attachment);
})

 
client.login(bottoken);