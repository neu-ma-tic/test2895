module.exports = ({
name: "ping",
code: `
$title[Bot ping]
$description[$username[$authorID], the ping is **$ping** ms]
$color[RANDOM]
$footer[Requested by $username[$authorID];$userAvatar[$authorID]]
$addTimestamp
`
})