const Dlang = require('discordbot-script');
const keepAlive = require('./server');

const bot = new Dlang({
	token: process.env.token,
	prefix: ['a/']
});

bot.Command({
	name: 'ping',
	code: `
	Pong!đ
**$ping** ms
  `
});
bot.Command({
	name: 'imp',
	code: `
	āļ <== Sus
	`
});
keepAlive();