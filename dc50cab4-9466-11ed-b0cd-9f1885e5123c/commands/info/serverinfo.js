module.exports = ({
  name: "serverinfo",
  code: `
$title[$serverName[$guildID] ]
$addField[Categories;$categoryCount]
$addField[Channels;$channelCount]
$addField[Roles;$roleCount]
$addField[Members;Total: $membersCount[]
Online: $membersCount[online]
Offline: $membersCount[offline]
Do not disturb: $membersCount[dnd]
Idle: $membersCount[idle]
Humans: $membersCount[human]
Bots: $membersCount[bot]]
$addField[Server invite;$getServerInvite[$guildID]]
$addField[Verification level;$toLowercase[$serverVerificationLvl]]
$addField[Region;$region]
$addField[Owner;$username[$ownerID]#$discriminator[$ownerID]]
$addField[Server created;$creationTime[$guildID] ($creationDate[$guildID])]
$addField[Server ID;$guildID]
$addField[Server name;$serverName[$guildID]]
$thumbnail[$serverIcon]
$color[RANDOM]
$addTimestamp
$footer[Requested by $username[$authorID];$userAvatar[$authorID]]
$suppressErrors[Unexpected error occured]
`})