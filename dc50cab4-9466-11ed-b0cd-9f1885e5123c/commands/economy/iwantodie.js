module.exports = ({
  name: "beg",
  code: `
  $onlyIf[$randomText[yes;no]!=yes;{execute:gbeg}]
  $onlyIf[$randomText[yes;no]!=no;{execute:bbeg}]
  $globalCooldown[90s;You still need to wait {time} to beg again, $username[]]
  `
})