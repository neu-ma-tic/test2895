module.exports = ({
  name: "youtube",
  code: ` $addAttachment[https://some-random-api.ml/canvas/youtube-comment?username=$username[$mentioned[1;yes]]&comment=$noMentionMessage[]&avatar=$userAvatar[$mentioned[1;yes]]]
$onlyIf[$noMentionMessage[]!=;Please provide a message]
`
});