const fs = require('fs')
const Discord = require('discord.js')
const keep_alive = require('./keep_alive.js')

const client = new Discord.Client()
require('discord-buttons')(client)
const { MessageButton, MessageActionRow } = require('discord-buttons')

var MemberFilePath = './Config/Member.json'
var MemberFileRead = fs.readFileSync(MemberFilePath)
var MemberFile = JSON.parse(MemberFileRead)

var ConfigFilePath = './Config/ServerConfig.json'
var ConfigFileRead = fs.readFileSync(ConfigFilePath)
var ConfigFile = JSON.parse(ConfigFileRead)

var Prefix = "yx>"
var Embed = new Discord.MessageEmbed()
Embed.setColor("BLUE")

client.once("ready", () => {
    console.log("=====> Log <=====")
    client.user.setActivity(' 一个人的游戏', { type: "PLAYING" })
})

client.on('guildMemberAdd', member => {
    if(MemberFile[member.id] == null) {
        if(!member.user.bot) createFile(member)
    }
    member.setNickname(getMemberNickName(member))
})
client.on('guildMemberUpdate', (oldMember, newMember) => {
    if(newMember.nickname && oldMember.nickname !== newMember.nickname) {
        if(newMember.nickname !== getMemberNickName(newMember)) {
            var NickName = getMemberNickName(newMember)
            newMember.setNickname(NickName)
            console.log("從名字中 | "+NickName)
        }
    }
})
client.on("messageDelete", async message => {
    if(message.author.bot) return
    var logs = await message.guild.fetchAuditLogs({type: 72})
    let messageAttachment = message.attachments.size > 0 ? message.attachments.array()[0].url : null
    
    Embed.setAuthor(message.author.tag, message.author.avatarURL())
    Embed.setTitle("")
    Embed.setDescription("🗑️由 <@"+message.author.id+"> 发送的信息在 <#"+message.channel.id+">🗑️\n"+message.content)
    Embed.setImage()
    Embed.setTimestamp()
    if(messageAttachment) Embed.setImage(messageAttachment)
    if(message.channel.id !== "882513313316089857") client.channels.cache.get("882513313316089857").send(Embed)
})
client.on('messageUpdate', (oldMessage, newMessage) => {
    if(oldMessage.content == newMessage.content) return
    if(newMessage.author.bot) return
    Embed.setTitle("")
    Embed.setAuthor(newMessage.author.tag, newMessage.author.avatarURL())
    Embed.setDescription("✏️由 <@"+newMessage.author.id+"> 发送的信息在 <#"+newMessage.channel.id+">✏️\n\n```旧信息``` \n"+oldMessage.content+"\n```新信息```\n"+newMessage.content)
    Embed.setImage()
    Embed.setTimestamp()
    if(newMessage.channel.id !== "883543231973965895") client.channels.cache.get("883543231973965895").send(Embed)
})
client.on('clickButton', async (button) => {
    var File = getMemberFile(button.clicker)
    var LevelRole = File["Title"].LevelRoleHas
    var LimitRole = File["Title"].LimitRoleHas
    
    var PBMenuMy = new MessageButton()
     .setLabel("称号背包")
     .setID("PBMenuMy")
     .setStyle("blurple")
    var PBMenuHave = new MessageButton()
     .setLabel("你拥有的称号")
     .setID("PBMenuHave")
     .setStyle("blurple")

    if(button.id === "PBMenuMy"){
        var CustomRole = "未解锁"
        var NowChoose = File["Title"].NowChoose
    
        if(File["Title"].CustomRoleHas == "1") {
             if(File["Title"].CustomRole == "Unset"){
                var CustomRole = "未设置"
            } else var CustomRole = File["Title"].CustomRole
        } else var CustomRole = "未解锁"
                        
        var FileNowChoose =  File["Title"].NowChoose
        var Array = FileNowChoose.toString().split(" ")
        if(File["Title"].NowChoose == 0){
            var NowChoose = "未选择"
        } else if(File["Title"].NowChoose == "custom"){
            var NowChoose = "自定义"
        } else if(File["Title"].NowChoose.startsWith("level-")){
            var rank = Array[0].replace("level-", "")
            var NowChoose = "等级称号-"+rank
        } else if(File["Title"].NowChoose.startsWith("limit-")){
            var rank = Array[0].replace("limit-", "")
            var NowChoose = "限定称号-"+rank
        }
        
        Embed.setAuthor(button.clicker.user.tag, button.clicker.user.avatarURL())
        Embed.setTitle("你的称号背包 | 当前称号选择 : " + NowChoose)
        Embed.setDescription("**自定义称号**\n"+CustomRole+"\n**等级称号**\n已获得 : "+LevelRole+"\n**限定称号**\n已获得 : "+LimitRole.length)
        Embed.setImage()
        button.message.edit(Embed, PBMenuHave)
    }
    if(button.id === "PBMenuHave"){
        var embed = new Discord.MessageEmbed()
        embed.setTitle("等级称号")
        embed.setAuthor(button.clicker.user.tag, button.clicker.user.avatarURL())
        if(1 <= LevelRole) embed.addField('等级称号-1', getTitle("Level", "1"))
        if(2 <= LevelRole) embed.addField('等级称号-2', getTitle("Level", "2"))
        if(3 <= LevelRole) embed.addField('等级称号-3', getTitle("Level", "3"))
        if(4 <= LevelRole) embed.addField('等级称号-4', getTitle("Level", "4"))
        if(5 <= LevelRole) embed.addField('等级称号-5', getTitle("Level", "5"))
        if(6 <= LevelRole) embed.addField('等级称号-6', getTitle("Level", "6"))
        if(7 <= LevelRole) embed.addField('等级称号-7', getTitle("Level", "7"))
        if(8 <= LevelRole) embed.addField('等级称号-8', getTitle("Level", "8"))
        if(LimitRole.includes("1")) embed.addField('限定称号-1', getTitle("Limit", "1"))
        if(LimitRole.includes("2")) embed.addField('限定称号-2', getTitle("Limit", "2"))
        if(LimitRole.includes("3")) embed.addField('限定称号-3', getTitle("Limit", "3"))
        if(LimitRole.includes("4")) embed.addField('限定称号-4', getTitle("Limit", "4"))
        button.message.edit(embed, PBMenuMy)
    }  
})

