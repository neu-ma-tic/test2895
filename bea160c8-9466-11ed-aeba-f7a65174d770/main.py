import discord
from discord.ext import commands

TOKEN = 'NzQ4ODE5MzA0OTI0OTcxMDE4.X0i-Ug.eJjfWdNjO-6rHN1wZwekmk9nN90'
bot = commands.Bot(command_prefix='!')

@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def test(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(arg)  # отправляем обратно аргумент

bot.run(TOKEN)
