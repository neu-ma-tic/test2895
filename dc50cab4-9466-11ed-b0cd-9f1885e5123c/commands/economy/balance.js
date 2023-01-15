module.exports = ({
  name: "balance",
  aliases: ["bal","money","cash"],
  code: `
  $title[**$username[$mentioned[1;yes]]#$discriminator[$mentioned[1;yes]]**'s balance]
  $description[**$getVar[name]**: $getVar[currency;$authorID]]
  $footer[Requested by $username[];$userAvatar[$authorID]]
  $color[RANDOM]
  $addTimestamp 
  $suppressErrors[Error occured]
  `
})