client.on('message', message => {
    if(message.channel.name !== undefined){
        var msgArray = message.content.split(" ")
        var args = msgArray.slice(1)
        Embed.setAuthor(message.author.tag, message.author.avatarURL())
        Embed.setTitle()
        Embed.setDescription()
        Embed.setImage()
        Embed.setTimestamp()
        if(message.author.bot || message.webhookID){
            if(message.content.startsWith("UpdateLevel") && message.channel.id == "880666654835613717"){
                var Member = message.mentions.members.first()
                var File = getMemberFile(Member)
                var LevelRole = parseInt(args/5)
                if(LevelRole > 0) {
                    MemberFile[Member.id] = {
                        "Name" : File.Name,
                        "Role" : File.Role,
                        "Basic" : {
                            "GMimg" : File["Basic"].GMimg,
                            "GNimg" : File["Basic"].GNimg,
                        },
                        "Title" : {
                            "NowChoose" : File["Title"].NowChoose,
                            "CustomRole" : File["Title"].CustomRole,
                            "CustomRoleHas" : File["Title"].CustomRoleHas,
                            "LevelRoleHas" : LevelRole,
                            "LimitRoleHas" : File["Title"].LimitRoleHas,
                        }
                    }
                    fs.writeFileSync(MemberFilePath, JSON.stringify(MemberFile, null, 2))
                }
                client.channels.cache.get("851680299825496094").send("恭喜 <@"+Member+">，你的聊天已升级至 "+args+" 级，恭喜恭喜:partying_face:")
            }
        } else {
            var File = getMemberFile(message.member)
            var TimeNow = getTime("time")
            if(message.channel.parent.id == "850367776577421334"){
                const LogOfChat = new Discord.WebhookClient("882501225277431808", "vmJQTobjhT7PimW60K9Myhp8aI5bNHkxzjPWQY37qVHweUv1nUjN1UZ9HtMdUTkUtKE4")
                LogOfChat.send({
                    content: message,
                    username: message.member.nickname+" | "+message.channel.name,
                    avatarURL: message.author.avatarURL(),
                })
            } else if(message.channel.parent.id == "851674679836147722"){
                const LogOfCmd = new Discord.WebhookClient("882507143683641395", "rihMmRFn4xcKIOafD_vNlPoe0xNYAYFAyKjPCvh5MY7Hmir10wQ5fKyLJmwfGUSAIT27")
                LogOfCmd.send({
                    content: message,
                    username: message.member.nickname+" | "+message.channel.name,
                    avatarURL: message.author.avatarURL(),
                })
            }
            if(MemberFile[message.member.id] == null) createFile(message.member)
            if(message.member.nickname == null || message.member.nickname !== getMemberNickName(message.member)){
                var NickName = getMemberNickName(message.member)
                if(message.author.id !== "652168792683708466"){
                    message.member.setNickname(NickName)
                    console.log("從信息中 | 原:"+message.member.nickname+" | 新:"+NickName)
                }
            }
            if(message.content.startsWith(Prefix)){
                var command = msgArray[0].replace(Prefix, "")
                if(command == "prefix"){
                    if(args == "" || args[0] == "my"){
                        let User = message.mentions.members.first() || message.member
                        var File = getMemberFile(User)
                        var PBMenuHave = new MessageButton()
                        .setLabel("你拥有的称号")
                        .setID("PBMenuHave")
                        .setStyle("blurple")
                        
                        var LevelRole = File["Title"].LevelRoleHas
                        var LimitRole = File["Title"].LimitRoleHas
        
                        if(File["Title"].CustomRoleHas == "1") {
                            if(File["Title"].CustomRole == "Unset"){
                                var CustomRole = "未设置"
                            } else var CustomRole = File["Title"].CustomRole
                        } else var CustomRole = "未解锁"
                        
                        var FileNowChoose =  File["Title"].NowChoose
                        var Array = FileNowChoose.toString().split(" ")
                        if(File["Title"].NowChoose == 0){
                            var NowChoose = "未选择"
                        } else if(File["Title"].NowChoose == "custom"){
                            var NowChoose = "自定义"
                        } else if(File["Title"].NowChoose.startsWith("level-")){
                            var rank = Array[0].replace("level-", "")
                            var NowChoose = "等级称号-"+rank
                        } else if(File["Title"].NowChoose.startsWith("limit-")){
                            var rank = Array[0].replace("limit-", "")
                            var NowChoose = "限定称号-"+rank
                        }

                        Embed.setAuthor(User.user.tag, User.user.avatarURL())
                        Embed.setTitle("你的称号背包 | 当前称号选择 : " + NowChoose)
                        Embed.setDescription("**自定义称号**\n"+CustomRole+"\n**等级称号**\n已获得 : "+LevelRole+"\n**限定称号**\n已获得 : "+LimitRole.length)
                        message.channel.send(Embed, PBMenuHave)
                    } else if(args[0] == "reset"){
                        MemberFile[message.author.id] = {
                            "Name" : File.Name,
                            "Role" : File.Role,
                            "Basic" : {
                                "GMimg" : File["Basic"].GMimg,
                                "GNimg" : File["Basic"].GNimg,
                            },
                            "Title" : {
                                "NowChoose" : 0,
                                "CustomRole" : File["Title"].CustomRole,
                                "CustomRoleHas" : File["Title"].CustomRoleHas,
                                "LevelRoleHas" : File["Title"].LevelRoleHas,
                                "LimitRoleHas" : File["Title"].LimitRoleHas,
                            }
                        }
                        fs.writeFileSync(MemberFilePath, JSON.stringify(MemberFile, null, 2))
                        message.channel.send("已重置你的称号")
                    } else if(args[0] == "set"){
                        if(args[1] == "custom"){
                            if(File["Title"].CustomRoleHas == "1"){
                                MemberFile[message.author.id] = {
                                    "Name" : File.Name,
                                    "Role" : File.Role,
                                    "Basic" : {
                                        "GMimg" : File["Basic"].GMimg,
                                        "GNimg" : File["Basic"].GNimg,
                                    },
                                    "Title" : {
                                        "NowChoose" : "custom",
                                        "CustomRole" : File["Title"].CustomRole,
                                        "CustomRoleHas" : File["Title"].CustomRoleHas,
                                        "LevelRoleHas" : File["Title"].LevelRoleHas,
                                        "LimitRoleHas" : File["Title"].LimitRoleHas,
                                    }
                                }
                                fs.writeFileSync(MemberFilePath, JSON.stringify(MemberFile, null, 2))
                                if(Titlefile.CustomRole == "Unset"){
                                    message.channel.send("以设置当前称号为 自定义称号 | 未设置")
                                } else {
                                    message.channel.send("以设置当前称号为 自定义称号 | " + Titlefile.CustomRole)
                                }
                            } else message.channel.send("未解锁自定义称号")
                        } else if(args[1] == "level"){
                            if(args[2] == "") return message.channel.send("请输入称号ID")
                            if(isNaN(args[2])) return message.channel.send("请输入数字")
                            if(args[2] < 0) message.channel.send("不存在该称号")
                            if(0 < args[2]){
                                if(args[2] <= File["Title"].LevelRoleHas){
                                    var Title = getTitle("Level", args[2])
                                    MemberFile[message.author.id] = {
                                        "Name" : File.Name,
                                        "Role" : File.Role,
                                        "Basic" : {
                                            "GMimg" : File["Basic"].GMimg,
                                            "GNimg" : File["Basic"].GNimg,
                                        },
                                        "Title" : {
                                            "NowChoose" : "level-" + args[2],
                                            "CustomRole" : File["Title"].CustomRole,
                                            "CustomRoleHas" : File["Title"].CustomRoleHas,
                                            "LevelRoleHas" : File["Title"].LevelRoleHas,
                                            "LimitRoleHas" : File["Title"].LimitRoleHas,
                                        }
                                    }
                                    fs.writeFileSync(MemberFilePath, JSON.stringify(MemberFile, null, 2))
                                    message.channel.send("你已选择称号为 等级称号-" + args[2] + " | " + Title)
                                } else message.channel.send("你还未解锁该称号")
                            }
                        } else if(args[1] == "limit"){
                            if(args[2] == "") return message.channel.send("请输入称号ID")
                            if(isNaN(args[2])) return message.channel.send("请输入数字")
                            var NowChoose = "no"
                            if(args[2] == 1){
                                if(!File["Title"].LimitRoleHas.includes("1"))return message.channel.send("未解锁该称号")
                                var NowChoose = "limit-1"
                            } else if(args[2] == 2){
                                if(!File["Title"].LimitRoleHas.includes("2"))return message.channel.send("未解锁该称号")
                                var NowChoose = "limit-2"
                            } else if(args[2] == 3){
                                if(!File["Title"].LimitRoleHas.includes("3"))return message.channel.send("未解锁该称号")
                                var NowChoose = "limit-3"
                            } else if(args[2] == 4){
                                if(!File["Title"].LimitRoleHas.includes("4"))return message.channel.send("未解锁该称号")
                                var NowChoose = "limit-4"
                            } else message.channel.send("不存在这个称号")
                                
                            if(NowChoose !== "no"){
                                var Title = getTitle("Limit", args[2])
                                MemberFile[message.author.id] = {
                                        "Name" : File.Name,
                                    "Role" : File.Role,
                                    "Basic" : {
                                        "GMimg" : File["Basic"].GMimg,
                                        "GNimg" : File["Basic"].GNimg,
                                    },
                                    "Title" : {
                                        "NowChoose" : NowChoose,
                                        "CustomRole" : File["Title"].CustomRole,
                                        "CustomRoleHas" : File["Title"].CustomRoleHas,
                                        "LevelRoleHas" : File["Title"].LevelRoleHas,
                                        "LimitRoleHas" : File["Title"].LimitRoleHas,
                                    }
                                }
                                fs.writeFileSync(MemberFilePath, JSON.stringify(MemberFile, null, 2))
                                message.channel.send("你已选择称号为 限定称号-" + args[2] + " | " + Title)
                            }
                        } else message.channel.send("用法: yx>prefix set [称号类别] [称号ID]")
                    } else message.channel.send("没有这个指令")
                }
            } else if(message.content.startsWith("早安")){
                if(TimeNow == "半夜"){
                    message.reply("现在还是半夜呢，你可真早")
                } else if(TimeNow == "早上"){
                    message.reply(randomMesReply("GM"))
                    message.channel.send(File["Basic"].GMimg)
                } else message.reply("早上已经过去了哦，你可真迟")
            } else if(message.content.startsWith("午安")){
                if(TimeNow == "晚上"){
                    message.reply("下午已经过去了拉，你可真迟呢")
                } else if(TimeNow == "下午"){
                    message.reply(randomMesReply("GA"))
                } else message.reply("现在还没到下午呢，你太心急了")
            } else if(message.content.startsWith("晚安")){
                if(TimeNow == "凌晨"){
                    message.reply("时间都到凌晨了还没睡，真是夜猫子呢")
                } else if(TimeNow == "晚上"){
                    message.reply(randomMesReply("GN"))
                    message.channel.send(File["Basic"].GNimg)
                } else message.reply("晚上还没到呢，就那么想看月亮吗")
            } else if(message.content == "撩我") message.reply(randomMesReply("Tease"))
            if(message.content == "没有人喜欢我" || message.content == "沒有人喜歡我") message.reply("我叫没有人")
            let messageAttachment = message.attachments.size > 0 ? message.attachments.array()[0].url : null
            if(messageAttachment){
                Embed.setTitle("")
                Embed.setDescription("")
                Embed.setImage(messageAttachment)
                client.channels.cache.get("879198941055418418").send(Embed)
            }
        }
    } else message.author.send("抱歉，目前不支持私信功能哦")
})

