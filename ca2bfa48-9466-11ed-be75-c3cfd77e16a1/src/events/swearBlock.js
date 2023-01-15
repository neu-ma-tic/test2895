const { Listener } = require('discord-akairo');

class SwearBlockListener extends Listener {
	constructor() {
		super('swear-block', {
			emitter: 'client',
			event: 'message'
		});
	}

	exec(msg) {
		let allowedWords = ['swear', 'swear2'];
		let split = msg.content.split(" ");
		const found = allowedWords.some(r=> split.includes(r));
		if(found) {
			msg.delete();
		}
	}
}

module.exports = SwearBlockListener;