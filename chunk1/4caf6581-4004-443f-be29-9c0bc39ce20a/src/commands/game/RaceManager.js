const Discord = require('discord.js')
const icon = ['π¦', 'π΄', 'π', 'π’', 'π¦₯', 'π¦', 'π¦', 'π', 'π³', 'π¦']

module.exports = class Race {
    constructor(message, knex) {
        this.author = message.member
        this.time = new Date()
        this.channel = message.channel
        this.members = new Discord.Collection()
        this.started = false
        this.prize = Number(message.data.arg[1])
        this.timer = setTimeout(()=> {
            this.play()
        }, 120000)
        this.knex = knex
    }
    async join(message) {
        if(this.started) return message.reply('μ΄λ―Έ κ²μμ΄ μ§νμ€μλλ€.')
        if(this.members.has(message.member.id)) return message.reply('μ΄λ―Έ κ²μμ μ°Έκ°νμ΅λλ€.')
        if(this.members.size >= 10) return message.reply('κ²½μ£Όλ μ΅λ 10λͺλ§ μ°Έκ°ν  μ μμ΅λλ€.')
        else {
            const p = await this.pay(message.author.id, this.prize).then(r=> r)

            if(p) {
                this.members.set(message.member.id, message.member)
                if(this.members.size === 0) await message.reply('wtf')
                else if(this.members.size === 1) await message.channel.send('{member}λμ΄ μλ‘μ΄ κ²½μ£Ό κ²μμ μμνμμ΅λλ€!\n\n\n**{money}**μμ μμ§νμ¨λ€λ©΄, κ²μμ μ°Έκ°ν  μ μμ΅λλ€.\n`{prefix}κ²½μ£Ό μμ`μΌλ‘ κ²μμ μ§νν  μ μμΌλ©°, **2λΆ** λκΈ° ν μ§λμΌλ‘ κ²μμ μμν©λλ€.\n`{prefix}κ²½μ£Ό μ°Έκ°`λ‘ κ²μμ μ°Έκ°νμΈμ.'.bind({ prefix: message.data.prefix, money: this.prize, member: message.member }))
                else await message.reply('κ²μμ μ°Έκ°νλ©° **{money}**μμ μ§λΆνμμ΅λλ€!\nκ²½μ£Όκ²μμμ μΉλ¦¬μ, λμ λλ €λ°μΌμ€ μ μμΌλ©°, `{prefix}κ²½μ£Ό λκ°κΈ°`λ‘ λ°°νκΈμ λλ €λ°μ μ μμ΅λλ€.'.bind({ money: this.prize, prefix: message.data.prefix }))
            }
            else {
                if(this.members.size === 0) clearTimeout(this.timer)
                return message.reply('ν΄λΉ κ²μμ μ°Έκ°νμλ €λ©΄ μκΈμΈ {money}μμ μμ§νκ³  κ³μμΌν©λλ€.'.bind({ money: this.prize }))
            }

        }
    }
    async leave(message){
        if(this.started) return message.reply('μ΄λ―Έ κ²μμ΄ μ§νμ€μλλ€.')
        if(!this.members.has(message.member.id)) message.reply('κ²μμ μ°Έκ°νμ§ μμμ΅λλ€.')
        else {
            if(message.author.id === this.author.id) return message.reply('λ°© μμ±μλ λκ° μ μμ΅λλ€.\n`{prefix}κ²½μ£Ό ν­ν`λ₯Ό μ΄μ©ν΄μ£ΌμΈμ.'.bind({ prefix: message.data.prefix }))
            this.members.delete(message.member.id)
            await this.back(message.author.id, this.prize)
            message.reply('κ²μμμ λκ°μ΅λλ€. (λμ λ°νλμμ΅λλ€)')
            if(this.members.size === 0) this.destroy()
        }
    }
    async play(message){
        if(message && message.author.id !== this.author.id) return message.reply('κ²½μ£Όλ°©μ₯λ§ μμν  μ μμ΅λλ€.')

        clearTimeout(this.timer)
        
        if(this.members.size <= 1) {
            this.channel.send(`${this.author}, κ²½μ£Ό μ°Έκ°μκ° μμ΄ κ²μμ΄ μ·¨μλμμ΅λλ€.`)
            return this.destroy()
        }
        else {
            this.started = true
            let players = shuffle(icon)
            let mems = this.members.array()
            
            const m = await this.channel.send(mems.map((el, n) => {
                mems[n].process = 0
                return `${players[n]}${'.'.repeat(100)}π [ ${el} ]`
            } ).join('\n'))
            
            this._run(m, mems, players)
        }
    }
    async _run(msg, users, players) {
        setTimeout(async ()=> {
            await msg.edit(users.map((el, n)=> {
                let rand = (users[n].process + (Math.floor(Math.random() * 20) -7))
                users[n].process = (users[n].process + (rand)) >= 100 ? 100 : (users[n].process + (rand)) <= 0 ? 1 : (users[n].process + (rand))
                return `${'.'.repeat(users[n].process)}${players[n]}${'.'.repeat(100 - users[n].process)}π [ ${el} ]`
            }).join('\n'))
            if(users.filter(el=> el.process >= 100).length >= 1) {
                this.destroyed = true
                await users.filter(el=> el.process >= 100).forEach(u=> this.back(u.id, Math.round(this.prize*this.members.size/users.filter(el=> el.process >= 100).length)))
                return await this.channel.send(`**π₯³ μΆνν©λλ€ π₯³**\nμ°μΉ: ${users.filter(el=> el.process >= 100).join(' ')}\n\nμ°μΉμμκ² **${Math.round(this.prize*this.members.size/users.filter(el=> el.process >= 100).length)}**μμ΄ μ§κΈλ©λλ€!`)
            }
            else this._run(msg, users, players)
        }, 800)
    }
    destroy(message) {
        if(message && message.author.id !== this.author.id) return message.reply('κ²½μ£Όλ°©μ₯λ§ ν­νν  μ μμ΅λλ€.')
        if(this.started && message) return message.reply('μ΄λ―Έ κ²μμ΄ μμνμμ΅λλ€!')
        this.destroyed = true
        clearTimeout(this.timer)
        this.members.each(v=> this.back(v.id, this.prize))
        if(message) message.channel.send('κ²½μ£Όκ° μ·¨μλμμ΅λλ€.')
        else this.channel.send('κ²½μ£Όκ° μ·¨μλμμ΅λλ€.')
    }
    async pay(id, money) {
        const user = (await this.knex('users').where({ id }))[0].money
        if(user < money) {
            return false
        } else {
            await this.knex('users').where({ id }).update({ money: user - money })
            return true
        }
    }

    async back(id, money) {
        const user = (await this.knex('users').where({ id }))[0].money
        await this.knex('users').where({ id }).update({ money: Number(user)+money})
    }
}

function shuffle(a) {
    let j, x, i
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1))
        x = a[i]
        a[i] = a[j]
        a[j] = x
    }
    return a
}
