module.exports = ({
  name: "work",
  code: `
  $title[$username[] went to work]
  $description[Your work:
  Type the thing below to get the money!
  
  **$randomString[7]**
  
  You only have 30 seconds to answer.]
  $color[RANDOM]
  $footer[Requested by $username[];$userAvatar[$authorID]]
  $awaitMessages[$randomString[7];$authorID;30s;work;You ran out of time, $username[]]
 $globalCooldown[2m;You need to wait {time} to work again, $username[]]
 $addTimestamp
  `
})