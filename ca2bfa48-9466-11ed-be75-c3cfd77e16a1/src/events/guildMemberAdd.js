const { Listener } = require('discord-akairo');

class GuildMemberAddListener extends Listener {
	constructor() {
		super('guildMemberAdd', {
			emitter: 'client',
			event: 'guildMemberAdd'
		});
	}

	exec(member) {
		let addRoles = ['785973981219258368', '785958057091661864'];
		member.roles.add(addRoles);
	}
}

module.exports = GuildMemberAddListener;