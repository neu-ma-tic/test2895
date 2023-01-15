module.exports = ({
  name: "phcomment",
  code: `$addAttachment[$api[https://nekobot.xyz/api/imagegen?type=phcomment&username=$username[$mentioned[1;yes]]&text=$noMentionMessage[]&image=$userAvatar[$mentioned[1;yes]];message]]
$suppressErrors[An error occured]
$onlyIf[$noMentionMessage[]!=;Provide some text]
`})