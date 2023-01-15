module.exports = ({
  name: "snipe",
  code: `
$author[$username[$getChannelVar[author]]#$discriminator[$getChannelVar[author]];$userAvatar[$getChannelVar[author]]]
$description[$getChannelVar[snipe]]
$color[RANDOM]
$onlyIf[$getChannelVar[snipe]!=;Currently empty]
`
})