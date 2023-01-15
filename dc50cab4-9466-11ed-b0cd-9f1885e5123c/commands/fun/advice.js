module.exports = ({
  name: "advice",
  code: `
  $title[Here's your advice, $username[]]
  $description[**$api[https://api.adviceslip.com/advice;slip;advice]**]
  $footer[Requested by $username[];$userAvatar[$authorID]]
  $addTimestamp
  $color[RANDOM]
  `
});