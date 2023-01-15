module.exports = ({
  name: "clyde",
  code : `
  $addAttachment[https://ctk-api.herokuapp.com/clyde/$message[]]
  $onlyIf[$message[]!=;What do you want clyde to say?]`
});