const { Listener } = require('discord-akairo');

let db = require("quick.db");
let request = new (require("rss-parser"))();
let config = require("../config");

class YoutubeListener extends Listener {
	constructor() {
		super('youtube', {
			emitter: 'client',
			event: 'ready'
		});
	}

	exec() {
		handleUploads();
	}
}

module.exports = YoutubeListener;

function handleUploads() {
	if (db.fetch(`postedVideos`) === null) db.set(`postedVideos`, []);
	setInterval(() => {
		request.parseURL(`https://www.youtube.com/feeds/videos.xml?channel_id=${config.channel_id}`)
			.then(data => {
				if (db.fetch(`postedVideos`).includes(data.items[0].link)) return;
				else {
					db.set(`videoData`, data.items[0]);
					db.push("postedVideos", data.items[0].link);
					let parsed = db.fetch(`videoData`);
					let channel = this.client.channels.cache.get(config.channel);
					if (!channel) return;
					let message = config.messageTemplate
						.replace(/{author}/g, parsed.author)
						.replace(/{title}/g, Discord.Util.escapeMarkdown(parsed.title))
						.replace(/{url}/g, parsed.link);
					channel.send(message);
				}
			});
	}, config.watchInterval);
}