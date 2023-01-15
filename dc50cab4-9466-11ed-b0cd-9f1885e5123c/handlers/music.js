const ytdlDiscord = require('ytdl-core-discord');
const { MessageEmbed } = require('discord.js')

module.exports = {
	async play(song, message) {
		const queue = message.client.queue.get(message.guild.id);
		let embed = new MessageEmbed().setColor("BLUE");
		
		if (!song) {
			queue.channel.leave();
			message.client.queue.delete(message.guild.id);
			embed.setAuthor('🎶 Music queue has ended.')
			return queue.textChannel
			  .send(embed)
			  .catch(console.error);
		}
		
		try {
			var stream = await ytdlDiscord(song.url, {
				highWaterMark: 1 << 25
			});
		} catch (error) {
			if (queue) {
				queue.songs.shift();
				module.exports.play(queue.songs[0], message);
			}
			
			if (error.message.includes === "copyright") {
				return message.channel.send("⚠️ This video contains copyright content!");
			} else {
				console.error(error);
			}
		}
		
		const dispatcher = queue.connection
		  .play(stream, { type: "opus" })
		  .on('finish', () => {
		  	if (queue.loop) {
		  		let lastsong = queue.songs.shift();
		  		queue.songs.push(lastsong);
		  		module.exports.play(queue.songs[0], message);
		  	} else {
		  		queue.songs.shift();
		  		module.exports.play(queue.songs[0], message);
		  	}
		  })
		  .on('error', console.error);
		  
		  dispatcher.setVolumeLogarithmic(queue.volume / 100);
		  embed.setAuthor('🎵 Started playing song', message.client.user.displayAvatarURL({ dynamic: true }))
		  .setDescription(`**[${song.title}](${song.url})**`);
		  
		  queue.textChannel
		    .send(embed)
		    .catch(err => message.channel.send('❌ Unable to play song D:'));
	}
};