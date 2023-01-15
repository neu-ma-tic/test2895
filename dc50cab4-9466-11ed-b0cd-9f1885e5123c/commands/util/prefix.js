module.exports = ({
  name: "prefix",
  code: `
$setServerVar[prefix;$message[]]
Prefix has been set to **$message[]**
$onlyIf[$message[]!=;What should be the new prefix?]
$onlyPerms[manageserver;You need the manage server perm]
$onlyIf[$charCount<5;Prefix too long]

`})