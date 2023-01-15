<p align="center">
    <img width="300" height="auto" src="https://i.imgur.com/yCFscwQ.png" alt="WiseMan" />
</p>

## WiseMan - Discord Bot 🤖

[![forthebadge](https://forthebadge.com/images/badges/gluten-free.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/made-with-crayons.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/made-with-javascript.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

This bot allows you to level up based on the time you spend in a vocal channel and how much you write in a text channel

**If you don't need/want to host and set it up on your own you can add your bot to your server clicking here:
[Invite](https://discord.com/oauth2/authorize?client_id=589693244456042497&scope=bot&permissions=2147483639)**

## Commands 🎨

You need to add the prefix `!` before the command e.g: `!rank`.

- **rank** - It shows you your rank.
- **propic** - It shows you your profile image.
- **github** - It shows you the github repo link.
- **help** - It shows you all the commands.
- **poll** - It allows you to make a poll.
- **setPrefix** - It allows you to set a new prefix for your server.
- **setNotificationChannel** - It allows you to set a new text channel where the notification will be sent.
- **setRank** - It allows you to set a custom role for each level.

**and much more...**

## Steps ▶️

Install the dependencies

```
$ npm i
```

Create an `.ENV` file and replace `*TOKEN*` with the token.
You can take the token from [discord developers page](https://discordapp.com/developers/applications/) > Bot

```
$ TOKEN="*TOKEN*"
```

Start the bot

```
$ npm start
```

> *The repo has 2 versions (two branch) the ```master``` rely on **firebase** and ```mongodbVersion``` that rely on **mongodb**, follow the right configuration based on the database you use.
> the master is the branch supported, mongodb be in the future could be outdated and not supported anymore*

## Configuration ⚙️

- The only configurations are the prefix and the minutes in the `config.json`.

  The `minutes` are the minutes for wich every time the bot level up you (i.g: by default the bot update your rank every hour for the time-based system).

```
{
   "prefix": "!",
   "minutes": 60
}
```

### Firebase 🔥

Create a firebase account and insert into `.ENV` the following data

```
apiKey="APITOKEN"
authDomain="AUTHDOMAIN
databaseURL="DATABASEURL"
projectId="PROJECTID"
storageBucket="STORAGEBUCKET"
messagingSenderId="MESSAGESENDERID"
appId="APPID"
measurementId="MEASUREMENTID" // this should be optional
```


## Support 💻

If you want to be an active contributor join the discord server [here](https://discord.gg/fnmKKWPWpB) 

## Donation 💰

- If you want to support the me and the discord development consider voting the bot [here](https://top.gg/bot/589693244456042497) and
donating:


[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=WJWDBJENVNGHE)

or 

[Donate](https://ko-fi.com/ladvace)



## Authors ❤️

- **Gianmarco Cavallo** (ladvace) - [Github Profile](https://github.com/Ladvace)

### If you have any problems or question open an issue or feel free to contact me! 🔧😃