client.login(process.env['Bot_Token'])

function getTime(format){
    const LocalDate = new Date()
    const MyDate = new Date(LocalDate.toLocaleString('en-US', { timeZone: 'Asia/Kuala_Lumpur' }))
    const Hour =  MyDate.getHours()
    var dd = String(MyDate.getDate()).padStart(2, '0')
    var mm = String(MyDate.getMonth() + 1).padStart(2, '0')
    var yyyy = MyDate.getFullYear()

    if(format == "basic") return MyDate
    if(format == "time"){
        if(Hour < 3){
            return "凌晨"
        } else if(Hour < 5){
            return "半夜"
        } else if(Hour < 12){
            return "早上"
        } else if(Hour < 18){
            return "下午"
        } else return "晚上"
    }
    if(format == "date") return mm + '-' + dd + '-' + yyyy
}
function randomMesReply(format){
    if(format == "GM") var Message = ConfigFile["Reply"].GM
    if(format == "GA") var Message = ConfigFile["Reply"].GA
    if(format == "GN") var Message = ConfigFile["Reply"].GN
    if(format == "Tease") var Message = ConfigFile["Reply"].Tease

    var replyMessage = Message[Math.floor(Math.random() * Message.length)]
    return replyMessage
}
function createFile(User){
    var MemberName = User.user.username
    MemberFile[User.id] = {
        "Name" : MemberName,
        "Role" : "成员",
        "Basic" : {
            "GMimg" : "https://cdn.discordapp.com/attachments/850368259768844289/876609982181814282/a_2.jpg",
            "GNimg" : "https://cdn.discordapp.com/attachments/850368259768844289/876610938348916786/unknown.jpg",
        },
        "Title" : {
            "NowChoose" : 0,
            "CustomRole" : "Unset",
            "CustomRoleHas" : 0,
            "LevelRoleHas" : 0,
            "LimitRoleHas" : [],
        }
    }
    fs.writeFileSync(MemberFilePath, JSON.stringify(MemberFile, null, 2))
}
function getMemberFile(User){
    var MemberID = User.id
    if(MemberFile[MemberID] == null)  createFile(User)
    return MemberFile[MemberID]
}
function getTitle(Quality, Rank){
    if(Quality == "Level"){
        if(Rank == "1") return "初出茅廬"
        if(Rank == "2") return "初露鋒芒"
        if(Rank == "3") return "名聲鵲起"
        if(Rank == "4") return "小有名氣"
        if(Rank == "5") return "一戰成名"
        if(Rank == "6") return "奇才異能"
        if(Rank == "7") return "聲譽卓著"
        if(Rank == "8") return "威風八面"
    } else if(Quality == "Limit"){
        if(Rank == "1") return "帶頭先鋒"
        if(Rank == "2") return "獨立自主"
        if(Rank == "3") return "引領潮流"
        if(Rank == "4") return "時尚達人"
    } else return "无"
}
function getMemberNickName(User){
    var MemberFile = getMemberFile(User)
    var Name = MemberFile.Name
    var Role = MemberFile.Role
    var NowChoose = MemberFile["Title"].NowChoose
    if(NowChoose == "0") return NickName = "【无 | " + Name + " | " + Role + "】"
    if(NowChoose == "custom" && MemberFile["Title"].CustomRole == "Unset") return "【无 | " + Name + " | " + Role + "】"
    if(NowChoose == "custom") return "【" + MemberFile["Title"].CustomRole + " | " + Name + " | " + Role + "】"
    
    var Array = NowChoose.split(" ")
    if(NowChoose.startsWith("level-")){
        var rank = Array[0].replace("level-", "")
    } else if(NowChoose.startsWith("limit-")) var rank = Array[0].replace("limit-", "")
    var TitleUser = getTitle("Level", rank)
    return "【" + TitleUser  + " | " + Name + " | " + Role + "】"
}