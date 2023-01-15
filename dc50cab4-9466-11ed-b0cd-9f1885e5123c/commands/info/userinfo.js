module.exports = ({
  name: "userinfo",
  code: `
$thumbnail[$userAvatar[$mentioned[1;yes]]]
$title[$username[$mentioned[1;yes]]'s account info]
$addField[Highest role;$replaceText[<@&$highestRole[$mentioned[1;yes]]>;<@&everyone>;No roles]]
$addField[Device;$replaceText[$replaceText[$replaceText[$replaceText[$platform[$mentioned[1;yes]];mobile;Mobile phone];desktop;Desktop];web;Browser];offline;Offline]]
$addField[Status;$status[$mentioned[1;yes]]]
$addField[Activity;$activity[$mentioned[1;yes]]]
$addField[User roles;$replaceText[$replaceText[你好布奇哈哈$memberRoles[$mentioned[1;yes]]你好布奇哈哈;你好布奇哈哈你好布奇哈哈;No roles];你好布奇哈哈;]]
$addField[Joined server;$creationTime[$mentioned[1;yes];member] ($creationDate[$mentioned[1;yes]];member)]
$addField[Account created;$creationTime[$mentioned[1;yes];user] ($creationDate[$mentioned[1;yes];user])]
$addField[User ID;$mentioned[1;yes]]
$addField[Full username;$username[$mentioned[1;yes]]#$discriminator[$mentioned[1;yes]]]
$color[RANDOM]
$addTimestamp
$footer[Requested by $username[$authorID];$userAvatar[$authorID]]
$suppressErrors[Unexpected error occured]
`}) 

//suppressErrors