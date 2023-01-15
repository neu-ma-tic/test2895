const { AkairoClient, CommandHandler, InhibitorHandler, ListenerHandler } = require('discord-akairo');
require('dotenv').config;

class DiscordBot extends AkairoClient {
	constructor() {
		super({
			ownerID: ['299693860240752650', '612166290190106624'],
		}, {
			disableMentions: 'everyone'
		});

		this.commandHandler = new CommandHandler(this, {
			directory: './src/commands/',
			prefix: process.env.music,
			handleEdits: true,
    	commandUtil: true
		});

		this.inhibitorHandler = new InhibitorHandler(this, {
			directory: './src/inhibitors/'
		});

		this.listenerHandler = new ListenerHandler(this, {
			directory: './src/events/'
		});

		this.listenerHandler.setEmitters({
    	commandHandler: this.commandHandler,
    	inhibitorHandler: this.inhibitorHandler,
    	listenerHandler: this.listenerHandler
		});

		this.commandHandler.loadAll();

		this.commandHandler.useInhibitorHandler(this.inhibitorHandler);
		this.inhibitorHandler.loadAll();

		this.commandHandler.useListenerHandler(this.listenerHandler);
		this.listenerHandler.loadAll();

	}
}

const bot = new DiscordBot();
bot.login(process.env.token);

require('./src/Discord-MusicBot-master/index');
