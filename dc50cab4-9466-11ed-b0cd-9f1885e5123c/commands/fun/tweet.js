module.exports = ({
  name: "tweet",
  code: `
$addAttachment[$api[https://nekobot.xyz/api/imagegen?type=tweet&username=$username[$mentioned[1;yes]]&text=$noMentionMessage[];message]]
$suppressErrors[An error occured]
$onlyIf[$noMentionMessage[]!=;Provide some text]
`})
