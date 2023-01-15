const Client = require("@replit/database");
const client = new Client();

const db =async()=>{
  await Client.set("key", "value");
let key = await Client.get("key");
return key;
}

console.log(db());