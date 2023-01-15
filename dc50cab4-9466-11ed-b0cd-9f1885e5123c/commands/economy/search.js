module.exports = ({
  name: "search",
  code: `
  $title[$username[] went searching]
  $description[You have 3 places to choose from, choose one and type it in the chat:
  
  **$randomText[tree;house;cabin;car;mailbox;wallet;bag;handbag;purse;suitcase;lockpick;closet], $randomText[dome;truck;hut;butt;dark;basement;attic;roof;floor;dustbin;dumpster;dog;cat], or $randomText[bed;chair;basin;streets;fridge;carpet;cabinet;pocket;laudry;pants]**
  
  You have 20s to respond with a valid option]
  $awaitMessages[$randomText[tree;house;cabin;car;mailbox;wallet;bag;handbag;purse;suitcase;lockpick;closet],$randomText[dome;truck;hut;butt;dark;basement;attic;roof;floor;dustbin;dumpster;dog;cat],$randomText[bed;chair;basin;streets;fridge;carpet;cabinet;pocket;laudry;pants];$authorID;20s;search,search,search;You ran out of time, $username[]]
 $color[RANDOM]
 $addTimestamp
 $footer[Requested by $username[];$userAvatar[$authorID]]
 $globalCooldown[1m;You still need to wait {time} to search again, $username[]]
  `
})