module.exports = ({
  name: "roleinfo",
  code: `
$title[Role $roleName[$mentionedRoles[1]] info]
$addField[Role position;$rolePosition[$mentionedRoles[1]]/$roleCount]
$addField[Role created;$creationTime[$mentionedRoles[1]] ($creationDate[$mentionedRoles[1]])]
$addField[Role ID;$mentionedRoles[1]]
$addField[Role name;$roleName[$mentionedRoles[1]]]
$color[RANDOM]
$addTimestamp
$footer[Requested by $username[$authorID];$userAvatar[$authorID]]
$onlyIf[$mentionedRoles[1]!=;Mention a role]
`})