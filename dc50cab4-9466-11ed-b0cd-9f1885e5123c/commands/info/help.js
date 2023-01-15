module.exports = ({
	name: "help",
	aliases: ["bothelp"],
	code: `
	$title[Help Menu]
	$description[**Fun**\n\`\`\`advice, neko, birb, cat, dog, fox, koala, panda, zebra, urban, meme, 8ball, rps, joke\`\`\`\n\n**Info**\n\`\`\`snipe, userinfo, serverinfo, roleinfo, ping, help, avatar, prefix, say, setwelcome, covid\`\`\`\n\n**Music**\n\`\`\`play, pause, nowplaying, queue, jump, pause, resume, skip, stop, loop\`\`\`]
	$footer[Bot made by: $username[635319965335158796]#$discriminator[635319965335158796] and $username[743767109817073664]#$discriminator[743767109817073664]]
	$color[$random[0;999999]]
	$thumbnail[$client[avatarURL]]
	`
})